from fastapi.responses import FileResponse
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def get_page():
	return FileResponse(f"index.html")

@app.get("/style.css")
def get_style():
	return FileResponse("style.css")