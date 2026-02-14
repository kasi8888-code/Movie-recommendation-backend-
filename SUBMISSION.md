# Backend Submission - Movie Recommendation API

## 1. GitHub Repository Link

**Repository URL:** https://github.com/kasi8888-code/Movie-recommendation-backend-

**Branch:** `feature/movie-logic`

**Live Code:** https://github.com/kasi8888-code/Movie-recommendation-backend-/tree/feature/movie-logic

---

## 2. API Endpoints Description

### **Endpoint 1: GET /**
- **Purpose:** Welcome message and API information
- **Method:** GET
- **URL:** `http://127.0.0.1:8000/`
- **Request Body:** None
- **Response:**
  ```json
  {
      "message": "Welcome to the Movie Recommendation API! Use the /recommendations endpoint with a POST request to get movie suggestions based on your mood."
  }
  ```
- **Status Code:** 200 OK

---

### **Endpoint 2: GET /models**
- **Purpose:** List all available Gemini AI models
- **Method:** GET
- **URL:** `http://127.0.0.1:8000/models`
- **Request Body:** None
- **Response:**
  ```json
  {
      "available_models": [
          {
              "name": "models/gemini-2.5-flash",
              "supported_actions": [
                  "generateContent",
                  "countTokens",
                  "createCachedContent",
                  "batchGenerateContent"
              ]
          }
      ]
  }
  ```
- **Status Code:** 200 OK

---

### **Endpoint 3: POST /recommend**
- **Purpose:** Get personalized movie recommendations based on mood
- **Method:** POST
- **URL:** `http://127.0.0.1:8000/recommend`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
      "mood": "adventurous"
  }
  ```
- **Response:**
  ```json
  {
      "mood": "adventurous",
      "gemini_suggested_genre": "Adventure",
      "recommended_movies": [
          {
              "adult": false,
              "backdrop_path": "/tyjXlexbNZQ0ZT1KEJslQtBirqc.jpg",
              "genre_ids": [12, 53, 878],
              "id": 840464,
              "original_language": "en",
              "original_title": "Greenland 2: Migration",
              "overview": "Having found the safety of the Greenland bunker...",
              "popularity": 365.031,
              "poster_path": "/z2tqCJLsw6uEJ8nJV8BsQXGa3dr.jpg",
              "release_date": "2026-01-07",
              "title": "Greenland 2: Migration",
              "video": false,
              "vote_average": 6.536,
              "vote_count": 405
          }
      ]
  }
  ```
- **Status Code:** 200 OK
- **Supported Moods:** happy, sad, adventurous, romantic, scared, excited, bored, angry, etc.

---

### **Endpoint 4: POST /favourites**
- **Purpose:** Save a movie to favorites list
- **Method:** POST
- **URL:** `http://127.0.0.1:8000/favourites`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
      "title": "Zootopia 2",
      "mood_context": "adventurous",
      "description": "After cracking the biggest case in Zootopia's history...",
      "genres": "Animation, Comedy, Adventure",
      "release_date": "2025-11-26",
      "rating": 7.6
  }
  ```
- **Response:**
  ```json
  {
      "message": "Movie saved to favourites successfully!"
  }
  ```
- **Status Code:** 200 OK

---

### **Endpoint 5: GET /favourites**
- **Purpose:** Retrieve all saved favorite movies
- **Method:** GET
- **URL:** `http://127.0.0.1:8000/favourites`
- **Request Body:** None
- **Response:**
  ```json
  {
      "favourites": [
          {
              "id": 1,
              "title": "Zootopia 2",
              "mood_context": "adventurous",
              "description": "After cracking the biggest case in Zootopia's history...",
              "genres": "Animation, Comedy, Adventure",
              "release_date": "2025-11-26",
              "rating": 7.6
          }
      ]
  }
  ```
- **Status Code:** 200 OK

---

## 3. Tech Stack Used

### **Backend Framework**
- **FastAPI** (v0.100+) - Modern, fast web framework for building APIs with Python

### **AI/ML**
- **Google Gemini AI** (google-genai SDK v1.0+) - AI-powered genre recommendation based on mood analysis
- **Model Used:** `gemini-2.5-flash` - Latest Gemini model for content generation

### **External APIs**
- **TMDB API** (The Movie Database) - Movie data, metadata, and information retrieval

### **Database**
- **SQLite3** - Lightweight relational database for storing user favorites

### **Python Libraries**
- **Pydantic** - Data validation and settings management using Python type annotations
- **python-dotenv** - Environment variable management for secure API key storage
- **requests** - HTTP library for making API calls to TMDB
- **uvicorn** - ASGI server for running FastAPI applications

### **Development Tools**
- **Python 3.13** - Programming language
- **Git** - Version control
- **Postman** - API testing and documentation

### **Environment**
- **Virtual Environment (venv)** - Isolated Python environment for dependency management

---

## 4. How to Run Locally

### **Prerequisites**
- Python 3.13 or higher installed
- Git installed
- Google Gemini API Key ([Get it here](https://ai.google.dev/))
- TMDB API Key ([Get it here](https://www.themoviedb.org/settings/api))

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/kasi8888-code/Movie-recommendation-backend-.git
cd Movie-recommendation-backend-
git checkout feature/movie-logic
```

### **Step 2: Create Virtual Environment**
```bash
# On Windows
python -m venv venv
venv\Scripts\Activate.ps1

# On Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### **Step 3: Install Dependencies**
```bash
pip install fastapi uvicorn google-genai python-dotenv requests
```

**Or create a `requirements.txt`:**
```txt
fastapi>=0.100.0
uvicorn>=0.23.0
google-genai>=1.0.0
python-dotenv>=1.0.0
requests>=2.31.0
```

Then install:
```bash
pip install -r requirements.txt
```

### **Step 4: Configure Environment Variables**
Create a `.env` file in the project root:
```env
GEMINI_API_KEY=your_gemini_api_key_here
TMDB_API_KEY=your_tmdb_api_key_here
```

**To get API keys:**
- **Gemini API Key:** Visit https://ai.google.dev/ → Create project → Generate API key
- **TMDB API Key:** Visit https://www.themoviedb.org/ → Settings → API → Request API key

### **Step 5: Run the Application**
```bash
uvicorn main:app --reload
```

**Expected Output:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [XXXX] using StatReload
INFO:     Started server process [XXXX]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### **Step 6: Access the API**
- **Base URL:** http://127.0.0.1:8000
- **Interactive Docs (Swagger UI):** http://127.0.0.1:8000/docs
- **Alternative Docs (ReDoc):** http://127.0.0.1:8000/redoc

### **Step 7: Test with Postman**
1. Open Postman
2. Import the endpoints or create requests manually
3. Test each endpoint as described in Section 2

### **Troubleshooting**
- **Port 8000 already in use:** Use `uvicorn main:app --reload --port 8001`
- **Module not found errors:** Reinstall dependencies with `pip install -r requirements.txt`
- **API key errors:** Verify `.env` file exists and contains valid keys
- **Database errors:** Delete `movies.db` and restart the server

---

## 5. Screenshots of Request/Response

### **Instructions for Taking Screenshots:**

#### **Screenshot 1: GET / (Welcome Endpoint)**
1. Open Postman
2. Create GET request to `http://127.0.0.1:8000/`
3. Click "Send"
4. Take screenshot showing:
   - Request URL
   - Method (GET)
   - Response body
   - Status code (200 OK)

#### **Screenshot 2: GET /models (List Models)**
1. Create GET request to `http://127.0.0.1:8000/models`
2. Click "Send"
3. Take screenshot showing available Gemini models

#### **Screenshot 3: POST /recommend (Movie Recommendations)**
1. Create POST request to `http://127.0.0.1:8000/recommend`
2. Set Headers: `Content-Type: application/json`
3. Set Body (raw JSON):
   ```json
   {
       "mood": "adventurous"
   }
   ```
4. Click "Send"
5. Take screenshot showing:
   - Request body
   - Response with genre and movie list
   - Status code (200 OK)

#### **Screenshot 4: POST /recommend - Different Mood**
1. Use same endpoint with different mood:
   ```json
   {
       "mood": "happy"
   }
   ```
2. Take screenshot showing Comedy genre recommendation

#### **Screenshot 5: POST /favourites (Save Favorite)**
1. Create POST request to `http://127.0.0.1:8000/favourites`
2. Set Headers: `Content-Type: application/json`
3. Set Body (raw JSON):
   ```json
   {
       "title": "Zootopia 2",
       "mood_context": "adventurous",
       "description": "After cracking the biggest case in Zootopia's history...",
       "genres": "Animation, Comedy, Adventure",
       "release_date": "2025-11-26",
       "rating": 7.6
   }
   ```
4. Click "Send"
5. Take screenshot showing success message

#### **Screenshot 6: GET /favourites (Retrieve Favorites)**
1. Create GET request to `http://127.0.0.1:8000/favourites`
2. Click "Send"
3. Take screenshot showing the saved movie in the response

#### **Screenshot 7: Interactive API Docs**
1. Open browser to `http://127.0.0.1:8000/docs`
2. Take screenshot showing Swagger UI with all endpoints

---

## Additional Information

### **Project Structure**
```
Movie-recommendation-backend-/
├── main.py              # Main FastAPI application
├── .env                 # Environment variables (not in repo)
├── .gitignore          # Git ignore rules
├── README.md           # Project documentation
├── SUBMISSION.md       # This file
├── movies.db           # SQLite database (auto-generated)
└── venv/               # Virtual environment (not in repo)
```

### **Security Features**
- ✅ API keys stored in `.env` (excluded from Git)
- ✅ `.gitignore` protects sensitive files
- ✅ Input validation using Pydantic models
- ✅ Error handling for all endpoints

### **Key Features**
- AI-powered mood-to-genre mapping
- Real-time movie data from TMDB
- Persistent favorites storage
- RESTful API design
- Interactive API documentation
- Comprehensive error handling

### **Testing Recommendations**
1. Test all endpoints in sequence
2. Try different moods: happy, sad, adventurous, romantic, scared
3. Save multiple favorites
4. Verify database persistence (restart server and check favorites)
5. Test error cases (invalid mood, missing fields)

---

## Contact & Support

**Developer:** Naveen Kasi  
**GitHub:** https://github.com/kasi8888-code  
**Repository:** https://github.com/kasi8888-code/Movie-recommendation-backend-

For questions or issues, please open an issue on the GitHub repository.

---

**Submission Date:** February 13, 2026  
**Project:** AWS Cloud Club Recruitment Task - Backend Development
