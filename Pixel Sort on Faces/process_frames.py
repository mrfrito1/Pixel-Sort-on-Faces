import os
import cv2
import separar_frames
import face_masks
from sort_image import choices, sort_image

def load_images_and_masks(image_folder, mask_folder):
    images = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith(".png")]
    masks = [os.path.join(mask_folder, f) for f in os.listdir(mask_folder) if f.endswith(".png")]

    if len(images) != len(masks):
        raise ValueError("The number of images and masks does not match.")

    return images, masks

def process_frames(images, masks, output_folder, choices):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for image_path, mask_path in zip(images, masks):
        image = cv2.imread(image_path)
        mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

        sort_image(image.shape[:2], image, mask, [(0, 255)], 0.0, choices["lightness"])

        output_path = os.path.join(output_folder, os.path.basename(image_path))
        cv2.imwrite(output_path, image)

if __name__ == "__main__":
    input_folder = "frames"
    mask_folder = "face_masks"
    output_folder = "frames_sorted"
    choices = {"lightness": 0.5} # example of defining choices variable
    images, masks = load_images_and_masks(input_folder, mask_folder)
    process_frames(images, masks, output_folder, choices)