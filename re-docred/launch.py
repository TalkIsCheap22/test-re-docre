import openai
openai.api_key = "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"
 
conversation=[{"role": "system", "content": "You are a helpful assistant."}]
while True:
    prompt = "1+1等于几"
    conversation.append({"role": "user","content": prompt})
    completion = openai.Completion.create(
        prompt=prompt,
        model="gpt-3.5-turbo",
        messages = conversation,
        temperature=1,
        max_tokens=2048
    )
    response = completion.choices[0].text
    #conversation.append({"role": "assistant", "content": response['choices'][0]['message']['content']}) #将上一次会话信息返回给chatgpt
    #print("\n" + response['choices'][0]['message']['content'] + "\n") #打印答案
    break