from fastapi import FastAPI
from pydantic import BaseModel
from camel_tools.diacritizer import Diacritizer

app = FastAPI(
    title="Arabic Tashkeel API",
    version="1.0.0"
)

# تحميل مشكّل CAMeL Tools مرة واحدة عند تشغيل السيرفر
diacritizer = Diacritizer()


class TashkeelRequest(BaseModel):
    text: str


@app.get("/")
def root():
    return {
        "status": "online",
        "service": "Arabic Tashkeel API",
        "engine": "CAMeL Tools"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post("/tashkeel")
def tashkeel(request: TashkeelRequest):

    text = request.text.strip()

    if not text:
        return {
            "success": False,
            "error": "النص فارغ"
        }

    try:
        result = diacritizer.diacritize(text)

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
