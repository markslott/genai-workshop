## Book Report Workshop

This little sample will help you get started using the power of search, machine learning, and generative AI to do incredible things with search.  
In this project, you will load in an open source book, chunk the raw text into passages, setup an index and pipeline in Elastic, and load the data.  When the data loads, it will be inferenced against the ELSER sparse encoding model.  
This will give you the power of semantic search!

### Prereqs

You will need to have an Elastic cluster set up and the ELSER model downloaded into your cluster.  

You will also need to have Docker installed.  

Configure the following environment variables for the scripts to work:  
  
`CLOUD_ID`  
`ELASTIC_USER`  
`ELASTIC_PASSWORD`

### Instructions

1. Go to https://www.gutenberg.org/ and download the raw text to a book.  Pick any book you like, just make sure you download the text version of it  

2. Run the following command:  
 `chunk-book.py -i <path to your book file>`  
It will chunk the book into passages  

3. Run the `create-index-and-pipeline.py` script.  It will create an index in Elastic and configure the an ingest pipeline to perform the inferencing.  

4. Run the `run-filebeat-docker.sh` shell script.  It will start a docker container that will ingest the passages into Elastic.  

Once you've completed those steps, you are ready to start querying!