import json


def get_articles() -> dict:
    with open('articles.json', 'r', encoding='UTF-8') as f:
        return json.load(f)


def save_article(name, text):
    with open('articles.json', 'r', encoding='utf=8') as f:
        data = json.load(f)
    data[name] = text
    with open('articles.json', 'w', encoding='utf=8') as f:
        json.dump(data, f, ensure_ascii=False)


def delete_article(name):
    with open('articles.json', 'r', encoding='utf=8') as f:
        data = json.load(f)
    del data[name]
    with open('articles.json', 'w', encoding='utf=8') as f:
        json.dump(data, f, ensure_ascii=False)


# save_article('Дворовая кошка', 'Обычная кошка')
# delete_article('Мейн-кун')