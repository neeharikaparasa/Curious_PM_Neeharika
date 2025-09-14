# Load packages for API requests and timestamp generation
import requests
from datetime import datetime

def screenshot(url, mobile=False, dark=False):
    # API key for authentication with ScreenshotOne service
    access_key = "GF79y21HQ0WHfg"  # Get from screenshotone.com dashboard
    
    # Build query string with basic screenshot parameters
    params = f"access_key={access_key}&url={url}&full_page=true&block_ads=true&block_cookie_banners=true"
    
    # Add mobile device parameters if requested
    if mobile: 
        params += "&device_scale_factor=2&viewport_width=375&viewport_height=667"
    
    # Add dark mode parameter if requested
    if dark: 
        params += "&dark_mode=true"
    
    # Make API request and get binary image data
    img_data = requests.get(f"https://api.screenshotone.com/take?{params}").content
    
    # Generate unique filename with current timestamp
    filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    
    # Write binary image data to file
    open(filename, 'wb').write(img_data)
    
    # Confirm screenshot was saved successfully
    print(f"📸 Screenshot saved: {filename}")

# Get website URL from user and take screenshot
url = input("Enter website URL: ")
screenshot(url, mobile=True, dark=True)