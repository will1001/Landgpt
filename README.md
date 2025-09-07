# LandGPT - LangChain Examples Project

Koleksi contoh implementasi LangChain untuk membangun aplikasi AI dengan Large Language Models (LLMs).

## 📋 Daftar Isi
- [Fitur](#fitur)
- [Prerequisites](#prerequisites)
- [Instalasi](#instalasi)
- [Penggunaan](#penggunaan)
- [Contoh-contoh](#contoh-contoh)
- [Konfigurasi](#konfigurasi)
- [Troubleshooting](#troubleshooting)

## ✨ Fitur

- **Basic LangChain Usage**: Contoh penggunaan dasar LLM dengan LangChain
- **Prompt Templates**: Template prompts yang dapat digunakan kembali
- **Chain Operations**: Multi-step processing chains
- **AI Agents**: Agent dengan custom tools dan built-in tools
- **Conversational AI**: Chatbot dengan memory/context
- **Text Analysis**: Analisis sentiment dan topik

## 🛠 Prerequisites

- Python 3.8 atau lebih tinggi
- OpenAI API key
- Git

## 🚀 Instalasi

### 1. Clone Repository
```bash
git clone <repository-url>
cd Landgpt
```

### 2. Setup Environment (Otomatis)
```bash
./setup_langchain.sh
```

### 3. Setup Manual (Opsional)
```bash
# Buat virtual environment
python3 -m venv langchain_env
source langchain_env/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install wikipedia
```

### 4. Set API Key
```bash
export OPENAI_API_KEY='your-openai-api-key-here'
```

## 📖 Penggunaan

### Aktivasi Environment
```bash
source langchain_env/bin/activate
```

### Menjalankan Contoh Dasar
```bash
python langchain_examples.py
```

### Menjalankan Contoh Agent
```bash
python langchain_agent_example.py
```

## 📚 Contoh-contoh

### 1. Basic LLM Usage (`langchain_examples.py`)

#### a. Penggunaan LLM Sederhana
```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo")
response = llm.invoke("What is LangChain?")
print(response.content)
```

#### b. Prompt Template
```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a translator from {input_language} to {output_language}."),
    ("human", "{text}")
])

chain = prompt | llm | StrOutputParser()
result = chain.invoke({
    "input_language": "English",
    "output_language": "Indonesian", 
    "text": "Hello world"
})
```

#### c. Text Analysis Chain
```python
analysis_chain = prompt | llm | StrOutputParser()
result = analysis_chain.invoke({"text": "Your text here"})
```

### 2. AI Agents (`langchain_agent_example.py`)

#### a. Basic Agent dengan Built-in Tools
```python
from langchain.agents import initialize_agent, load_tools

tools = load_tools(["wikipedia", "llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)
result = agent.run("What is the population of Jakarta?")
```

#### b. Custom Tools
```python
from langchain.tools import Tool

def custom_calculator(expression: str) -> str:
    return str(eval(expression))

tools = [
    Tool(
        name="Calculator",
        func=custom_calculator,
        description="Calculate math expressions"
    )
]
```

#### c. Conversational Agent dengan Memory
```python
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
agent = initialize_agent(tools, llm, memory=memory)
```

## ⚙️ Konfigurasi

### Environment Variables
```bash
# Required
export OPENAI_API_KEY="your-api-key"

# Optional
export LANGCHAIN_TRACING_V2="true"
export LANGCHAIN_API_KEY="your-langsmith-key"
```

### Model Configuration
Ubah model di dalam kode:
```python
# Untuk GPT-4
llm = ChatOpenAI(model="gpt-4")

# Untuk model lain
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")
```

## 🔧 Troubleshooting

### Error: "No module named 'langchain'"
```bash
# Pastikan virtual environment aktif
source langchain_env/bin/activate

# Install ulang requirements
pip install -r requirements.txt
```

### Error: "OpenAI API key not found"
```bash
# Set API key
export OPENAI_API_KEY="your-key-here"

# Atau buat file .env
echo "OPENAI_API_KEY=your-key-here" > .env
```

### Error: "Rate limit exceeded"
- Tunggu beberapa menit sebelum mencoba lagi
- Gunakan model yang lebih murah seperti `gpt-3.5-turbo`
- Periksa usage limit di OpenAI dashboard

### Error: "Wikipedia module not found"
```bash
pip install wikipedia
```

## 📁 Struktur Project

```
Landgpt/
├── langchain_examples.py      # Contoh dasar LangChain
├── langchain_agent_example.py # Contoh AI Agents
├── requirements.txt           # Dependencies Python
├── setup_langchain.sh        # Script setup otomatis
├── .gitignore                # Git ignore rules
└── README.md                 # Dokumentasi ini
```

## 🤝 Kontribusi

1. Fork repository ini
2. Buat branch feature (`git checkout -b feature/amazing-feature`)
3. Commit perubahan (`git commit -m 'Add amazing feature'`)
4. Push ke branch (`git push origin feature/amazing-feature`)
5. Buka Pull Request

## 📄 Lisensi

Project ini menggunakan lisensi MIT - lihat file [LICENSE](LICENSE) untuk detail.

## 📞 Bantuan

Jika mengalami kesulitan, buka issue di repository ini atau hubungi maintainer.

---

**Happy Coding with LangChain! 🚀**