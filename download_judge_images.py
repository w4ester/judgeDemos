#!/usr/bin/env python3
"""
Judge Image Downloader

This script downloads judge images from Google Drive links and saves them
to the appropriate directory for use in the Cyber UXcellence Judges demo pages.
"""

import os
import re
import requests
import sys
from urllib.parse import urlparse, parse_qs

# Directory to save the images
IMAGES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images/judges")

# Make sure the directory exists
os.makedirs(IMAGES_DIR, exist_ok=True)

# List of judge names and their Google Drive links
JUDGES = [
    {"name": "ron-gula", "url": "https://drive.google.com/file/d/1KLRrAjZ-ax5f3bFyV9uRuQCgtDSJHc8U/view?usp=drive_link"},
    {"name": "troy-wilkinson", "url": "https://drive.google.com/file/d/1F-BXjOiCZnekCtcyF54oxwQSce-ckNaM/view?usp=drive_link"},
    {"name": "malcolm-harkins", "url": "https://drive.google.com/file/d/1PEO_Aj5NuyE3pqviAUVNc9OQK7-0cUQu/view?usp=drive_link"},
    {"name": "rinki-sethi", "url": "https://drive.google.com/file/d/13UqEDGnPURWq8KHnlrUIMADah199GNGc/view?usp=drive_link"},
    {"name": "damian-chung", "url": "https://drive.google.com/file/d/10c0gNXPetjuD6w80ZmUWn7JTpPil8mQP/view?usp=drive_link"},
    {"name": "nick-shevelyov", "url": "https://drive.google.com/file/d/1cIbx6PJgktFu1F4aw2ktn2mf2m443Obs/view?usp=drive_link"},
    {"name": "patricia-titus", "url": "https://drive.google.com/file/d/11CeXB3AOwgn-0coQV2hwd_yek59mF2NP/view?usp=drive_link"},
    {"name": "michael-baker", "url": "https://drive.google.com/file/d/1nVb5zKM9W9EnSlpoDMSKJKUjcJi2yarj/view?usp=drive_link"},
    {"name": "peter-kilpe", "url": "https://drive.google.com/file/d/1_IrYCoaydfCg2fpptE_gqPke9wOYUE5E/view?usp=drive_link"},
    {"name": "alicia-lynch", "url": "https://docs.google.com/presentation/d/14w8czYOAVF0FO0cn9SlDq8535MJi708q/edit?usp=drive_link&ouid=111856581302773520394&rtpof=true&sd=true"},
    {"name": "meagan-petri", "url": "https://drive.google.com/file/d/1B7pKPofA87X2IlRCOPloHdvca-CNBKaO/view?usp=drive_link"}
]

def extract_file_id(url):
    """Extract the Google Drive file ID from the URL."""
    parsed_url = urlparse(url)
    
    # Handle different Google Drive URL formats
    if parsed_url.path.startswith('/file/d/'):
        # For URLs like https://drive.google.com/file/d/FILE_ID/view
        file_id = parsed_url.path.split('/')[3]
    elif parsed_url.path.startswith('/presentation/d/'):
        # For Google Presentation URLs
        file_id = parsed_url.path.split('/')[3]
    elif 'id=' in parsed_url.query:
        # For URLs with id parameter
        query_params = parse_qs(parsed_url.query)
        file_id = query_params.get('id', [''])[0]
    else:
        # Try to find any alphanumeric pattern that looks like a file ID
        match = re.search(r'[-\w]{25,}', url)
        if match:
            file_id = match.group(0)
        else:
            raise ValueError(f"Could not extract file ID from URL: {url}")
    
    return file_id

def download_file(url, output_path):
    """Download a file from Google Drive."""
    file_id = extract_file_id(url)
    
    # Two different approaches to download from Google Drive
    approaches = [
        {
            'url': f"https://drive.google.com/uc?export=download&id={file_id}",
            'headers': {}
        },
        {
            'url': f"https://drive.google.com/uc?id={file_id}&export=download",
            'headers': {}
        }
    ]
    
    for approach in approaches:
        try:
            print(f"Trying to download with URL: {approach['url']}")
            response = requests.get(approach['url'], headers=approach['headers'], stream=True)
            
            # Check if the response is valid
            if response.status_code == 200 and int(response.headers.get('Content-Length', 0)) > 1000:
                # Save the file
                with open(output_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                print(f"Successfully downloaded to {output_path}")
                return True
        except Exception as e:
            print(f"Download attempt failed: {e}")
    
    print(f"Failed to download file from {url}")
    return False

def create_preview_images():
    """Create preview images for the design versions."""
    preview_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
    
    for i in range(1, 8):
        preview_path = os.path.join(preview_dir, f"preview-version{i}.jpg")
        
        # If preview doesn't exist, create a placeholder
        if not os.path.exists(preview_path):
            try:
                with open(preview_path, 'w') as f:
                    f.write(f"Placeholder for Version {i} preview image. Replace with an actual screenshot.")
                print(f"Created placeholder for preview-version{i}.jpg")
            except Exception as e:
                print(f"Failed to create preview placeholder: {e}")

def main():
    """Main function to download all judge images."""
    print(f"Downloading judge images to: {IMAGES_DIR}")
    
    # Download each judge image
    for judge in JUDGES:
        output_path = os.path.join(IMAGES_DIR, f"{judge['name']}.jpg")
        
        # Skip if file already exists
        if os.path.exists(output_path):
            print(f"File already exists: {output_path} - Skipping")
            continue
        
        print(f"Downloading image for {judge['name']}...")
        success = download_file(judge['url'], output_path)
        
        if not success:
            # Create a placeholder file
            with open(output_path, 'w') as f:
                f.write(f"Placeholder for {judge['name']}'s photo. Could not download from: {judge['url']}")
            print(f"Created placeholder file for {judge['name']}")
    
    # Create preview images
    create_preview_images()
    
    print("Done!")

if __name__ == "__main__":
    main()
