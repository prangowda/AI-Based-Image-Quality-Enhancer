## 📜 **AI-Based Image Quality Enhancer**  

### 🖼️ **Overview**  
The **AI-Based Image Quality Enhancer** is a tool designed to improve image quality by **reducing noise, sharpening, enhancing contrast, and performing AI-based super-resolution** using a **pre-trained Super-Resolution Convolutional Neural Network (SRCNN)** model.  

---

## 🚀 **Features**  
✅ **Noise Reduction** – Removes unwanted noise from images  
✅ **Contrast & Sharpness Enhancement** – Enhances visibility and clarity  
✅ **AI Super-Resolution** – Converts low-resolution images into high-resolution using deep learning  
✅ **Batch Processing Support** – Enhance multiple images at once  
✅ **User-Friendly CLI** – Command-line interface for ease of use  

---

## 🛠️ **Technologies Used**  
- **Python** 🐍  
- **OpenCV** 👀  
- **TensorFlow/Keras** 🤖  
- **NumPy** 🔢  
- **Pillow** 🖼️  

---

## 📂 **Project Structure**  

```
📂 Image-Quality-Enhancer/
│── 📜 enhance_image.py         # Script for image enhancement
│── 📜 super_resolution.py      # AI-based super-resolution script
│── 📜 requirements.txt         # List of dependencies
│── 📜 README.md                # Project documentation
│── 📂 models/                  # Pre-trained SRCNN model
│── 📂 input_images/            # Folder for input images
│── 📂 output_images/           # Folder for enhanced images
```

---

## 🛠️ **Installation & Setup**  

### **Step 1: Clone the Repository**  
```bash
git clone https://github.com/prangowda/Image-Quality-Enhancer.git
cd Image-Quality-Enhancer
```

### **Step 2: Install Dependencies**  
```bash
pip install -r requirements.txt
```

---

## 🎯 **How to Use?**  

### **1️⃣ Enhance Image Quality (Noise Reduction, Sharpening, Contrast Boost)**  
Run the following command:  
```bash
python enhance_image.py --input input_images/sample.jpg --output output_images/enhanced.jpg
```
👉 **Example:**  
- **Input:** Blurry or noisy image  
- **Output:** Clearer, sharper image  

---

### **2️⃣ AI-Based Super-Resolution (Enhance Low-Resolution Images)**  
Run the following command:  
```bash
python super_resolution.py --input input_images/sample.jpg --output output_images/high_res.jpg
```
👉 **Example:**  
- **Input:** Low-resolution image  
- **Output:** High-resolution version of the image  

---

## 📸 **Example Output**  
| **Original Image**  | **Enhanced Image**  | **Super-Resolution Image**  |
|---------------------|---------------------|-----------------------------|
| ![Before](input_images/sample.jpg) | ![After](output_images/enhanced.jpg) | ![Super-Res](output_images/high_res.jpg) |

---

## 🛠️ **Enhancements & Future Work**  
🚀 **Implement ESRGAN** – Use **Generative Adversarial Networks (GANs)** for realistic super-resolution  
🔥 **Mobile & Web UI** – Create a user-friendly **web and mobile application**  
📸 **Video Support** – Extend enhancement to videos  
