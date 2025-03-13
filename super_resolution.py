import cv2
import numpy as np
import tensorflow as tf
import argparse

# Load the pre-trained SRCNN model
model = tf.keras.models.load_model("models/srcnn_model.h5")

def super_resolve_image(input_path, output_path):
    # Load the low-resolution image
    img = cv2.imread(input_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)  # Convert to YCrCb color space

    # Resize image to match model input size
    img_resized = cv2.resize(img, (128, 128))

    # Normalize and reshape for model input
    img_y = img_resized[:, :, 0].astype("float32") / 255.0
    img_y = np.expand_dims(img_y, axis=[0, -1])

    # Run Super-Resolution
    img_y_sr = model.predict(img_y)
    img_y_sr = np.clip(img_y_sr[0] * 255.0, 0, 255).astype("uint8")

    # Resize output to original dimensions
    img_y_sr = cv2.resize(img_y_sr, (img.shape[1], img.shape[0]))

    # Merge back channels and convert to BGR
    img_resized[:, :, 0] = img_y_sr
    img_bgr = cv2.cvtColor(img_resized, cv2.COLOR_YCrCb2BGR)

    # Save the super-resolved image
    cv2.imwrite(output_path, img_bgr)
    print(f"Super-resolved image saved as {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Super-Resolution")
    parser.add_argument("--input", required=True, help="Input image path")
    parser.add_argument("--output", required=True, help="Output image path")
    args = parser.parse_args()

    super_resolve_image(args.input, args.output)
