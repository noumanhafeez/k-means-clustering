import random
from src.calculate_distance import distance
from utils.logger import get_logger

logger = get_logger("kmeans")


def kmeans(pixels, K, max_iterations=10):

    logger.info(f"Starting K-Means with K={K}, max_iterations={max_iterations}")

    centroids = random.sample(pixels, K)
    logger.info(f"Initial centroids selected")

    for iteration in range(max_iterations):

        logger.info(f"Iteration {iteration + 1} started")

        clusters = [[] for _ in range(K)]

        # Assign pixels
        for pixel in pixels:
            distances = [distance(pixel, c) for c in centroids]
            cluster_index = distances.index(min(distances))
            clusters[cluster_index].append(pixel)

        # Update centroids
        new_centroids = []

        for index, cluster in enumerate(clusters):

            if len(cluster) == 0:
                logger.warning(f"Cluster {index} is empty. Choosing random centroid.")
                new_centroids.append(random.choice(pixels))
            else:
                r = sum(p[0] for p in cluster) / len(cluster)
                g = sum(p[1] for p in cluster) / len(cluster)
                b = sum(p[2] for p in cluster) / len(cluster)

                new_centroids.append((int(r), int(g), int(b)))

        if new_centroids == centroids:
            logger.info(f"Converged at iteration {iteration + 1}")
            break

        centroids = new_centroids

    logger.info("K-Means completed")
    return centroids