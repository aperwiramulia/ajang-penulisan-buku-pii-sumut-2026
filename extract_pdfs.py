import os
from PyPDF2 import PdfReader

folder = r"C:\Users\KomisarisP1-Ahmad_PM\OneDrive\VS code\Penulisan Buku PII Sumut 2026"
for fname in os.listdir(folder):
    if fname.lower().endswith('.pdf'):
        path = os.path.join(folder, fname)
        print(f"Reading {fname}")
        reader = PdfReader(path)
        text = []
        for page in reader.pages:
            txt = page.extract_text()
            if txt:
                text.append(txt)
        outname = os.path.join(folder, os.path.splitext(fname)[0]+'.txt')
        with open(outname, 'w', encoding='utf-8') as f:
            f.write("\n".join(text))
        print(f"Wrote {outname}")
