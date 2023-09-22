{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOcxDDZmOv6uHcYOsoRyihf",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/sruthi7868/sruthi7868/blob/main/data_flow_diagram.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "gNV1Q_jN489-"
      },
      "outputs": [],
      "source": [
        "python\n",
        "import graphviz\n",
        "\n",
        "# Create a new Graphviz object\n",
        "graph = graphviz.Digraph()\n",
        "\n",
        "# Add nodes to the graph\n",
        "graph.node('Input Data')\n",
        "graph.node('Initialization')\n",
        "graph.node('Evaluation')\n",
        "graph.node('Party Formation')\n",
        "graph.node('Party Leaders')\n",
        "graph.node('Position Update')\n",
        "graph.node('Constituency Allocation')\n",
        "graph.node('Constituency Winners')\n",
        "graph.node('Position Update (Recent Past-Based)')\n",
        "graph.node('Termination Criteria')\n",
        "graph.node('Output')\n",
        "\n",
        "# Add edges between nodes\n",
        "graph.edge('Input Data', 'Initialization')\n",
        "graph.edge('Initialization', 'Evaluation')\n",
        "graph.edge('Evaluation', 'Party Formation')\n",
        "graph.edge('Party Formation', 'Party Leaders')\n",
        "graph.edge('Party Leaders', 'Position Update')\n",
        "graph.edge('Position Update', 'Constituency Allocation')\n",
        "graph.edge('Constituency Allocation', 'Constituency Winners')\n",
        "graph.edge('Constituency Winners', 'Position Update (Recent Past-Based)')\n",
        "graph.edge('Position Update (Recent Past-Based)', 'Termination Criteria')\n",
        "graph.edge('Termination Criteria', 'Output')\n",
        "\n",
        "# Render and save the graph as an image file\n",
        "graph.render('data_flow_diagram', format='png', view=True)\n"
      ]
    }
  ]
}