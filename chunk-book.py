#!/usr/bin/env python3

import sys, json, getopt
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import TokenTextSplitter


BATCH_SIZE = 1000

def main(argv):
    inputfile = ""
    outputpath = "./passages"
    opts, args = getopt.getopt(argv,"hi:o:",["ifile=","opath="])
    for opt, arg in opts:
        if opt == '-h':
            print('chunk-docs.py -i <inputfile> -o <outputpath>')
            sys.exit()
        elif opt in ("-i","--ifile"):
            inputfile = arg
        elif opt in ("-o","--opath"):
            outputpath = arg

    if inputfile == "" or outputpath == "":
        print('chunk-docs.py -i <inputfile> -o <outputpath>')
        sys.exit()

    #now break the text in the book up into 512 token passages and batch them up
    #into nsjson files to be bulk loaded
    loader = TextLoader(file_path=inputfile,autodetect_encoding=True)
    book = loader.load()
    text_splitter = TokenTextSplitter(chunk_size=512, chunk_overlap=256)
    passages = text_splitter.split_documents(book)
    
    passages_batch = []
    passage_index = 0  
    for passage in passages:
        passage_index += 1
        passage_json = {
            "text": passage.page_content,
            "seq": passage_index
        }
        #once we hit the batch size, write the passages ndjson file and start a new batch
        if passage_index % BATCH_SIZE == 0:
            writeFile("{path}/{filename}-{seq}.ndjson".format(path=outputpath,
                        filename="batch", seq=passage_index), "\n".join(passages_batch))
            passages_batch = []
        else:
            passages_batch.append(json.dumps(passage_json))
        
    
    #write the remaining passages to an ndjson file.  
    writeFile("{path}/{filename}-{seq}.ndjson".format(path=outputpath,
              filename="batch", seq=passage_index), "{}\n".format("\n".join(passages_batch)))

    print("Total passages: {}".format(passage_index))


def writeFile(filename: str, payload) -> None:
    file = open(filename, "w")
    file.write(payload)
    file.write("\n")
    file.close()


if __name__ == "__main__":
    main(sys.argv[1:])
