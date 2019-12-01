from flask import Flask,render_template, request
#from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer

from nazimProject.mainn import *

app = Flask(__name__)


#english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
#trainer = ChatterBotCorpusTrainer(english_bot)
#trainer.train('chatterbot.corpus.english')

@app.route('/')
def home():
    return render_template('index.html')




# while True:
#     inptt = input('say anything')
#     if inptt.lower() == "bye":
#         break
#     print(chat(inptt))
#




@app.route('/process',methods=['POST'])
def process():
    while True:
        user_input = request.form['user_input']
        if user_input.lower() == "bye":
            break
        bot_response = str(chat(user_input))
        print("shondesh: " + bot_response)
        return render_template('index.html', user_input=user_input,
                               bot_response=bot_response
                               )



    # userText = request.args.get('msg')
    # return str(english_bot.get_response(userText))


if __name__ == '__main__':
    app.run(debug=True)



