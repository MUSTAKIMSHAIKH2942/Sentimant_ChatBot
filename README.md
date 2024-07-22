# Sentimant_ChatBot
README.md
# Chatbot Application

This is a simple chatbot application built with Flask. The frontend resembles a chat application like WhatsApp.

## Features

- Responsive design
- User and bot messages styled differently
- Auto-scroll to the newest message
- Input area with text field and send button

## Requirements

- Python 3.7+
- Flask
- pandas

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/chatbot_app.git
    cd chatbot_app
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python app.py
    ```

5. Open your browser and go to `http://127.0.0.1:5000`.

## File Structure

chatbot_app/
├── app.py # Main application file
├── requirements.txt # Project dependencies
├── static/ # Static files (CSS, images, etc.)
│ └── styles.css # CSS for the chat UI
├── templates/ # HTML templates
│ └── index.html # Main HTML template
└── README.md # This README file


