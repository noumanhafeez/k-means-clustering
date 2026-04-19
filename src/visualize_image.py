import matplotlib.pyplot as plt
from utils.logger import get_logger
from config import SHOW_CENTROIDS

logger = get_logger("visualizer")


def show_images(original, compressed, centroids):

    logger.info("Displaying images using matplotlib")

    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    axes[0].imshow(original)
    axes[0].set_title("Original")
    axes[0].axis("off")

    axes[1].imshow(compressed)
    axes[1].set_title("Compressed")
    axes[1].axis("off")

    plt.tight_layout()
    plt.show()

    if SHOW_CENTROIDS:

        logger.info("Displaying centroid RGB values")

        for i, color in enumerate(centroids, start=1):
            logger.info(f"Centroid {i}: {color}")

        fig, ax = plt.subplots(figsize=(10, 2))

        for i, color in enumerate(centroids):

            rgb = [c / 255 for c in color]

            ax.barh(
                y=0,
                width=1,
                left=i,
                color=rgb
            )

            ax.text(
                i + 0.1,
                0,
                str(color),
                va="center",
                fontsize=10
            )

        ax.set_xlim(0, len(centroids))
        ax.axis("off")
        plt.title("Dominant Colors / Centroids")
        plt.show()