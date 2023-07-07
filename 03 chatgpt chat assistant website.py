import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a Historic assistant"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Geschiedenis Chatbot")

demo.launch(share=True)
