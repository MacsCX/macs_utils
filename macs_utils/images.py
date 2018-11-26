from PIL import Image, ImageDraw, ImageChops
import sys
import os
import math
from macs_utils import utils as u
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


# IMAGE PROCESSING
def draw_diff(image1: Image, image2: Image, tolerance: int = 5, color: str = "magenta") -> Image:
    image1_copy = image1.copy()
    image_diff = ImageChops.difference(image1, image2).convert("RGB")

    draw = ImageDraw.Draw(image1_copy)

    width, height = image_diff.size

    for w in range(width):
        for h in range(height):

            pixel = image_diff.getpixel((w, h))

            if sum(pixel) >= int(255 * 3 * tolerance / 100):
                draw.rectangle((w, h, w + 1, h + 1), fill=color)

    return image1_copy


def arrange_images_vertically(images: list, descriptions: list = [], desc_row_height: int = 0,
                              background_color: str = 'white', desc_color: str = 'black') -> Image:
    result_height = sum([im.size[1] for im in images]) + desc_row_height * len(images)
    result_width = max(*[im.size[0] for im in images])

    result = Image.new("RGBA", (result_width, result_height), background_color)
    draw = ImageDraw.Draw(result)

    iterated_y = 0

    for m in range(len(images)):
        image_y = iterated_y + desc_row_height
        text_y = iterated_y + int(desc_row_height / 2) - 5

        draw.text(text=descriptions[m], xy=(10, text_y), fill=desc_color)
        result.paste(images[m], (0, image_y))

        iterated_y += images[m].size[1] + desc_row_height

    return result


def arrange_images_horizontally(images: list, descriptions: list = [], desc_row_height: int = 0,
                                background_color: str = 'white', dilatation: int = 0,
                                desc_color: str = 'black') -> Image:
    result_height = max(*[im.size[1] for im in images]) + desc_row_height
    result_width = sum([im.size[0] for im in images])

    result = Image.new("RGBA", (result_width, result_height), background_color)
    draw = ImageDraw.Draw(result)

    iterated_x = 0
    text_y = int(desc_row_height / 2) - 5
    for m in range(len(images)):
        result.paste(images[m], (iterated_x, desc_row_height))
        draw.text(text=descriptions[m], xy=(iterated_x + 10, text_y), fill=desc_color)

        iterated_x += images[m].size[0] + dilatation

    return result
