import argparse
import csv
import re
import sys
from Bio import Entrez

# Set email for PubMed API usage
Entrez.email = "shubhammittal588@gmail.com"

def fetch_pubmed_papers(query, debug=False):
    """Fetch papers from PubMed based on a query."""
    try:
        handle = Entrez.esearch(db="pubmed", term=query, retmax=10)
        record = Entrez.read(handle)
        handle.close()

        pmids = record["IdList"]
        if debug:
            print(f"Found {len(pmids)} papers")

        papers = []
        for pmid in pmids:
            details = Entrez.efetch(db="pubmed", id=pmid, rettype="medline", retmode="text")
            text = details.read()
            details.close()

            paper = parse_paper_details(text)
            if paper:
                papers.append(paper)

        return papers
    except Exception as e:
        print(f"Error fetching papers: {e}", file=sys.stderr)
        return []

def parse_paper_details(text):
    """Extract relevant details from PubMed entry."""
    lines = text.split("\n")
    paper = {"PubmedID": None, "Title": None, "Publication Date": None, "Non-academic Author(s)": [], 
             "Company Affiliation(s)": [], "Corresponding Author Email": None}

    affiliations = []
    current_affiliation = None

    for line in lines:
        if line.startswith("PMID- "):
            paper["PubmedID"] = line.split("- ")[1].strip()
        elif line.startswith("TI  - "):
            paper["Title"] = line.split("- ")[1].strip()
        elif line.startswith("DP  - "):
            paper["Publication Date"] = line.split("- ")[1].strip()
        elif line.startswith("AD  - "):
            current_affiliation = line.split("- ")[1].strip()
            affiliations.append(current_affiliation)
        elif line.startswith("    "):
            if current_affiliation:
                current_affiliation += " " + line.strip()
                affiliations[-1] = current_affiliation

    # Extract company-affiliated authors
    for aff in affiliations:
        if any(word in aff.lower() for word in ["pharma", "biotech", "inc", "ltd", "corp"]):
            paper["Company Affiliation(s)"].append(aff)

    return paper if paper["Company Affiliation(s)"] else None

def save_to_csv(papers, filename):
    """Save the extracted papers to a CSV file."""
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=papers[0].keys())
        writer.writeheader()
        writer.writerows(papers)
    print(f"Results saved to {filename}")


def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed research papers with non-academic authors.")
    parser.add_argument("query", help="Search query for PubMed")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    parser.add_argument("-f", "--file", help="Output CSV file name")
    
    args = parser.parse_args()
    
    papers = fetch_pubmed_papers(args.query, args.debug)
    
    if not papers:
        print("No papers found with non-academic affiliations.")
        return
    
    if args.file:
        save_to_csv(papers, args.file)
    else:
        for paper in papers:
            print(paper)

if __name__ == "__main__":
    main()
