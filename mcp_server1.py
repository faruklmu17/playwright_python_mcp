import aiosqlite
from fastmcp import FastMCP
from typing import List, Dict, Optional

mcp = FastMCP("Employee MCP Server")

# Path to the database — adjust based on actual location
DB_PATH = "db/employees.db"

@mcp.resource("employees://all")
async def get_all_employees() -> List[Dict]:
    """Returns all employee records as a list of dictionaries."""
    async with aiosqlite.connect(DB_PATH) as conn:
        cursor = await conn.execute('SELECT * FROM employees')
        columns = [column[0] for column in cursor.description]
        employees = [dict(zip(columns, row)) async for row in cursor]
        await cursor.close()
    return employees

@mcp.resource("employees://{employee_id}")
async def get_employee_by_id(employee_id: int) -> Optional[Dict]:
    """Returns a single employee record based on employee ID."""
    async with aiosqlite.connect(DB_PATH) as conn:
        cursor = await conn.execute('SELECT * FROM employees WHERE id = ?', (employee_id,))
        row = await cursor.fetchone()
        if row:
            columns = [column[0] for column in cursor.description]
            result = dict(zip(columns, row))
        else:
            result = None
        await cursor.close()
    return result
@mcp.resource("employees://{employee_id}")
async def get_employee_by_id(employee_id: int) -> Optional[Dict]:
    async with aiosqlite.connect(DB_PATH) as conn:
        cursor = await conn.execute('SELECT * FROM employees WHERE id = ?', (employee_id,))
        row = await cursor.fetchone()
        if row:
            columns = [column[0] for column in cursor.description]
            return dict(zip(columns, row))
        return None

if __name__ == "__main__":
    mcp.run()

