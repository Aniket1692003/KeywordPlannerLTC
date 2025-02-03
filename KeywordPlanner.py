import networkx as nx
import matplotlib.pyplot as plt

# Define keywords
keywords = [
    "Self Awareness",
    "Positivity",
    "Healing",
    "Gratitude",
    "Faith",
    "Energy",
    "Biodiversity",
    "Mindfulness",
    "Balance",
    "Connection",
    "Buddha Tree",
    "Yin yang",
    "Chakra",
    "Phoenix rising",
    "Hands",
    "Mandala",
    "Waves",
    "Peacock Feather",
    "Rising Sun",
    "Sustainability",
    "Growth",
    "Harmony",
    "Nurture",
    "Co dependence",
    "Natural Resources",
    "Self Sufficiency",
    "Connect",
    "Cycle of seasons",
    "Roots",
    "Sunrise",
    "Water droplets",
    "Rain",
    "Soil",
    "Wellness",
    "Nutrition",
    "Exercise",
    "Mental health",
    "Discipline",
    "Immunity",
    "Endurance",
    "Strength",
    "Performance",
    "Triangle",
    "Heartbeat",
    "Gym",
    "Pulse",
    "Yoga pose",
    "Horse",
    "Ground",
    "Bow arrow",
    "Armed Forces",
    "Ashoka pillar",
    "Lion",
    "Honor",
    "Heritage",
    "Freedom",
    "Development",
    "Responsibility",
    "Integrity",
    "Duty",
    "Identity",
    "Culture",
    "Indian Flag",
    "Ashoka Chakra",
    "Salute",
    "Flame",
    "Sun rise",
    "Orange",
    "Progress",
    "Service",
    "Rights",
    "Unity",
    "Empowerment",
    "Strategy",
    "Bonding",
    "Problem solving",
    "Innovation",
    "Vision",
    "Leadership",
    "Guidance",
    "Collaboration",
    "Trust",
    "Evolve",
    "Light",
    "Fire torch",
    "Lighthouse",
    "Building Blocks",
    "Compass",
    "Togetherness",
    "Holistic Development",
    "Adaptability",
    "Inspiration",
    "Belief",
    "Enlightenment",
    "Direction"
]

central_keywords = {"Unity", "Direction", "Strength", "Bonding", "Evolve"}

# Build graph and add nodes with attribute marking central nodes
G = nx.Graph()
for kw in keywords:
    G.add_node(kw, central=(kw in central_keywords))

# Remove previous generic connections:
# for kw in keywords:
#    if kw not in central_keywords:
#         for center in central_keywords:
#             G.add_edge(kw, center)
# ...
# for i in range(len(central_list)):
#    for j in range(i + 1, len(central_list)):
#         G.add_edge(central_list[i], central_list[j])

# Add meaningful connections for main 5 keywords via dedicated groups
groups_central = [
    {"Unity", "Togetherness", "Collaboration", "Connection"},
    {"Direction", "Guidance", "Vision", "Compass"},
    {"Strength", "Endurance", "Gym", "Performance", "Pulse"},
    {"Bonding", "Trust", "Responsibility", "Integrity", "Duty"},
    {"Evolve", "Innovation", "Growth", "Development", "Progress"}
]

for group in groups_central:
    group_nodes = list(group & set(keywords))
    for i in range(len(group_nodes)):
        for j in range(i + 1, len(group_nodes)):
            if not G.has_edge(group_nodes[i], group_nodes[j]):
                G.add_edge(group_nodes[i], group_nodes[j])

# Add extra meaningful connections among non-central keywords by grouping similar keywords
groups = [
    {"Healing", "Wellness", "Nutrition", "Mental health", "Exercise"},
    {"Biodiversity", "Natural Resources", "Cycle of seasons", "Roots", "Rain", "Soil", "Sunrise", "Water droplets", "Rising Sun", "Sun rise"},
    {"Self Awareness", "Mindfulness", "Gratitude", "Faith", "Chakra", "Phoenix rising", "Mandala", "Buddha Tree", "Yin yang", "Light", "Enlightenment", "Belief", "Inspiration"},
    {"Sustainability", "Development", "Progress", "Innovation"},
    {"Indian Flag", "Ashoka Chakra", "Ashoka pillar", "Heritage", "Lion", "Honor", "Culture"},
    {"Discipline", "Immunity", "Endurance", "Gym", "Pulse"},
    {"Positivity", "Energy", "Balance", "Responsibility", "Integrity", "Duty", "Identity"}
]

for group in groups:
    group_nodes = list(group & set(keywords))
    for i in range(len(group_nodes)):
        for j in range(i + 1, len(group_nodes)):
            if not G.has_edge(group_nodes[i], group_nodes[j]):
                G.add_edge(group_nodes[i], group_nodes[j])

# UPDATED EXTRA: Boost extra targeted connections for each central keyword by adding more relevant keywords
central_extra_connections = {
    "Unity": ({"Togetherness", "Collaboration", "Connection", "Bonding", "Trust", "Service", "Empowerment", "Culture", "Heritage", "Gratitude"}
              | {"Positivity", "Responsibility", "Integrity", "Duty", "Identity", "Holistic Development", "Inspiration", "Adaptability", "Leadership", "Guidance"}),
    "Direction": ({"Guidance", "Vision", "Compass", "Leadership", "Strategy", "Innovation", "Progress", "Mindfulness", "Faith"}
                  | {"Lighthouse", "Building Blocks", "Salute", "Flame", "Indian Flag", "Ashoka Chakra", "Ashoka pillar", "Heritage", "Culture", "Identity"}),
    "Strength": ({"Endurance", "Gym", "Performance", "Pulse", "Discipline", "Immunity", "Exercise", "Mental health"}
                 | {"Healing", "Wellness", "Nutrition", "Energy", "Heartbeat", "Horse", "Fire torch", "Lion", "Honor", "Adaptability", "Balance", "Inspiration"}),
    "Bonding": ({"Trust", "Responsibility", "Integrity", "Duty", "Connection", "Collaboration", "Empowerment", "Service", "Culture"}
                | {"Togetherness", "Gratitude", "Mindfulness", "Harmony", "Faith", "Positivity", "Development", "Progress", "Growth", "Inspiration", "Adaptability"}),
    "Evolve": ({"Innovation", "Growth", "Development", "Progress", "Adaptability", "Inspiration", "Vision", "Strategy"}
               | {"Holistic Development", "Empowerment", "Culture", "Leadership", "Guidance", "Collaboration", "Responsibility", "Integrity", "Duty", "Trust", "Service", "Gratitude"})
}

for central in central_keywords:
    extra_nodes = central_extra_connections.get(central, set())
    for node in extra_nodes & set(keywords):
        if not G.has_edge(central, node):
            G.add_edge(central, node)

# Recompute degrees and sort nodes in descending order
degrees = dict(G.degree())
sorted_nodes = sorted(degrees.items(), key=lambda x: x[1], reverse=True)

# --- NEW CODE BLOCK: Adjust non-central node degrees to be between 10 and 17 deterministically ---
non_central = sorted([n for n in G.nodes() if not G.nodes[n].get("central")])
# First, remove extra edges for nodes with degree > 17
for v in non_central:
    while G.degree(v) > 17:
        neighbors = sorted(list(G.neighbors(v)))
        removed = False
        for w in neighbors:
            # Prefer to remove edge with non-central neighbor
            if not G.nodes[w].get("central"):
                G.remove_edge(v, w)
                removed = True
                break
        if not removed and neighbors:
            # If no non-central neighbor available, remove the first edge
            G.remove_edge(v, neighbors[0])

# Then, add edges for nodes with degree < 10
for v in non_central:
    while G.degree(v) < 10:
        # Choose candidate from non-central nodes (deterministically sorted)
        candidates = [w for w in non_central if w != v and not G.has_edge(v, w) and G.degree(w) < 17]
        if candidates:
            w = candidates[0]
            G.add_edge(v, w)
        else:
            break
# Recompute degrees and sorted list after adjustments
degrees = dict(G.degree())
sorted_nodes = sorted(degrees.items(), key=lambda x: x[1], reverse=True)

# NEW: Use Plotly and Dash for interactive visualization instead of matplotlib

import json
import plotly
import plotly.graph_objects as go
from flask import Flask, render_template_string

# UPDATED: Increase spacing with a larger k value
pos = nx.spring_layout(G, k=1.2, seed=42)

# Prepare edge traces
edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x += [x0, x1, None]
    edge_y += [y0, y1, None]

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=1.5, color='#888'),
    hoverinfo='none',
    mode='lines'
)

# UPDATED: Prepare node traces with dynamic sizing and bolder text.
node_x = []
node_y = []
node_text = []
node_color = []
node_size = []
for node in G.nodes():
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)
    deg = G.degree(node)
    node_text.append(f"{node}: {deg}")
    node_color.append("red" if G.nodes[node].get("central") else "lightblue")
    # Dynamic sizing: base scale with degree plus extra boost for central nodes.
    size = deg * 3 + (6 if G.nodes[node].get("central") else 3)
    node_size.append(size)

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers+text',
    text=[node for node in G.nodes()],
    textposition="top center",
    hoverinfo='text',
    marker=dict(
        color=node_color,
        size=node_size,
        line_width=2
    ),
    textfont=dict(
        family="Arial Black, sans-serif",
        size=12,
        color="#333"
    )
)

fig = go.Figure(
    data=[edge_trace, node_trace],
    layout=go.Layout(
        title="<br>Interactive Keyword Network Graph",
        titlefont=dict(size=26, color="#222", family="Roboto, Helvetica, Arial, sans-serif"),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(255,255,255,1)",
        autosize=True,
        showlegend=False,
        hovermode='closest',
        margin=dict(l=20, r=20, t=80, b=20),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
    )
)

# Convert the Plotly figure to JSON
graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

# Compute node ranking list for display
nodeRanking = [f"{node}: {deg}" for node, deg in sorted_nodes]

# UPDATED HTML template with Google Font and refined CSS for a cleaner display
html_template = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Interactive Keyword Network Graph</title>
  <link href="https://fonts.googleapis.com/css?family=Roboto:400,700&display=swap" rel="stylesheet">
  <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
  <style>
    html, body {
      margin: 0;
      padding: 0;
      height: 100%;
      width: 100%;
      font-family: 'Roboto', sans-serif;
      background: linear-gradient(135deg, #f7f7f7, #ffffff);
      display: flex;
    }
    #ranking-panel {
      width: 20%;
      background: #fff;
      border-right: 2px solid #eee;
      overflow-y: auto;
      padding: 20px;
    }
    #ranking-panel h2 {
      margin-top: 0;
      text-align: center;
      font-size: 22px;
      font-weight: 700;
      color: #333;
    }
    #ranking-panel ul {
      list-style: none;
      padding: 0;
      margin: 0;
    }
    #ranking-panel li {
      padding: 8px 10px;
      margin: 4px 0;
      border-radius: 4px;
      background: #fafafa;
      border: 1px solid #ececec;
      font-size: 14px;
      color: #555;
    }
    #graph-panel {
      flex-grow: 1;
      background: #fff;
      position: relative;
    }
    #graph {
      width: 100%;
      height: 100%;
    }
  </style>
</head>
<body>
  <div id="ranking-panel">
    <h2>Node Ranking</h2>
    <ul>
      {% for node in nodeRanking %}
      <li>{{ node }}</li>
      {% endfor %}
    </ul>
  </div>
  <div id="graph-panel">
    <div id="graph"></div>
  </div>
  <script>
    var graph = {{ graphJSON | safe }};
    Plotly.newPlot('graph', graph.data, graph.layout, {responsive: true});
  </script>
</body>
</html>
"""

# Create and run Flask app on localhost:3001
app = Flask(__name__)

@app.route("/")
def index():
    return render_template_string(html_template, graphJSON=graphJSON, nodeRanking=nodeRanking)

if __name__ == '__main__':
    app.run(debug=True, port=3001)
