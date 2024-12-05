def popular_words(text, words):
    text_lower = text.lower()
    words_in_text = text_lower.split()
    return {word: words_in_text.count(word) for word in words}

# test
assert popular_words(
    '''When I was One I had just begun When I was Two I was nearly new''',
    ['i', 'was', 'three', 'near']
) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'

print('OK')