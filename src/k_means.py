import random
from src.calculate_distance import distance

def kmeans(pixels, K, max_iterations=10):

    centroids = random.sample(pixels, K)

    for _ in range(max_iterations):

        clusters = [[] for _ in range(K)]

        # Assign pixels to nearest centroid
        for pixel in pixels:
            distances = [distance(pixel, c) for c in centroids]
            cluster_index = distances.index(min(distances))
            clusters[cluster_index].append(pixel)

        # Update centroids
        new_centroids = []

        for cluster in clusters:

            if len(cluster) == 0:
                new_centroids.append(random.choice(pixels))
            else:
                r = sum(p[0] for p in cluster) / len(cluster)
                g = sum(p[1] for p in cluster) / len(cluster)
                b = sum(p[2] for p in cluster) / len(cluster)

                new_centroids.append((int(r), int(g), int(b)))

        if new_centroids == centroids:
            break

        centroids = new_centroids

    return centroids