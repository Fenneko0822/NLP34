
from django.shortcuts import render
from transformers import BartTokenizer, BartForConditionalGeneration
import torch

model = BartForConditionalGeneration.from_pretrained('./final_bart_model').to("cpu")
tokenizer = BartTokenizer.from_pretrained('./final_bart_model')

def summarize_view(request):
    summary = None
    input_text = ""
    if request.method == "POST":
        input_text = request.POST.get("input_text", "")
        inputs = tokenizer(input_text, return_tensors="pt", max_length=512, truncation=True, padding="max_length")
        with torch.no_grad():
            summary_ids = model.generate(inputs["input_ids"], max_length=128, num_beams=4)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return render(request, "summarize.html", {"summary": summary, "input_text": input_text})
