from typing import Union

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request

from templates.welcome_templates import get_welcome_message
from templates.function_templates import generate_function_example
from templates.library_templates import generate_library_example

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/")
async def handle_request(request: Request):
    payload = await request.json()

    intent = payload["queryResult"]["intent"]["displayName"]
    parameters = payload["queryResult"]["parameters"]
    output_contexts = payload["queryResult"]["outputContexts"]

    if(intent == "Default Welcome Intent"):
        return JSONResponse(
            {
                "fulfillmentText": get_welcome_message(),
                "outputContexts": output_contexts
            }
        )
    
    if(intent == "Default Fallback Intent"):
        return JSONResponse(
            {
                "fulfillmentText": "Sorry, I don't understand that.",
                "outputContexts": output_contexts
            }
        )
    
    if(intent == "explain_functions"):
        functions = parameters["function"]
        return JSONResponse(
            {
                "fulfillmentText": generate_function_example(functions),
                "outputContexts": output_contexts
            }
        )
    
    if(intent == "explain_libraries"):
        library = parameters["library"]
        return JSONResponse(
            {
                "fulfillmentText": generate_library_example(library),
                "outputContexts": output_contexts
            }
        )
    
