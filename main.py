import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

def summarize():

    url = urltext.get("1.0", "end").strip()

    article = Article(url)

    article.download()

    article.parse()

    article.nlp()

    title.config(state="normal")
    author.config(state="normal")
    publication.config(state="normal")
    summary.config(state="normal")
    sentiment.config(state="normal")

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    author.delete('1.0', 'end')
    author.insert('1.0', article.authors)

    publication.delete('1.0', 'end')
    publication.insert('1.0', article.publish_date)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    analysis = TextBlob(article.text)
    sentiment.delete('1.0', 'end')

    if analysis.polarity < 0:
        sentiment.insert('1.0', "Negative")
    elif analysis.polarity > 0:
        sentiment.insert('1.0', "Positive")
    else:
        sentiment.insert('1.0', "Neutral")

    title.config(state="disabled")
    author.config(state="disabled")
    publication.config(state="disabled")
    summary.config(state="disabled")
    sentiment.config(state="disabled")

root = tk.Tk()

root.title("News Summarizer")
root.geometry("1200x600")

tlabel = tk.Label(root, text="Title")
tlabel.pack()

title = tk.Text(root, height=1, width=140)
title.config(state="disabled", bg="#dddddd")
title.pack()


alabel = tk.Label(root, text="Author")
alabel.pack()

author = tk.Text(root, height=1, width=140)
author.config(state="disabled", bg="#dddddd")
author.pack()


plabel = tk.Label(root, text="Publication Date")
plabel.pack()

publication = tk.Text(root, height=1, width=140)
publication.config(state="disabled", bg="#dddddd")
publication.pack()


slabel = tk.Label(root, text="Summary")
slabel.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state="disabled", bg="#dddddd")
summary.pack()

selabel = tk.Label(root, text="Sentiment Analysis")
selabel.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state="disabled", bg="#dddddd")
sentiment.pack()

ulabel = tk.Label(root, text="URL")
ulabel.pack()

urltext = tk.Text(root, height=1, width=140)
urltext.pack()

button = tk.Button(root, text="Summarize", command=summarize)
button.pack()

root.mainloop()