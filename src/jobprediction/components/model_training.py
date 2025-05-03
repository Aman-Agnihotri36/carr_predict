import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import warnings
from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.neural_network import MLPClassifier
from sklearn.decomposition import PCA
from scipy import sparse
from imblearn.over_sampling import RandomOverSampler
from mpl_toolkits.mplot3d import Axes3D
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import os
from src.jobprediction.entity.config_entity import ModelTrainingConfig
import json

class ModelTraining:
  def __init__(self, config=ModelTrainingConfig):
    self.config=config

  def save_dict_to_json(self, data):
      try:
        destination=self.config.report_path
        # Ensure the directory exists
        os.makedirs(os.path.dirname(destination), exist_ok=True)
        with open(destination, 'w') as f:
          json.dump(data, f, indent=4)  # Use indent for pretty printing
        print(f"Dictionary saved to {destination}")
      except Exception as e:
        print(f"Error saving dictionary to JSON: {e}")

  def load_data(self):
    df=pd.read_csv(self.config.processed_data_path)
    return df

  def training(self):
    data = self.load_data()

    x = data.iloc[:,:-1]
    y = data.iloc[:,-1]

    X = OneHotEncoder().fit_transform(x)
    Y = y.copy(deep=True)

    X2 = StandardScaler(with_mean=False).fit_transform(X)
    y2 = y.copy(deep=True)

    y_trans = y.copy(deep=True)

    Y1=LabelEncoder().fit_transform(y_trans)
    Y2=np.asarray(y_trans)

    CRM_Managerial_Roles = ['CRM Business Analyst','CRM Technical Developer','Project Manager','Information Technology Manager']
    Analyst = ['Business Systems Analyst','Business Intelligence Analyst','E-Commerce Analyst']
    Mobile_Applications_Web_Development = ['Mobile Applications Developer','Web Developer','Applications Developer']
    QA_Testing = ['Software Quality Assurance (QA) / Testing','Quality Assurance Associate']
    UX_Design = ['UX Designer','Design & UX']
    Databases = ['Database Developer','Database Administrator','Database Manager','Portal Administrator']
    Programming_Systems_Analyst = ['Programmer Analyst','Systems Analyst']
    Networks_Systems = ['Network Security Administrator','Network Security Engineer','Network Engineer',
                        'Systems Security Administrator','Software Systems Engineer','Information Security Analyst']
    SE_SDE = ['Software Engineer','Software Developer']
    Technical_Support_Service = ['Technical Engineer','Technical Services/Help Desk/Tech Support','Technical Support']
    others = ['Solutions Architect','Data Architect','Information Technology Auditor']

    y_trans = y_trans.replace(['CRM Business Analyst','CRM Technical Developer','Project Manager',
                    'Information Technology Manager'],'CRM/Managerial Roles')
    y_trans = y_trans.replace(['Business Systems Analyst','Business Intelligence Analyst','E-Commerce Analyst'],'Analyst')
    y_trans = y_trans.replace(['Mobile Applications Developer','Web Developer',
                        'Applications Developer'],'Mobile Applications/ Web Development')
    y_trans = y_trans.replace(['Software Quality Assurance (QA) / Testing','Quality Assurance Associate'],'QA/Testing')
    y_trans = y_trans.replace(['UX Designer','Design & UX'] , 'UX/Design')
    y_trans = y_trans.replace(['Database Developer','Database Administrator',
                        'Database Manager','Portal Administrator'] , 'Databases')
    y_trans = y_trans.replace(['Programmer Analyst','Systems Analyst'],'Programming/ Systems Analyst')
    y_trans = y_trans.replace(['Network Security Administrator','Network Security Engineer',
                        'Network Engineer','Systems Security Administrator',
                        'Software Systems Engineer','Information Security Analyst'],'Networks/ Systems')
    y_trans = y_trans.replace(['Software Engineer','Software Developer'] ,'SE/SDE')
    y_trans = y_trans.replace(['Technical Engineer','Technical Services/Help Desk/Tech Support',
                        'Technical Support'],'Technical Support/Service')
    y_trans = y_trans.replace(['Solutions Architect','Data Architect','Information Technology Auditor'],'others')

    X3 = sparse.csr_matrix.copy(X2)
    y3 = y_trans.copy(deep=True)

    ros = RandomOverSampler(random_state=42)
    X_ovs, y_ovs = ros.fit_resample(X3, y3)

    X_train, X_test, y_train, y_test = train_test_split(X_ovs,y_ovs,test_size=0.2)

    clf = MLPClassifier(activation=self.config.activation, hidden_layer_sizes = (50,50,50), solver = self.config.solver) #, random_state=1)
    clf.fit(X_train,y_train)

    print("Training Accuracy Score: ",accuracy_score(clf.predict(X_train),y_train))
    print("Testing Accuracy Score: ",accuracy_score(clf.predict(X_test),y_test))


    with open(self.config.model_path, "wb") as f:
        pickle.dump(clf, f)

    results={
        "Train Accuracy": accuracy_score(clf.predict(X_train),y_train),
        "Test Accuracy": accuracy_score(clf.predict(X_test),y_test)
    }

    self.save_dict_to_json(results)
