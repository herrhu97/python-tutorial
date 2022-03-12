import hmac

message = b'hello, world!'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
print(h.hexdigest())