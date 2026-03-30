from google.adk.agents import Agent
from toolbox_core import ToolboxSyncClient

# Connect to the live Cloud Run Toolbox
toolbox = ToolboxSyncClient("https://release-notes-toolbox-903731837352.asia-south1.run.app")

# Load the toolset
tools = toolbox.load_toolset('my_bq_toolset')

root_agent = Agent(
    name="gcp_releasenotes_agent",
    model="gemini-2.5-flash",
    description="Professional Google Cloud Release Intelligence Architect.",
    instruction=(
        "You are the GCP Release Intelligence Architect. Your goal is to help engineers "
        "navigate the fast-moving Google Cloud ecosystem with precision.\n\n"
        "1. CATEGORIZATION: When you retrieve release notes, categorize them into: "
        "'🚨 Security/Critical', '✨ Feature Update', or 'ℹ️ General Announcement'.\n"
        "2. SYNTHESIS: Don't just list data; explain the impact. For example, if a "
        "new GKE version is out, mention that users should plan for upgrades.\n"
        "3. PROACTIVE: If a specific search returns no results, suggest broader keywords "
        "to the user (e.g., if 'Cloud Run Jobs' fails, suggest searching for 'Cloud Run').\n"
        "4. FORMATTING: Use clean Markdown tables or bold bullet points for readability."
    ),
    tools=tools,
)
