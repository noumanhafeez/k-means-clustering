from PIL import Image
from src.calculate_distance import distance
from src.k_means import kmeans


def compress_image(image_path, K):

    img = Image.open(image_path)
    img = img.convert("RGB")

    width, height = img.size
    pixels = list(img.get_flattened_data())

    centroids = kmeans(pixels, K)

    new_pixels = []

    for pixel in pixels:
        distances = [distance(pixel, c) for c in centroids]
        cluster_index = distances.index(min(distances))
        new_pixels.append(centroids[cluster_index])

    new_img = Image.new("RGB", (width, height))
    new_img.putdata(new_pixels)

    return img, new_img, centroids