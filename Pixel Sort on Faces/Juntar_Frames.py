import cv2
import os
import tqdm
from tqdm.auto import tqdm
from moviepy.editor import VideoFileClip

def frames_to_video(input_folder, output_video_path, fps=30):
    # Obtén la lista de archivos de imagen en la carpeta de entrada
    image_files = [f for f in os.listdir(input_folder) if f.endswith('.jpg') or f.endswith('.png')]
    image_files.sort()

    # Obtiene la altura y ancho de la primera imagen
    img = cv2.imread(os.path.join(input_folder, image_files[0]))
    height, width, _ = img.shape

    # Crea el objeto VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Ajusta el codec según tu preferencia
    video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    # Lee y escribe cada frame al archivo de video
    with tqdm(total=len(image_files), desc='Processing frames', unit='frame') as pbar:
        for filename in image_files:
            img = cv2.imread(os.path.join(input_folder, filename))
            video_writer.write(img)
            pbar.update(1)

    # Libera el objeto VideoWriter
    video_writer.release()

# Definir las rutas de entrada y salida
input_folder_path = '/Users/g.s.e/Programacion/VideoDxm/frames_sorted'
output_video_path = '/Users/g.s.e/Programacion/VideoDXM/output_video.mp4'

# Leer el video original y obtener la tasa de FPS
video_clip = VideoFileClip ('/Users/g.s.e/Programacion/VideoDxm/input_video.mp4')
fps = video_clip.fps

# Llamada a la función para convertir los frames a video
frames_to_video(input_folder_path, output_video_path, fps)