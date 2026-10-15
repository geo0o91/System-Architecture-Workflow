import time

class AIAgent:
    def __init__(self, name, role, instruction):
        self.name = name
        self.role = role
        self.instruction = instruction

    def execute_task(self, inputs):
        print(f"\n🧠 [{self.name} - {self.role}] is processing the instruction...")
        time.sleep(1.5)  # Simulating thinking time
        
        # This is where your custom logical routing rules live
        if "RESEARCH" in self.instruction:
            output = f"RESEARCH REPORT:\n- High demand detected for Python, RAG architectures, and Vector Databases in Ottawa tech hubs.\n- Source Input Analyzed: {inputs}"
        elif "ARCHITECT" in self.instruction:
            output = f"ARCHITECTURAL SYSTEM DESIGN:\n- Proposed Stack: Python + LangChain + ChromaDB.\n- Bridge Strategy: Map applicant's WES Computer Engineering credentials directly to local automated workflows.\n- Action Item: Build a local RAG app using the provided data: {inputs}"
        else:
            output = f"Task completed with inputs: {inputs}"
            
        return output

class MultiAgentOrchestrator:
    def __init__(self):
        print("🏗️ Initializing Canadian AI Multi-Agent Orchestration Framework...")
        # 1. Define Agent 1: The Market Analyst
        self.researcher = AIAgent(
            name="Agent_Alpha", 
            role="Market & Data Researcher", 
            instruction="RESEARCH and extract specific tech stack demands from Canadian market data."
        )
        # 2. Define Agent 2: The Technical System Architect
        self.architect = AIAgent(
            name="Agent_Beta", 
            role="Solutions Systems Architect", 
            instruction="ARCHITECT a production deployment roadmap combining regional demands with an engineer's background."
        )

    def run_pipeline(self, raw_input_data):
        print(f"\n🚀 System Launch: Ingesting raw market signal data...")
        
        # Step 1: First agent runs research
        research_result = self.researcher.execute_task(raw_input_data)
        print(f"✅ Research Stage Complete.\nResult Output:\n{research_result}")
        
        # Step 2: Hand off the research output directly to the second agent (Chaining)
        final_architecture = self.architect.execute_task(research_result)
        print(f"\n✅ Architectural Routing Complete.")
        
        return final_architecture

# --- Execution Block ---
if __name__ == "__main__":
    # Simulate a raw data input coming from Canadian tech postings
    raw_market_data = "Ottawa Tech Openings 2026: Seeking specialists in automation, cloud computing, and automated data pipelines."
    
    # Initialize and execute the multi-agent system
    orchestrator = MultiAgentOrchestrator()
    final_output = orchestrator.run_pipeline(raw_market_data)
    
    print("\n================== FINAL SYSTEM OUTPUT ==================")
    print(final_output)
    print("=========================================================")
