import re

def website_split():
    # Example string containing multiple websites
    websites_string = """
    JTI: https://www.linkedin.com/company/jti/
    """

    # Splitting using newline character as delimiter
    websites_list = websites_string.split("\n")

    # Extracting websites using regular expression pattern
    pattern = r"(www\.[^\s]+)"
    websites = [re.search(pattern, website).group() for website in websites_list if re.search(pattern, website)]

    # Printing the extracted websites
    for website in websites:
        print(website)

website_split()

