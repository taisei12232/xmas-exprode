from typing import List

import cv2
import numpy as np
import uvicorn
from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import FileResponse

from my_types import HelloWorldType, IntegerArrayType

app = FastAPI()


@app.get("/")
def root() -> HelloWorldType:
    return {"Hello": "World"}


@app.post("/test")
async def image(image_file: UploadFile = File(...)):
    contents: bytes = await image_file.read()
    array: IntegerArrayType = np.fromstring(contents, np.uint8)
    img: IntegerArrayType = cv2.imdecode(array, cv2.IMREAD_GRAYSCALE)
    image2 = cv2.bitwise_not(img)
    cv2.imwrite("image2.png", image2)
    return FileResponse("image2.png")


def main() -> None:
    print("===== main() =====")
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True, workers=1)


if __name__ == "__main__":
    main()
