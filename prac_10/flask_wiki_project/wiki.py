"""
CP1404/CP5632 Practical
Flask + Wiki project
"""

from flask import Flask, render_template, request
import wikipedia

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_query = request.form['query']
        try:
            results = wikipedia.search(search_query)
            if results:
                first_result = wikipedia.page(results[0])
                return render_template('result.html',
                                       title=first_result.title,
                                       summary=first_result.summary)
            else:
                return render_template('result.html',
                                       title="No results",
                                       summary="No Wikipedia page found.")
        except wikipedia.exceptions.DisambiguationError as e:
            return render_template('result.html',
                                   title="Disambiguation Error",
                                   summary=f"Multiple results found: {e.options}")
        except wikipedia.exceptions.PageError:
            return render_template('result.html',
                                   title="Page Error",
                                   summary="Page not found.")
    return render_template('search.html')


if __name__ == '__main__':
    app.run(debug=True)
