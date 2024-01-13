import numpy as np
import cv2
import math
import functools
from typing import Tuple, List, Callable, Any

def sort_image(
        size: Tuple[int, int],
        image_data: np.ndarray,
        mask_data: np.ndarray,
        intervals: List[Tuple[int, int]],
        randomness: float,
        sorting_function: Callable[[np.ndarray], np.ndarray]):

    def get_pixel_value(image: np.ndarray, x: int, y: int) -> Tuple[int, int, int]:
        return tuple(image[y, x])

    def set_pixel_value(image: np.ndarray, x: int, y: int, value: Tuple[int, int, int]):
        image[y, x] = value

    def sort_line(image: np.ndarray, x1: int, y1: int, x2: int, y2: int):
        line_pixels = []
        for y in range(y1, y2):
            for x in range(x1, x2):
                if mask_data[y, x] > 0:
                    line_pixels.append(get_pixel_value(image_data, x, y))

        line_pixels.sort(key=sorting_function, reverse=True)

        for i, pixel in enumerate(line_pixels):
            set_pixel_value(image_data, x1 + i % (x2 - x1), y1 + i // (x2 - x1), pixel)

    def sort_intervals(intervals: List[Tuple[int, int]]):
        intervals.sort(key=lambda interval: interval[0] + interval[1] / 2)

    def random_interval(width: int, height: int, randomness: float):
        interval_width = int(math.ceil(width * randomness))
        interval_height = int(math.ceil(height * randomness))

        x = np.random.randint(0, width - interval_width)
        y = np.random.randint(0, height - interval_height)

        return (x, x + interval_width), (y, y + interval_height)

    def random_intervals(width: int, height: int, count: int, randomness: float):
        intervals = []
        for _ in range(count):
            intervals.append(random_interval(width, height, randomness))

        return intervals

    def sort_image_random_intervals(image: np.ndarray, count: int, randomness: float):
        sort_intervals(intervals)
        for interval in intervals:
            sort_line(image, interval[0][0], interval[0][1], interval[1][0], interval[1][1])

    def sort_image_horizontal_vertical(image: np.ndarray):
        sort_intervals(intervals)
        for interval in intervals:
            sort_line(image, interval[0][0], 0, interval[0][1], image.shape[0])
            sort_line(image, 0, interval[1][0], image.shape[1], interval[1][1])

    def sort_image_diagonal(image: np.ndarray):
        sort_intervals(intervals)
        for interval in intervals:
            sort_line(image, interval[0][0], interval[0][1], interval[1][0], interval[1][1])
            sort_line(image, interval[0][1], interval[0][0], interval[1][1], interval[1][0])

    def sort_image_custom(image: np.ndarray, custom_sort_function: Callable[[np.ndarray], np.ndarray]):
        sort_image_random_intervals(image, 1, 0.1)
        custom_sort_function(image)

    if len(intervals) == 0:
        intervals = random_intervals(size[0], size[1], 1, randomness)

    sort_image_custom(image_data, sorting_function)

@functools.cache
def lightness(pixel: Tuple[int, int, int]) -> float:
    r, g, b = pixel
    return (r + g + b) / 3

@functools.cache
def hue(pixel: Tuple[int, int, int]) -> float:
    r, g, b = pixel
    max_value = max(r, g, b)
    min_value = min(r, g, b)

    if max_value == min_value:
        return 0

    if max_value == r:
        h = (g - b) / (max_value - min_value)
    elif max_value == g:
        h = 2 + (b - r) / (max_value - min_value)
    else:
        h = 4 + (r - g) / (max_value - min_value)

    return (h + 1) / 6

@functools.cache
def saturation(pixel: Tuple[int, int, int]) -> float:
    max_value = max(pixel)
    if max_value == 0:
        return 0
    return (max_value - min(pixel)) / max_value

def intensity(pixel: Tuple[int, int, int]) -> int:
    return sum(pixel)

def minimum(pixel: Tuple[int, int, int]) -> int:
    return min(pixel)

choices = {
    "lightness": lightness,
    "hue": hue,
    "intensity": intensity,
    "minimum": minimum,
    "saturation": saturation
}