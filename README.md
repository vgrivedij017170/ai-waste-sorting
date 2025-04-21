# AI-Waste-Sorting

## Description

`Flask` application that allows users to upload images of waste items and classify them into
categories such as batteries, clothes, e-waste, glass, light bulbs, organic. The app uses a
`TensorFlow` model for image classification and provides users with information and video resources related to the type
of waste.

## Features

- Upload images of waste items.
- Classify waste items using a pre-trained TensorFlow model.
- Display relevant information and video resources based on the classified category.
- User-friendly interface for uploading images and viewing results.

## Libraries Used 

- `Flask`: create the server, handle HTTP requests, manage routing
- `TensorFlow`: load a pre-trained model (`classifyWaste.h5`)
- `NumPy`: convert the uploaded images into arrays, normalize pixel values, and prepare them for input into the TensorFlow model for classification.

## Endpoints

| Endpoint               | Method | Description                                                                   |
|------------------------|--------|-------------------------------------------------------------------------------|
| `/`                    | GET    | Displays the main page for uploading images.                                  |
| `/`                    | POST   | Handles image uploads and classifies the uploaded image.                      |
| `/classify/<img_path>` | GET    | Classifies the uploaded image and returns the predicted category and details. |
| `/display/<filename>`  | GET    | Displays the uploaded image.                                                  |

### Endpoint Details

* **`/` (GET)**: This is the home endpoint where the main upload interface is displayed. Users can upload an image here.

* **`/` (POST)**: This endpoint processes the uploaded image. It checks if a file is uploaded, validates the file type,
  saves the image, and then classifies it. After processing, it redirects to the home page and displays the
  classification results.

* **`/classify/<img_path>` (GET)**: This endpoint is called to classify the uploaded image based on its path. It returns
  the predicted waste category and additional details related to that category.

* **`/display/<filename>` (GET)**: This endpoint redirects to the location of the uploaded image for display purposes.
