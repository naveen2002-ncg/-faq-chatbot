import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import string
import os

# Download NLTK data if not already present
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)

# Load FAQ data from JSON file
def load_faq_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

# Load FAQ data from CSV file
def load_faq_data_csv(filename):
    import csv
    faqs = []
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if 'question' in row and 'answer' in row:
                faqs.append({'question': row['question'], 'answer': row['answer']})
    return faqs

# Preprocess text: tokenize, lowercase, remove stopwords and punctuation, lemmatize, expand synonyms
def preprocess(text, expand_synonyms=False):
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text.lower())
    tokens = [t for t in tokens if t not in stop_words and t not in string.punctuation]
    lemmas = [lemmatizer.lemmatize(t) for t in tokens]
    if expand_synonyms:
        expanded = set(lemmas)
        for lemma in lemmas:
            for syn in wordnet.synsets(lemma):
                for l in syn.lemmas():
                    expanded.add(l.name().replace('_', ' '))
        return expanded
    return set(lemmas)

# Find the best matching FAQ answer with improved NLP
def find_best_answer(user_question, faqs):
    user_tokens = preprocess(user_question, expand_synonyms=True)
    best_match = None
    best_score = 0
    for faq in faqs:
        faq_tokens = preprocess(faq['question'])
        score = len(user_tokens & faq_tokens)
        if score > best_score:
            best_score = score
            best_match = faq['answer']
    return best_match

def main():
    json_file = 'faq_data.json'
    csv_file = 'faq_data.csv'
    faqs = None
    if os.path.exists(json_file) and os.path.exists(csv_file):
        print("Both JSON and CSV FAQ files found.")
        choice = input("Type 'json' to use JSON or 'csv' to use CSV: ").strip().lower()
        if choice == 'csv':
            faqs = load_faq_data_csv(csv_file)
        else:
            faqs = load_faq_data(json_file)
    elif os.path.exists(csv_file):
        faqs = load_faq_data_csv(csv_file)
    elif os.path.exists(json_file):
        faqs = load_faq_data(json_file)
    else:
        print("No FAQ data file found (faq_data.json or faq_data.csv).")
        return
    print("Welcome to the FAQ Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == 'exit':
            print("Goodbye!")
            break
        answer = find_best_answer(user_input, faqs)
        if answer:
            print(f"Bot: {answer}")
        else:
            print("Bot: Sorry, I don't know the answer to that question.")

if __name__ == '__main__':
    main() 