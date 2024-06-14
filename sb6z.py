import openai
import os

# Set your OpenAI API key
openai.api_key = "api-key"

# Function to read tags and captions from text files
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

# Read tags and captions
tags = read_file('---')
captions = read_file('---')

# Combine tags and captions into a dictionary
image_data = {}

# Parse tags
for tag_line in tags:
    if ": " in tag_line:
        img_name, img_tags = tag_line.split(": ", 1)
        img_tags = img_tags.strip()
        image_data[img_name] = {"tags": img_tags}

# Parse captions
current_image = None
for caption_line in captions:
    caption_line = caption_line.strip()
    if caption_line.endswith(".jpg:"):
        current_image = caption_line.split(":")[0]
        if current_image in image_data:
            image_data[current_image]["captions"] = []
        else:
            image_data[current_image] = {"captions": []}
    elif current_image and (caption_line.startswith("1:") or caption_line.startswith("2:") or caption_line.startswith("3:")):
        img_caption = caption_line.split(": ", 1)[1]
        image_data[current_image]["captions"].append(img_caption)

# Function to classify context using OpenAI's GPT-4
def classify_context(description):
    prompt = f"""
    Classify the following image description into one of these categories: Personal, Social, Professional.
    Choose the most appropriate category strictly from these three options.

    Description: {description}
    Category (Personal, Social, Professional):
    """
    
    for _ in range(3):  # Retry up to 3 times if the response is not valid
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Specify GPT-4 model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=10,
            temperature=0
        )
        category = response.choices[0].message['content'].strip()
        if category in ["Personal", "Social", "Professional"]:
            return category
    
    # If all retries fail, return a default category or handle the failure
    return "Personal"

# Analyze and classify each image
results = {}
for img_name, data in image_data.items():
    if "captions" in data and data["captions"]:
        description = f"Tags: {data['tags']}\nCaptions: {' '.join(data['captions'])}"
        category = classify_context(description)
        results[img_name] = category
    else:
        # If no captions are present, use tags for classification
        description = f"Tags: {data['tags']}"
        category = classify_context(description)
        results[img_name] = category

# Write results to a text file
output_file_path = '---'
with open(output_file_path, 'w') as output_file:
    for img_name, category in results.items():
        output_file.write(f"Image: {img_name}, Category: {category}\n")

print(f"Results have been written to {output_file_path}")
