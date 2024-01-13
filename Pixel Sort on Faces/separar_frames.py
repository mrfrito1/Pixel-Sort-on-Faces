import cv2
import os
from tqdm import tqdm

def extraer_frames(ruta_video, carpeta_salida):
    os.makedirs(carpeta_salida, exist_ok=True)

    video = cv2.VideoCapture(ruta_video)
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    for i in tqdm(range(total_frames), desc="Separando Frames", total=total_frames):
        success, frame = video.read()
        if not success:
            break
        ruta_imagen = os.path.join(carpeta_salida, f"frame_{i:04d}.jpg")
        cv2.imwrite(ruta_imagen, frame)

    video.release()

ruta_video = "/Users/g.s.e/Programacion/VideoDXM/input_video.mp4"
carpeta_salida = "/Users/g.s.e/Programacion/VideoDXM/frames"
extraer_frames(ruta_video, carpeta_salida)