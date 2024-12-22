import logging  
import random  
import time  
import requests  
from pyrogram import Client, filters  
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup  
from pyrogram.enums import ChatAction, ParseMode  
from Merisa import QuantamBot as app  

# Constants and Configuration  
POKEAPI_BASE_URL = r"https://pokeapi.co/api/v2/"  
LOG_LEVEL = logging.INFO  
FUN_FACTS = [  
    "Did you know? Charmander's flame on its tail is a direct indicator of its health and mood.",  
    "Fun Fact: Squirtle's shell is not just for protection - it can also be used as a storage space.",  
    "Trivia: Caterpie is the shortest Pokémon in the original 151, measuring only 1.0 meter tall.",  
]  
RATE_LIMIT = 5  # in seconds  
last_request_time = 0  

# Setup logging configuration  
logging.basicConfig(level=LOG_LEVEL)  
logger = logging.getLogger(__name__)  

def rate_limited():  
    """Decorator to enforce rate-limiting on function calls."""  
    def decorator(func):  
        def wrapper(*args, **kwargs):  
            global last_request_time  
            current_time = time.time()  
            if current_time - last_request_time < RATE_LIMIT:  
                time.sleep(RATE_LIMIT - (current_time - last_request_time))  
            last_request_time = current_time  
            return func(*args, **kwargs)  
        return wrapper  
    return decorator  

@rate_limited()  
def fetch_data(endpoint: str):  
    """Fetch data from a specified PokeAPI endpoint and handle exceptions."""  
    url = f"{POKEAPI_BASE_URL}{endpoint}"  
    try:  
        response = requests.get(url)  
        response.raise_for_status()  
        return response.json()  
    except requests.HTTPError as err:  
        logger.error(f"HTTP error: {err}")  
        return None  
    except requests.RequestException as err:  
        logger.error(f"Network error: {err}")  
        return None  

async def send_reply(client, message, response_message, photo=None):  
    """Helper function to send a response message, optionally with a photo."""  
    if photo:  
        await message.reply_photo(  
            photo=photo,  
            caption=response_message,  
            parse_mode=ParseMode.MARKDOWN  
        )  
    else:  
        await message.reply_text(response_message, parse_mode=ParseMode.MARKDOWN)  

@app.on_message(filters.command("pokemon"))  
async def get_pokemon(client, message):  
    """Handle the /pokemon command to fetch Pokémon details."""  
    command_parts = message.text.split(None, 1)  
    if len(command_parts) < 2:  
        await message.reply_text("⚠️ Please provide a Pokémon name.", parse_mode=ParseMode.MARKDOWN)  
        return  

    pokemon_name = command_parts[1].strip()  
    data = fetch_data(f"pokemon/{pokemon_name.lower()}")  

    if not data:  
        await message.reply_text("❌ Could not retrieve Pokémon data. Please try again later.", parse_mode=ParseMode.MARKDOWN)  
        return  

    try:  
        name = data["name"].capitalize()  
        abilities = ', '.join(ability["ability"]["name"].capitalize() for ability in data["abilities"])  
        stats = {stat["stat"]["name"].capitalize(): stat["base_stat"] for stat in data["stats"]}  
        types = ', '.join(type_info["type"]["name"].capitalize() for type_info in data["types"])  
        height = data["height"] / 10  
        weight = data["weight"] / 10  
        base_experience = data["base_experience"]  

        response_message = (  
            f"✨ **{name}** ✨\n\n"  
            f"**Abilities**: {abilities}\n"  
            f"**Types**: {types}\n"  
            f"**Height**: {height} m\n"  
            f"**Weight**: {weight} kg\n"  
            f"**Base Experience**: {base_experience}\n\n"  
            f"**Stats**:\n"  
        )  
        
        for stat, value in stats.items():  
            response_message += f"• {stat}: {value}\n"  
        
        species_data = fetch_data(f"pokemon-species/{pokemon_name.lower()}")  
        if species_data:  
            evolution_chain_url = species_data["evolution_chain"]["url"]  
            evolution_data = fetch_data(evolution_chain_url.replace(POKEAPI_BASE_URL, ""))  
            if evolution_data:  
                evolutions = []  
                chain = evolution_data["chain"]  
                while chain:  
                    evolutions.append(chain["species"]["name"].capitalize())  
                    chain = chain["evolves_to"][0] if chain["evolves_to"] else None  
                evolution_links = [f"[{evolution}](https://pokeapi.co/api/v2/pokemon/{evolution.lower()})" for evolution in evolutions]  
                response_message += f"\n**Evolutions**: {', '.join(evolution_links)}\n"  

        poke_img_url = f"https://img.pokemondb.net/artwork/{pokemon_name.lower()}.jpg"  
        fun_fact = random.choice(FUN_FACTS)  

        await send_reply(client, message, response_message + f"\n\n💡 **Fun Fact**: {fun_fact}", poke_img_url)  
    except KeyError:  
        await message.reply_text("❌ Pokémon not found. Please check the name and try again.", parse_mode=ParseMode.MARKDOWN)  

async def fetch_and_reply(endpoint: str, entity_name: str, icon: str, client, message):  
    """Generic function to fetch data and send a formatted response."""  
    data = fetch_data(endpoint)  
    if data:  
        items = [item["name"].capitalize() for item in data.get("results", [])]  
        response_message = f"{icon} **{entity_name}** {icon}\n\n" + "\n".join(items)  
        await send_reply(client, message, response_message)  
    else:  
        await message.reply_text(f"❌ Could not retrieve {entity_name.lower()}. Please try again later.", parse_mode=ParseMode.MARKDOWN)  

@app.on_message(filters.command("berries"))  
async def get_berries(client, message):  
    """Handle the /berries command to list berries."""  
    await fetch_and_reply("berry/", "Berries", "🍓", client, message)  

@app.on_message(filters.command("contests"))  
async def get_contests(client, message):  
    """Handle the /contests command to list contests."""  
    await fetch_and_reply("contest-type/", "Contests", "🏆", client, message)  

@app.on_message(filters.command("encounters"))  
async def get_encounters(client, message):  
    """Handle the /encounters command to list encounter methods."""  
    await fetch_and_reply("encounter-method/", "Encounters", "🚶", client, message)  

@app.on_message(filters.command("evolution"))  
async def get_evolution(client, message):  
    """Handle the /evolution command to list all evolution chains."""  
    data = fetch_data("evolution-chain/")  
    if data:  
        evolutions = [f"Evolution Chain #{evolution['url'].split('/')[-2]}" for evolution in data.get("results", [])]  
        response_message = "🧬 **Evolutions** 🧬\n\n" + "\n".join(evolutions)  
        await send_reply(client, message, response_message)  
    else:  
        await message.reply_text("❌ Could not retrieve evolution data. Please try again later.", parse_mode=ParseMode.MARKDOWN)  

@app.on_message(filters.command("games"))  
async def get_games(client, message):  
    """Handle the /games command to list game versions."""  
    await fetch_and_reply("version/", "Games", "🎮", client, message)  

@app.on_message(filters.command("items"))  
async def get_items(client, message):  
    """Handle the /items command to list items."""  
    await fetch_and_reply("item/", "Items", "🛒", client, message)  

@app.on_message(filters.command("locations"))  
async def get_locations(client, message):  
    """Handle the /locations command to list locations."""  
    await fetch_and_reply("location/", "Locations", "🗺️", client, message)  

@app.on_message(filters.command("machines"))  
async def get_machines(client, message):  
    """Handle the /machines command to list machines."""  
    data = fetch_data("machine/")  
    if data:  
        machines = [f"Machine #{machine['url'].split('/')[-2]}" for machine in data.get("results", [])]  
        response_message = "🛠️ **Machines** 🛠️\n\n" + "\n".join(machines)  
        await send_reply(client, message, response_message)  
    else:  
        await message.reply_text("❌ Could not retrieve machines. Please try again later.", parse_mode=ParseMode.MARKDOWN)  

@app.on_message(filters.command("moves"))  
async def get_moves(client, message):  
    """Handle the /moves command to list moves."""  
    await fetch_and_reply("move/", "Moves", "⚔️", client, message)  

# Module metadata  
__MODULE__ = "Pᴏᴋᴇᴅᴇx"  
__HELP__ = """  
⬤ /pokemon <name> ➥ Search for a Pokémon character.  
⬤ /berries ➥ Get a list of berries.  
⬤ /contests ➥ Explore Pokémon contests.  
⬤ /encounters ➥ Discover encounter methods.  
⬤ /evolution ➥ Uncover evolution chains.  
⬤ /games ➥ Dive into Pokémon games.  
⬤ /items ➥ Explore available items.  
⬤ /locations ➥ Locate various Pokémon locations.  
⬤ /machines ➥ Learn about machines.  
⬤ /moves ➥ Get a list of moves.  
"""
