#!/usr/bin/env python3
"""
LangChain Examples - Basic usage patterns
Based on official LangChain documentation
"""

import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

# Example 1: Basic LLM Usage
def basic_llm_example():
    """Basic example of using LLM with LangChain"""
    # Initialize the LLM (requires OPENAI_API_KEY environment variable)
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    
    # Simple invocation
    response = llm.invoke("What is LangChain?")
    print("Basic LLM Response:", response.content)
    return response.content

# Example 2: Using Prompt Templates]










def prompt_template_example():
    """Example using prompt templates for structured input"""
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    
    # Create a prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant that translates {input_language} to {output_language}."),
        ("human", "{text}")
    ])
    
    # Create a chain
    chain = prompt | llm | StrOutputParser()
    
    # Use the chain
    result = chain.invoke({
        "input_language": "English",
        "output_language": "French",
        "text": "Hello, how are you?"
    })
    
    print("Translation Result:", result)
    return result

# Example 3: Simple Chatbot Chain
def chatbot_example():
    """Example of a simple chatbot using LangChain"""
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    
    # Create a chatbot prompt
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant. Answer questions clearly and concisely."),
        ("human", "{question}")
    ])
    
    # Create the chain
    chatbot_chain = prompt | llm | StrOutputParser()
    
    # Example usage
    questions = [
        "What is artificial intelligence?",
        "How does machine learning work?",
        "What are the benefits of using LangChain?"
    ]
    
    responses = []
    for question in questions:
        response = chatbot_chain.invoke({"question": question})
        responses.append((question, response))
        print(f"Q: {question}")
        print(f"A: {response}\n")
    
    return responses

# Example 4: Text Analysis Chain
def text_analysis_example():
    """Example of text analysis using LangChain"""
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    
    # Create analysis prompt
    prompt = ChatPromptTemplate.from_template("""
    Please analyze the following text and provide:
    1. Main topic
    2. Sentiment (positive, negative, neutral)
    3. Key points (maximum 3)
    
    Text: {text}
    
    Analysis:
    """)
    
    # Create the chain
    analysis_chain = prompt | llm | StrOutputParser()
    
    # Example text
    sample_text = """
    LangChain is an amazing framework for building applications with large language models. 
    It provides a simple and intuitive way to create complex AI workflows. 
    The community is very supportive and the documentation is comprehensive.
    """
    
    result = analysis_chain.invoke({"text": sample_text})
    print("Text Analysis Result:", result)
    return result

# Example 5: Multi-step Chain
def multi_step_chain_example():
    """Example of a multi-step processing chain"""
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    
    # Step 1: Generate a topic
    topic_prompt = ChatPromptTemplate.from_template(
        "Generate a random interesting topic about {subject}"
    )
    topic_chain = topic_prompt | llm | StrOutputParser()
    
    # Step 2: Write about the topic
    writing_prompt = ChatPromptTemplate.from_template(
        "Write a short paragraph (2-3 sentences) about: {topic}"
    )
    writing_chain = writing_prompt | llm | StrOutputParser()
    
    # Execute the multi-step chain
    subject = "technology"
    topic = topic_chain.invoke({"subject": subject})
    article = writing_chain.invoke({"topic": topic})
    
    print(f"Generated Topic: {topic}")
    print(f"Generated Article: {article}")
    return topic, article

def main():
    """Run all examples"""
    print("=== LangChain Examples ===\n")
    
    # Check if API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("Warning: OPENAI_API_KEY not set. These examples require an OpenAI API key.")
        print("Set it with: export OPENAI_API_KEY='your-api-key-here'")
        return
    
    try:
        print("1. Basic LLM Example:")
        basic_llm_example()
        print("\n" + "="*50 + "\n")
        
        print("2. Prompt Template Example:")
        prompt_template_example()
        print("\n" + "="*50 + "\n")
        
        print("3. Chatbot Example:")
        chatbot_example()
        print("\n" + "="*50 + "\n")
        
        print("4. Text Analysis Example:")
        text_analysis_example()
        print("\n" + "="*50 + "\n")
        
        print("5. Multi-step Chain Example:")
        multi_step_chain_example()
        
    except Exception as e:
        print(f"Error running examples: {e}")
        print("Make sure you have installed the required packages:")
        print("pip install langchain langchain-openai")

if __name__ == "__main__":
    main()