from pyrogram import Client, filters

from Merisa import QuantamBot as app
from pyurbandict import UrbanDict

def get_urban_definition(word_to_search):
    # Initialize UrbanDict with the provided word
    word = UrbanDict(word_to_search)

    # Search for the word in Urban Dictionary
    results = word.search()

    # Check if results are found
    if results:
        # Get the first result
        x = results[0]

        # Create a dictionary to store the details
        definition_details = {
            "Word": x.word,
            "Definition": x.definition,
            "Example": x.example,
            "Author": x.author,
            "Thumbs Up": x.thumbs_up,
            "Thumbs Down": x.thumbs_down,
            "Written On": x.written_on,
            "Permalink": x.permalink,
            "Definition ID": x.defid
        }
        return definition_details
    else:
        return f"No results found. for {word_to_search}"

# Usage example
# word_info = get_urban_definition("python")
# print(word_info)

@app.on_message(filters.command("ud"))
async def ud_command(client, message):
    # Extract the word from the command
    x=await message.reply("wait a while")
    word = message.text.split(" ", 1)[1] if len(message.text.split(" ", 1)) > 1 else None

    if not word:
        await message.reply("Please provide a word to define. Usage: /ud <word>")
        return

    # Search for the definition using UrbanDict
    urban_dict = get_urban_definition(word)
    await x.edit_text(urban_dict)


