from mlflow_project import logger
from mlflow_project.components.model_evaluation import ModelEvaluation
from mlflow_project.config.configuration import ConfigurationManager

STAGE_NAME_05 = "Model Evaluation Pipeline"


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def forward(self):
        """Runs the model evaluation pipeline."""
        config_manager = ConfigurationManager()
        model_evaluation_config = config_manager.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()


if __name__ == "__main__":
    try:
        logger.info(f"{STAGE_NAME_05} has started")
        model_evaluation_pipeline = ModelEvaluationPipeline()
        model_evaluation_pipeline.forward()
        logger.info(f"{STAGE_NAME_05} has completed")
    except Exception as e:
        logger.exception(e)
        raise e
