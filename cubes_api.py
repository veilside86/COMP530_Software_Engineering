from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND

def api_reply(data):
    if not data:
        return JSONResponse({"message": "No Cubes Data Found"}, status_code=HTTP_404_NOT_FOUND)
    result = prepare_result(data)
    return JSONResponse(result, status_code=HTTP_200_OK)


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}
