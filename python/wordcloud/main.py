# download ipaexg.ttf from https://moji.or.jp/ipafont/ipaex00401/
from wordcloud import WordCloud

text = 'hello world, こんにちは'
wordcloud = WordCloud().generate(text)

wordcloud = WordCloud(max_font_size=40, font_path='./ipaexg.ttf').generate(text)

wordcloud.to_file('wordcloud.png')
