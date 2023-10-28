import asyncio

import telegram

token = "your_token_key"
chat_id = "your_chat_id"


async def report_message(error_message: str) -> None:
    """
    Sends a notification message to a Telegram group.

    Args:
    - error_message (str): The error message to be reported.

    Returns:
    - None
    """
    bot = telegram.Bot(token=token)

    await bot.sendMessage(chat_id=chat_id, text=error_message)

    print("Error reported to the telegram group!")


if __name__ == '__main__':
    # Example Usage
    try:
        result = 5 / 0
        print(result)
    except ZeroDivisionError as e:
        error_text = f"Error: {str(e)}"
        asyncio.run(report_message(error_message=error_text))
