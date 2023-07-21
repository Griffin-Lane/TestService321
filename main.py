from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#class Response(BaseModel):
#	results:typing.list[Result]

@app.post("/predict", response_model=Response)
async def predict_api(request:Request):
	#results = predict(request.question)
	return "yay"


