from config import (
    IMAGE_PATH,
    K_CLUSTERS,
    K_VALUES,
    USE_MULTI_K,
    SAVE_OUTPUT,
    OUTPUT_FOLDER
)

from src.image_processing import compress_image
from src.visualize_image import show_images
from utils.logger import get_logger
import os

logger = get_logger("main")


def run_for_k(k):

    logger.info(f"\nRunning compression for K={k}")

    original, compressed, centroids = compress_image(
        IMAGE_PATH,
        k
    )

    if SAVE_OUTPUT:

        image_name = os.path.splitext(os.path.basename(IMAGE_PATH))[0]
        output_path = f"{OUTPUT_FOLDER}{image_name}_k_{k}.jpg"

        compressed.save(output_path)

        logger.info(f"Saved: {output_path}")

    show_images(original, compressed, centroids)


def main():

    logger.info("Program started")

    if USE_MULTI_K:

        for k in K_VALUES:
            run_for_k(k)

    else:

        run_for_k(K_CLUSTERS)

    logger.info("Program finished")


if __name__ == "__main__":
    main()