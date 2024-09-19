# Podcast Feedback & Questions Telegram Bot

This project is a Telegram bot designed for the psychology podcast "Что-то на окейном". The bot enables users to submit questions and feedback directly to the podcast hosts. The bot collects user input and forwards it to specific Telegram chats for the podcast organizers to review.

## Features

- **Submit Questions**: Users can submit questions about the podcast, which are sent directly to the hosts.
- **Submit Feedback**: Users can leave feedback after listening to an episode.
- **Simple Interaction**: The bot provides an easy-to-use interface with just two buttons: "Ask a Question" and "Leave Feedback".

## How It Works

1. When a user starts the bot, they are prompted with two options:
   - **Ask a Question**: The user is asked to type their question, which is sent to the podcast's question chat.
   - **Leave Feedback**: The user can submit feedback, which is sent to the feedback chat.

2. The bot handles user input, identifies whether it's a question or feedback, and forwards it to the respective Telegram chat.

## Getting Started

### Prerequisites

- Python 3.x
- `pyTelegramBotAPI` (install using `pip`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/podcast-feedback-bot.git
   cd podcast-feedback-bot
   ```

2. Install dependencies:

   ```bash
   pip install pyTelegramBotAPI
   ```

3. Add your bot token and chat IDs in the script:

   - Replace the `API_TOKEN` with your own Telegram bot token.
   - Set the correct `QUESTIONS_CHAT_ID` and `REVIEWS_CHAT_ID` to the Telegram group or channel IDs where you want to receive the questions and feedback.

4. Run the bot:

   ```bash
   python bot.py
   ```
