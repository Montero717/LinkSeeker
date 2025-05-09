import os
import webbrowser
from googlesearch import search as google_search
from duckduckgo_search import DDGS
import re
from colorama import Fore, Style, init
init(autoreset=True)

print(Fore.RED + r"""

██╗     ██╗███╗   ██╗██╗  ██╗    ███████╗███████╗███████╗██╗  ██╗███████╗██████╗ 
██║     ██║████╗  ██║██║ ██╔╝    ██╔════╝██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║     ██║██╔██╗ ██║█████╔╝     ███████╗█████╗  █████╗  █████╔╝ █████╗  ██████╔╝
██║     ██║██║╚██╗██║██╔═██╗     ╚════██║██╔══╝  ██╔══╝  ██╔═██╗ ██╔══╝  ██╔══██╗
███████╗██║██║ ╚████║██║  ██╗    ███████║███████╗███████╗██║  ██╗███████╗██║  ██║
╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝    ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     
---------------------------------------------------------------------------------""")

def save_results(filename, results):
    """Save the results to a text file"""
    with open(filename, "w", encoding="utf-8") as file:
        for i, result in enumerate(results, 1):
            file.write(f"{i}. {result}\n")
    print(f"\n📁 Results saved to file: {filename}")

def internet_search(query, engine="google", num_results=10):
    """Search the query using the specified engine"""
    results = []

    # Print search message temporarily
    print(f"🔍 Searching for '{query}' using {engine.capitalize()} ...", end="\r")

    if engine == "google":
        for i, result in enumerate(google_search(query, num_results=num_results, lang="en"), 1):
            if i == 1:
                print(" " * 80, end="\r")  # Clear the "Searching..." message
            print(f"{i}. {result}")
            results.append(result)

    elif engine == "duckduckgo":
        with DDGS() as ddgs:
            for i, r in enumerate(ddgs.text(query, max_results=num_results), 1):
                if 'href' in r:
                    if i == 1:
                        print(" " * 80, end="\r")  # Clear the "Searching..." message
                    print(f"{i}. {r['href']}")
                    results.append(r['href'])

    else:
        print("❌ Unsupported search engine.")
        return

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
                corrected_url = re.sub(r"^\d+\.\s*(https?://)", r"\1", url)
                corrected_url = corrected_url.strip()
                if corrected_url.startswith("https://") or corrected_url.startswith("http://"):
                    urls.append(corrected_url)
                else:
                    print(f"❌ Invalid URL format: {url}")
                    continue

        print("\n🚀 Opening all URLs in your browser...")
        for url in urls:
            webbrowser.open_new_tab(url)

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

            if choice in ("1", "2"):
                query = input("🔎 Enter the search keyword: ").strip()
                while True:
                    try:
                        num = int(input("🔢 How many links do you want? "))
                        break
                    except ValueError:
                        print("❗ Please enter a valid number.")
                engine = "google" if choice == "1" else "duckduckgo"
                internet_search(query, engine, num_results=num)
            elif choice == "3":
                correct_and_open_urls()
            else:
                print("❗ Invalid choice. Please enter 1, 2, or 3 only.")

        except KeyboardInterrupt:
            print("\n🚫 Program interrupted by user.")
            break

if __name__ == "__main__":
    main()
