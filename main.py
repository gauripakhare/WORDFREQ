import flet as ft
import string
from collections import Counter

def count_word_frequency(text):
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator).lower()
    words = text.split()
    word_count = Counter(words)
    return word_count

def main(page: ft.Page):
    page.title = "Word Frequency Analyzer"

    input_field = ft.TextField(label="Enter text here", multiline=True, width=500)
    result_text = ft.Text()
    
    def analyze_text(e):
        user_text = input_field.value
        frequency = count_word_frequency(user_text)
        result = "\n".join([f"{word}: {count}" for word, count in frequency.items()])
        result_text.value = result
        page.update()

    analyze_button = ft.ElevatedButton(text="Analyze", on_click=analyze_text)

    page.add(input_field, analyze_button, result_text)

ft.app(target=main)
