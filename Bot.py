import json
import requests
import io
import base64
from PIL import Image
from datetime import datetime
from telegram import Update, InputFile
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

bot_token = "YOUR_BOT_TOKEN"

url = "URL_OF_STABLE_DIFFUSION"
num_images_to_generate = 1  # Adjust the number of images to generate

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome to your image generation bot! You can start by sending your prompt message.")

def handle_text_input(update: Update, context: CallbackContext):
    message = update.message
    text = message.text

    prompt = text
    print(f"Received prompt: {prompt}")

    if text.startswith("!steps = "):
        try:
            new_steps = int(text.split("!steps = ")[1])
            context.user_data["steps"] = new_steps
            message.reply_text(f"Changed steps to {new_steps}")
        except ValueError:
            message.reply_text("Invalid steps format. Use '!steps = {number}' to change the steps.")
        return

    if "steps" in context.user_data:
        steps = context.user_data["steps"]
    else:
        steps = 20

    for i in range(1, num_images_to_generate + 1):
        payload = {
            "prompt": prompt,
            "steps": steps,  
        }

        
        start_time = datetime.now()

        # Send an initial message to indicate the start of image generation
        message.reply_text("Image generation in progress...")

        response = requests.post(url, json=payload)

        if response.status_code == 200:
            r = response.json()
            image_data = r["images"][0]
            image = Image.open(io.BytesIO(base64.b64decode(image_data)))

            
            end_time = datetime.now()
            time_taken = end_time - start_time

            
            response_message = f"Image generated in {time_taken.total_seconds()} seconds"

            image_byte_array = io.BytesIO()
            image.save(image_byte_array, format="PNG")
            image_byte_array.seek(0)

            # Send the generated image 
            message.reply_photo(
                photo=InputFile(image_byte_array),
                caption=f"Prompt: {prompt}\n{response_message}\nSteps: {steps}"
            )

        else:
            message.reply_text(f"Image generation failed! Contact Shashank with status code: {response.status_code}")

def main():
    updater = Updater(token=bot_token, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text_input))
    dispatcher.add_handler(MessageHandler(Filters.command, start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()