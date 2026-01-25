# ===============================
# backend/run.py
# ===============================

"""
Application entry point.

This script launches the FastAPI app with Uvicorn.
"""

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",  # module:function
        host="0.0.0.0",
        port=8000,
        reload=True     # auto-restart on code changes (dev only)
    )
