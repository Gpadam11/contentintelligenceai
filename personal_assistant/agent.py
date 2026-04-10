import os
import logging
from google.adk.agents.llm_agent import Agent
from google.adk.tools import load_artifacts

# 1. Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("LogicToLinkedIn")

# 2. Specialist 1: The Technical Researcher
researcher = Agent(
    name="researcher_agent",
    model=os.getenv("MODEL", "gemini-2.5-flash"),
    tools=[load_artifacts],  # Allows reading uploaded README files
    instruction="""
    You are a Technical Value Analyst. 
    1. If the user mentions a file/artifact, use 'load_artifacts' to read it.
    2. Extract the core technical features and the 'Project Goal'.
    3. Translate these into jargon-free text.
    
    CRITICAL: You MUST format your response EXACTLY like this template:
    
    [The Jargon-Buster]
    Technical Feature: <Insert short technical feature here>
    Business Benefit: <Insert jargon-free, plain English benefit here>
    """,
    output_key="research_notes"
)

# 3. Specialist 2: The Brand Marketer
marketer = Agent(
    name="marketer_agent",
    model=os.getenv("MODEL", "gemini-2.5-flash"),
    instruction="""
    You are a Personal Branding Expert. 
    Use the research notes provided to write a creative LinkedIn post.
    - NO AI CLICHÉS: No 'delve', 'unleash', 'tapestry'.
    - Avoid "hallucinating" timelines.
    
    CRITICAL: You MUST format your response EXACTLY like this template:
    
    [The LinkedIn Post]
    Hook: <A relatable pain point or observation>
    The Core: <The tech feature + benefit>
    The Takeaway: <One punchy sentence summarizing the value>
    Engagement: <A conversational question to spark comments> 👇
    #<Add 3-4 relevant hashtags>
    """
)

# # 4. The Orchestrator (The "Root" for ADK)
# root_agent = Agent(
#     name="logic_to_linkedin_pipeline",
#     model=os.getenv("MODEL", "gemini-2.5-flash"),
#     sub_agents=[researcher, marketer], 
#     description="Main entry point for the Technical-to-LinkedIn workflow.",
#     instruction="""
#     You are the Manager of a high-end content pipeline.
#     When the user gives you a prompt:
#     1. Immediately delegate the input to 'researcher_agent'.
#     2. Pass the researcher's exact output to 'marketer_agent'.
#     3. Output the combined results from BOTH agents to the user.
    
#     STRICT RULE: Do NOT make small talk. Do not say "Hello" or "I am transferring this." 
#     Just output the [The Jargon-Buster] section followed immediately by [The LinkedIn Post] section.
#     """
# )

# 4. The Orchestrator (The "Root" for ADK)
root_agent = Agent(
    name="logic_to_linkedin_pipeline",
    model=os.getenv("MODEL", "gemini-2.5-flash"),
    sub_agents=[researcher, marketer], 
    description="Main entry point for the Technical-to-LinkedIn workflow.",
    instruction="""
    You are the Manager of a high-end content pipeline.
    
    1. If the user says 'hi' or asks what you can do: 
       Briefly explain that you turn technical specs into jargon-free value and LinkedIn posts.
    
    2. When the user provides technical input:
       - Send it to 'researcher_agent' first.
       - Then take those notes and send them to 'marketer_agent'.
       - Finally, display BOTH the [The Jargon-Buster] and [The LinkedIn Post] sections to the user.
    
    STRICT RULE: Do not just say you are transferring; actually show the final results!
    """
)