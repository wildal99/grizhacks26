import gemini
from fastapi import FastAPI

app = FastAPI()


@app.get("/main")
def main():
    response = gemini.uploadRecording("4981.mp3")
    print(response)
    gemini.analyzeSpeach(response)
    gemini.delete(response)