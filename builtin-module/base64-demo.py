import base64

print(base64.b64encode(b'binary\x00string'))
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))
# 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数
# 所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode(b'abcd--__'))


def safe_base64_decode(s):
    while len(s) % 4 != 0:
        s += '='
    return base64.b64decode(s)


assert b'abcd' == safe_base64_decode(
    'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode('YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')
