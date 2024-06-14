# Gemini ChatBot
Gemini ChatBot is a Django-based web application that allows users to have conversational interactions with an AI assistant powered by Google's Gemini API.

## Features

- Real-time chat interface for seamless conversations with the AI assistant
- Support for multiple chat sessions
- Integration with Google's Generative AI for intelligent and contextual responses
- Responsive design for optimal viewing experience across devices

## Prerequisites

- Python 3.10
- Pipenv (Python virtual environment and package management tool)
### If you do not have pipenv installed use this command:
```bash
  pip install pipenv
```
## Installation

1.Clone the repository:
```bash
git clone https://github.com/ShreYyy20/Gemini_Chatbot.git
cd Gemini_Chatbot
```

2. Install dependencies using pipenv:
```bash
pipenv install
```
3. Activate the virtual environment:
```bash
pipenv shell
```

4.Set the environment variable for the API key:
```bash
export GENERATIVE_AI_KEY="Your API key here"
```
Replace "Your API key here" the actual Gemini API key

6. Apply the database migrations:
```python
python manage.py migrate
```

 ## Usage
 
1. Start the development server:
```python
python manage.py runserver
```

2. Open your web browser and visit http://YourIPAddress/8000/chat to access the Gemini ChatBot.


## Contributing
Contributions are welcome! If you find any issues or want to add new features, please open an issue or submit a pull request.


## Please note that the Web UI is currently a basic rough version for implementation and can be customized according to your preferences.

