import requests

url = "https://pro-gamer.pl"


def download_site(url):
    """
    Downloads the HTML content of a website based on the provided URL.

    Args:
        url (str): The URL of the website to be downloaded.

    Returns:
        None
    """

    # Create a session object to make the GET request to the URL
    with requests.Session() as session:
        # Send a GET request to the URL and receive the response
        response = session.get(url, stream=True)

        # Raise an exception if the response indicates an error
        response.raise_for_status()

        # Open a file named "index.html" in write binary mode
        # and write the response content in chunks
        with open("index.html", "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

    # Print a success message
    print("Page downloaded successfully.")


download_site(url)
