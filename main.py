def parse(query: str) -> dict:
    value_dict = {}
    if '?' in query:
        ls1, ls2 = [], []
        for i in [i for i in query.split('?')][1].split('&'):
            if '=' in i:
                ls1.append(i.split('=')[0])
                ls2.append(i.split('=')[1])
        value_dict = dict(zip(ls1, ls2))
        return value_dict
    else:
        return value_dict




if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('https://www.google.com/search?q=ice+age%%BBD&client=ubuntu&hs=GhV&channel=fs&sxsrf=ALiCzsZr8H8g3tW') == {'q': 'ice+age%%BBD', 'client': 'ubuntu', 'hs': 'GhV', 'channel': 'fs', 'sxsrf': 'ALiCzsZr8H8g3tW'}
    assert parse('https://github.com/github/gitignore/blob/main/Python.gitignore') == {}
    assert parse('https://ithillel.zoom.us/j/93520894591?pwd=N1M3MHVSZFppL1JWL0RoRFVKalAydz09#success') == {'pwd': 'N1M3MHVSZFppL1JWL0RoRFVKalAydz09#success'}
    assert parse('https://www.youtube.com/watch?v=6K83dgjkQNw&t=90s') == {'v': '6K83dgjkQNw', 't': '90s'}
    assert parse('http://127.0.0.1:8000/') == {}
    assert parse('https://www.youtube.com/watch?v=oH2RJNILkLs') == {'v': 'oH2RJNILkLs'}
    assert parse('https://docs.python.org/3/c-api/index.html') == {}
    assert parse('https://www.digitalocean.com/community/tutorials') == {}
    assert parse('https://stepik.org/lesson/4757/step/3?unit=1059') == {'unit': '1059'}
    assert parse('https://play.google.com/store/apps/details?id=com.google.android.apps.dynamite&hl=ru&gl=US') == {'id': 'com.google.android.apps.dynamite', 'hl': 'ru', 'gl': 'US'}


def parse_cookie(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
