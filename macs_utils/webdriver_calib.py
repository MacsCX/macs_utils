#!/usr/local/bin/python3.6

import argparse
import os
from time import sleep

from selenium import webdriver

from macs_utils import utils as u
from macs_utils import webdriver as wb

parser = argparse.ArgumentParser()
parser.add_argument('browser', help='Browser to calibrate: chrome, firefox, safari')
parser.add_argument('calib_file_path', help='JSON file with calibration data')
parser.add_argument('--width', help='target window width')
parser.add_argument('--height', help='target window height')
parser.add_argument('--save_screen', action='store_true', help='save calib screenshot')
args = parser.parse_args()

browser = args.browser.lower()
calib_file_path = args.calib_file_path
target_width = args.width or 1366
target_height = args.height or 768
is_screen_to_save = args.save_screen

target_width = int(target_width)
target_height = int(target_height)

# Choose browser
if browser == "chrome":
    driver = webdriver.Chrome()

elif browser == "firefox":
    driver = webdriver.Firefox()

elif browser == "safari":
    driver = webdriver.Safari()
else:
    driver = webdriver.Chrome()

# Find and read calib file
if os.path.exists(calib_file_path):
    browsers_calib = u.read_json_file(calib_file_path)
else:
    browsers_calib = {}
    browsers_calib[browser] ={}
    
if not browser in browsers_calib.keys():
    browsers_calib[browser] = {}

driver.set_window_position(0, 0)
driver.set_window_size(target_width, target_height)
driver.get("https://www.rapidtables.com/web/tools/window-size.html")
sleep(3)
driver.find_element_by_xpath("//a[@aria-label='dismiss cookie message']").click() # cookie message
sleep(1)

date_of_calib = u.pretty_dt_now()

calib_screenshot = wb.capture_screenshot(driver)
width, height = calib_screenshot.size

width_offset = target_width - width
height_offset = target_height - height

browsers_calib[browser][f'{target_width}x{target_height}'] = {'dateOfCalib': date_of_calib, 'widthOffsetToAdd': width_offset, 'heightOffsetToAdd': height_offset}
u.save_to_json(browsers_calib, calib_file_path)

driver.close()

if is_screen_to_save:
    calib_screenshot.save(f'{browser}_{target_width}x{target_height}_{date_of_calib}.png')

print(f"Browser: {browser}")
print(f"Target size: {target_width} x {target_height}")
print(f"\nWidth offset to add: {width_offset}")
print(f"Height offset to add: {height_offset}")

