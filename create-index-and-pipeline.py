#!/usr/bin/env python3
from elasticsearch import Elasticsearch, RequestError
import os, sys

CLOUD_ID = os.getenv('CLOUD_ID')
USER = os.getenv('ELASTIC_USER')
PASSWORD = os.environ.get('ELASTIC_PASSWORD')

ES_INDEX = "book"
ES_PIPELINE = "book-pipeline"


def main(argv):
   
    if CLOUD_ID == "" or USER == "" or PASSWORD == "":
        print("Must have the CLOUD_ID, ELASTIC_USER, and ELASTIC_PASSWORD environment vars set")
        sys.exit()
    es = Elasticsearch(cloud_id=CLOUD_ID,basic_auth=(USER, PASSWORD))
    
  
    mappings = {
        "dynamic" : True,
        "properties" : {
            "elser" : {
                "properties" : {
                    "tokens" : {
                        "type" : "rank_features"
                    }
                }
            }
        }
    }
    
    try:
        es.indices.create(index=ES_INDEX, mappings=mappings)
    except RequestError as es1:
        if es1.message != "resource_already_exists_exception":
            print("Error on create index: {}".format(es1.message))
    
    processors = [{
        "inference": {
            "model_id": ".elser_model_2_linux-x86_64",
            "input_output": [
            {
                "input_field": "text",
                "output_field": "elser.tokens"
            }
            ]
        }
    }]
    try:
        es.ingest.put_pipeline(id=ES_PIPELINE, processors=processors)
    except RequestError as es1:
        print("Error on create pipeline: {}".format(es1.message))

    
if __name__ == "__main__":
    main(sys.argv[1:])
