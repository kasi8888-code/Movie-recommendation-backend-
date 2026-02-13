import os 
import sqlite3
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv
import requests
load_dotenv()
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
TMDB_API_KEY=os.getenv("TMDB_API_KEY")
if(not GEMINI_API_KEY or not TMDB_API_KEY):
    raise ValueError("API keys not found. Please set GEMINI_API_KEY and TMDB_API_KEY in the .env file.")
client = genai.Client(api_key=GEMINI_API_KEY)
app =FastAPI(title="Movie Recommendation API", description="Backend for AWS Cloud Club Recruitment Task.", version="1.0.0")
DB_NAME = "movies.db"
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS favourites(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            mood_context TEXT NOT NULL,
            description TEXT,
            genres TEXT,
            release_date TEXT,
            rating REAL
        )
    ''')
    conn.commit()
    conn.close()

init_db()
class MoodRequest(BaseModel):
    mood:str
class FavouriteMovie(BaseModel):
    title:str
    mood_context:str
    description:str
    genres:str="Unknown"
    release_date:str
    rating:float 
def get_genre_from_gemini(mood: str):
    prompt =f"""Act as a movie expert. I am feeling '{mood}'. 
    Suggest strictly ONE movie genre that matches this mood from the following list: 
    Action, Adventure, Animation, Comedy, Crime, Documentary, Drama, Family, Fantasy, History, Horror, Music, Mystery, Romance, Science Fiction, TV Movie, Thriller, War, Western.
    
    Reply ONLY with the genre name. Nothing else.
    """
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        print(f"Gemini API Error: {type(e).__name__}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Gemini API failed: {str(e)}")
    
def get_movies_from_tmdb(genre_name: str):
    genre_map={
        "Action": 28, "Adventure": 12, "Animation": 16, "Comedy": 35, 
        "Crime": 80, "Documentary": 99, "Drama": 18, "Family": 10751, 
        "Fantasy": 14, "History": 36, "Horror": 27, "Music": 10402, 
        "Mystery": 9648, "Romance": 10749, "Science Fiction": 878, 
        "TV Movie": 10770, "Thriller": 53, "War": 10752, "Western": 37

    }
    genre_id=genre_map.get(genre_name,35)
    url=f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres={genre_id}&sort_by=popularity.desc"
    response=requests.get(url)
    return response.json().get("results",[])[:5]

@app.get("/")
def read_root():
    return {"message": "Welcome to the Movie Recommendation API! Use the /recommendations endpoint with a POST request to get movie suggestions based on your mood."}

@app.get("/models")
def list_models():
    """List available Gemini models"""
    try:
        models = []
        for m in client.models.list():
            models.append({
                "name": m.name,
                "supported_actions": m.supported_actions
            })
        return {"available_models": models}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/recommend")
def recommend_movies(mood_request: MoodRequest):
    try:
        genre=get_genre_from_gemini(mood_request.mood)
        movies=get_movies_from_tmdb(genre)
        return {"mood":mood_request.mood,"gemini_suggested_genre": genre,
        "recommended_movies": movies}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@app.post("/favourites")
def save_favourite(movie:FavouriteMovie):
    try:
        conn=sqlite3.connect(DB_NAME)
        cursor=conn.cursor()
        cursor.execute('''
            INSERT INTO favourites (title, mood_context, description, genres, release_date, rating)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (movie.title, movie.mood_context, movie.description, movie.genres, movie.release_date, movie.rating))
        conn.commit()
        conn.close()
        return {"message": "Movie saved to favourites successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@app.get("/favourites")
def get_favourites():
    try:
        conn=sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM favourites')
        rows=cursor.fetchall()
        conn.close()
        return {"favourites":[dict(row) for row in rows]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
        