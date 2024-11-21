import string

def generate_hashtag(input_string):
    hashtag = '#' + ''.join(word.capitalize() for word in input_string.split() if word.isalnum())
    return hashtag[:140] if len(hashtag) > 140 else hashtag

# запрос
request = input("Введите строку для хэштега: ")
print(generate_hashtag(request))
