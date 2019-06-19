import urllib.request, json
from pymystem3 import Mystem
import pymorphy2
import markovify

token = '''1eb90fa31eb90fa31eb90fa3e61ed2374211eb91eb90fa343b35eab2f930b0e535fb496'''
m = Mystem()

print('Здесь мы смотрим, сколько прилагательных употребляет пользователь.')
print('Заодно мы сгенерируем 5 предложений в духе его постов Вконтакте')
link = input('Введите id пользователя: например, hesitantshade - моей подруги, которая мне помогла')
print('У меня были проблемы с настройкой окружения, поэтому если что, напишите, пожалуйста мне, на polinaponomareva.pp.@gmail.com')
#часть 1 - выкачиваем vkapi 1000 постов пользователя
posts = []
of = 100
http = 'https://api.vk.com/method/wall.get?domain=%s&count=100&v=5.92&access_token=%s' % (link, token)
req = urllib.request.Request(http)
response = urllib.request.urlopen(req)
result = response.read().decode('utf-8')
data = json.loads(result)
posts += data['response']['items']
while of < 1000:
    http = 'https://api.vk.com/method/wall.get?domain=%s&count=100&offset=%d&v=5.92&access_token=%s' % (
        link, of, token)
    req = urllib.request.Request(http)
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8')
    data = json.loads(result)
    of += 100
    posts += data['response']['items']
texts = []
for post in posts:
    texts.append(posts['text'])
#часть 2 - майстем
adjcounter = 0
for text in texts:
    lemmas = m.lemmatize(text)
    ana = m.analyze(text)
    for word in ana:
        if 'analysis' in word:
            if word['analysis']['gr'].startswith('A='):
                adjcounter += 1
adjcounter = adjcounter/1000
line = 'В речи пользователя {} прилагательных'.format(adjcounter)
print(line)
#часть 3 - марковская цепь
joined = ' '.join(texts)
m = markovify.Text(joined)
for i in range(5):
    print(m.make_sentence())




