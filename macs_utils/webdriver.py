from PIL import Image, ImageDraw, ImageChops
import sys
import os
import math
import macs_utils.images as im
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


def driver_init(browser: str = "chrome", *args, **kwargs) -> RemoteWebDriver:
    if browser.lower() == "chrome":
        return webdriver.Chrome(*args, **kwargs)
    elif browser.lower() == "firefox":
        return webdriver.Firefox(*args, **kwargs)
    elif browser.lower() == "safari":
        return webdriver.Safari(*args, **kwargs)
    elif browser.lower() == "edge":
        return webdriver.Edge(*args, **kwargs)
    else:
        raise ValueError("Wrong browser! Available browsers: chrome, firefox, safari, edge")
# GENERAL
def set_env_path(drivers_path: str):
    os.environ["PATH"] += ":" + drivers_path


# WEBDRIVER

def capture_screenshot(driver: RemoteWebDriver) -> Image:
    return im.base64_to_image(driver.get_screenshot_as_base64())


def window_size_with_added_offsets(browser: str, screen_target_width: int, screen_target_height: int,
                                   add_to_width: int = 0, add_to_height: int = 0, offsets: dict = None):
    return (
        screen_target_width + offsets[browser]['1366x768']["widthOffsetToAdd"] + add_to_width,
        screen_target_height + offsets[browser]['1366x768']["heightOffsetToAdd"] + add_to_height
    )


def set_right_bottom_corner(element: WebElement):
    element.right_bottom_corner = dict(
        x=element.rect["x"] + element.rect["width"],
        y=element.rect["y"] + element.rect["height"]
    )


def get_screen_size(driver: RemoteWebDriver):
    html = driver.find_element_by_tag_name("html")

    return (
        int(html.size["width"]),
        int(html.size["height"]),
    )


# TODO make scroll, scrollTo, scrollBy
def scroll_to(driver: RemoteWebDriver, x: int, y: int):
    driver.execute_script(f"window.scrollTo({x}, {y})")


def scroll_by(driver: RemoteWebDriver, x: int, y: int):
    driver.execute_script(f"window.scrollBy({x}, {y})")


# def scroll_to_element(driver: RemoteWebDriver, element: WebElement, x_margin: int = 0, y_margin=0):
#     screen_width, screen_height = get_screen_size(driver)
#     # TODO implement this method for element's larger/wider than screen
#
#     set_right_bottom_corner(element)
#
#     if element.right_bottom_corner["x"] + 2 * x_margin > screen_width:
#         scroll_x = element.right_bottom_corner["x"] + x_margin - screen_width
#     else:
#         scroll_x = 0
#
#     if element.right_bottom_corner["y"] + 2 * y_margin > screen_height:
#         scroll_y = element.right_bottom_corner["y"] + y_margin - screen_height
#     else:
#         scroll_y = 0
#
#     scroll_to(driver, scroll_x, scroll_y)


def take_partial_screenshot(driver: RemoteWebDriver, x1: int, y1: int, x2: int, y2: int) -> Image:
    screen = capture_screenshot(driver)
    return screen.crop((x1, y1, x2, y2))


def take_element_screenshot(driver: RemoteWebDriver, element: WebElement, x_margin: int = 0,
                            y_margin: int = 0, scroll_x: int = 0, scroll_y: int = 0):
    # ActionChains(driver).move_to_element(element).perform()
    #
    #
    # sleep(2)
    x1 = element.location_once_scrolled_into_view["x"] - x_margin
    y1 = element.location_once_scrolled_into_view["y"] - y_margin

    x2 = element.location_once_scrolled_into_view["x"] + element.size["width"] + x_margin
    y2 = element.location_once_scrolled_into_view["y"] + element.size["height"] + y_margin

    return take_partial_screenshot(driver, x1, y1, x2, y2)
