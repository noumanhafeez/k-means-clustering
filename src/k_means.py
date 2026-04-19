import random
from src.calculate_distance import distance
from utils.logger import get_logger

logger = get_logger("kmeans")


def kmeans(pixels, K, max_iterations):

    logger.info(f"Starting K-Means with K={K}")

    centroids = random.sample(pixels, K)

    for iteration in range(max_iterations):

        logger.info(f"Iteration {iteration + 1}")

        clusters = [[] for _ in range(K)]

        for pixel in pixels:
            distances = [distance(pixel, c) for c in centroids]
            cluster_index = distances.index(min(distances))
            clusters[cluster_index].append(pixel)

        new_centroids = []

        for cluster in clusters:

            if not cluster:
                new_centroids.append(random.choice(pixels))
            else:
                r = sum(p[0] for p in cluster) / len(cluster)
                g = sum(p[1] for p in cluster) / len(cluster)
                b = sum(p[2] for p in cluster) / len(cluster)

                new_centroids.append((int(r), int(g), int(b)))

        if new_centroids == centroids:
            logger.info("Converged early")
            break

        centroids = new_centroids

    logger.info("K-Means finished")

    return centroids