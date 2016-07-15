import requests

def send_request(API_KEY, text, kind, conversation_identifier):
  URL = "http://www.botlytics.co/api/v1/messages?token=" + API_KEY
  if (len(conversation_identifier) > 0):
      return requests.post(URL, {"message":{"text":text,"kind":kind,"conversation_identifier":conversation_identifier}})
  else:
      return requests.post(URL, {"message":{"text":text,"kind":kind}})

ta = send_request("7d1621e65ebb3f29", "heloe", "incoming", "okok")
print(ta.text)


