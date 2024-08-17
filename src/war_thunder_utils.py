import json
import os
import re
import tempfile
import shutil

def load_partial_json(file_path):
    """
    Load a JSON file partially to handle large files or files with potential corruption.
    """
    try:
        with open(file_path, 'r') as f:
            data = f.read()
            # Attempt to load the JSON data
            return json.loads(data[:data.rfind('}')+1])
    except Exception as e:
        print(f"Failed to load JSON from {file_path}: {e}")
        return []

def save_data_to_json(data, output_file, visited_urls, visited_urls_file):
    """
    Save data to JSON files using temporary files for atomic operations.
    """
    try:
        # Save data to a temporary file
        with tempfile.NamedTemporaryFile(mode='w', delete=False, dir='.') as tmp_file:
            json.dump(data, tmp_file, indent=4)
            temp_file_path = tmp_file.name
        shutil.move(temp_file_path, output_file)
        print(f"Data saved to {output_file}")

        # Save visited URLs to a temporary file
        with tempfile.NamedTemporaryFile(mode='w', delete=False, dir='.') as tmp_file:
            json.dump(list(visited_urls), tmp_file, indent=4)
            temp_file_path = tmp_file.name
        shutil.move(temp_file_path, visited_urls_file)
        print(f"Visited URLs saved to {visited_urls_file}")
    except Exception as e:
        print(f"Failed to save data: {e}")

def extract_hashtags(description):
    """
    Extract hashtags from a given text description.
    """
    return re.findall(r"#(\w+)", description) if description else []

def extract_image_urls(item):
    """
    Extract image URLs from a BeautifulSoup item.
    """
    return [img.get("src") for img in item.find_all("img")]

def process_camouflage_item(item, vehicle_name):
    """
    Process a camouflage item from BeautifulSoup and extract relevant information.
    """
    post_id = item.get("post_id")
    user = item.find("a", class_="nickname").text.strip()
    date = item.find("a", class_="date").text.strip()
    description = item.find("div", class_="description").text.strip() if item.find("div", class_="description") else None
    hashtags = extract_hashtags(description)
    image_urls = extract_image_urls(item)
    download_link_tag = item.find("a", class_="downloads button_item")
    download_link = download_link_tag.get("href") if download_link_tag else None

    return {
        "post_id": post_id,
        "user": user,
        "date": date,
        "description": description,
        "hashtags": hashtags,
        "vehicle_name": vehicle_name,
        "image_urls": image_urls,
        "download_link": download_link
    }
