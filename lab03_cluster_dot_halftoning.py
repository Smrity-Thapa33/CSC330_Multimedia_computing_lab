import numpy as np 
import cv2 
import matplotlib.pyplot as plt # For image display
import os 

def convert_to_grayscale(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE) 
    return image # Return grayscale image

# Predefined 2x2 cluster dot patterns for 5 intensity levels
dot_patterns = {
    0: np.array([[0, 0], [0, 0]], dtype=np.uint8), 
    1: np.array([[255, 0], [0, 0]], dtype=np.uint8), 
    2: np.array([[255, 255], [0, 0]], dtype=np.uint8), 
    3: np.array([[255, 255], [255, 0]], dtype=np.uint8), 
    4: np.array([[255, 255], [255, 255]], dtype=np.uint8),
}

def cluster_dot_halftoning(grayscale_image, cluster_size=2):
    height, width = grayscale_image.shape 
    halftoned_image = np.zeros_like(grayscale_image) # I halftoned image
   
    for i in range(0, height, cluster_size): 
        for j in range(0, width, cluster_size):
            cluster = grayscale_image[i:i+cluster_size, j:j+cluster_size]
            avg_intensity = np.mean(cluster) 
            dot_level = int(avg_intensity / 255 * 4) 
            pattern = dot_patterns[dot_level] 
            halftoned_image[i:i+cluster.shape[0], j:j+cluster.shape[1]] = pattern[:cluster.shape[0], :cluster.shape[1]] 
    return halftoned_image 

def display_images(original, halftoned):
    plt.figure(figsize=(10, 5)) 

    plt.subplot(1, 2, 1) # First subplot (original)
    plt.imshow(original, cmap='gray') # Show original grayscale image
    plt.title("Original Grayscale Image") 
    plt.axis('off') 
    
    plt.subplot(1, 2, 2) # Second subplot (halftoned)
    plt.imshow(halftoned, cmap='gray') # Show halftoned image
    plt.title("Halftoned Image (2x2 Cluster)") # Title
    plt.axis('off') 
   
    plt.tight_layout() 
    plt.show() 
def main():
    image_path = input("Enter the path to the image: ") 
    
    if not os.path.isfile(image_path): 
        print("Invalid file path. Please try again.") 
        return 
    grayscale_image = convert_to_grayscale(image_path) 
    halftoned_image = cluster_dot_halftoning(grayscale_image) # Apply halftoning
    display_images(grayscale_image, halftoned_image) 
main() # Call main function