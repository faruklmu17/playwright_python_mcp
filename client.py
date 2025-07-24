import asyncio
from fastmcp import Client

async def main():
    # Connect to the server via stdio (by running server.py as a subprocess)
    async with Client("mcp_server1.py") as client:
        print("Listing resources:")
        resources = await client.list_resources()
        print(resources)

        print("\nListing tools:")
        tools = await client.list_tools()
        print(tools)
        response = await client.read_resource("employees://2")
        print(response)

if __name__ == "__main__":
    asyncio.run(main())
