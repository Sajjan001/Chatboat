# Nirmaan Chatboat 🤖

A beautiful AI chatbot built with Flask, HTML/CSS/JavaScript, and powered by Groq's Llama 3.1 model.

## Features

✨ **Beautiful UI**
- Ocean/boat themed dark interface
- Responsive design
- Smooth animations
- Message bubbles with gradients

🧠 **Intelligent Chat**
- Real-time AI responses
- Smart context-aware thinking
- Chat history management
- Clean message display

## Local Setup

### Prerequisites
- Python 3.8+
- Groq API Key (get from [groq.com](https://console.groq.com))

### Installation

1. **Clone or download the repository**

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Create .env file**
```bash
cp .env.example .env
# Edit .env and add your GROQ_API_KEY
```

4. **Run the server**
```bash
python server.py
```

5. **Open in browser**
```
http://localhost:5000
```

## Deployment on Render

### Step 1: Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/nirmaan-chatboat.git
git push -u origin main
```

### Step 2: Deploy on Render
1. Go to [render.com](https://render.com)
2. Sign up / Log in
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Fill in the details:
   - **Name**: `nirmaan-chatboat`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python server.py`
   - **Plan**: Free (or paid if you want more resources)

6. Add Environment Variable:
   - Click "Environment"
   - Add new variable:
     - **Key**: `GROQ_API_KEY`
     - **Value**: Your Groq API Key

7. Click "Create Web Service"

### Step 3: Access Your Bot
Once deployed, Render will give you a URL like:
```
https://your-app-name.onrender.com
```

Open this URL to use your chatbot!

## Project Structure

```
.
├── server.py           # Flask backend
├── index.html          # Frontend UI
├── requirements.txt    # Python dependencies
├── Procfile           # Deployment config
├── render.yaml        # Render config
├── .env.example       # Environment variables template
└── .gitignore         # Git ignore rules
```

## Files Explained

- **server.py**: Flask server with API endpoints
- **index.html**: Beautiful HTML/CSS/JS interface
- **requirements.txt**: Python packages needed
- **Procfile**: Tells Render how to run the app
- **render.yaml**: Alternative Render configuration
- **.env**: Stores API keys (don't commit this!)

## Environment Variables

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_groq_api_key_here
PORT=5000
```

## API Endpoints

### POST `/api/chat`
Send a message and get a response

**Request:**
```json
{
  "message": "What is artificial intelligence?"
}
```

**Response:**
```json
{
  "response": "AI is...",
  "success": true
}
```

### POST `/api/clear`
Clear chat history

**Response:**
```json
{
  "success": true,
  "message": "Chat cleared"
}
```

## Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Flask (Python)
- **AI**: Groq Llama 3.1
- **Deployment**: Render
- **Libraries**: langchain-groq, python-dotenv

## Get Groq API Key

1. Visit [console.groq.com](https://console.groq.com)
2. Sign up for a free account
3. Create an API key
4. Copy and paste it in your `.env` file

## Troubleshooting

### Port 5000 already in use
```bash
python server.py  # Flask will use PORT env variable
```

### ModuleNotFoundError
```bash
pip install -r requirements.txt
```

### GROQ_API_KEY not set
Make sure your `.env` file has the correct API key

### Deployment fails on Render
- Check that `requirements.txt` is correct
- Verify `Procfile` exists and is correct
- Check environment variables in Render dashboard

## License

Free to use and modify!

## Support

For issues or questions, feel free to modify and improve!

---

**Made with ❤️ by Nirmaan Chatboat** 🚢⚓
