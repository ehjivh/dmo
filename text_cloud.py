import os
import glob
import markdown
from collections import Counter
import networkx as nx
from itertools import combinations

import matplotlib.pyplot as plt

def extract_text_from_markdown(file_path):
	with open(file_path, 'r', encoding='utf-8') as file:
		text = file.read()
	html = markdown.markdown(text)
	return html

def get_words(text):
	words = text.split()
	return [word.strip('.,!?()[]{}<>:;\'"') for word in words if word.isalpha()]

def build_cooccurrence_network(words, window_size=2):
	G = nx.Graph()
	for i in range(len(words) - window_size + 1):
		window = words[i:i + window_size]
		for word1, word2 in combinations(window, 2):
			if G.has_edge(word1, word2):
				G[word1][word2]['weight'] += 1
			else:
				G.add_edge(word1, word2, weight=1)
	return G

def plot_network(G):
	pos = nx.spring_layout(G)
	weights = [G[u][v]['weight'] for u, v in G.edges()]
	nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color=weights, width=2.0, edge_cmap=plt.cm.Blues)
	plt.show()

def main():
	md_folder = 'md'
	all_words = []
	for md_file in glob.glob(os.path.join(md_folder, '*.md')):
		text = extract_text_from_markdown(md_file)
		words = get_words(text)
		all_words.extend(words)
	
	word_counts = Counter(all_words)
	common_words = [word for word, count in word_counts.items() if count > 1]
	
	G = build_cooccurrence_network(common_words)
	plot_network(G)

if __name__ == "__main__":
	main()