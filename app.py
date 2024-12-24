from object_detection_practice.logger import logging
from object_detection_practice.exception import SignException
import sys
from object_detection_practice.pipeline.training_pipeline import TrainPipeline

obj = TrainPipeline()
obj.run_pipeline()
