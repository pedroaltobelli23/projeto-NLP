import json
from youtube_transcript_api import YouTubeTranscriptApi

# Opening JSON file
# with open('projeto-NLP/categorias.json') as json_file:
#     cat = json.load(json_file)
 
#     # Print the type of data variable
#     print("Type:", type(cat))
#     print(cat[0].keys())
#     # Print the data of dictionary
#     # print("\ncategoria1:", data[0])
    
with open('parsed_data_renamed_train.json') as json_file:
    data = json.load(json_file)
    saida = []
    max_size = 15
    i = 0
    # Print the type of data variable
    print("Type:", type(data))
    
    for id in data.keys():
        a = data[id]
        
        if i < max_size: 
            for el in a:
                if el == 1: #categoria de videogames
                    try:
                        transcript = YouTubeTranscriptApi.get_transcript(id)
                        saida.append(id)
                        i+=1
                        print(id)
                    except:
                        continue


    print(len(data))
    print(saida)

    # Print the data of dictionary
    # print("\ncategoria1:", data[0])