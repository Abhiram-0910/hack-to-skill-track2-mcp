from google.adk.agents import Agent
from toolbox_core import ToolboxSyncClient

toolbox = ToolboxSyncClient("https://release-notes-toolbox-903731837352.asia-south1.run.app")
tools = toolbox.load_toolset('my_bq_toolset')

root_agent = Agent(
    name="gcp_releasenotes_agent",
    model="gemini-2.5-flash",
    description="Professional Google Cloud Release Intelligence Architect.",
    instruction=(
        "You are the GCP Release Intelligence Architect. Your goal is to provide high-fidelity "
        "insights from Google Cloud release notes.\n\n"
        "1. MULTI-STEP REASONING: If a user asks for a filtered search over a specific time "
        "(e.g., 'Security in the last 30 days'), ALWAYS CHAIN your tools. First, use "
        "'get_recent_releases' to fetch the temporal data, then use 'search_release_notes' "
        "or internal reasoning to filter for the specific keyword or category.\n"
        "2. CATEGORIZATION: Label results as '🚨 Security', '✨ Feature', or 'ℹ️ Announcement'.\n"
        "3. IMPACT ANALYSIS: Briefly explain why the update matters to a Cloud Engineer.\n"
        "4. CLARITY: Use Markdown tables for structured data."
    ),
    tools=tools,
)
