from flask import Flask, request, jsonify
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize Groq API with environment variable
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY environment variable is not set. Please set it in your .env file or environment.")
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    temperature=0.7
)

# Store chat history
chat_history = []

@app.route('/')
def home():
    html_content = open('index.html', encoding='utf-8').read()
    return html_content

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Check if question is AI-related using LLM
        is_ai_question = check_if_ai_question_with_llm(user_message)
        
        if not is_ai_question:
            return jsonify({
                'response': "I'm specifically designed to answer questions about Artificial Intelligence, Machine Learning, and related topics. Please ask me about AI! 🤖\n\nSome examples:\n• What is Artificial Intelligence?\n• How do neural networks work?\n• What is machine learning?\n• Difference between AI and ML\n• How does deep learning work?",
                'success': True,
                'is_warning': True
            })
        
        # Add user message to history
        chat_history.append(user_message)
        
        # Generate thinking context (internal, not shown to user)
        thinking_context = generate_thinking_context(user_message)
        
        # Create enhanced prompt with thinking context
        enhanced_message = f"{thinking_context}\n\nUser question: {user_message}"
        
        # Get response from LLM with enhanced context
        response = llm.invoke(chat_history + [enhanced_message])
        bot_response = response.content
        
        # Add bot response to history
        chat_history.append(bot_response)
        
        return jsonify({
            'response': bot_response,
            'success': True
        })
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({
            'error': str(e),
            'success': False
        }), 500

def check_if_ai_question_with_llm(question):
    """Check if the question is AI-related using LLM"""
    try:
        # Create a prompt to check if question is AI-related
        check_prompt = f"""You are an AI expert. Determine if the following question is related to Artificial Intelligence, Machine Learning, Deep Learning, Data Science, or related technical AI topics.

Question: {question}

Answer with ONLY "YES" or "NO". If it's about AI/ML/Deep Learning/Data Science/Neural Networks/LLMs/ChatGPT/NLP/Computer Vision or similar topics, answer YES. Otherwise answer NO."""
        
        # Call LLM to check
        response = llm.invoke(check_prompt)
        result = response.content.strip().upper()
        
        return "YES" in result
    
    except Exception as e:
        print(f"Error checking AI question: {str(e)}")
        # If there's an error, allow the question through
        return True

def generate_thinking_context(question):
    """Generate internal thinking context based on question"""
    context = ""
    
    lower_q = question.lower()
    
    # Identify question type and generate relevant thinking
    if any(word in lower_q for word in ['what is', 'what are', 'define', 'explain']):
        context = "Think about the definition and key characteristics. Provide a clear, comprehensive explanation with examples if relevant."
    
    elif any(word in lower_q for word in ['how to', 'how do', 'how can', 'steps', 'process']):
        context = "Break down the process into clear, logical steps. Provide a step-by-step guide that's easy to follow."
    
    elif any(word in lower_q for word in ['why', 'reason', 'cause', 'purpose']):
        context = "Explain the underlying reasons and motivations. Provide logical reasoning with relevant context."
    
    elif any(word in lower_q for word in ['which', 'better', 'compare', 'difference', 'vs']):
        context = "Compare the options objectively. Highlight strengths and weaknesses of each, then provide a thoughtful recommendation."
    
    elif any(word in lower_q for word in ['who', 'author', 'creator', 'person']):
        context = "Provide relevant biographical or contextual information about the person or entity."
    
    elif any(word in lower_q for word in ['where', 'location', 'place', 'country', 'city']):
        context = "Provide geographical context and relevant location-specific information."
    
    elif any(word in lower_q for word in ['when', 'date', 'time', 'year', 'happened']):
        context = "Provide chronological information with relevant historical context."
    
    else:
        context = "Provide a thorough, well-reasoned response that directly addresses the question. Be clear and concise."
    
    return context

@app.route('/api/clear', methods=['POST'])
def clear_chat():
    global chat_history
    chat_history = []
    return jsonify({'success': True, 'message': 'Chat cleared'})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print(f"Starting Nirmaan Chatboat server on port {port}...")
    print("Open your browser to: http://localhost:{port}")
    app.run(host='0.0.0.0', port=port, debug=False)
