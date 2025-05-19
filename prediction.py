from transformers import pipeline

summarizer = pipeline("summarization", model="path/to/your/output_dir")

text = "Your input text that you want to summarize..."
summary = summarizer(text, max_length=50, min_length=10, do_sample=False)

print(summary)
