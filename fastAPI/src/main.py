if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.app:app", reload=True, port=8001)
