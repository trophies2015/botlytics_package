import http.client

conn = http.client.HTTPConnection("www.botlytics.co")

payload = "{\"message\":{\"text\":\"Hello!\",\"kind\":\"incoming\",\"conversation_identifier\":\"user_123\"}}"

headers = { 'content-type': "application/json" }

conn.request("POST", "/api/v1/messages?token=7d1621e65ebb3f29", payload, headers)

res = conn.getresponse()
data = res.read()
