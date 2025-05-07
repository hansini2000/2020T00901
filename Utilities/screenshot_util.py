import os
from datetime import datetime

def take_screenshot(driver, name):
    screenshots_dir = os.path.join(os.getcwd(), "Screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{name}_{timestamp}.png"
    filepath = os.path.join(screenshots_dir, filename)

    driver.save_screenshot(filepath)
    print(f"📸 Screenshot saved: {filepath}")
