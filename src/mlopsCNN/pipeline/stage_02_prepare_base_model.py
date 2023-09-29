from mlopsCNN.config.configuration import ConfigurationManager
from mlopsCNN.components.prepare_base_model import PrepareBaseModel
from mlopsCNN import logger

import tensorflow as tf
tf.config.experimental.set_visible_devices([], 'GPU')

gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        # Currently, memory growth needs to be the same across GPUs
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
    except RuntimeError as e:
        print(e)



STAGE_NAME = "Prepare base model"

class PrepareBaseModelTrainingPipelin:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()



if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = PrepareBaseModelTrainingPipelin()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<")
    except Exception as e:
        logger.error(f">>>>>> stage {STAGE_NAME} failed <<<<<<<")
        logger.error(f">>>>>> {e} <<<<<<<")



