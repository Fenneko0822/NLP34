import os
import csv
import glob
import pandas as pd
import pubmed_parser as pp

def batch_process_pubmed_xmls(folder_path, output_csv_path):
    results = []
    xml_files = glob.glob(os.path.join(folder_path, "*.xml"))
    print(f"Found {len(xml_files)} XML files in {folder_path}")
    
    total_files = len(xml_files)
    processed_files = 0
    skipped_files = 0
    
    for file_path in xml_files:
        try:
            # get the filename
            filename = os.path.splitext(os.path.basename(file_path))[0]
            
            # get the text
            dicts_out = pp.parse_pubmed_paragraph(file_path, all_paragraph=True)
            text = ' '.join([d['text'] for d in dicts_out if d.get('text') and d['text'].strip() != ''])
            
            # get the summary
            summary = str(pp.parse_pubmed_xml(file_path).get('abstract') or '')
            
            # Only add to results if both text and summary are not empty
            if text.strip() and summary.strip():
                results.append({
                    'filename': filename,
                    'text': text,
                    'summary': summary
                })
                processed_files += 1
                print(f"Processed: {filename}")
            else:
                skipped_files += 1
                print(f"Skipped: {filename} (empty text or summary)")
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            skipped_files += 1
    
    df = pd.DataFrame(results)
    df.to_csv(output_csv_path, index=False)
    print(f"Successfully saved {len(results)} records to {output_csv_path}")
    print(f"Summary: Processed {processed_files} files, Skipped {skipped_files} files, Total {total_files} files")

if __name__ == "__main__":
    folder_path = r"C:\Users\balen\Downloads\oa_comm_xml.PMC000xxxxxx.baseline.2024-12-18\PMC000xxxxxx"
    output_csv_path = "output.csv"
    batch_process_pubmed_xmls(folder_path, output_csv_path)
