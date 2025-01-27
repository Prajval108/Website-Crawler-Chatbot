# Website Crawler ChatBot

The **Website Crawler ChatBot** is a Python-based application designed to scrape data from a provided website URL, process the data, and enable a question-answering (QA) experience based on the extracted content. The chatbot leverages **litellm** for its modular Large Language Model (LLM) implementation to provide intelligent and context-aware responses.

---

## Features

1. **Web Data Crawling**: Scrapes and processes content from a user-provided website URL.
2. **Modular LLM Integration**: Uses **litellm** for flexible LLM configuration and functionality.
3. **Contextual QA**: Allows users to ask questions related to the scraped website content.
4. **Error Handling**: Ensures smooth operation with error reporting.

---

## Project Structure

- **`chatbot.py`**: Implements the `ChatBot` class, responsible for interacting with the LLM, managing responses, and maintaining context.
- **`data_extraction.py`**: Extracts raw content from the provided website URL.
- **`data_processing.py`**: Processes the extracted raw data into structured information for the chatbot.
- **`environment.py`**: Manages API configuration and environmental variables.
- **`main.py`**: The main entry point for running the chatbot.

---

## Setup Instructions

### Prerequisites

1. **Python 3.10+**: Make sure you have Python installed on your machine.
2. **Dependencies**: Install required Python libraries.
3. **API Key**: Obtain an API key for the LLM provider via [litellm](https://docs.litellm.ai/docs/providers).


## Installation

1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables:
   - Create a `.env` file in the project directory:
     ```env
     GROQ_API_KEY=your_groq_api_key
     MODEL_ID=groq/llama3-8b-8192
     ```
   - Replace `your_groq_api_key` with your actual API key from the [groq quickstart](https://console.groq.com/docs/quickstart).
    For more details regarding model switching, refer to the [litellm documentation](https://docs.litellm.ai/docs/providers).

4. Run the application:
   ```bash
   python main.py
   ```

---

### Usage

1. When the chatbot starts, you'll be prompted to enter a website URL:
   ```
   Enter a website URL to provide context: <your_website_url>
   ```
   Example: `https://example.com`

2. Once the website content is processed, you can ask any question related to the website:
   ```
   You: What is the main topic of the website?
   AI: [Response based on the website content]
   ```

3. To exit the chatbot, type:
   ```
   exit
   ```



---
