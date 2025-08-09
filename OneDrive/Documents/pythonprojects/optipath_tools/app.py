from flask import Flask, render_template, request
import json
from path_finder import dijkstra
from draw import draw_graph
from time import time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    path = []
    cost = 0
    timestamp = 0  # for cache busting

    if request.method == 'POST':
        graph_input = request.form['graph_input']
        start = request.form['start']
        end = request.form['end']

        try:
            graph = json.loads(graph_input)
            cost, path = dijkstra(graph, start, end)
            print(f"Shortest path found: {path} with cost {cost}")
            draw_graph(graph, path)
            timestamp = int(time())
        except Exception as e:
            print("Error:", e)

    return render_template('index.html', path=path, cost=cost, timestamp=timestamp)

if __name__ == '__main__':
    app.run(debug=True)
