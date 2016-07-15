import requests

def send_request(API_KEY, text, kind, conversation_identifier):
  URL = "http://www.botlytics.co/api/v1/messages?token=" + API_KEY
  if (len(conversation_identifier) > 0):
      return requests.post(URL, data={"message":{"text":text,"kind":kind,"conversation_identifier":conversation_identifier}}, headers={"content-type":"application/json"})
  else:
      return requests.post(URL, data={"message":{"text":text,"kind":kind}}, headers={"content-type":"application/json"})


