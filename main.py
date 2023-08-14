# Importing modules
import tkinter as tk
import nltk
nltk.download('punkt')
from newspaper import Article
import pyttsx3

def get_summary():
    url = url_text.get('1.0', 'end').strip()

    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    title.config(state='normal')
    summary.config(state='normal')

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    title.config(state='disable')
    summary.config(state='disable')

    global summary_global_var
    summary_global_var = 'Title: ' + article.title + '. Summary: ' + article.summary

def listen_summary():
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-25)
    engine.say(summary_global_var, rate)
    engine.runAndWait()

root = tk.Tk()
root.title('Article Summarizer')
root.geometry('1200x600')

title_label = tk.Label(root, text='Title', font=('Helvetica', 12, 'bold'))
title_label.pack()

title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#dddddd')
title.pack()

summary_label = tk.Label(root, text='Summary', font=('Helvetica', 12, 'bold'))
summary_label.pack()

summary = tk.Text(root, height=26, width=140)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

url_label = tk.Label(root, text='URL')

url_text = tk.Text(root, height=1, width=140)
url_text.pack()

summarize_button = tk.Button(root, text='Summarize', command=get_summary)
summarize_button.pack()

listen_button = tk.Button(root, text='Listen to Summary', command=listen_summary)
listen_button.pack()

root.mainloop()
