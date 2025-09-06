#!/bin/bash
# Setup script for LangChain examples

echo "Setting up LangChain environment..."

# Create virtual environment
python3 -m venv langchain_env

# Activate virtual environment
source langchain_env/bin/activate

# Install requirements
pip install -r requirements.txt

# Additional packages for agent examples
pip install wikipedia

echo "Setup complete!"
echo ""
echo "To use these examples:"
echo "1. Activate the virtual environment: source langchain_env/bin/activate"
echo "2. Set your OpenAI API key: export OPENAI_API_KEY='your-api-key'"
echo "3. Run the examples:"
echo "   - python langchain_examples.py"
echo "   - python langchain_agent_example.py"