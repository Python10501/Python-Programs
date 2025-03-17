#Retrieval Augmented Generation

from exa_py import Exa

exa = Exa("API KEY REMOVED FOR SECURITY")

result = exa.search_and_contents(
    "Top 10 AI startups",
    text=True
)

print(result)