from llama_index.llms.openai import OpenAI
import asyncio
import os
from dotenv import load_dotenv

#import basic agent functionality
from llama_index.core.agent.workflow import FunctionAgent

#import memory of previous messages via Context
from llama_index.core.workflow import Context 

#import RAG capabilities
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage


# Load environment variables
load_dotenv()


# Define a simple calculator tool that multiplies 2 numbers
def multiply(a: float, b: float) -> float:
    """Useful for multiplying two numbers."""
    return a * b

# Create or load RAG index so I need not reprocess the documents every time I run the script.

##Check if a stored index exists (error handling)
if not os.path.exists("storage"):
    ### If it exists, load the existing index
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    index.storage_context.persist("storage")
else:
    ### If a stored index doesn't exist, create and store a new one
    storage_context = StorageContext.from_defaults(persist_dir="storage")
    index = load_index_from_storage(storage_context)

#Create the query engine from whichever index is available
query_engine = index.as_query_engine()


async def search_documents(query: str) -> str:
    """Useful for answering natural language questions about a pdf file on french fiscal law."""
    response = await query_engine.aquery(query)
    return str(response)

# Create an agent workflow with a Calculator Tool and the RAG Tool
agent = FunctionAgent(
    tools=[multiply,search_documents],
    llm=OpenAI(api_key=os.getenv("OPENAI_API_KEY"),model="gpt-4o-mini"),
    system_prompt="You are a helpful assistant that can multiply two numbersand search through documents to answer questions.",
)

# create context in which (memory of) previous messages will be stored during conversation.
ctx = Context(agent)

# Now we can ask the agent to do calculations and ask questions about the documents in the data folder
async def main():
    # 1 Run the agent alone 
    #response = await agent.run("What is 1234 * 4567?")
    # 2 run agent with context
    # response = await agent.run("My name is Logan", ctx=ctx)
    # response = await agent.run("What is my name?", ctx=ctx)
    # 3 run agent with context and ask about the content of the document : agent can now seamlessly switch between tools (using the calculator and searching through documents to answer questions).
    response = await agent.run(
        "Le bénéfice de la exonération est-il perdu dès lors que la commune sort de la liste des ZAFR? Et quel est le résultat de 20*4?"
    )
    print(str(response))


# Run the agent
if __name__ == "__main__":
    asyncio.run(main())