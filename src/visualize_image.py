import matplotlib.pyplot as plt
from utils.logger import get_logger

logger = get_logger("visualizer")


def show_images(original, compressed, centroids):

    logger.info("Displaying images using matplotlib")

    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    axes[0].imshow(original)
    axes[0].set_title("Original Image")
    axes[0].axis("off")

    axes[1].imshow(compressed)
    axes[1].set_title("Compressed Image")
    axes[1].axis("off")

    plt.tight_layout()
    plt.show()

    logger.info("Displaying dominant colors")

    plt.figure(figsize=(8, 2))

    for i, color in enumerate(centroids):
        plt.fill_between(
            [i, i + 1],
            0,
            1,
            color=[c / 255 for c in color]
            )

        plt.xlim(0, len(centroids))
        plt.title("Dominant Colors")
        plt.axis("off")
        plt.show()