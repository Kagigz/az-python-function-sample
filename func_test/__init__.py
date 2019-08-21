import logging
import json
import azure.functions as func
from ..shared_code import entity_recognition
from ..shared_code import stopwords

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    file_sent = None
    text = ""

    try:
        file_sent = req.get_body()
    except ValueError:
        pass
    else:
        text = str(file_sent)

    processed_text = stopwords.remove_stop_words(text)
    entities = entity_recognition.get_entities(text)

    if file_sent:
        return func.HttpResponse(
            json.dumps([ {
            "processedText": processed_text, 
            "entities": entities
            } ]),
            status_code=200
        )
    else:
        return func.HttpResponse(
             "Please pass a file in the request body",
             status_code=400
        )