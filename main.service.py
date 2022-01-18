import argparse
import scripts
from loguru import logger

def lambda_handler(event, context):
    logger.info(f"event: {event}")