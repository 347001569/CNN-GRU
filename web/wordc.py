from wordcloud import WordCloud

def get_text():
    classes=[
        'news_car',
        'news_entertainment',
        'news_game',
        'news_sports',
        'news_tech'
    ]
    news_car=''
    news_entertainment=''
    news_game=''
    news_sports=''
    news_tech=''


    with open('item/sum_news.txt','r',encoding='utf-8') as file:
        reads=file.readlines()
        for read in reads:
            index=read.find(' ')

            if read[:index] =='news_car':
                read=read[index+1:].replace('/n',' ')
                news_car+=read

            if read[:index] == 'news_entertainment':
                read=read[index+1:].replace('/n',' ')
                news_entertainment+=read

            if read[:index] == 'news_game':
                read = read[index + 1:].replace('/n', ' ')
                news_game += read

            if read[:index] == 'news_sports':
                read = read[index + 1:].replace('/n', ' ')
                news_sports += read

            if read[:index] == 'news_tech':
                read = read[index + 1:].replace('/n', ' ')
                news_tech += read

    generate_cloud(news_car,'news_car')
    generate_cloud(news_entertainment,'news_entertainment')
    generate_cloud(news_game,'news_game')
    generate_cloud(news_sports,'news_sports')
    generate_cloud(news_tech,'news_tech')


def generate_cloud(cloud_text,cloud_name):
    wc = WordCloud(
        background_color="white", #背景颜色
        max_words=200, #显示最大词数
        font_path="C:\Windows\Fonts\simhei.ttf",  #使用字体
        min_font_size=15,
        max_font_size=50,
        width=400  #图幅宽度
        )
    wc.generate(cloud_text)
    wc.to_file("item/%s.png"%cloud_name)

def main():
    get_text()


main()