import json

with open('test_revised.json', 'r') as file:
    json_str = file.read()
datas = json.loads(json_str)
#print(len(data))   #500
for i in range(10):
    data = datas[i]
    with open("text{num}.txt".format(num=i+1), 'w') as file:
        file.write("Title: " + data["title"] + "\nContent: ")
        content = ""
        for sent in data["sents"]:
            for word in sent:
                if word != "," and word != ".":
                    content += (word + ' ')
                else:
                    content = content[:-1] + word[0]
        file.write(content + "\n")
        