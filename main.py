from fastapi import FastAPI
from pydantic import BaseModel
import mishkal.tashkeel

app = FastAPI(
    title="Arabic Tashkeel API",
    version="1.0.0"
)

tashkeel = mishkal.tashkeel.TashkeelClass()


class TashkeelRequest(BaseModel):
    text: str


@app.get("/")
def root():
    return {
        "status": "online",
        "service": "Arabic Tashkeel API",
        "engine": "Mishkal"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post("/tashkeel")
def tashkeel_text(request: TashkeelRequest):

    text = request.text.strip()

    if not text:
        return {
            "success": False,
            "error": "النص فارغ"
        }

    try:

        result = tashkeel.tashkeel(text)

        return {
            "success": True,
            "original": text,
            "diacritized": result
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }
