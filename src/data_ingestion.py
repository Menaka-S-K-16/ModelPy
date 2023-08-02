import os
import sys
import pandas as pd
from data_transformation import DataTransformation
from model_trainer import ModelTrainer
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        #logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('C:\\Users\\kame1005\\Desktop\\vs code projects\\SampleProject2023\\data\\stud.csv')
            #logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            #logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            #logging.info("Inmgestion of the data iss completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise e
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()
    
    data_Transform=DataTransformation()
    train_arr,test_arr,_=data_Transform.initiate_data_transformation(train_data,test_data)

    modeltrainer=ModelTrainer()
    print("....train_arr", train_arr,"...test_arr",test_arr)
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))
    