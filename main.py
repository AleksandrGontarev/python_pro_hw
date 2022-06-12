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


# def parse_cookie(query: str) -> dict:
#     return {}
#
#
# if __name__ == '__main__':
#     assert parse_cookie('name=Dima;') == {'name': 'Dima'}
#     assert parse_cookie('') == {}
#     assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
#     assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
