import os
import webbrowser
from googlesearch import search as google_search
from duckduckgo_search import DDGS
import re

def save_results(filename, results):
    """Save the results to a text file"""
    with open(filename, "w", encoding="utf-8") as file:
        for i, result in enumerate(results, 1):
            file.write(f"{i}. {result}\n")
    print(f"\n📁 Results saved to file: {filename}")

def internet_search(query, engine="google", num_results=100):
    """Search the query using the specified engine"""
    results = []
    if engine == "google":
        print(f"\n🔍 Searching for '{query}' using Google ...")
        results = list(google_search(query, num_results=num_results, lang="en"))
    elif engine == "duckduckgo":
        print(f"\n🔍 Searching for '{query}' using DuckDuckGo ...")
        with DDGS() as ddgs:
            ddg_results = ddgs.text(query, max_results=num_results)
            results = [r['href'] for r in ddg_results if 'href' in r]
    else:
        print("❌ Unsupported search engine.")
        return

    # Print and save the results
    for i, result in enumerate(results, 1):
        print(f"{i}. {result}")
    
    # Save results to file
    safe_query = query.strip().replace(" ", "_")
    filename = f"{safe_query}-{engine}.txt"
    save_results(filename, results)

def correct_and_open_urls():
    """Correct manually entered URLs and open them in the browser"""
    try:
        print("\nPlease enter the URLs in the following format:")
        print("1. https://example.com")
        print("2. https://anotherlink.com")
        print("...")

        urls = []
        while True:
            url = input("🔗 Enter a URL (or type 'done' to finish): ").strip()
            if url.lower() == 'done':
                break
            if url:
                # Correcting the URL format if it contains extra characters
                corrected_url = re.sub(r"^\d+\.\s*(https?://)", r"\1", url)  # Remove the number prefix
                corrected_url = corrected_url.strip()
                if corrected_url.startswith("https://") or corrected_url.startswith("http://"):
                    urls.append(corrected_url)
                else:
                    print(f"❌ Invalid URL format: {url}")
                    continue

        print("\n🚀 Opening all URLs in your browser...")
        for url in urls:
            webbrowser.open_new_tab(url)

        # Save the URLs to a file
        save_results("manual_urls.txt", urls)

    except ValueError:
        print("❌ Please enter a valid URL.")

def main():
    """Main function to run the program continuously"""
    while True:
        try:
            print("\n🌐 Choose an option:")
            print("1. Google Search")
            print("2. DuckDuckGo Search")
            print("3. Open Manual URLs")

            choice = input("Enter your choice (1, 2, or 3): ").strip()

            if choice == "1":
                query = input("🔎 Enter the search keyword: ").strip()
                internet_search(query, "google")
            elif choice == "2":
                query = input("🔎 Enter the search keyword: ").strip()
                internet_search(query, "duckduckgo")
            elif choice == "3":
                correct_and_open_urls()
            else:
                print("❗ Invalid choice. Please enter 1, 2, or 3 only.")

        except KeyboardInterrupt:
            print("\n🚫 Program interrupted by user.")
            break

if __name__ == "__main__":
    main()
