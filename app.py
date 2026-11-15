import streamlit as st
from tavily import TavilyClient
from google import genai

st.set_page_config(page_title="Pre-Meeting Research Agent", page_icon="📋")
st.title("📋 Pre-Meeting Research Agent")
st.write("Generate a 1-page briefing on any company or person from the last 30 days.")

tavily_key = st.sidebar.text_input("Tavily API Key", type="password")
gemini_key = st.sidebar.text_input("Gemini API Key", type="password")

target = st.text_input("Company or Person Name", placeholder="e.g., NVIDIA or Jensen Huang")
meeting_time = st.text_input("Scheduled Meeting Date & Time", placeholder="e.g., Nov 16, 2026 at 10:00 AM")

if st.button("Generate Briefing"):
    if not tavily_key or not gemini_key or not target:
        st.warning("Please enter both API keys and a target name.")
    else:
        with st.spinner("Researching developments from the last 30 days..."):
            tavily = TavilyClient(api_key=tavily_key)
            results = tavily.search(
                query=f"{target} recent news product launches leadership hires updates",
                topic="news",
                time_range="month",
                max_results=5
            )
            
            context = "\n".join(
                [f"- {r['title']} ({r['url']}): {r['content']}" for r in results["results"]]
            )
            
            client = genai.Client(api_key=gemini_key)
            prompt = f"""
            Prepare a concise, one-page pre-meeting briefing for a meeting with {target} scheduled for {meeting_time}.
            Use ONLY the recent 30-day search results below:
            {context}
            
            Format cleanly with:
            1. Executive Summary (2-3 sentences)
            2. Key Recent Developments (News, Launches, Hires) with inline source URLs
            3. Useful Discussion Points (3 bullets)
            4. Smart Open Questions to Ask (3 bullets)
            """
            
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=prompt
            )
            st.markdown("---")
            st.markdown(response.text)