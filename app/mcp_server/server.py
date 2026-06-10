from app.mcp_server.tools import list_tools


def run_server():
    return {"tools": list_tools()}


if __name__ == "__main__":
    print(run_server())
