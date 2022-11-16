#program for simple chat-bot
from nltk.chat.util import Chat, reflections
#reflections

pairs=[
    ['hi',['hello whatsapp?']],
    ['good morning',['happy morning']],
    ['how are you',['I am good hope your doing great']],
    ['say a joke',['I am a doggy']], 
    ['what is your age',['I am thrice as old as you']], 
    ['do u know how to sing',['Yeah ofcourse']],
    ['sing a song',['twinkle twinkle little star']],
    ['need help',['how can i help you?']],
    ['what is your name',['I am chat Bot']]
    
]

chat = Chat(pairs,reflections)
chat.converse()
