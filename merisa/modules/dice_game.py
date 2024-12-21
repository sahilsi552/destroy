from pyrogram import Client, enums, filters  
import asyncio  
from Merisa import QuantamBot  
from pyrogram.handlers import MessageHandler  
import random  
import logging  

# 🏆 User-defined variables and constants  
EMOJI_TYPES = {  
    "dice": "🎲",  
    "dart": "🎯",  
    "basket": "🏀",  
    "jackpot": "🎰",  
    "ball": "🎳",  
    "football": "⚽",  
}  

leaderboard = {}  

# 🎥 Configure logging  
logging.basicConfig(level=logging.INFO)  
logger = logging.getLogger(__name__)  

# 🛡️ Helper functions  
def log_error(command, user_mention, error):  
    logger.error(f"Error in {command} command by user {user_mention}: {error}")  

def get_user_name(message):  
   return message.from_user.first_name  
          
async def send_dice_and_reply(bot, message, emoji):  
    try:  
        response = await bot.send_dice(message.chat.id, emoji)  
        score = response.dice.value  
        user_id = message.from_user.id  
        user_mention = get_user_name(message)  

        leaderboard[user_id] = {  
            'name': user_mention,  
            'score': max(leaderboard.get(user_id, {'score': 0})['score'], score)  
        }  

        await message.reply_text(f"Hey {user_mention}, your score is: {score} {emoji} 🎉", quote=True)  
        logger.info(f"{emoji} command executed by user {user_mention} with score {score}")  
    except Exception as e:  
        await message.reply_text(f"An error occurred: {e}", quote=True)  
        log_error(emoji, get_user_name(message), e)  

# 🌟 New features  
async def display_leaderboard(bot, message):  
    if not leaderboard:  
        await message.reply_text("No scores recorded yet. Be the first! 🌟", quote=True)  
        return  
    
    leaderboard_text = "\n".join([f"{data['name']}: {data['score']}" for _, data in sorted(leaderboard.items(), key=lambda item: item[1]['score'], reverse=True)])  
    await message.reply_text(f"🏆 **Leaderboard** 🏆\n\n{leaderboard_text}", quote=True)  

@QuantamBot.on_message(filters.command("leaderboard"))  
async def handle_leaderboard_command(bot, message):  
    await display_leaderboard(bot, message)  

async def reset_leaderboard(bot, message):  
    leaderboard.clear()  
    await message.reply_text("Leaderboard has been reset! 🔄", quote=True)  

@QuantamBot.on_message(filters.command("resetleaderboard"))  
async def handle_reset_leaderboard_command(bot, message):  
    await reset_leaderboard(bot, message)  

# 🕹️ Commands mapping  
for command, emoji in EMOJI_TYPES.items():  
    @QuantamBot.on_message(filters.command(command))  
    async def handle_command(bot, message, emoji=emoji):  
        await send_dice_and_reply(bot, message, emoji)  

# Existing features  
@QuantamBot.on_message(filters.command("coinflip"))  
async def coinflip(bot, message):  
    try:  
        result = random.choice(["Heads", "Tails"])  
        await message.reply_text(f"🪙 Coin Flip Result: {result}", quote=True)  
        logger.info(f"Coinflip command executed by user {get_user_name(message)} with result {result}")  
    except Exception as e:  
        await message.reply_text(f"An error occurred: {e}", quote=True)  
        log_error("coinflip", get_user_name(message), e)  

@QuantamBot.on_message(filters.command("rockpaperscissors"))  
async def rockpaperscissors(bot, message):  
    try:  
        choices = ["Rock 🪨", "Paper 📄", "Scissors ✂️"]  
        user_choice = random.choice(choices)  
        bot_choice = random.choice(choices)  
        result = "It's a tie!" if user_choice == bot_choice else (  
            "You win!" if (user_choice == "Rock 🪨" and bot_choice == "Scissors ✂️") or  
                          (user_choice == "Paper 📄" and bot_choice == "Rock 🪨") or  
                          (user_choice == "Scissors ✂️" and bot_choice == "Paper 📄") else "You lose!"  
        )  
        await message.reply_text(f"🪨📄✂️ Rock-Paper-Scissors\n\nYou: {user_choice}\nBot: {bot_choice}\n\n**{result}**", quote=True)  
        logger.info(f"Rock-Paper-Scissors command executed by user {get_user_name(message)} with result {result}")  
    except Exception as e:  
        await message.reply_text(f"An error occurred: {e}", quote=True)  
        log_error("rockpaperscissors", get_user_name(message), e)  

@QuantamBot.on_message(filters.command("dicepoker"))  
async def dicepoker(bot, message):  
    try:  
        suits = ['♥️ Hearts', '♦️ Diamonds', '♣️ Clubs', '♠️ Spades']  
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']  
        deck = [f"{value} of {suit}" for value in values for suit in suits]  
        hand = random.sample(deck, 5)  
        hand_str = '\n'.join(hand)  
        
        value_counts = {value: sum(card.startswith(value) for card in hand) for value in values}  
        suit_counts = {suit: sum(card.endswith(suit.split()[1]) for card in hand) for suit in suits}  
        is_flush = max(suit_counts.values()) == 5  
        sorted_values = sorted([values.index(card.split()[0]) for card in hand])  
        is_straight = all(sorted_values[i] + 1 == sorted_values[i + 1] for i in range(4))  
        
        if is_flush and is_straight:  
            hand_rank = "🃏 Straight Flush"  
        elif 4 in value_counts.values():  
            hand_rank = "🃏 Four of a Kind"  
        elif 3 in value_counts.values() and 2 in value_counts.values():  
            hand_rank = "🃏 Full House"  
        elif is_flush:  
            hand_rank = "🃏 Flush"  
        elif is_straight:  
            hand_rank = "🃏 Straight"  
        elif 3 in value_counts.values():  
            hand_rank = "🃏 Three of a Kind"  
        elif list(value_counts.values()).count(2) == 2:  
            hand_rank = "🃏 Two Pair"  
        elif 2 in value_counts.values():  
            hand_rank = "🃏 One Pair"  
        else:  
            hand_rank = "🃏 High Card"  
        
        await message.reply_text(  
            f"🎲 **Your Poker Hand** 🎲\n\n{hand_str}\n\n**Hand Rank:** {hand_rank}",  
            quote=True  
        )  
        logger.info(f"Dicepoker command executed by user {get_user_name(message)} with hand {hand_str} and rank {hand_rank}")  
    except Exception as e:  
        await message.reply_text(f"An error occurred: {e}", quote=True)  
        log_error("dicepoker", get_user_name(message), e)  

__HELP__ = """  
*To Play Games Using Emojis:*  

✦ /dice 🎲 : Have a thrilling dice game with BaBa  
✦ /dart 🎯 : Engage in a dart competition with BaBa  
✦ /basket 🏀 : Have a fun basketball shoot-out with BaBa  
✦ /ball 🎳 : Go on a virtual bowling session with BaBa  
✦ /football ⚽ : Have an exciting football match with BaBa  
✦ /jackpot 🎰 : Spin the slot machine and try your luck with BaBa  
✦ /dicepoker 🎲 : Play a dice poker game with BaBa  
✦ /coinflip 🪙 : Flip a coin and see the result  
✦ /rockpaperscissors 🪨📄✂️ : Play Rock-Paper-Scissors with BaBa  
✦ /leaderboard 🏆 : View the top scores and compete with others  
✦ /resetleaderboard 🔄 : Reset the leaderboard for a fresh start  
"""  

__MODULE__ = "🎯 Match"