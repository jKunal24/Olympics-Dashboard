import kaggle
import os
import pandas as pd

#Looking up for the Kaggle credentials for authentication to pull data
os.environ['KAGGLE_CONFIG_DIR'] = 'C:/Users/User/.kaggle'  

# Setting Kaggle repository name  to look for required fiels
dataset = 'piterfm/paris-2024-olympic-summer-games'

# Setting the local path where folder need to download and unzip all files from kaggle repository.
download_path = 'C:/Users/User/Desktop/POWER BI/Olympics Dashboard/Source'

# Validation to check for perviously existing files with same name and delete them to avoid conflict while importing data into power bi.
for file in os.listdir(download_path):
    file_path = os.path.join(download_path, file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)  # Delete the file
            print(f"Deleted {file_path}")
    except Exception as e:
        print(f"Error deleting {file_path}: {e}")
      
# Download the dataset from Kaggle
kaggle.api.dataset_download_files(dataset, path=download_path, unzip=True)

# Package of files to be downloaded from the said Kaggle repository.
csv_files = [
    'athletes.csv',
    'events.csv',
    'medallists.csv',
    'medals.csv',
    'medals_total.csv',
    'schedules.csv',
    'schedules_preliminary.csv',
    'teams.csv',
    'torch_route.csv',
    'venues.csv'
]
#Using pandas dataframe to store data of all downloaded csv files into a dictionary and load it into power bi .
dataframes = {}

for file in csv_files:
    # locating the file in the kaggle resource
    file_path = os.path.join(download_path, file)
    
    # Load the CSV file into a Pandas DataFrame
    df = pd.read_csv(file_path)
    table_name = file.split('.')[0]
    dataframes[table_name] = df
