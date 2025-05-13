import os
import csv
import glob
import pandas as pd
import pubmed_parser as pp

def batch_process_pubmed_xmls(folder_path, output_csv_path):
    results = []
    xml_files = glob.glob(os.path.join(folder_path, "*.xml"))
    print(f"Found {len(xml_files)} XML files in {folder_path}")
    
    for file_path in xml_files:
        try:
            # get the filename
            filename = os.path.splitext(os.path.basename(file_path))[0]

            # get the text
            dicts_out = pp.parse_pubmed_paragraph(file_path, all_paragraph=True)
            text = ' '.join([d['text'] for d in dicts_out if d.get('text') and d['text'].strip() != ''])

            # get the summary
            summary = pp.parse_pubmed_xml(file_path).get('abstract', '')

            results.append({
                'filename': filename,
                'text': text,
                'summary': summary
            })

            print(f"Processed: {filename}")
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    df = pd.DataFrame(results)
    df.to_csv(output_csv_path, index=False)
    print(f" Successfully saved {len(results)} records to {output_csv_path}")

if __name__ == "__main__":
    folder_path = r"C:\Users\balen\Downloads\oa_comm_xml.PMC000xxxxxx.baseline.2024-12-18\PMC000xxxxxx"
    output_csv_path = "output.csv"
    batch_process_pubmed_xmls(folder_path, output_csv_path)
