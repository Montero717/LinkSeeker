# LinkSeeker
This is a simple and interactive Python tool that helps you search the web using Google or DuckDuckGo directly from the command line. It also lets you enter and open URLs manually, fixing any formatting issues automatically. All search results and URLs are saved in text files so you can revisit them anytime.

# Internet Search Tool

An interactive Python tool that helps you search the web using Google or DuckDuckGo directly from the command line. It also lets you manually input and open URLs in your browser, automatically fixing any formatting issues. All search results and URLs are saved in text files for easy reference.

---

## 🔧 Features

- **Google Search**: Perform web searches via Google.
- **DuckDuckGo Search**: Perform web searches via DuckDuckGo.
- **Manual URL Input**: Enter URLs manually; the tool corrects formatting and opens them in your default browser.
- **Result Saving**: Search results and URLs are saved in `.txt` files for later review.
- **Simple CLI**: User-friendly command-line interface.

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```
2. Install dependencies:
   ```bash
   pip install google duckduckgo-search
   ```

*Requires Python 3.6+.*

---

## 🚀 Usage

Run the main script:

```bash
python main.py
```

Follow the prompts:

1. **Google Search**: Enter `1`, then type your query.
2. **DuckDuckGo Search**: Enter `2`, then type your query.
3. **Open Manual URLs**: Enter `3`, then input URLs one by one.

To exit, press `Ctrl+C`.

---

## 📁 Output Files

- Searches are saved as:
  - `your_query-google.txt`
  - `your_query-duckduckgo.txt`
- Manual URLs are saved to `manual_urls.txt`.

---

## 📝 Example

```bash
Enter your choice (1, 2, or 3): 1
🔎 Enter the search keyword: AI tools for students
🔍 Searching for 'AI tools for students' using Google ...
1. https://example1.com
2. https://example2.com
...
📁 Results saved to file: AI_tools_for_students-google.txt
```

---

## 📄 License

This tool is open-source and available under the MIT License. Feel free to use and modify it!

---

## 🧠 Credits

- Developed by [montero75hz].
- Powered by [discord.py](https://discordpy.readthedocs.io/).

---

*Search smarter, open links faster—all from your terminal.*

