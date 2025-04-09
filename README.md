# 🖼️ Image Compressor App 🚀

Welcome to the **Image Compressor App**, a simple yet powerful tool built with **Kivy** and **Pillow (PIL)** to compress your images while maintaining their original dimensions. 🌟 

Whether you want to reduce the size of your images for faster uploads or save some storage space, this app makes it easy to adjust the quality of your images using a sleek slider. 🔧

## 🛠️ Features

- **📤 Upload Your Image**: Easily select any image from your computer for compression.
- **🎚️ Adjustable Quality**: Use a slider to set the desired compression quality from 1% to 100%.
- **💾 Save Compressed Image**: Save the newly compressed image to your chosen directory in either JPEG or PNG format.
- **💡 Supports Multiple Formats**: Your images can be saved in both **JPEG** and **PNG** formats.

## 📋 Requirements

To run this app, you'll need to install the following Python packages:

- **Kivy**: A Python framework for building interactive applications with beautiful user interfaces.
- **Pillow (PIL)**: A Python Imaging Library for handling and manipulating images.

### Installation

To install the required dependencies, run the following command in your terminal:

```bash
pip install kivy pillow
```

## 🚀 How to Run

1. Clone this repository or download the Python script to your local machine.
2. Make sure you have the required dependencies installed (check the section above).
3. Run the application with:

```bash
python image_compressor.py
```

## 🔧 Usage

1. **Select an Image**: Click on the **Upload Image** button to pick an image from your computer.
2. **Adjust Compression Quality**: Use the slider to choose the compression level (from 1% to 100%).
3. **Save Your Compressed Image**: Once you're satisfied with the compression, click the **Save Compressed Image** button to store the image in your desired location.

## 🖥️ Code Breakdown

- **ImageCompressorApp**: This is the main class that builds the GUI using Kivy and handles the compression logic.
  - `build`: Sets up the layout and all components of the application.
  - `on_slider_value_change`: Updates the quality label based on the slider value.
  - `show_filechooser`: Opens the file chooser dialog to select an image for compression.
  - `compress_image`: Compresses the selected image based on the chosen quality.
  - `open_save_popup`: Opens a save dialog to allow the user to choose where and how to save the compressed image.
  - `save_image`: Saves the compressed image to the specified directory in JPEG or PNG format.
