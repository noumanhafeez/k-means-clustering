# Image Compression with K‑Means Clustering

A simple implementation of K‑Means clustering for image compression using color quantization. This project compresses an input RGB image by clustering its pixel colors into `K` clusters and replacing each pixel with the corresponding cluster centroid color.

## Purpose

This project was developed as part of a programming assignment to:

- Implement the K‑Means algorithm from scratch (without using any built‑in clustering libraries).
- Apply it to a real‑world task: **image compression via color quantization**.
- Study how **visual quality** and **color representation** change as the number of clusters (K) increases.

## Directory Structure

```

project_root/
├── config.py               # Configuration (image path, K values, saving options, etc.)
├── main.py                 # Main script to run compression for multiple K values.
├── src/
│   ├── calculate_distance.py   # Euclidean distance between two RGB pixels.
│   ├── image_processing.py     # Reads image, runs k‑means, compresses image.
│   ├── k_means.py              # K‑Means algorithm implementation.
│   └── visualize_image.py      # Display original vs compressed image and centroids.
├── utils/
│   └── logger.py               # Simple logging.
├── images/
│   ├── sample.jpeg             # Example input image.
│   └── <output images>         # Generated compressed images (e.g., sample_k_2.jpg).
└── README.md

```


## Requirements

- Python 3.8+
- Pillow (`PIL`)
- Matplotlib (optional, used by `visualize_image`)

Install dependencies with:

```bash
pip install pillow matplotlib
```

## How to Run

1. **Set parameters** in `config.py`:
   - `IMAGE_PATH`: Path to your input image (should be in the `images/` folder or adjust path).
   - `USE_MULTI_K`: Set to `True` to run over multiple K values.
   - `K_VALUES`: List of K values to test (e.g., `[2, 3, 5, 10, 15, 20]`).
   - `SAVE_OUTPUT`: If `True`, compressed images are saved in `OUTPUT_FOLDER`.
   - `OUTPUT_FOLDER`: Directory where compressed images will be saved.

2. **Run the program**:
   ```bash
   python main.py
   ```

3. **Output**:
   - For each `K`, the script:
     - Loads the input image.
     - Compresses it using K‑Means (with `MAX_ITERATIONS` iterations).
     - Shows the original and compressed images side‑by‑side.
     - If `SHOW_CENTROIDS = True`, it also prints and displays the dominant centroid colors.
     - If `SAVE_OUTPUT = True`, it saves the compressed image as `images/<basename>_k_<K>.jpg`.

## How Compression Works

- Each pixel is treated as a 3‑dimensional point `(R, G, B)`.
- K‑Means partitions all pixels into `K` clusters by minimizing the squared Euclidean distance between pixels and centroids.
- After convergence, each pixel is replaced by the centroid color of its cluster.
- The image is thus represented by only `K` distinct colors, which reduces the color palette and helps compress the image.
