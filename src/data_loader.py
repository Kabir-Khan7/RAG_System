from pathlib import Path
from typing import List, Any
from langchain_community.document_loaders import PyPDFLoader, TextLoader, CSVLoader
from langchain_community.document_loaders import Docx2txtLoader
from langchain_community.document_loaders.excel import UnstructuredExcelLoader
from langchain_community.document_loaders import JSONLoader

def load_all_document(data_dir: str) -> List[Any]:
    """ Load all supported file from data directory. Supported: PDF, TXT, CSV, Excel, Word, JSON """
    # Using project root data folder
    data_path = Path(data_dir).resolve()
    print(f"[DEBUG] Data Path: {data_path}")
    documents = []
    
    # PDF Files
    pdf_files = list(data_path.glob('**/*.pdf'))
    print(f"[DEBUG] found {len(pdf_files)} PDF Files: {[str(f) for f in pdf_files]}")
    for pdf_file in pdf_files:
        print(f"[DEBUG] Loading PDF: {pdf_file}")
        try:
            loader = PyPDFLoader(str(pdf_file))
            loaded = loader.load()
            print(f"[DEBUG] Loaded {len(loaded)} PDF docs from {pdf_file}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[ERROR] Failed to load PDF {pdf_file}: {e}")
    return documents
            
    # TXT Files
    txt_files = list(data_path.glob('**/*.txt'))
    print(f"[DEBUG] Found {len(txt_files)} TXT Files")
    for txt_file in txt_files:
        try:
            loader = TextLoader(str(txt_file), encoding='utf-8')
            loaded = loader.load()
            print(f"[DEBUG] Loaded {len(loaded)} docs from {txt_file.name}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[ERROR] Failed to load TXT {txt_file.name}: {e}")
    return documents

    # CSV Files 
    csv_files = list(data_path.glob('**/*.csv'))
    print(f"[DEBUG] Found {len(csv_files)} CSV Files")
    for csv_file in csv_files:
        try:
            loader = CSVLoader(
                file_path=str(csv_file),
                encoding='utf-8',
                csv_args={'delimiter': ','}
            )
            loaded = loader.load()
            print(f"[DEBUG] Loaded {len(loaded)} rows from {csv_file.name}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[ERROR] Failed to load csv {csv_file.name}: {e}")
    return documents
            
    # Excel Files 
    excel_files = list(data_path.glob('**/*.xlsx')) + list(data_path.glob('**/*.xls'))
    for excel_file in excel_files:
        try:
            loader = UnstructuredExcelLoader(str(excel_file), mode="elements")
            loaded = loader.load()
            print(f"[DEBUG] Loaded {len(loaded)} elements from {excel_file.name}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[ERROR] Failed to load Excel {excel_file.name}: {e}")
    return documents     

    # Word Files
    word_files = list(data_path.glob('**/*.docx')) + list(data_path.glob('**/*.doc'))
    print(f"[DEBUG] Found {len(word_files)} Word Files")
    for word_file in word_files:
        try:
            loader = Docx2txtLoader(str(word_file))
            loaded = loader.load()
            print(f"[DEBUG] Loaded {len(loaded)} docs from {word_file.name}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[ERROR] Faied to load word {word_file.name}: {e}")
    return documents      
            
    # JSON
    json_files = list(data_path.glob('**/*.json'))
    print(f"[DEBUG] found {len(json_files)} JSON files")
    for json_file in json_files:
        try:
            loader = JSONLoader(
                file_path=str(json_file),
                jq_schema='.',
                text_content=False
            )
            loaded = loader.load()
            print(f"[DEBUG] Loaded {len(loaded)} records from {json_file.name}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[ERROR] Failed to load JSON {json_file.name}: {e}")
    return documents                    
        
    
