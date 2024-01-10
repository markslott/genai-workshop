#!/bin/sh
docker run -it --env CLOUD_ID --env ELASTIC_USER --env ELASTIC_PASSWORD \
 --volume="./passages:/workshop/passages:rw" \
 markslott/genai-workshop
