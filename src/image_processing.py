from PIL import Image
from src.calculate_distance import distance
from src.k_means import kmeans
from utils.logger import get_logger

logger = get_logger("image_processor")


def compress_image(image_path, K):

    logger.info(f"Opening image: {image_path}")

    img = Image.open(image_path)
    img = img.convert("RGB")

    width, height = img.size
    logger.info(f"Image size: {width} x {height}")

    pixels = list(img.getdata())

    logger.info("Running K-Means clustering")
    centroids = kmeans(pixels, K)

    new_pixels = []

    for pixel in pixels:
        distances = [distance(pixel, c) for c in centroids]
        cluster_index = distances.index(min(distances))
        new_pixels.append(centroids[cluster_index])

    logger.info("Creating compressed image")

    new_img = Image.new("RGB", (width, height))
    new_img.putdata(new_pixels)

    logger.info("Image compression completed")

    return img, new_img, centroids