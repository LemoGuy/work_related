from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    # Get form data
    url = request.form.get('url')
    tag = request.form.get('tag')
    css_class = request.form.get('class')

    if not url or not tag:
        return jsonify({"error": "URL and HTML tag are required!"}), 400

    try:
        # Request the website
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find elements based on user input
        if css_class:
            containers = soup.find_all(tag, class_=css_class)
        else:
            containers = soup.find_all(tag)

        # Collect all text content from the specified containers
        data = []
        for container in containers:
            # Get all inner elements (e.g., <p>) inside the container
            for inner_element in container.find_all():
                data.append(inner_element.get_text(strip=True))

        # Ensure we have data to save
        if not data:
            return jsonify({"error": "No data found with the specified criteria!"}), 400

        # Create a DataFrame
        df = pd.DataFrame(data, columns=['Extracted Data'])

        # Define the folder to save files
        output_folder = 'scraped_files'
        os.makedirs(output_folder, exist_ok=True)  # Create folder if it doesn't exist

        # Generate a unique filename with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = os.path.join(output_folder, f'scraped_data_{timestamp}.xlsx')

        # Save the file in the designated folder
        df.to_excel(output_file, index=False)

        return jsonify({"success": True, "message": f"Data scraped successfully! Saved to {output_file}."})

    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
