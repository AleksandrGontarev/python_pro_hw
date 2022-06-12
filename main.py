def parse(query: str) -> dict:
    if "?" not in query:
        return {}
    params = query.split("?", 1)[-1]
    if not params:
        return {}
    if "&" not in params and "=" in params:
        name_or_color = params.split("=", 1)
        if name_or_color[0] == "name":
            return {'name': "".join(name_or_color[1:])}
        elif name_or_color[0] == "color":
            return {'color': "".join(name_or_color[1:])}
        elif name_or_color[0] != 'name' and name_or_color[0] != 'color':
            return {}
    elif "&" in params and "=" in params:
        name_or_color = params.split("&")
        name = name_or_color[0]
        name_parse = name.split('=', 1)
        color = name_or_color[1]
        color_parse = color.split("=", 1)
        if name_parse[0] == 'name' and color_parse[0] == 'color':
            return {
                    "name": "".join(name_parse[1:]),
                    "color": "".join(color_parse[1:])
                    }
        elif name_parse[0] == 'name':
            return {"name": "".join(name_parse[1:])}
        elif color_parse[0] == 'color':
            return {"color": "".join(color_parse[1:])}
        return {}
    else:
        return {}


if __name__ == '__main__':
     assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
     assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
     assert parse('http://example.com/') == {}
     assert parse('http://example.com/?') == {}
     assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
     assert parse('http://example.com/?name=?&color=?') == {'name': '?', 'color': '?'}
     assert parse('http://example.com/?&color=') == {'color': ''}
     assert parse('http://example.com/?name=') == {'name': ''}
     assert parse('http://example.com/?&') == {}
     assert parse('https://example.com/path/to/page?color=color') == {'color': 'color'}
     assert parse('https://example.com/path/to/page?name=color') == {'name': 'color'}
     assert parse('https://example.com/path/to/page?color') == {}
     assert parse('https://example.com/path/to/page?=') == {}
     assert parse('https://example.com/path/to/page?=?&') == {}
     assert parse('https://example.com/path/to/page?name==color') == {'name': '=color'}

def parse_cookie(query: str) -> dict:
    cookie = {}
    if "name=" in query:
        name = query.split('=', 1)[1]
        if ';age=' in name:
            name = name.split(';age=')[0]
        elif ';' in name:
            name = name.rsplit(';', 1)
        if name:
            cookie['name'] = ''.join(name)
    if ";age=" in query:
        age = query.split(';age=')[1].rsplit(';', 1)[0]
        if age:
            cookie['age'] = ''.join(age)
    elif "age=" in query:
        age = query.split('age=')[1].split(';')[0]
        if age:
            if age('age=')[0] != 'name=':
                cookie['age'] = age
    return cookie


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Dima;age=28=;') == {'name': 'Dima', 'age': '28='}
    assert parse_cookie('name==Dima;age=28;') == {'name': '=Dima', 'age': '28'}
    assert parse_cookie('name=;age=28;') == {'age': '28'}
    assert parse_cookie('name=;;;;age=28;') == {'name': ';;;', 'age': '28'}
    assert parse_cookie('name=age=28;age=') == {'name': 'age=28'}
    assert parse_cookie('name=age=28;age=') == {'name': 'age=28'}
    assert parse_cookie('name=;age=') == {}
    assert parse_cookie('name=Di=ma;age=') == {'name': 'Di=ma'}
    assert parse_cookie('name=name;age=age') == {'name': 'name', 'age': 'age'}
    assert parse_cookie('name=;;;;age=;;;') == {'name': ';;;', 'age': ';;'}
    assert parse_cookie('name=;=;age=;=;') == {'name': ';=', 'age': ';='}