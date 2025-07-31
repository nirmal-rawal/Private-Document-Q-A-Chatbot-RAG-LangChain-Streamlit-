from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS


#upload & laod  raw pdf

pdf_dic='pdfs/'

def uplaod_pdf(file):
    with open(pdf_dic+file.name,'wb')as f:
        f.write(file.getbuffer())
    

def load_pdf(file_path):
    loader=PDFPlumberLoader(file_path)
    documents=loader.load()
    return documents
    

file_path='pdfs/Nirmal_Rawal_AI.pdf'
documents=load_pdf(file_path)
# print('len of pages',len(documents))
#chunk create:
def create_chunks(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True
    )
    text_chunk=text_splitter.split_documents(documents)
    return text_chunk

chunk=create_chunks(documents)
# print('chunk of page',len(chunk))

#setup embaddings model with Deepshik r1 model with ollam 
ollam_model_name="deepseek-r1:7b"
def get_embadddings_model(ollam_model_name):
    embaddings=OllamaEmbeddings(model=ollam_model_name)
    
    return embaddings


#index the embaddings docs in vector store FAISS
FAISS_DB_PATH='vectorstore/db_faiss'
faiss_db=FAISS.from_documents(chunk,get_embadddings_model(ollam_model_name))
faiss_db.save_local(FAISS_DB_PATH)