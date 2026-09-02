import os
from tavily import TavilyClient


def find_evidence(claim):

    client = TavilyClient(
        api_key=os.getenv("TAVILY_API_KEY")
    )

    results = client.search(
        query=claim,
        max_results=3
    )

    evidence = []

    for result in results["results"]:
        evidence.append({
            "title": result["title"],
            "url": result["url"],
            "content": result["content"]
        })

    return evidence
