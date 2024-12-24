import sys, os
from object_detection_practice.exception import SignException
from object_detection_practice.logger import logging
from object_detection_practice.components.data_ingestion import DataIngestion

from object_detection_practice.entity.config_entity import (DataIngestionConfig,
                                               DataValidationConfig,
                                               ModelTrainerConfig,
                                               ModelPusherConfig)


from object_detection_practice.entity.artifacts_entity import (DataIngestionArtifact,
                                                  DataValidationArtifact,
                                                  ModelTrainerArtifact,
                                                  ModelPusherArtifacts)


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
    
    def start_data_ingestion(self)-> DataIngestionArtifact:
        try: 
            logging.info(
                "Entered the start_data_ingestion method of TrainPipeline class"
            )
            logging.info("Getting the data from URL")

            data_ingestion = DataIngestion(
                data_ingestion_config =  self.data_ingestion_config
            )

            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the data from URL")
            logging.info(
                "Exited the start_data_ingestion method of TrainPipeline class"
            )

            return data_ingestion_artifact

        except Exception as e:
            raise SignException(e, sys)
        
    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
        except Exception as e:
            raise SignException(e, sys)