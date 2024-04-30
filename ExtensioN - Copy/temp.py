# import requests
# from bs4 import BeautifulSoup

# # Replace 'your_amazon_product_url' with the actual Amazon product URL
# url = 'https://www.amazon.in/Display-Speakers-6000mAh-Charger-Interface/dp/B0CX1PNZN2/?_encoding=UTF8&pd_rd_w=m4IUv&content-id=amzn1.sym.4d5b78c6-4f80-4b93-8d16-deb7aaa19e3f%3Aamzn1.symc.afd86303-4a72-4e34-8f6b-19828329e602&pf_rd_p=4d5b78c6-4f80-4b93-8d16-deb7aaa19e3f&pf_rd_r=225T8PC2H8DGW6DA5SBJ&pd_rd_wg=UJun7&pd_rd_r=a71e6420-a3c8-4a50-b876-b61ccf88649a&ref_=pd_gw_ci_mcx_mr_hp_atf_m&th=1'

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
# }

# response = requests.get(url, headers=headers)

# # Check if the GET request was successfultemp.py
# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # Find the span element containing the rating
#     rating_span = soup.find('span', {'id': 'acrPopover'})

#     if rating_span:
#         rating_text = rating_span['title']
#         print(f'Product rating: {rating_text}')
#     else:
#         print('Rating not found')
# else:
#     print(f'Failed to fetch the webpage. Status code: {response.status_code}')



import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# Replace 'your_amazon_product_url' with the actual Amazon product URL
url = 'https://www.amazon.in/Display-Speakers-6000mAh-Charger-Interface/dp/B0CX1PNZN2/?_encoding=UTF8&pd_rd_w=m4IUv&content-id=amzn1.sym.4d5b78c6-4f80-4b93-8d16-deb7aaa19e3f%3Aamzn1.symc.afd86303-4a72-4e34-8f6b-19828329e602&pf_rd_p=4d5b78c6-4f80-4b93-8d16-deb7aaa19e3f&pf_rd_r=225T8PC2H8DGW6DA5SBJ&pd_rd_wg=UJun7&pd_rd_r=a71e6420-a3c8-4a50-b876-b61ccf88649a&ref_=pd_gw_ci_mcx_mr_hp_atf_m&th=1'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get(url, headers=headers)

# Check if the GET request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the span element containing the deal information
    deal_element = soup.find('span', {'id': 'dealBadgeSupportingText'})

    # Calculate yesterday's date
    yesterday_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

    if deal_element:
        # Extract the deal information
        deal = deal_element.span.text.strip()

        # Check if the deal was available yesterday
        if deal:
            print(f"Yesterday's deal: {deal}")
        else:
            print("No deal available for yesterday.")
    else:
        print("Deal information not found.")
else:
    print(f'Failed to fetch the webpage. Status code: {response.status_code}')