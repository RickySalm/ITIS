import requests
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from wordcloud import WordCloud
from urllib.parse import urlparse
import random
import time
limit = 100
start = '????'


def get_data(start_link):

	def valid_link(parsed_text):
		if bool(parsed_text.netloc) and bool(parsed_text.scheme):
			if connects:
				for el in connects:
					if parsed_text.netloc + parsed_text.path in el:
						return False
			return True
		return False
	connects = []
	domains = []

	def main(start_link):
		link = start_link
		if len(domains) < limit:
			try:
				total_requests = requests.get(link).text
			except:
				return None
			# print(f'стартовая ссылка {link}')
			page = ''.join(total_requests)
			soup = BeautifulSoup(page, 'lxml')

			parsed_main_link = urlparse(link)
			list_links = []
			for teg in soup.find_all('a'):
				link = teg.attrs.get('href')
				parsed_link = urlparse(link)
				if valid_link(parsed_link):
					print(link)
					# print(parsed_link)
					list_links.append(parsed_link)
			# print(list_links)
			# print(len(list_links))
			if len(list_links) < 11:
				for link in list_links:
					connects.append((parsed_main_link.netloc + parsed_main_link.path, link.netloc + link.path))
					domains.append(link.netloc)
			else:
				list_links = random.sample(list_links, 10)
				for link in list_links:
					connects.append((parsed_main_link.netloc + parsed_main_link.path, link.netloc + link.path))
					domains.append(link.netloc)
			# print('выборка отработала')
			for link in list_links:
				# print('в линке есть значения и он пошел выполняться дальше')
				main(link.scheme + '://' + link.netloc + link.path + link.params)
				# print('я сделяль :)')
			else:
				print('он пуст :/')
		else:
			print(len(domains))
			print('мы закончили))')
			return None
	main(start_link)
	return connects, domains


def domain_cloud(domains):
	"""
	Draw the cloud of words
	Args:
		domains (list of str): ['domain1', 'domain2'...]
	"""
	word_string = ' '.join(domains)
	params = dict(background_color="white", width=1200, height=1000, max_words=len(set(domains)))
	wordcloud = WordCloud(**params).generate(word_string)
	plt.imshow(wordcloud)
	plt.show()


def graph(connections, with_labels=True):
	"""
	Draw the graph based on a connections
	Args:
		connections (list of tuple): [(A, B), (B, C)...] links from A to B, B to C, etc
		with_labels (bool): plot the labels or not
	"""
	g = nx.Graph()
	g.add_edges_from(connections)
	nx.draw(g, verticalalignment='bottom', horizontalalignment='center', with_labels=False, node_size=30)
	# nx.draw(g, verticalalignment='bottom', horizontalalignment='center', with_labels=with_labels, node_size=30)
	plt.show()


s = time.time()
conn, dom = get_data('https://www.youtube.com/')
e = time.time()
print(e-s)
graph(conn)
domain_cloud(dom)
