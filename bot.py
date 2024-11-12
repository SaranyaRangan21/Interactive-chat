# bot.py

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
#from cleaner import clean_corpus

CORPUS_FILE = "C:\\Users\\sowmi\\Interactive-chat\\corpusdata.txt"

chatbot = ChatBot("Chatpot")

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(CORPUS_FILE)

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f">>> {chatbot.get_response(query)}")