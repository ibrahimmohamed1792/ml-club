import fastapi


app = fastapi.FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "ML CLUB"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

