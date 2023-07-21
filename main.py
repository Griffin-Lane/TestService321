import typing

from fastapi import FastAPI
from pydantic import BaseModel
import gradio as gr

# from predict import predict

def predict(query: str):
    # Encode the query using the bi-encoder and find potentially relevant passages
    hits=[1,2,3]
    results = [
        {
            "score": 0,
            "title": query,
            "text": "testing",
        }
        for hit in hits
    ]

    print("\n\n========\n")

    return results
app = FastAPI()


# --- fastapi /predict route ---


class Request(BaseModel):
    question: str


class Result(BaseModel):
    score: float
    title: str
    text: str


class Response(BaseModel):
    results: typing.List[Result]


@app.post("/predict", response_model=Response)
async def predict_api(request: Request):
    results = predict(request.question)
    return Response(
        results=[
            Result(score=r["score"], title=r["title"], text=r["text"]) for r in results
        ]
    )


# --- gradio demo ---


def gradio_predict(question: str):
    results = predict(question)

    best_result = results[0]

    return f"{best_result['title']}\n\n{best_result['text']}", best_result["score"]


demo = gr.Interface(
    fn=gradio_predict,
    inputs=gr.Textbox(
        label="Ask a question", placeholder="What is the capital of France?"
    ),
    outputs=[gr.Textbox(label="Answer"), gr.Number(label="Score")],
    allow_flagging="never",
)

app = gr.mount_gradio_app(app, demo, path="/")