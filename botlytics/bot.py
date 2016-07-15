import httplib
def send_request(API_KEY, text, kind, conversation_identifier):
  conn = httplib.HTTPConnection("www.botlytics.co")
  headers = { 'content-type': "application/json" }
  payload = ""
  URL = "/api/v1/messages?token=" + API_KEY
  if (len(conversation_identifier) > 0):
     payload = "{\"message\":{\"text\":\""+text+"\",\"kind\":\""+kind+"\",\"conversation_identifier\":\""+conversation_identifier+"\"}}"
  else:
     payload = "{\"message\":{\"text\":\""+text+"\",\"kind\":\""+kind+"\"}}"
  conn.request("POST", URL, payload, headers)
  res = conn.getresponse()
  data = res.read()
  return res

