from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

CORPUS_FILE = "./corpusdata.txt"

chatbot = ChatBot("Chatpot")

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(CORPUS_FILE)

def interactivechat(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def reply(request):
  if request.GET.get("q") is None or request.GET.get("q") == "":
    response="Enter the query"
  else:
    response=chatbot.get_response(request.GET.get("q"))
  data1={'output':response}
  template = loader.get_template('reply.html')
  context = {
    'data1': data1,
  }
  return HttpResponse(template.render(context, request))



 