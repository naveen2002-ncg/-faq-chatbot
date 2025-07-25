# FAQ Chatbot

A command-line chatbot that answers frequently asked questions about a specific topic or product using NLP techniques (NLTK). The bot matches user queries to relevant answers and is easily expandable with custom FAQ data in CSV format.

## Features

- Accepts questions in natural language
- Matches queries to relevant answers
- Uses NLP for intent and keyword detection (tokenization, stopwords, lemmatization, synonyms)
- Expandable with custom FAQ data (CSV)

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
   cd YOUR-REPO-NAME
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Edit FAQ data:**
   - Open `faq_data.csv` and add/edit questions and answers as needed.

## Usage

Run the chatbot from the command line:
```bash
python chatbot.py
```
- The bot will load FAQ data from `faq_data.csv`.
- Type your question and press Enter.
- Type `exit` to quit.

## Example
```
You: How do I track my order?
Bot: You can track your order using the tracking link sent to your email after shipping.

You: What payment methods do you accept?
Bot: We accept credit cards, debit cards, PayPal, and Apple Pay.
```

## Customization
- Add more questions and answers to `faq_data.csv` to expand the bot's knowledge.
- The NLP logic can be further improved or customized in `chatbot.py`.

## Notes
- Python 3.7–3.13 supported (no voice or web UI features).
- `.gitignore` is included to keep your repo clean.

## License
MIT License
