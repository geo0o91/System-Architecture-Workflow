import ollama

class IntelligentAgent:
    def __init__(self, name, role, system_instruction):
        self.name = name
        self.role = role
        self.system_instruction = system_instruction

    def process_with_llm(self, user_input):
        print(f"\n🧠 [{self.name} - {self.role}] is querying the local Llama model...")
        
        # Call the local LLM running on your laptop
        response = ollama.chat(
            model='llama3:8b',
            messages=[
                {'role': 'system', 'content': self.system_instruction},
                {'role': 'user', 'content': user_input}
            ]
        )
        return response['message']['content']

# --- Orchestration Engine ---
if __name__ == "__main__":
    print("🏗️ Booting Local LLM Multi-Agent System Engine...")
    
    # 1. Initialize Agent Alpha (The Analyst)
    analyst_agent = IntelligentAgent(
        name="Agent_Alpha",
        role="Canadian Market Analyst",
        system_instruction="You are an expert tech recruiter in Canada. Analyze the provided job posting or market trend text. Extract the top 3 technical skills required and summarize them in short, clear bullet points."
    )
    
    # 2. Initialize Agent Beta (The Strategic Mentor)
    mentor_agent = IntelligentAgent(
        name="Agent_Beta",
        role="Senior Engineering Career Coach",
        system_instruction="You are a senior AI solutions engineer helping an immigrant with a WES-recognized Computer Engineering qualification. Look at the extracted required skills and provide a highly practical 2-step study recommendation to bridge any gaps using Python."
    )
    
    # --- Execute the Data Pipeline Flow ---
    raw_market_signal = "Ottawa Tech Positions: Enterprise engineering teams are scaling automated pipelines. Massive shift toward Python data processing, LangChain development, and setting up local vector database architectures."
    
    # Step 1: Analyst reads the raw text signals
    extracted_analysis = analyst_agent.process_with_llm(raw_market_signal)
    print("\n================== AGENT ALPHA OUTPUT ==================")
    print(extracted_analysis)
    
    # Step 2: Hand off Alpha's structured summary into Beta's brain
    final_career_roadmap = mentor_agent.process_with_llm(extracted_analysis)
    print("\n================== AGENT BETA FINAL ROADMAP ==============")
    print(final_career_roadmap)
    print("=========================================================")
