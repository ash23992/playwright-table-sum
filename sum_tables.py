from playwright.sync_api import sync_playwright
import re

seeds = list(range(4, 14))  # Seeds 4 to 13
total_sum = 0

def extract_numbers(page):
    tables = page.query_selector_all("table")
    page_sum = 0

    for table in tables:
        text = table.inner_text()
        numbers = re.findall(r"-?\d+\.?\d*", text)
        page_sum += sum(float(n) for n in numbers)

    return page_sum


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    for seed in seeds:
        url = f"https://sanand0.github.io/tdsdata/js_table/?seed={seed}"
        print(f"Loading {url}")
        page.goto(url)
        page.wait_for_load_state("networkidle")

        seed_sum = extract_numbers(page)
        print(f"Seed {seed} sum:", seed_sum)

        total_sum += seed_sum

    browser.close()

print("FINAL_TOTAL_SUM =", total_sum)
