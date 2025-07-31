import streamlit as st 
from RAG_Pipeline import answer_query,retriver_docs,llm_model, memory
from vector_database import uplaod_pdf

upload_file=st.file_uploader("Upload file here",
                             type='pdf',
                             accept_multiple_files=False)

#chatbot skeletion (question and answering)

user_query=st.text_area("Enter you Question: ",height=150,placeholder="Ask Anythings")

Ask_question=st.button('Ask anything related to documents')

if Ask_question:
    
    
    if upload_file:
        uplaod_pdf(upload_file)  # Save the uploaded PDF to the pdfs folder
        st.chat_message('user').write(user_query)
        retriver_doc=retriver_docs(user_query)
        # Use memory-enabled answer_query
        response=answer_query(retriver_doc,llm_model,user_query, memory=memory)
        # fixed_response="Hi this is fixed response"
        st.chat_message("As lawyer").write(response)
    else:
        st.error('Kindely Upload first valid pdf file')
    
