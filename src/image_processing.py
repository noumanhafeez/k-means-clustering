from PIL import Image
from src.calculate_distance import distance
from src.k_means import kmeans
from utils.logger import get_logger
from config import MAX_ITERATIONS

logger = get_logger("image_processor")


def compress_image(image_path, K):

    logger.info(f"Opening {image_path}")

    img = Image.open(image_path).convert("RGB")

    width, height = img.size
    pixels = list(img.getdata())

    centroids = kmeans(pixels, K, MAX_ITERATIONS)

    new_pixels = []

    for pixel in pixels:
        distances = [distance(pixel, c) for c in centroids]
        cluster_index = distances.index(min(distances))
        new_pixels.append(centroids[cluster_index])

    new_img = Image.new("RGB", (width, height))
    new_img.putdata(new_pixels)

    logger.info("Compression complete")

    return img, new_img, centroids