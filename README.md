# Image Compressor App

This is a simple image compressor application built using the Kivy framework for the graphical user interface (GUI) and PIL (Python Imaging Library) for image processing. The app allows users to compress images while keeping their original dimensions. Users can select the desired compression quality using a slider and choose where to save the compressed image.

## Features

- **Upload Image**: Allows the user to upload an image from their computer.
- **Set Compression Quality**: Use a slider to set the compression quality of the image.
- **Save Image**: After compressing the image, users can choose where to save the compressed file.
- **Supports JPEG and PNG Formats**: You can save the compressed image in JPEG or PNG format.

## Requirements

To run this app, you need the following Python packages:

- **Kivy**: A Python framework for building GUI applications.
- **Pillow (PIL)**: A Python Imaging Library to handle image processing.

To install the required packages, use:

```bash
pip install kivy pillow
```

## How to Run

1. Clone this repository or download the Python script.
2. Ensure you have the required dependencies installed (as mentioned above).
3. Run the Python script:

```bash
python image_compressor.py
```

## Usage

1. **Select Image**: Click on the "Upload Image" button to choose an image from your computer.
2. **Adjust Compression Quality**: Use the slider to select the desired quality (from 1% to 100%).
3. **Save Image**: Once the image is uploaded and the compression quality is selected, click the "Save Compressed Image" button to save the image in the desired location.

## Code Overview

- **ImageCompressorApp**: The main class that creates the GUI using Kivy.
  - `build`: Sets up the layout and components of the app.
  - `on_slider_value_change`: Updates the slider label to show the selected compression quality.
  - `show_filechooser`: Opens the file chooser dialog to select an image.
  - `compress_image`: Compresses the selected image based on the selected quality.
  - `open_save_popup`: Prompts the user to enter the save name and select the save location.
  - `save_image`: Saves the compressed image in either PNG or JPEG format.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


