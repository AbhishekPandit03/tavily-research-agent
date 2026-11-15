# Pre-Meeting Research Agent

An AI-powered research assistant built for the **Global AI Hackathon (Tavily Track)** that generates a concise, source-backed one-page briefing before any scheduled meeting by analyzing news, launches, and updates from the preceding 30 days.

## Problem Statement
Preparing for business or technical meetings requires manually searching multiple news sources to track recent company or individual developments. This agent automates pre-meeting research into a structured, one-page briefing.

## Implementation & How It Works
1. **User Input:** The user enters a target company or person name alongside the scheduled meeting date and time via the Streamlit interface.
2. **30-Day Real-Time Retrieval:** The agent queries the **Tavily Search API** (`topic="news"`, `time_range="month"`) to retrieve verified news articles and updates from the last 30 days.
3. **Briefing Synthesis:** The retrieved articles and source URLs are passed to **Google Gemini (`gemini-3.8-flash`)** to generate an executive summary, key developments with inline source links, discussion points, and open questions.

## Technologies Used
- **Python 3**
- **Tavily Search API** (`tavily-python`)
- **Google Gemini API** (`google-genai`)
- **Streamlit** (`streamlit`)

## Installation & Setup
1. Clone this repository:
   ```bash
   git clone [https://github.com/AbhishekPandit03/tavily-research-agent.git](https://github.com/AbhishekPandit03/tavily-research-agent.git)
   cd tavily-research-agent
