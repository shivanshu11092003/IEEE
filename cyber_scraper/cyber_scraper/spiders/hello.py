import requests
import pprint  # For better data visualization
from transformers import pipeline  # For summarization
import spacy  # For NLP tasks

# Load the spaCy model (make sure to install it using `python -m spacy download en_core_web_sm`)
nlp = spacy.load("en_core_web_sm")

# Function to fetch data from the API
def fetch_data_from_api(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return JSON data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Function to summarize content using a pre-trained ML model
def summarize_content(content):
    summarizer = pipeline("summarization")
    if len(content) > 50:  # Check length
        summary = summarizer(content, max_length=150, min_length=40, do_sample=False)
        return summary[0]['summary_text']
    else:
        return "Content is too short to summarize."

# Function to extract related words using spaCy
def extract_related_words(content):
    doc = nlp(content)  # Process the text with spaCy
    related_words = set()  # Use a set to avoid duplicates
    for token in doc:
        if token.is_alpha and not token.is_stop:  # Check if the token is a word and not a stop word
            related_words.add(token.lemma_)  # Use the lemma (base form) of the word
    return list(related_words)

# Function to post related words back to the API
def post_related_words(api_url, related_words):
    try:
        response = requests.post(api_url, json={"related_words": related_words})
        response.raise_for_status()  # Raise an error for bad responses
        print("Successfully posted related words.")
    except requests.exceptions.RequestException as e:
        print(f"Error posting related words: {e}")

# Main function to run the workflow
def main():
    api_url = 'http://10.21.97.82:8000/NeuraSecure/list_data/'  # API URL to fetch data from
    data = fetch_data_from_api(api_url)  # Fetch data from the API

    if data:
        # Attempt to convert the data to a list if it is not one
        if isinstance(data, dict):
            # If data is a dictionary, check for a key that holds a list
            if 'items' in data:  # Example key that may contain a list
                data = data['items']
            else:
                # If there are multiple keys, you can consolidate the values into a list
                data = list(data.values())
        
        # Check if the response is now in the expected format
        if isinstance(data, list):
            for item in data:
                if 'content' in item:  # Check if 'content' key exists
                    content = item['content']
                    summary = summarize_content(content)
                    related_words = extract_related_words(content)
                    
                    print(f"Original Content: {content}")
                    print(f"Summary: {summary}")
                    print(f"Related Words: {related_words}\n")
                    
                    # Post related words to the API
                    post_api_url = 'http://10.21.97.82:8000/NeuraSecure/post_related_words/'  # Update with the correct URL
                    post_related_words(post_api_url, related_words)
        else:
            print("Data format could not be converted to a list. Here is the received data:")
            pprint.pprint(data)  # Print the data to understand its structure

if __name__ == "__main__":
    main()
