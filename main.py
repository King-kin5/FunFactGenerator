import json
import requests
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *


def get_fun_fact(_):
    # Clear the screen
    clear()

    # some html and a clown
    put_html(
        "<p align='left'><h1> Fun Fact Generator</h1></p>")

    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    response = requests.request("GET", url)
    data = json.loads(response.text)
    useless_fact = data['text']
    style(put_text(useless_fact), 'color:blue; font-size: 30px')
    put_buttons(
        [dict(label='Click me', value='outline-success',
              color='outline-success')], onclick=get_fun_fact)


def main():
    get_fun_fact(_)
# Driver Function
if __name__ == '__main__':
    # Put a heading "Fun Fact Generator" and a clown
    put_html(
        "<p align='left'><h1><img src='https://www.popsci.com/uploads/2023/05/19/clown2.png' width='25%'>   Fun Fact Generator</h1></p>")

    # hold the session for a long time
    # Put a Click me button
    put_buttons([dict(label='Click me', value='outline-success', color='outline-success')], onclick=get_fun_fact)
    hold()

    main()
