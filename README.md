# 🎬 Movie Recommendation API

A FastAPI-based movie recommendation system that uses Google's Gemini AI to suggest movies based on your mood. Built as part of the AWS Cloud Club Recruitment Task.

## ✨ Features

- **Mood-based Recommendations**: Get movie suggestions based on your current mood using Gemini AI
- **TMDB Integration**: Fetches real movie data from The Movie Database (TMDB)
- **Favorites Management**: Save and retrieve your favorite movies
- **RESTful API**: Clean and well-documented API endpoints
- **Interactive Docs**: Built-in Swagger UI documentation

## 🚀 Tech Stack

- **FastAPI** - Modern Python web framework
- **Google Gemini AI** - AI-powered genre recommendation
- **TMDB API** - Movie data and information
- **SQLite** - Local database for favorites
- **Python 3.13** - Programming language

## 📋 Prerequisites

- Python 3.13+
- Google Gemini API Key ([Get it here](https://ai.google.dev/))
- TMDB API Key ([Get it here](https://www.themoviedb.org/settings/api))

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd movie-backend
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     venv\Scripts\Activate.ps1
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install fastapi uvicorn google-genai python-dotenv requests
   ```

5. **Create a `.env` file**
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   TMDB_API_KEY=your_tmdb_api_key_here
   ```

## 🏃 Running the Application

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

## 📚 API Endpoints

### 1. **GET /** - Welcome Message
Returns a welcome message.

**Response:**
```json
{
    "message": "Welcome to the Movie Recommendation API!..."
}
```

---

### 2. **GET /models** - List Available Models
Returns available Gemini AI models.

**Response:**
```json
{
    "available_models": [
        {
            "name": "models/gemini-2.5-flash",
            "supported_actions": ["generateContent", "countTokens", ...]
        }
    ]
}
```

---

### 3. **POST /recommend** - Get Movie Recommendations
Get movie recommendations based on your mood.

**Request Body:**
```json
{
    "mood": "happy"
}
```

**Response:**
```json
{
    "mood": "happy",
    "gemini_suggested_genre": "Comedy",
    "recommended_movies": [
        {
            "title": "Movie Title",
            "overview": "Movie description...",
            "release_date": "2025-12-01",
            "vote_average": 7.5,
            ...
        }
    ]
}
```

**Supported Moods:** happy, sad, adventurous, romantic, scared, excited, bored, angry, etc.

---

### 4. **POST /favourites** - Save Favorite Movie
Add a movie to your favorites list.

**Request Body:**
```json
{
    "title": "Zootopia 2",
    "mood_context": "adventurous",
    "description": "After cracking the biggest case...",
    "genres": "Animation, Comedy, Adventure",
    "release_date": "2025-11-26",
    "rating": 7.6
}
```

**Response:**
```json
{
    "message": "Movie saved to favourites successfully!"
}
```

---

### 5. **GET /favourites** - Get All Favorites
Retrieve all saved favorite movies.

**Response:**
```json
{
    "favourites": [
        {
            "id": 1,
            "title": "Zootopia 2",
            "mood_context": "adventurous",
            "description": "After cracking the biggest case...",
            "genres": "Animation, Comedy, Adventure",
            "release_date": "2025-11-26",
            "rating": 7.6
        }
    ]
}
```

## 📖 Interactive Documentation

Once the server is running, visit:
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## 🧪 Testing with Postman

1. Import the endpoints into Postman
2. Set request method (GET/POST)
3. Add request body for POST requests
4. Send request and view response

### Example Test Flow:
```
1. GET /                    → Verify server is running
2. POST /recommend          → Get recommendations for "happy"
3. POST /favourites         → Save a favorite movie
4. GET /favourites          → Verify movie was saved
```

## 🗂️ Project Structure

```
movie-backend/
├── main.py              # Main application file
├── .env                 # Environment variables (API keys)
├── movies.db            # SQLite database (auto-generated)
├── venv/                # Virtual environment
└── README.md            # This file
```

## 🔑 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GEMINI_API_KEY` | Google Gemini API key for AI recommendations | ✅ Yes |
| `TMDB_API_KEY` | The Movie Database API key for movie data | ✅ Yes |

## 🛠️ How It Works

1. **User sends mood** → API receives mood input
2. **Gemini AI processes** → AI determines matching genre
3. **TMDB fetches movies** → Retrieves top 5 movies from that genre
4. **Response returned** → User receives personalized recommendations

## 📝 Genre Mapping

The API supports these genres:
- Action, Adventure, Animation, Comedy, Crime
- Documentary, Drama, Family, Fantasy, History
- Horror, Music, Mystery, Romance, Science Fiction
- TV Movie, Thriller, War, Western

## 🐛 Troubleshooting

### Common Issues:

**1. "ModuleNotFoundError: No module named 'dotenv'"**
```bash
pip install python-dotenv
```

**2. "API keys not found"**
- Make sure `.env` file exists in the project root
- Verify API keys are correctly set

**3. "No such table: favourites"**
- Restart the server to initialize the database

**4. "Gemini API 404 error"**
- Check if your API key is valid
- Ensure you're using the correct model name (`gemini-2.5-flash`)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Built with ❤️ for AWS Cloud Club Recruitment Task

## 🙏 Acknowledgments

- [Google Gemini AI](https://ai.google.dev/)
- [The Movie Database (TMDB)](https://www.themoviedb.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
