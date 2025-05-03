import os

def create_directory(destination_path):
  try:
    os.makedirs(destination_path, exist_ok=True)  # exist_ok=True prevents error if directory exists
    print(f"Directory '{destination_path}' created successfully.")
  except OSError as error:
    print(f"Error creating directory '{destination_path}': {error}")

# prompt: function to read yaml from a destinaton path

import yaml
import os

def read_yaml_file(filepath):
  if not os.path.exists(filepath):
    print(f"Error: File not found at {filepath}")
    return None
  try:
    with open(filepath, 'r') as file:
      yaml_data = yaml.safe_load(file)
      return yaml_data
  except yaml.YAMLError as e:
    print(f"Error parsing YAML file: {e}")
    return None
  except Exception as e:
    print(f"An unexpected error occurred: {e}")
    return None
