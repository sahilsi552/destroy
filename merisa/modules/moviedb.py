from pyrogram import Client, filters
import requests
from Merisa import QuantamBot as app

TMDB_API_KEY = "23c3b139c6d59ebb608fe6d5b974d888"

@app.on_message(filters.command("movie"))
async def movie_command(client, message):
    try:
        if len(message.command) > 1:
            movie_name = " ".join(message.command[1:])
            movie_info = get_movie_info(movie_name)
            await message.reply_text(movie_info)
        else:
            await message.reply_text("❖ Please enter a movie name after the /movie command. 🎬")
    except requests.exceptions.RequestException as e:
        await message.reply_text(f"❖ Network error occurred ➥ {str(e)} 🌐")
    except Exception as e:
        await message.reply_text(f"❖ An unexpected error occurred ➥ {str(e)} ⚠️")

def get_movie_info(movie_name):
    try:
        tmdb_api_url = f"https://api.themoviedb.org/3/search/movie"
        params = {"api_key": TMDB_API_KEY, "query": movie_name}
        response = requests.get(tmdb_api_url, params=params)
        response.raise_for_status()
        data = response.json()

        if data.get("results"):
            movie = data["results"][0]
            details_url = f"https://api.themoviedb.org/3/movie/{movie['id']}"
            details_params = {"api_key": TMDB_API_KEY}
            details_response = requests.get(details_url, params=details_params)
            details_response.raise_for_status()
            details_data = details_response.json()

            title = details_data.get("title", "N/A")
            release_date = details_data.get("release_date", "N/A")
            overview = details_data.get("overview", "N/A")
            vote_average = details_data.get("vote_average", "N/A")
            revenue = details_data.get("revenue", "N/A")
            runtime = details_data.get("runtime", "N/A")
            genres = ", ".join([genre["name"] for genre in details_data.get("genres", [])])
            director = ", ".join([crew["name"] for crew in details_data.get("credits", {}).get("crew", []) if crew["job"] == "Director"])
            production_companies = ", ".join([company["name"] for company in details_data.get("production_companies", [])])

            cast_url = f"https://api.themoviedb.org/3/movie/{movie['id']}/credits"
            cast_params = {"api_key": TMDB_API_KEY}
            cast_response = requests.get(cast_url, params=cast_params)
            cast_response.raise_for_status()
            cast_data = cast_response.json()
            actors = ", ".join([actor["name"] for actor in cast_data.get("cast", [])])

            similar_url = f"https://api.themoviedb.org/3/movie/{movie['id']}/similar"
            similar_params = {"api_key": TMDB_API_KEY}
            similar_response = requests.get(similar_url, params=similar_params)
            similar_response.raise_for_status()
            similar_data = similar_response.json()
            similar_movies = ", ".join([similar["title"] for similar in similar_data.get("results", [])[:5]])

            info = (
                f"🎬 **Title** ➥ {title}\n\n"
                f"📅 **Release Date** ➥ {release_date}\n\n"
                f"📝 **Overview** ➥ {overview}\n\n"
                f"⭐ **Vote Average** ➥ {vote_average}\n\n"
                f"🎭 **Actors** ➥ {actors}\n\n"
                f"🎬 **Director** ➥ {director}\n\n"
                f"🏢 **Production Companies** ➥ {production_companies}\n\n"
                f"💰 **Total Collection** ➥ {revenue}\n\n"
                f"⏳ **Runtime** ➥ {runtime} minutes\n\n"
                f"🎥 **Genres** ➥ {genres}\n\n"
                f"🎞️ **Similar Movies** ➥ {similar_movies}\n\n"
            )
            return info
        else:
            return "❖ Movie not found or API request failed. ❌"
    except requests.exceptions.RequestException as e:
        return f"❖ Network error occurred ➥ {str(e)} 🌐"
    except Exception as e:
        return f"❖ An unexpected error occurred ➥ {str(e)} ⚠️"

# __MODULE__ = "🍿 Movie" 
# __HELP__ = """  
# ✦ /movie : Let BaBa search the movie db for movies ✨  
# """