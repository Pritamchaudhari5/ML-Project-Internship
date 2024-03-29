from threading import Thread
from acipredict.component.data_ingestion import DataIngestion

from acipredict.config.configuration import Configuration
from acipredict.entity.artifact_entity import DataIngestionArtifact
from acipredict.exception import ACIPredictionException
import sys,os

class Pipeline(Thread):

    def __init__(self,config: Configuration = Configuration()) -> None:
        try:
            self.config = config

        except Exception as e:
            raise ACIPredictionException(e,sys) from e 

    def start_data_ingestion(self)-> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise ACIPredictionException(e,sys) from e 

    def start_data_validation(self)-> DataIngestionArtifact:
        try:
            pass
        except Exception as e:
            raise ACIPredictionException(e,sys) from e 

    def start_data_transformation(self)-> DataIngestionArtifact:
        try:
            pass
        except Exception as e:
            raise ACIPredictionException(e,sys) from e 

    def start_model_trainer(self)-> DataIngestionArtifact:
        try:
            pass
        except Exception as e:
            raise ACIPredictionException(e,sys) from e 

    def start_model_evaluation(self)-> DataIngestionArtifact:
        try:
            pass
        except Exception as e:
            raise ACIPredictionException(e,sys) from e 

    def start_model_pusher(self)-> DataIngestionArtifact:
        try:
            pass
        except Exception as e:
            raise ACIPredictionException(e,sys) from e 

    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
        except Exception as e:
            raise ACIPredictionException(e,sys) from e 