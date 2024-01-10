#!/bin/sh
docker run -d --name=filebeat-demo --user=root --volume="$(pwd)/filebeat.yml:/usr/share/filebeat/filebeat.yml:ro" \
 --volume="./passages:/usr/share/filebeat/files:rw" \
 --volume="/var/lib/docker/containers:/var/lib/docker/containers:ro" \
 --volume="/var/run/docker.sock:/var/run/docker.sock:ro" \
 --volume="./registry:/usr/share/filebeat/data:rw" docker.elastic.co/beats/filebeat:8.11.3 filebeat -e -d "*" --strict.perms=false \
 -E cloud.id=$CLOUD_ID \
 -E cloud.auth=$ELASTIC_USER:$ELASTIC_PASSWORD
