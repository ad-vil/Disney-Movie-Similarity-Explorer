# Disney Movie Similarity Explorer


## Overview
This Python script offers a comprehensive toolset to explore similarities between Disney movies. It leverages CSV data containing Disney movie titles to build a graph, where each movie is represented as a node, and edges denote similarity. The script provides three search algorithms: breadth-first search, depth-first search, and uniform cost search, enabling users to find paths between two given movies based on their similarity. Additionally, it visualizes the movie similarity graph using the NetworkX library to offer an intuitive understanding of the relationships between Disney movies.

## Features
#### - Data Loading: Loads Disney movie data from a CSV file.
#### - Graph Generation: Generates a graph representing movie similarities.
#### - Breadth-First Search: Finds paths between movies using a breadth-first traversal approach.
#### - Depth-First Search: Searches for paths between movies using a depth-first traversal technique.
#### - Uniform Cost Search: Finds paths between movies with the lowest accumulated cost.
#### - Visualization: Utilizes NetworkX to visualize the movie similarity graph, offering an intuitive representation of movie relationships.
#### - User Interaction: Prompts users to input two movie titles and displays the results of each search algorithm.
#### - Error Handling: Provides robust error handling for user inputs, ensuring smooth execution.
#### - Modular Design: Utilizes object-oriented programming principles to maintain a clean and modular codebase, enhancing readability and extensibility.
#### - Documentation: Includes detailed docstrings for classes and methods to facilitate code understanding and maintenance.

## Usage
#### - Clone the Repository: Clone the repository to your local machine.
#### - Install Dependencies: Install the required dependencies listed in the requirements.txt file using pip install -r requirements.txt.
#### - Run the Script: Run the main.py script using Python.
#### - Follow On-Screen Instructions: Follow the on-screen instructions to input two Disney movie titles.
#### - View Results: View the results of each search algorithm and explore the movie similarity graph visualization.

## Dependencies
#### - Python 3.x
#### - NetworkX
#### - Matplotlib
#### - CSV
