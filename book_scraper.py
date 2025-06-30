from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Step 1: Open the browser
driver = webdriver.Chrome()
driver.get("http://books.toscrape.com/")

# Step 2: Scrape data
books = []
book_elements = driver.find_elements(By.CLASS_NAME, "product_pod")

for book in book_elements:
    title = book.find_element(By.TAG_NAME, "h3").text
    price = book.find_element(By.CLASS_NAME, "price_color").text
    rating = book.get_attribute("class").split()[-1]

    books.append({
        "Title": title,
        "Price": price,
        "Rating": rating
    })

# Step 3: Save data to CSV
df = pd.DataFrame(books)
df.to_csv("books_data.csv", index=False)

print("✅ Data saved to books_data.csv")

# Step 4: Close browser
driver.quit()

