from PIL import Image
from realesrgan import RealESRGAN
import torch


class Upscaler():
    def __init__(self,listPhotos):
        self.images = listPhotos