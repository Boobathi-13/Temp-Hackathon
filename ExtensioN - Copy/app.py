from flask import Flask, render_template, request, jsonify, redirect
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
    return render_template('popup.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form.get('url')
    title, price, discount, mrp, rating, deal = scrape_amazon_data(url)
    if title and price and discount:
        search_query = extract_search_query(title)
        flipkart_search_url = "https://www.flipkart.com/search?q=" + urllib.parse.quote_plus(search_query)
        return jsonify({'success': True, 'title': title, 'price': price, 'discount': discount, 'mrp': mrp, 'rate': rating, 'fakeUrgency': deal, 'flipkart_search_url': flipkart_search_url})
    else:
        return jsonify({'success': False})

@app.route('/open_flipkart', methods=['GET'])
def open_flipkart():
    title = request.args.get('title')
    search_query = extract_search_query(title)
    flipkart_search_url = "https://www.flipkart.com/search?q=" + urllib.parse.quote_plus(search_query)
    return redirect(flipkart_search_url)

if __name__ == "__main__":
    app.run(debug=True)
