from bs4 import BeautifulSoup
import requests
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("API_KEY")

genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")


def generate_itinerary(destination, start_date, end_date, no_of_day, budget, activities):
    prompt = f"""
    Generate a personalized trip itinerary for a {no_of_day}-day trip to {destination} from {start_date} to {end_date},
    with a budget of {budget}(Currency:INR). Recommend and personalize as per the following activities: {activities}. Also include links to good hotel booking websites
    and flight/train booking options, along with approximate travel durations.
    Please provide a detailed itinerary for each day, including recommendations for activities, places to visit, where to stay, and dining options.
    Tailor the suggestions based on the length of the trip, and consider travel time between the source and destination. Also include maps or links to maps if possible.
    Also include the must not forget items for the trip.
    """
    response = model.generate_content(prompt)
    return (response.text)


# def scrape_images(destination):
#     url = f"https://en.wikipedia.org/wiki/{destination.replace(' ', '_')}"
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')

#     images = []
#     for img in soup.find_all('img'):
#         img_url = img.get('src')
#         if img_url.startswith('//'):
#             img_url = 'https:' + img_url
#         images.append(img_url)
#         if len(images) == 6:
#             break

#     return images


def scrape_images(destination, limit=6):
    # Step 1: Search for relevant pages for the destination
    search_url = "https://commons.wikimedia.org/w/api.php"
    search_params = {
        "action": "query",
        "list": "search",
        "srsearch": destination,
        "srlimit": limit,
        "format": "json"
    }
    search_response = requests.get(search_url, params=search_params)
    search_data = search_response.json()

    images = []
    keywords = destination.lower().split()

    # Step 2: For each result, find if the page contains images
    for item in search_data.get("query", {}).get("search", []):
        page_title = item["title"]

        # Fetch images from the page
        image_info_url = "https://commons.wikimedia.org/w/api.php"
        image_info_params = {
            "action": "query",
            "prop": "images",
            "titles": page_title,
            "format": "json"
        }
        image_info_response = requests.get(
            image_info_url, params=image_info_params)
        image_info_data = image_info_response.json()

        # Step 3: Extract the file names of the images and make another request to get their URLs
        pages = image_info_data.get("query", {}).get("pages", {})
        for page in pages.values():
            images_prop = page.get("images", [])
            for image in images_prop:
                image_file_name = image["title"]

                # Step 4: Get the actual image URL from the file name, but only if relevant
                file_info_url = "https://commons.wikimedia.org/w/api.php"
                file_info_params = {
                    "action": "query",
                    "titles": image_file_name,
                    "prop": "imageinfo|categories",
                    "iiprop": "url|extmetadata",
                    "format": "json"
                }
                file_info_response = requests.get(
                    file_info_url, params=file_info_params)
                file_info_data = file_info_response.json()

                file_pages = file_info_data.get("query", {}).get("pages", {})
                for file_page in file_pages.values():
                    # Check file categories
                    categories = file_page.get("categories", [])
                    category_names = [cat["title"].lower()
                                      for cat in categories]

                    # Check image description
                    imageinfo = file_page.get("imageinfo", [])
                    if imageinfo:
                        extmetadata = imageinfo[0].get("extmetadata", {})
                        description = extmetadata.get(
                            "ImageDescription", {}).get("value", "").lower()
                        image_url = imageinfo[0]["url"]

                        # Check if any keyword matches in category names or description
                        if any(keyword in ' '.join(category_names) for keyword in keywords) or \
                           any(keyword in description for keyword in keywords) or \
                           any(keyword in image_file_name.lower() for keyword in keywords):
                            images.append(image_url)

                # Stop if we reach the limit
                if len(images) >= limit:
                    break

        if len(images) >= limit:
            break

    return images
