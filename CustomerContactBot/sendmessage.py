import requests
from .models import TelebotSettings

def sendMessage():
    settings = TelebotSettings.objects.get(pk=1)
    TOKEN = str(settings.token)
    chat_id = str(settings.chat_id)
    text = str(settings.text)
    api = 'https://api.telegram.org/bot'
    method = api + TOKEN + '/sendMessage'

    a = text.find('{')
    b = text.find('}')
    c = text.rfind('{')
    d = text.rfind('}')

    message = text[0:a] + text[b+1:c] + text[d:-1]

    req = requests.post(method, data={
        'chat_id':chat_id,
        'text':message
    })

