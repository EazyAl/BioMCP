# server.py

from mcp.server.fastmcp import FastMCP
import requests

# Create an MCP server instance with a custom name
mcp = FastMCP("PubMed MVP")

@mcp.tool()
def search_pubmed(q: str) -> dict:
    """
    A tool to search PubMed using the E-utilities API.

    Parameters:
      - q: The search query string

    Returns a dict containing the PubMed JSON response.
    """
    if not q:
        return {"error": "Please provide a query."}
    
    # Define PubMed ESearch API parameters
    params = {
        "db": "pubmed",
        "term": q,
        "retmode": "json",
        "retmax": 5  # limit to 5 results for this MVP example
    }
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    
    # Make the API request to PubMed
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise exception for bad responses
    except requests.RequestException as e:
        return {"error": str(e)}
    
    # Return the JSON response to the caller
    return response.json()

if __name__ == "__main__":
    # Run the MCP server
    mcp.run()