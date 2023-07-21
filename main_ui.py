#!/usr/bin/env python3

import logging
import openai
from chat_utils import ask
import os
import gradio as gr
import requests
import logging
from typing import Dict, Any, Optional, List
from enum import Enum
import json

BEARER_TOKEN: str = os.environ.get("BEARER_TOKEN")
GENAI_DATA_ASK_API_ENDPOINT: str = os.environ.get("GENAI_DATA_ASK_API_ENDPOINT")
assert BEARER_TOKEN != None
assert GENAI_DATA_ASK_API_ENDPOINT != None

from pydantic import BaseModel


# class Source(str, Enum):
#     email = "email"
#     file = "file"
#     chat = "chat"
#     sql = "sql"

# class Metadata(BaseModel):
#     source: Optional[Source] = None
#     source_id: Optional[str] = None
#     url: Optional[str] = None
#     created_at: Optional[str] = None
#     author: Optional[str] = None
#     database: Optional[str] = None
#     tables: Optional[str] = None
#     sql: Optional[str] = None

# class ChunkWithMetadata(BaseModel):
#     text: str
#     metadata: Metadata

#     def format_with_metadata(self) -> str:
#         if self.metadata.tables:
#             return f"{self.metadata.tables}:{self.text}"
#         return f"{self.metadata.source_id}:{self.text}"

# class Ask(BaseModel):
#     question: str

# class Answer(BaseModel):
#     content: str
#     metadata: List[ChunkWithMetadata]


# def dispatch_payload(payload: Dict[str, Any]) -> Answer:
#     headers: Dict[str, str] = {
#         "Authorization": f"Bearer {BEARER_TOKEN}"
#     }
#     #url: str = f"{GENAI_DATA_ASK_API_ENDPOINT}/ask"
#     url: str = f"{GENAI_DATA_ASK_API_ENDPOINT}/ask?structured=true"
#     response: requests.Response = requests.post(url=url, headers=headers, json=payload)
#     status_code = response.status_code
#     content = response.json()
#     print(f"status_code: {status_code}")
#     print(f"content:")
#     print(json.dumps(content, indent=4))
#     ask = content.get('answer')
#     return Answer(**ask)

# def create_payload(question: str) -> Dict[str, Any]:

#     payload: Dict[str, Any] = {
#         "ask": {
#             "question": question
#         }
#     }
#     return payload


# def ask(query: str):
#     payload = create_payload(query)
#     response: Answer = dispatch_payload(payload)
#     metadata: List[ChunkWithMetadata] = response.metadata
#     # output = ''
#     # for m in metadata:
#     #     output = output + str(m) + "\n"
#     #     #m.metadata.<author....>
#     print(response.content)
#     #print(output)
#     return response.content

# def split_response(input_text: str, history: List):
#     history = history or []
#     response = chatbot(input_text)
#     # print(response)
#     # if "(Sources:" in response:
#     #     answer_response, sources = response.split("(Sources:", 1)
#     #     print(answer_response)
#     #     sources = "(Sources: " + sources
#     #     print(sources)
#     # elif "(source:" in response:
#     #     answer_response, sources = response.split("(source:", 1)
#     #     print(answer_response)
#     #     sources = "(source: " + sources
#     #     print(sources)
#     # else: 
#     #     answer_response, sources = response, ""
        
#     # full_response = f"{input_text}\n\n{answer_response}\n\n"
    
#     #history.append((input_text, answer_response))
    
#     print(response)
    
#     #return history, history
#     #return answer_response
#     return response

def chatbot(conversation):
    new_message = "using a hardcoded string" #ask(conversation)
    #return "User: " + conversation + "\n\nSystem: " + new_message + "\n\n"
    return new_message

if __name__ == "__main__":
    # demo = gr.Interface(fn=chatbot, #inputs="text", 
    #                     inputs=gr.inputs.Textbox(lines=20, label="Conversation"),
    #                     outputs="text", label="Response")
    
    # demo = gr.Interface(fn=split_response, 
    #                 inputs=[gr.inputs.Textbox(lines=20, label="Conversation"), "state"],
    #                 outputs=[
    #                     gr.inputs.Textbox(lines=10, label="Response"), 
    #                     gr.inputs.Textbox(lines=5, label="Sources"),
    #                     "state"
    #                 ]
    # )

    # demo.launch()
    
    # iface = gr.Interface(
    #     fn=split_response,
    #     inputs=[gr.inputs.Textbox(lines=20, label="Conversation"), "state"],
    #     outputs=["chatbot", "state"],
    #     allow_screenshot=False,
    #     allow_flagging="never",
    # )
    # #iface.launch(share=True)
    # iface.launch()
    
    with gr.Blocks() as demo:
        chat = gr.Chatbot()
        msg = gr.Textbox()
        clear = gr.ClearButton([msg, chat])
        
        # def respond(message, chat_history):
        #     bot_message = split_response(message, chat_history)
        #     chat_history.append((message, bot_message))
        #     return "", chat_history
        
        # msg.submit(respond, [msg, chat], [msg, chat])
        demo.launch()
    
    #while True:
        #user_query = input("Enter your question: ")
#        openai.api_key = OPENAI_API_KEY
        #logging.basicConfig(level=logging.WARNING,
        #                    format="%(asctime)s %(levelname)s %(message)s")
        #print(ask(user_query))
        
