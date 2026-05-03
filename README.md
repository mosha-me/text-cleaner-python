# text-cleaner-python
A simple Python script to clean strings by removing special characters, leading/trailing spaces, and converting text to lowercase.

# 🧹 Simple Python Text Cleaner

A lightweight and efficient Python utility function designed to sanitize and format messy strings. 

### 🚀 Use Cases:
- **Email Pre-processing:** Clean up unwanted characters from email drafts or subject lines.
- **Data Sanitization:** Prepare user input before saving it to a database.
- **Social Media Scraper:** Remove hashtags (#) and mentions (@) from scraped text data.
- **SEO Formatting:** Convert titles into clean, lowercase keywords.

### ✨ Key Features:
*   **Case Normalization:** Converts all text to lowercase for consistency.
*   **Whitespace Removal:** Strips leading, trailing, and redundant internal spaces.
*   **Character Filtering:** Automatically removes specific special characters (`@`, `#`, `$`, `&`).
*   **Clean Output:** Returns a polished string ready for any application.

### 💻 How to Use:
python
# Example Usage:
messy_input = "  H#ello# Pyth$& on  "
clean_output = texts_cleaner(messy_input)

print(clean_output) 
# Output: 'hello python'
