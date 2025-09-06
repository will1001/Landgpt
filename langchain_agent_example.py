#!/usr/bin/env python3
"""
LangChain Agent Examples - Advanced usage with tools
"""

import os
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain_openai import ChatOpenAI
from langchain.tools import Tool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentExecutor

def basic_agent_example():
    """Basic agent example with built-in tools"""
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    
    # Load some built-in tools
    tools = load_tools(["wikipedia", "llm-math"], llm=llm)
    
    # Initialize the agent
    agent = initialize_agent(
        tools, 
        llm, 
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
        verbose=True
    )
    
    # Run the agent
    result = agent.run("What is the population of Tokyo and what is 15% of that number?")
    print("Agent Result:", result)
    return result

def custom_tool_agent_example():
    """Example with custom tools"""
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    
    # Define custom tools
    def get_word_length(word: str) -> int:
        """Returns the length of a word"""
        return len(word)
    
    def reverse_word(word: str) -> str:
        """Reverses a word"""
        return word[::-1]
    
    def calculate_area(length: float, width: float) -> float:
        """Calculates the area of a rectangle"""
        return length * width
    
    # Create tool objects
    tools = [
        Tool(
            name="WordLength",
            func=get_word_length,
            description="Get the length of a word"
        ),
        Tool(
            name="ReverseWord", 
            func=reverse_word,
            description="Reverse a word"
        ),
        Tool(
            name="CalculateArea",
            func=lambda x: calculate_area(*map(float, x.split(','))),
            description="Calculate rectangle area. Input should be 'length,width'"
        )
    ]
    
    # Create the prompt
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant with access to various tools."),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])
    
    # Create the agent
    agent = create_openai_functions_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    
    # Test the agent
    queries = [
        "What is the length of the word 'LangChain'?",
        "Reverse the word 'hello'",
        "Calculate the area of a rectangle with length 5 and width 3"
    ]
    
    results = []
    for query in queries:
        print(f"\nQuery: {query}")
        result = agent_executor.invoke({"input": query})
        results.append(result)
        print(f"Result: {result['output']}")
    
    return results

def conversational_agent_example():
    """Example of a conversational agent with memory"""
    from langchain.memory import ConversationBufferMemory
    
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
    
    # Simple tools for the conversational agent
    tools = [
        Tool(
            name="Calculator",
            func=lambda x: str(eval(x)),
            description="Perform basic math calculations. Input should be a math expression."
        ),
        Tool(
            name="UpperCase",
            func=lambda x: x.upper(),
            description="Convert text to uppercase"
        )
    ]
    
    # Initialize memory
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )
    
    # Create conversational agent
    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
        verbose=True,
        memory=memory
    )
    
    # Simulate conversation
    conversation = [
        "Hi! My name is John.",
        "Calculate 25 + 17",
        "What was my name again?",
        "Convert 'hello world' to uppercase",
        "What was the result of the calculation I asked earlier?"
    ]
    
    responses = []
    for message in conversation:
        print(f"\nUser: {message}")
        response = agent.run(message)
        responses.append((message, response))
        print(f"Agent: {response}")
    
    return responses

def main():
    """Run all agent examples"""
    print("=== LangChain Agent Examples ===\n")
    
    # Check if API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("Warning: OPENAI_API_KEY not set. These examples require an OpenAI API key.")
        print("Set it with: export OPENAI_API_KEY='your-api-key-here'")
        return
    
    try:
        print("1. Basic Agent with Built-in Tools:")
        basic_agent_example()
        print("\n" + "="*60 + "\n")
        
        print("2. Custom Tool Agent Example:")
        custom_tool_agent_example()
        print("\n" + "="*60 + "\n")
        
        print("3. Conversational Agent with Memory:")
        conversational_agent_example()
        
    except Exception as e:
        print(f"Error running agent examples: {e}")
        print("Make sure you have installed the required packages:")
        print("pip install langchain langchain-openai wikipedia")

if __name__ == "__main__":
    main()