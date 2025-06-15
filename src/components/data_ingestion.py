from src.exception import CustomException
from src.logger import logging
import os
import sys
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split



@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')


class DataIngestion():

    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        '''
        This function initiates the data ingestion and returns the path to train, 
        test, and raw data.

        returns: Tuple of three paths (train, test, and raw data)
        '''

        logging.info('Initiating the data ingestion method or component')

        try:
            # Read data from the source (database, local files, etc)
            df = pd.read_csv('notebook/data/StdsPerform.csv')
            logging.info('Data is read as a dataframe')

            # Creating directories
            logging.info('Create artifacts directory and save the raw data')
            os.makedirs(os.path.dirname(
                self.ingestion_config.raw_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,
                        index=False, header=True)

            # Split the data into train and test
            logging.info('Train test split initiated')
            train, test = train_test_split(df, test_size=.2, random_state=42)

            logging.info('Saving train test split inside artifacts directory')
            train.to_csv(self.ingestion_config.train_data_path,
                         index=False, header=True)
            test.to_csv(self.ingestion_config.test_data_path,
                        index=False, header=True)

            logging.info('Ingestion of the data is complete')

            return (
                self.ingestion_config.raw_data_path,
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.info(f'Exception is raised: {e}')
            raise CustomException(e, sys)


if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()