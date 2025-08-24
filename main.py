from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
soup = BeautifulSoup(response.text, "html.parser")

# Create a list of all the links on the page using a CSS Selector
all_link_elements = soup.select(".StyledPropertyCardDataWrapper a")
all_links = [link["href"] for link in all_link_elements]
# print(f"There are {len(all_links)} links to individual listings in total: \n")
# print(all_links)

# Create a list of all the addresses on the page using a CSS Selector
all_address_elements = soup.select(".StyledPropertyCardDataWrapper address")
all_addresses = [address.get_text().replace(" | ", " ").strip() for address in all_address_elements]
# print(f"\n After having been cleaned up, the {len(all_addresses)} addresses now look like this: \n")
# print(all_addresses)

# Create a list of all the prices on the page using a CSS Selector
all_price_elements = soup.select(".PropertyCardWrapper span")
all_prices = [price.get_text()[:6] for price in all_price_elements if "$" in price.get_text()]
print(f"\n After having been cleaned up, the {len(all_prices)} prices now look like this: \n")
print(all_prices)