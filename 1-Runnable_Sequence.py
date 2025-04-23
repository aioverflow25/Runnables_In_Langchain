from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
model = ChatGroq(
    model="gemma2-9b-it"
)
template = PromptTemplate(
    template= "Write a poem on {topic}",
    input_variables=['topic']
)
parser = StrOutputParser()
chain = RunnableSequence(template,model,parser)
print(chain.invoke({'topic','Black Hole'}))