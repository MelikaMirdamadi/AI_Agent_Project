from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
load_dotenv()


@tool
def greeting (name : str ) -> str:
    """
    useful for greeting to users
    """
    print("greeting function is called")
    return f"Hello {name}, how can I assist you today?"


@tool
def calculator (x:int , y:int ) -> str:
    """
    useful for calculating sum of two numbers 
    """
    
    print("calculator function is called")
    return f"this {x} + {y} equal to {x+y}"

def main():
    model = ChatOllama(model="mistral")
    
    
    tools=[greeting,calculator]
    agent_executable = create_react_agent(model , tools)

    print("Hello, welcome, I'm AI assistant, ask me your question , and type 'exit' to quit")    
    
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        print("AI: " , end="")
        for chunk in agent_executable.stream(
            {'messages': [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and 'messages' in chunk['agent']:
                for message in chunk["agent"]['messages']:
                    print(message.content , end="")                        
                    
        print()
        
if __name__ == "__main__":
    main()