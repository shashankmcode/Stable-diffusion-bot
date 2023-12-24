

# Stable Diffusion bot

This Telegram bot allows you to generate images based on prompts using the Stable Diffusion model. You can interact with the bot by sending text prompts through Telegram, and it will respond with the generated images.

## Prerequisites

Before using the bot, make sure to install the required Python package:

```bash
pip install python-telegram-bot==13.7
```

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/shashankmcode/Stable-diffusion-bot.git
   cd Stable-diffusion-bot
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Obtain a Telegram bot token:

   - Create a new bot on Telegram by talking to [BotFather](https://t.me/botfather).
   - Copy the generated bot token.

4. Replace the placeholder in the script:

   - Open the script (`image_generation_bot.py`) in a text editor.
   - Replace the `YOUR_BOT_TOKEN` placeholder with the Telegram bot token.

5. Set the URL of the Stable Diffusion model:

   - Replace the `URL_OF_STABLE_DIFFUSION` placeholder with the actual URL.

6. Adjust the number of images to generate:

   - Modify the `num_images_to_generate` variable in the script to set the desired number of images to generate.

## Usage

1. Run the script:

   ```bash
   python Bot.py
   ```

2. Start a conversation with the bot on Telegram.

3. Send a prompt message to initiate image generation.

4. Optionally, you can change the number of steps for image generation by sending a message starting with `!steps = {number}`.

## Commands

- `/start`: Start the conversation with the bot.
- Sending any text message initiates image generation based on the provided prompt.

## Example

| Image 1 | Image 2 |
|---------|---------|
| ![Alt Text](https://github.com/shashankmcode/Stable-diffusion-bot/blob/main/image3.jpeg) | ![Alt Text](https://github.com/shashankmcode/Stable-diffusion-bot/blob/main/image.jpeg) |

## Credits

This bot is powered by the Stable Diffusion model.

For issues or inquiries, contact Shashank at [shashankhs5242@gmail.com](mailto:shashankhs5242@gmail.com).
