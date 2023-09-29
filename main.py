"""main """

from mlopsCNN import logger
from mlopsCNN.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlopsCNN.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipelin
from mlopsCNN.pipeline.stage_03_training import TrainingPipeline
from mlopsCNN.pipeline.stage_04_evaluation import EvaluationPipeline

STAGE_NAME = "1 Data Ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<\n")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==================================================================================x")
except Exception as e:
    logger.error(f">>>>>> stage {STAGE_NAME} failed <<<<<<<")
    logger.error(f">>>>>> {e} <<<<<<<")




STAGE_NAME = "2 Prepare base model"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<\n")
    obj = PrepareBaseModelTrainingPipelin()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==================================================================================x")
except Exception as e:
    logger.error(f">>>>>> stage {STAGE_NAME} failed <<<<<<<")
    logger.error(f">>>>>> {e} <<<<<<<")




STAGE_NAME = "3 Training Activated......."

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<\n")
    obj = TrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==================================================================================x")
except Exception as e:
    logger.error(f">>>>>> stage {STAGE_NAME} failed <<<<<<<")
    logger.error(f">>>>>> {e} <<<<<<<")



STAGE_NAME = "Evaluation Stage......."


try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<\n")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==================================================================================x")
except Exception as e:
    logger.error(f">>>>>> stage {STAGE_NAME} failed <<<<<<<")
    logger.error(f">>>>>> {e} <<<<<<<")