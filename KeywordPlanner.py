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
    "Wayfinding",
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
    "Guidance",
    # New thematic nodes for richer connections:
    "Community",
    "Solidarity",
    "Purpose",
    "Clarity",
    "Vitality",
    "Power",
    "Camaraderie",
    "Transformation",
    # New nodes for additional central connections for "Unity":
    "Friendship", "Cooperation", "Alliance", "Cohesion", "Integration", "Synergy", "Amity", "Concord", "Fraternity",
    # For "Guidance":
    "Navigation", "Orientation", "Trajectory", "Determination", "Focus", "Steadiness", "Course", "Intuition",
    # For "Strength":
    "Might", "Robustness", "Stamina", "Force", "Potency", "Durability", "Hardiness", "Resilience", "Vigor",
    # For "Bonding":
    "Affinity", "Warmth", "Fellowship", "Closeness", "Rapport", "Union", "Kinship", "Attachment", "Support", "Linkage",
    # For "Evolve":
    "Metamorphosis", "Evolution", "Advancement", "Reinvention", "Renewal", "Reformation", "Shift", "Breakthrough", "Emergence", "Revamp"
]

central_keywords = {"Unity", "Guidance", "Strength", "Bonding", "Evolve"}

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
    {"Unity", "Togetherness", "Collaboration", "Connection", "Community", "Solidarity"},
    {"Guidance", "Wayfinding", "Vision", "Compass", "Purpose", "Clarity"},
    {"Strength", "Endurance", "Gym", "Performance", "Pulse", "Vitality", "Power"},
    {"Bonding", "Trust", "Responsibility", "Integrity", "Duty", "Camaraderie"},
    {"Evolve", "Innovation", "Growth", "Development", "Progress", "Transformation"}
]

for group in groups_central:
    group_nodes = list(group & set(keywords))
    for i in range(len(group_nodes)):
        for j in range(i + 1, len(group_nodes)):
            if not G.has_edge(group_nodes[i], group_nodes[j]):
                G.add_edge(group_nodes[i], group_nodes[j])

# Add extra meaningful connections among non-central keywords by grouping similar keywords
groups = [
    # Health and wellness group
    {"Healing", "Wellness", "Nutrition", "Mental health", "Exercise", "Roots"},
    # Mindfulness and inner growth group
    {"Self Awareness", "Mindfulness", "Gratitude", "Faith", "Chakra", "Phoenix rising", "Mandala", "Enlightenment", "Inspiration"},
    # Environment and sustainability group
    {"Biodiversity", "Natural Resources", "Sustainability", "Soil", "Rain", "Roots"},
    # Cultural heritage group
    {"Indian Flag", "Ashoka Chakra", "Ashoka pillar", "Heritage", "Lion", "Honor", "Culture", "Roots"},
    # Energy and balance group
    {"Positivity", "Energy", "Balance", "Pulse", "Power", "Roots"},
    # Discipline and resilience group
    {"Discipline", "Immunity", "Gym"}
]

for group in groups:
    group_nodes = list(group & set(keywords))
    for i in range(len(group_nodes)):
        for j in range(i + 1, len(group_nodes)):
            if not G.has_edge(group_nodes[i], group_nodes[j]):
                G.add_edge(group_nodes[i], group_nodes[j])

# UPDATED EXTRA: Boost extra targeted connections for each central keyword by adding more relevant keywords
central_extra_connections = {
    "Unity": {"Togetherness", "Collaboration", "Connection", "Community", "Solidarity", "Empowerment", "Service", "Culture", "Heritage", "Gratitude",
              "Friendship", "Cooperation", "Alliance", "Cohesion", "Integration", "Synergy", "Amity", "Concord", "Fraternity"},
    "Guidance": {"Wayfinding", "Vision", "Compass", "Purpose", "Clarity", "Leadership", "Strategy", "Innovation", "Progress", "Mindfulness", "Faith",
                  "Navigation", "Orientation", "Trajectory", "Determination", "Focus", "Steadiness", "Course", "Intuition"},
    "Strength": {"Endurance", "Gym", "Performance", "Pulse", "Vitality", "Power", "Discipline", "Immunity", "Exercise", "Mental health",
                 "Might", "Robustness", "Stamina", "Force", "Potency", "Durability", "Hardiness", "Resilience", "Vigor"},
    "Bonding": {"Trust", "Responsibility", "Integrity", "Duty", "Camaraderie", "Connection", "Collaboration", "Empowerment", "Service", "Culture",
                "Affinity", "Warmth", "Fellowship", "Closeness", "Rapport", "Union", "Kinship", "Attachment", "Support", "Linkage"},
    "Evolve": {"Innovation", "Growth", "Development", "Progress", "Transformation", "Adaptability", "Inspiration", "Vision", "Strategy",
               "Metamorphosis", "Evolution", "Advancement", "Reinvention", "Renewal", "Reformation", "Shift", "Breakthrough", "Emergence", "Revamp"}
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

# Create Flask app instance
app = Flask(__name__)

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
    line=dict(width=1, color='rgba(150,150,150,0.4)'),
    hoverinfo='none',
    mode='lines'
)

# Split nodes into central and non-central traces
def create_node_trace(nodes, is_central=False):
    node_x = []
    node_y = []
    node_text = []
    node_sizes = []
    node_ids = []  # Add node IDs for click events
    
    for node in nodes:
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        deg = G.degree(node)
        node_text.append(f"{node}: {deg}")
        size = deg * 3 + (10 if is_central else 3)
        node_sizes.append(size)
        node_ids.append(node)  # Store node ID
    
    return go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        text=[node for node in nodes],
        textposition="top center",
        hoverinfo='text',
        ids=node_ids,  # Add IDs for click events
        marker=dict(
            color='red' if is_central else 'lightblue',
            size=node_sizes,
            line=dict(color='black', width=2),
            opacity=0.85,
            symbol='circle'
        ),
        textfont=dict(
            family="Poppins, sans-serif",
            size=11,
            color="black"
        )
    )

# Create traces for central and non-central nodes
central_nodes = [node for node in G.nodes() if G.nodes[node].get("central")]
non_central_nodes = [node for node in G.nodes() if not G.nodes[node].get("central")]

central_node_trace = create_node_trace(central_nodes, is_central=True)
non_central_node_trace = create_node_trace(non_central_nodes, is_central=False)

fig = go.Figure(
    data=[edge_trace, non_central_node_trace, central_node_trace],
    layout=go.Layout(
        title=dict(
            text="<b>LTC Keyword Graph</b>",
            font=dict(size=28, color="#2C3E50", family="Poppins, sans-serif"),
            x=0.5,
            y=0.95
        ),
        paper_bgcolor="#F8FAFB",
        plot_bgcolor="#F8FAFB",
        autosize=True,
        showlegend=False,
        hovermode='closest',
        margin=dict(l=20, r=20, t=90, b=20),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        dragmode='pan'
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
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap" rel="stylesheet">
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <style>
        html, body {
            margin: 0;
            padding: 0;
            height: 100%;
            width: 100%;
            font-family: 'Poppins', sans-serif;
            background: #F8FAFB;
            display: flex;
        }
        #ranking-panel {
            width: 300px;
            background: white;
            box-shadow: 2px 0 10px rgba(0,0,0,0.1);
            overflow-y: auto;
            padding: 25px;
        }
        #ranking-panel h2 {
            margin: 0 0 20px 0;
            text-align: center;
            font-size: 24px;
            font-weight: 600;
            color: #2C3E50;
        }
        #ranking-panel ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        #ranking-panel li {
            padding: 12px 15px;
            margin: 8px 0;
            border-radius: 8px;
            background: #F8FAFB;
            border: 1px solid #E5E9F2;
            font-size: 14px;
            color: #2C3E50;
            transition: all 0.3s ease;
            cursor: pointer;
        }
        #ranking-panel li:hover {
            transform: translateX(5px);
            background: #EEF2F7;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }
        #graph-panel {
            flex-grow: 1;
            background: white;
            position: relative;
            border-radius: 0 0 0 20px;
            box-shadow: -2px 0 10px rgba(0,0,0,0.05);
        }
        #graph {
            width: 100%;
            height: 100%;
        }
        .plotly-graph-div {
            border-radius: 0 0 0 20px;
        }
        
        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(255, 51, 51, 0.4); }
            70% { box-shadow: 0 0 0 10px rgba(255, 51, 51, 0); }
            100% { box-shadow: 0 0 0 0 rgba(255, 51, 51, 0); }
        }
        
        #ranking-panel li.central-node {
            background: linear-gradient(135deg, #fff5f5, #fff);
            border-left: 4px solid #FF3333;
            font-weight: 600;
            color: #FF3333;
            padding-left: 20px;
            animation: pulse 2s infinite;
        }
        
        #ranking-panel li.central-node:hover {
            background: linear-gradient(135deg, #ffe8e8, #fff);
            transform: translateX(10px);
            box-shadow: 0 2px 8px rgba(255,51,51,0.2);
        }
        
        #ranking-panel li.central-node::before {
            content: "★";
            margin-right: 8px;
            color: #FF3333;
        }
        
        .highlighted-node {
            stroke: #FF3333 !important;
            stroke-width: 3px !important;
        }
        
        .highlighted-edge {
            stroke: #FF3333 !important;
            stroke-width: 2px !important;
            opacity: 1 !important;
        }
        
        .dimmed {
            opacity: 0.1 !important;
        }
    </style>
</head>
<body>
    <div id="ranking-panel">
        <h2>Keyword Connections</h2>
        <ul>
            {% for node in nodeRanking %}
            <li class="{{ 'central-node' if node.split(':')[0].strip() in central_keywords else '' }}">
                {{ node }}
            </li>
            {% endfor %}
        </ul>
    </div>
    <div id="graph-panel">
        <div id="graph"></div>
    </div>
    <script>
        var graph = {{ graphJSON | safe }};
        var myPlot = document.getElementById('graph');
        var currentlySelected = null;
        // Store original sizes for reset
        var originalSizes = graph.data.map(trace => trace.marker ? trace.marker.size : null);
        
        Plotly.newPlot('graph', graph.data, graph.layout, {
            responsive: true,
            scrollZoom: true,
            displayModeBar: false
        });

        function resetView() {
            Plotly.restyle(myPlot, {
                'marker.opacity': 1,
                'textfont.opacity': 1,
                'line.opacity': 1,
                'marker.size': originalSizes
            });
            currentlySelected = null;
        }

        myPlot.on('plotly_click', function(data) {
            if (!data.points[0]) return;
            
            var clickedNode = data.points[0];
            var nodeId = clickedNode.text.split(':')[0].trim();
            
            // If clicking the same node, reset the view
            if (currentlySelected === nodeId) {
                resetView();
                return;
            }
            
            currentlySelected = nodeId;
            var neighbors = {{ neighbors | tojson }};
            var clickedNodeNeighbors = neighbors[nodeId] || [];
            
            // Create update object for all traces
            var update = {
                'marker.opacity': [],
                'textfont.opacity': [],
                'marker.size': []
            };

            // Update edge trace opacity
            var edgeUpdate = {
                'line.opacity': Array(graph.data[0].x.length).fill(0.1)
            };

            // Set opacity for nodes based on neighbors
            for (var i = 1; i < graph.data.length; i++) {
                var trace = graph.data[i];
                var opacities = Array(trace.x.length).fill(0.1);
                var sizes = Array(trace.x.length).fill(originalSizes[i][0]);
                var textOpacities = Array(trace.x.length).fill(0.1);

                trace.text.forEach((text, index) => {
                    var nodeName = text.split(':')[0].trim();
                    if (nodeName === nodeId || clickedNodeNeighbors.includes(nodeName)) {
                        opacities[index] = 1;
                        textOpacities[index] = 1;
                        sizes[index] = originalSizes[i][index] * 1.2;  // Increase size by 20%
                    }
                });

                update['marker.opacity'].push(opacities);
                update['textfont.opacity'].push(textOpacities);
                update['marker.size'].push(sizes);
            }

            // Highlight edges connected to clicked node
            clickedNodeNeighbors.forEach(neighbor => {
                for (var i = 0; i < graph.data[0].x.length; i += 3) {
                    var x0 = graph.data[0].x[i];
                    var y0 = graph.data[0].y[i];
                    var x1 = graph.data[0].x[i + 1];
                    var y1 = graph.data[0].y[i + 1];
                    
                    if ((Math.abs(x0 - clickedNode.x) < 0.01 && Math.abs(y0 - clickedNode.y) < 0.01) ||
                        (Math.abs(x1 - clickedNode.x) < 0.01 && Math.abs(y1 - clickedNode.y) < 0.01)) {
                        edgeUpdate['line.opacity'][i] = 1;
                        edgeUpdate['line.opacity'][i + 1] = 1;
                        edgeUpdate['line.opacity'][i + 2] = 1;
                    }
                }
            });

            // Apply updates
            Plotly.restyle(myPlot, edgeUpdate, [0]);
            Plotly.restyle(myPlot, update, Array.from({length: graph.data.length - 1}, (_, i) => i + 1));
            
            // Double click anywhere to reset
            myPlot.once('plotly_doubleclick', function() {
                Plotly.restyle(myPlot, {
                    'marker.opacity': 1,
                    'textfont.opacity': 1,
                    'line.opacity': 1,
                    'marker.size': originalSizes
                });
            });
        });

        myPlot.on('plotly_doubleclick', resetView);
    </script>
</body>
</html>
"""

# Add neighbors dictionary to pass to template
@app.route("/")
def index():
    # Create neighbors dictionary
    neighbors = {node: list(G.neighbors(node)) for node in G.nodes()}
    return render_template_string(
        html_template,
        graphJSON=graphJSON,
        nodeRanking=nodeRanking,
        central_keywords=central_keywords,
        neighbors=neighbors
    )

if __name__ == '__main__':
    # Disable the reloader to prevent SystemExit from extra processes.
    app.run(debug=True, use_reloader=False, port=3001)
