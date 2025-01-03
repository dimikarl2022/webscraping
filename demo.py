from scraper import scrape_website

def main():
    url = "https://example.com"
    print(f"Demonstrating advanced scraper with {url}")
    
    # Example with filters and JSON export
    content = scrape_website(
        url,
        filters={
            "min_length": 10,
            "keywords": ["content", "section"]
        },
        export_format="json",
        export_path="scraped_content.json"
    )
    
    print("\nExtracted content:")
    print(f"Title: {content.title}")
    print("\nHeadings:")
    for heading in content.headings:
        print(f"- {heading}")
    
    print("\nParagraphs:")
    for para in content.paragraphs:
        print(f"- {para}")
    
    print("\nMetadata:")
    for key, value in content.metadata.items():
        print(f"- {key}: {value}")

if __name__ == "__main__":
    main()