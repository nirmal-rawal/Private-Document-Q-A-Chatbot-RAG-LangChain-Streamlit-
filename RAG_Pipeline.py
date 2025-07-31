from langchain_ollama import OllamaLLM
from vector_database import ollam_model_name,faiss_db
from langchain_core.prompts import ChatPromptTemplate
from langchain.memory import ConversationBufferMemory

#set up the ollam model
llm_model=OllamaLLM(model=ollam_model_name)
# Set up memory for conversation
memory = ConversationBufferMemory(memory_key="history", return_messages=True)

# set up the retriver
def retriver_docs(query):
    return faiss_db.similarity_search(query)

def get_context(documents):
    context="\n\n".join([docs.page_content for docs in documents])
    return context



custom_prompt_template = """
Use the pieces of information provided in the context to answer user's question.
If you dont know the answer, just say that you dont know, dont try to make up an answer. 
Dont provide anything out of the given context
Question: {question} 
Context: {context} 
Answer:
"""

def answer_query(documents, llm_model, query, memory=memory):
    context = get_context(documents)
    prompt = ChatPromptTemplate.from_template(custom_prompt_template)
    # Retrieve conversation history from memory
    history = memory.load_memory_variables({})["history"]
    # Add history to the prompt context if needed
    full_context = f"{history}\n\n{context}" if history else context
    chain = prompt | llm_model
    response = chain.invoke({'question': query, 'context': full_context})
    # Save the user query and AI response to memory
    memory.save_context({"input": query}, {"output": response})
    return response

# question="If a government forbids the right to assemble peacefully which articles are violated and why?"
# retrieved_docs=retriver_docs(question)
# print("AI Lawyer: ",answer_query(documents=retriver_docs, model=llm_model, query=question))