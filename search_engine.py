from exa_py import Exa

exa = Exa("API KEY REMOVED FOR SECURITY")

query = input("Search here: ")

response = exa.search(
    query,
    num_results=5,
    type="keyword",
    include_domains=["https://www.wikipedia.org/"],
)

for result in response.results:
    print(f"Title: {result.title}")
    print(f"URL: {result.url}")
    print()