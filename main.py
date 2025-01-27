from chatbot import ChatBot
from data_extraction import fetch_website_content, extract_relevant_data
from data_processing import process_data

def main():
    print("Welcome to the Website Crawler ChatBot! Type 'exit' to quit.")

    bot = ChatBot()
    
    url = input("Enter a website URL to provide context: ").strip()
    try:
        html_content = fetch_website_content(url)
        raw_data = extract_relevant_data(html_content)
        structured_data = process_data(raw_data)
        bot.load_context(structured_data)
        print("Context loaded successfully!")
    except Exception as e:
        print(f"Error loading website context: {e}")
        return
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = bot.get_response(user_input)
        print(f"AI: {response}")

if __name__ == "__main__":
    main()
