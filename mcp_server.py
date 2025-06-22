import os
import json
from typing import Dict, Optional
from fastmcp import FastMCP

mcp = FastMCP("Playwright QA MCP Server")
REPORT_PATH = "report.json"

@mcp.resource("qa://test-report")
async def get_test_report() -> Optional[Dict]:
    """Returns the Playwright test report."""
    if not os.path.exists(REPORT_PATH):
        return {"error": "report.json not found"}
    with open(REPORT_PATH, "r") as f:
        return json.load(f)

@mcp.tool()
async def clear_test_report() -> bool:
    """Deletes the report.json file."""
    if os.path.exists(REPORT_PATH):
        os.remove(REPORT_PATH)
        return True
    return False
# 👇 Add this before mcp.run()
if os.path.exists(REPORT_PATH):
    print("\n--- Loaded Test Report Preview ---")
    with open(REPORT_PATH, "r") as f:
        preview = json.load(f)
        print(json.dumps(preview, indent=2)[:500] + "\n...")  # show preview only
    print("----------------------------------\n")
else:
    print("No report.json found.")
if __name__ == "__main__":
    print("MCP server is running...")
    mcp.run(transport="stdio")


