import json
import csv
import re

input_file = 'train.txt'           
output_file = 'train.csv'  

def clean_text(text):
    text = re.sub(r'</?S>', '', text)      # remove <S> and </S>
    text = re.sub(r'\s+', ' ', text).strip()  # remove extra spaces
    return text

with open(input_file, 'r', encoding='utf-8') as infile, \
     open(output_file, 'w', newline='', encoding='utf-8') as outfile:

    writer = csv.writer(outfile)
    writer.writerow(['text', 'summary'])  # heading of the table

    for line_num, line in enumerate(infile, 1):
        try:
            data = json.loads(line)

            # get and clean article_text
            article_sentences = data.get('article_text', [])
            article_text = clean_text(' '.join(article_sentences))

            # get and clean abstract_text
            abstract_sentences = data.get('abstract_text', [])
            abstract_text = clean_text(' '.join(abstract_sentences))

            if article_text and abstract_text:
                writer.writerow([article_text, abstract_text])
            
        except json.JSONDecodeError:
            print(f"Skipping line {line_num}: JSON parsing failed")
        except Exception as e:
            print(f"Error at line {line_num}: {e}")
