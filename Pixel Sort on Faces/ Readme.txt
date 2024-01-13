Pixel Sort on Faces Project

This Python project focuses on applying the pixel sort effect exclusively to faces detected in videos. The project workflow consists of three main scripts: separar_frames.py, face_masks.py, and process_frames.py.

Project Workflow:
separar_frames.py:

Converts the input video into individual images, saving them in the 'frames' folder.
face_masks.py:

Utilizes facial recognition to generate masks for each frame, representing the face's location.
Saves these masks as images with a black background and a white rectangle on the face area in the 'face_masks' folder.
process_frames.py:

Reads images from the 'frames' folder.
Reads corresponding masks from the 'face_masks' folder.
Applies a custom pixel sort effect inspired by sort_image.py to the face regions defined by the masks.
Saves the resulting processed images in the 'frames_sorted' folder.
Custom Pixel Sorting:
The custom pixel sorting method is inspired by the sort_image.py script from the pixelsort repository. This repository provides a variety of sorting functions, including lightness, hue, saturation, intensity, and minimum RGB value, enhancing the flexibility of the pixel sorting effect.

Requirements:
Python 3.x
OpenCV library
PIL library
Usage:
Run separar_frames.py to extract frames from the input video.
Execute face_masks.py for facial recognition and mask creation.
Finally, run process_frames.py to apply the custom pixel sort effect to face regions.
Credits:
This project gives credit to the pixelsort repository for providing the foundation for the custom pixel sorting method (sort_image.py), enhancing the capabilities of the pixel sorting effect applied in this project.

Feel free to explore the pixelsort repository for additional pixel sorting functionalities and inspiration.

Acknowledgments:
Special thanks to the original author of sort_image.py in the pixelsort repository for their contribution to the field of pixel sorting.

License:
This project inherits the license from the pixelsort repository, available here.

Happy Pixel Sorting! 🎨✨