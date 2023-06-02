from acipredict.pipeline.pipeline import Pipeline 
from acipredict.exception import ACIPredictionException

from acipredict.logger import logging


def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()


    except ACIPredictionException as e:
        logging.error(f"{e}")
        print(e)



if __name__ == "__main__":
    main()