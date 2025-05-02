# Smart Artificial Plants Chatbot 

A feature-rich conversational interface for an artificial plants e-commerce platform, built with FastAPI and vanilla JavaScript.

## 📋 Overview

The Artificial Plants Chatbot provides an interactive way for customers to explore artificial plants, receive personalized recommendations, get maintenance advice, and manage their shopping cart - all through a natural language interface.

This project combines modern backend technologies like FastAPI with a clean, responsive frontend to create a seamless shopping experience.

## ✨ Key Features

- **Conversational Interface**: Natural language interaction with the chatbot
- **Product Catalog**: Browse artificial plants by category (Indoor, Office, Outdoors)
- **Smart Plant Finder**: Get plant recommendations based on location, size, and style preferences
- **Maintenance Tips**: Access care instructions and advice for artificial plants
- **Shopping Cart**: Add and remove items with real-time feedback
- **AI-Powered Q&A**: Intelligent responses to customer questions using vector search technology

## 🛠️ Technology Stack

### Backend
- **FastAPI**: High-performance Python web framework
- **FAISS**: Vector similarity search for efficient question answering
- **Python 3.10+**: Core programming language

### Frontend
- **Vanilla JavaScript**: No framework dependencies
- **CSS3**: Responsive design with custom styling
- **HTML5**: Semantic markup structure

## 📁 Project Structure

```
artificial-plants-chatbot/
├── app.py                  # Main FastAPI application entry point
├── Dockerfile              # Container configuration
├── Procfile                # Railway deployment config
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not in repo)
├── modules/                # Backend API modules
│   ├── cart.py             # Shopping cart functionality
│   ├── find_plant.py       # Plant recommendation system
│   ├── maintenance.py      # Maintenance tips functionality
│   ├── products.py         # Product catalog and categories
│   └── qa.py               # FAISS-based Q&A functionality
├── static/                 # Static assets
│   ├── images/             # Product images
│   └── index.html          # Main frontend interface
└── data/                   # Vector search data
    ├── faiss_index.bin     # FAISS vector index
    └── document_texts.npy  # Embedded documents
```

## 🌐 Deployment

This project is deployed on Railway.com and accessible at:
https://chatbottest-production.up.railway.app/

## 💡 UI Features & Customization

### Responsive Design
The interface adapts to different screen sizes, from desktop to mobile devices.

### Typing Indicator
When the bot is processing a response, a typing indicator with animated dots appears to show the user that the system is working.

### CSS Theming
The color scheme can be customized by modifying CSS variables:

```css
:root {
  --chat-bg: #fdfaef;
  --border-color: #40442e;
  --header-bg: #40442e;
  /* Additional variables... */
}
```

## 🧠 AI Component

### Vector Search with FAISS
- The system uses Facebook AI Similarity Search (FAISS) to find relevant information based on user queries.
- The FAISS index is built from product descriptions and maintenance information.

### Natural Language Processing
- The system uses advanced natural language processing to understand user queries.
- The chatbot generates natural-sounding responses based on retrieved information.

## 📊 Performance Considerations

### Production Recommendations
- The current implementation uses in-memory storage for the shopping cart
- For production use, consider implementing a database for persistent storage.

### FAISS Index Updates
- The FAISS index should be rebuilt when significant changes are made to product data.
- A scheduled job can automate this process.
