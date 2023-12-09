# Rover Bot
Jacob Foti and Ryan Hong 
<img src="https://www.gather-cowork.com/wp-content/uploads/2021/06/happy-pup-1.png" alt="Rover" width="200" height="200">
## 1. Project Overview 
- RoverBot is a Discord bot that offers various fun and useful commands. It can translate text, provide cute dog pictures, answer questions using AI, and even generate images from text prompts.

## 2. Usage 
1. **Translate Text**: Translate text from one language to another.
   - Command: `!translate [input language code] [output language code] [text]`
   - Example: `!translate de en guten tag`
   Output: `good afternoon`
   
2. **Cute Dog Pictures**: Get adorable dog pictures.
   - Command: `!dog`

3. **Ping**: Rover responds with a friendly "Boop!"
   - Command: `!ping`

4. **Pet Rover**: Show some love to Rover by petting him.
   - Command: `!pet [number]`

5. **Feed Rover**: Feed Rover a virtual treat.
   - Command: `!feed`

6. **AI Question Answering**: Ask any question, and Rover will provide an answer using AI.
   - Command: `!gpt [question]`

7. **AI Image Generation**: Rover can generate images based on text prompts.
   - Command: `!image [prompt]`

8. **List of Commands**: Display a list of all available commands.
   - Command: `!cmds`

## Installation and Setup

To run RoverBot, follow these steps:

1. Clone this repository to your local machine.

2. Create a `.env` file and add the following environment variables:
DISCORD_TOKEN=your_discord_bot_token
API_KEY=your_openai_api_key

3. Install the required Python packages using pip:
pip install -r requirements.txt

4. Run the bot using Python:
python bot.py

5. Make sure to invite RoverBot to your Discord server and give it the necessary permissions.

Enjoy using RoverBot on your Discord server!

## 3. Dependencies 
- pip3 install python-dotenv
- pip3 install discord.py
- pip3 install translate
- pip3 install openai
- pip3 install requests
  
## 4. Project Structure
- Our Discord bot was developed using Python and the Discord.py library. The project structure consists of a single Python script, bot.py, where we implemented the bot's functionality. This script utilizes the Discord.py library to interact with the Discord API and respond to user commands.


## 5. Collaboration 
- Jacob took the lead in coding the bot's core functionality, while Ryan contributed to coding some of the bot's commands. Ryan also took charge of writing the project's README documentation.

## 6. Acknowledgement 
- Our bot relies on external resources, including the Dog API (https://dog.ceo/api) to fetch random dog images. Additionally, we used the OpenAI API for tasks such as generating images and text-based responses. These APIs greatly enriched the functionality of our Discord bot and contributed to its diverse features. We appreciate the services provided by these APIs in making our project possible.

- During the development process, we encountered challenges and questions related to both coding and bot functionality. We utilized ChatGPT as a valuable resource for assistance when we faced obstacles or needed guidance. ChatGPT's ability to provide solutions and explanations was instrumental in overcoming hurdles and optimizing our bot's performance.

## 7. Reflection 
- There were some challenged when figuring out how to get the Discord bot to properly work. Specifically, at times the coded command wouldn't work and it took some trial and error to fix it. ChatGPT also helped us with some of these problems because it provided an easy way to solve the problem. During many of our tests, the function wouldn't work and outputted an error message, which Jacob knew how to fix most of the time. There were many issues specifically with OpenAI's image generation, as it kept returning errors. This was fixed using ChatGPT's help.
- From a learning perspective, I think we both learned a lot about what it actually takes to code a Discord bot. Going foward, if we ever need to know how to make a bot, we will be able to use @client.command. ChatGPT was able to help us with a lot of the coding issues we had, as well as problems with the bot itself. 
