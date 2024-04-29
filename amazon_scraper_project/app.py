from flask import Flask, render_template, request, jsonify
from scrape import scrape_amazon_data
import urllib.parse

app = Flask(__name__)

# Function to extract the specified product title for searching on Flipkart
def extract_search_query(title):
    # Extract the specified product title
    search_query = title.split('|')[0].strip()
    return search_query

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['GET'])
def scrape():
    url = request.args.get('url')
    title, price, discount, mrp = scrape_amazon_data(url)
    if title and price and discount:
        # Extract the specified product title for searching on Flipkart
        search_query = extract_search_query(title)
        
        # Construct Flipkart search URL with the specified product title
        flipkart_search_url = "https://www.flipkart.com/search?q=" + urllib.parse.quote_plus(search_query)
        
        return jsonify({'success': True, 'title': title, 'price': price, 'discount': discount, 'mrp': mrp, 'flipkart_search_url': flipkart_search_url})
    else:
        return jsonify({'success': False})

if __name__ == "__main__":
    app.run(debug=True)