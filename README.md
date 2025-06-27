🛡️ Insurance Claim GenAI Assistant
    This is an AI-powered insurance assistant platform that supports various intelligent agents to help streamline insurance workflows using GenAI (TinyLLaMA / DistilGPT2 / Transformers). Built using Streamlit, it supports:

    ✅ Claim extraction
    ✅ Fraud detection
    ✅ LLaMA-based summarization
    ✅ Insurance product recommendation
    ✅ Risk assessment
    ✅ Customer support Q&A

🗂️ Folder Structure
    insurance-claim-genai/
    │
    ├── app/
    │   ├── main.py                # Streamlit navigation entry point
    │   ├── pages/
    │   │   ├── 1_Upload.py        # Claim file upload + analysis
    │   │   ├── 2_Reports.py       # Analytics report (charts, stats)
    │   │   ├── 3_About.py         # About the app
    │   │   ├── 4_Product_Recommendation.py
    │   │   ├── 5_Risk_Assessment.py
    │   │   └── 6_Customer_Agent.py
    │
    ├── backend/
    │   ├── claim_parser.py        # Regex-based claim field extractor
    │   ├── fraud_checker.py       # Simple fraud rule engine
    │   └── summarizer.py          # LLaMA summary generation
    │
    ├── sample_claims/             # Sample .txt files for testing
    ├── README.md                  # You're here!
    └── requirements.txt           # Required Python packages


🚀 Features
1. 📂 Upload & Analyze Claims
    Upload multiple .txt claim files
    Extracts: Claimant Name, Policy Number, Claim Amount, Date, Reason
    Flags potential fraud (high amount, suspicious keywords)

2. 🧠 LLaMA Summarizer
    Uses TinyLLaMA or DistilGPT2 to generate human-like summaries
    Summarization uses key fields (name, date, amount, reason)

3. 📊 Reports Dashboard
    Claim amount distribution
    Fraud vs Safe claims        
    Claims over time

4. 📦 Product Recommendation Agent
    Takes user inputs (age, income, goal)
    Suggests personalized insurance product using DistilGPT2

5. ⚖️ Risk Assessment Agent
    Evaluates a user's risk based on answers
    Generates a text-based summary of risk profile

6. 💬 Customer Support Agent
    Ask insurance-related queries
    Provides answers based on GenAI reasoning


🛠️ Installation & Setup
    Make sure you have Python 3.8+ and pip installed.
    1. Clone the repository:
        git clone https://github.com/your-username/insurance-claim-genai.git
        cd insurance-claim-genai

    2. Install dependencies
        pip install -r requirements.txt
    
    3.Run the Streamlit app
        streamlit run app/main.py


📁 Sample Claim File Format (.txt)
    Each file should contain structured plain text:
        Policy Number: ABC12345
        Claimant Name: Disha Waghmare
        Claim Amount: ₹50000
        Date of Incident: 2024-12-01
        Claim Reason: Accident damage to vehicle

🧠 Agents in This Project
 | Agent Type                   | Description                         |
| ---------------------------- | ----------------------------------- |
| ✅ Claim Analysis Agent       | Extracts & analyzes claims          |
| 💡 Fraud Detection Agent     | Flags potential frauds              |
| 🧠 LLaMA Summary Agent       | Summarizes claim with generative AI |
| 💬 Customer Support Agent    | Answers insurance questions (LLM)   |
| 📦 Product Recommender Agent | Recommends a policy based on inputs |
| ⚖️ Risk Assessment Agent     | Analyzes risk from user info        |


✨ Future Work
    Add database (SQLite or Firebase) for storing uploaded claims
    Add claim approval probability using classification model
    Export reports as PDF or Excel
    Add chatbot UI for customer agent
    Mobile-friendly UI

👩‍💻 Built With
    Python 3.10
    Streamlit
    HuggingFace Transformers (TinyLLaMA / DistilGPT2)
    Pandas, Plotly
    Regex, Rule Engines

📬 Contact
    Made with 💙 by Disha Waghmare  
    📧 Reach me for suggestions or collaborations