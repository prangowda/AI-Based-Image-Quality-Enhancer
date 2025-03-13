import cv2
import numpy as np
import argparse
from PIL import ImageEnhance, Image

def enhance_image(input_path, output_path):
    # Read the image
    img = cv2.imread(input_path)
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply noise reduction
    denoised = cv2.fastNlMeansDenoising(gray, None, 30, 7, 21)

    # Increase sharpness using Unsharp Masking
    blurred = cv2.GaussianBlur(denoised, (0,0), 3)
    sharp = cv2.addWeighted(denoised, 1.5, blurred, -0.5, 0)

    # Enhance contrast
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    enhanced = clahe.apply(sharp)

    # Save the enhanced image
    cv2.imwrite(output_path, enhanced)

    print(f"Enhanced image saved as {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enhance Image Quality")
    parser.add_argument("--input", required=True, help="Input image path")
    parser.add_argument("--output", required=True, help="Output image path")
    args = parser.parse_args()
    
    enhance_image(args.input, args.output)
