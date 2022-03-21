import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

symbols = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. " # 70 уровней цвета
# symbols = symbols[::-1]

"""
# Гифку в символы?! Легко
# а потом это обратно в гифку или вывести в терминал :)
gif = Image.open('test.gif')
frames = gif.n_frames  # кол-во кадров
for frame in range(frames):
    gif.seek(frame)
    # .....
"""


def img2array(path, width=None):
	"""
	На вход принимает путь к картинке и превращает её в 3х мерный массив пикселей (X, Y, цвет).
	Пиксель закодирован тремя цветами RGB (красным, зеленым и синим).
	Args:
		path (str): путь к файлу
		width (int): желаемая ширина
	Returns:
		list: 3х-мерный список пикселей
	"""
	with Image.open(path) as img:
		# размеры текущего изображения (размеры "матрицы")
		orig_width, orig_height = img.size
		if width:
			# вычисление масштаба, по указанной ширине
			scale = width / orig_width
			# вычисление новой высоты по масштабу, обязательно int, кол-во пикселей не может быть float
			height = int(scale * orig_height)
		else:
			width, height = orig_width, orig_height
		# изменение размера изображение
		img.thumbnail((width, height))
		# показать, что вышло
		plt.imshow(img)
		plt.show()
		# вернуть данные как наш любимый список :)
		return np.asarray(img).tolist(), width, height


def pixel2symbol(pixels, width, height):
	"""
	На вход принимает 3х-мерный список пикселей, возвращает 2х-мерную матрицу того же размера,
	где вместо пикселя один символ
	Args:
		pixels (list): 3х-мерный список пикселей
		height (int): высота
		width (int): ширина
	Returns:
		list: список символов
	"""
	# коэф. для сопастовление среднего значения цвета и элемента ASCII
	ratio = 255 / 70
	# создается двумерный список для арта
	ascii_art = [[' ' for i in range(width)] for j in range(height)]
	# проходимся по каждому элементу в списке пикселей
	for h in range(height):
		for w in range(width):
			# собираем значения цветов пикселя
			red = pixels[h][w][0]
			green = pixels[h][w][1]
			blue = pixels[h][w][2]
			# вычисляем среднее значение цвета
			color_value = (red + green + blue)/3
			symbol_ascii = int((color_value / ratio)-1)
			ascii_art[h][w] = symbols[symbol_ascii]
	return ascii_art



def save_art(ascii_art, path):
	"""
	Сохранить арт как картинку, просто написал :)
	Args:
		ascii_art (list): 2х-мерный массив символов
		path (str): куда сохранять
	"""
	font = {'family': 'monospace',
	        'color': 'black',
	        'weight': 'normal',
	        'size': 4}
	width, height = len(ascii_art[0]), len(ascii_art)
	plt.plot(0, 0, '.', color='w')
	plt.plot(width, height, '.', color='w')
	# per row
	for y, row in enumerate(ascii_art[::-1]):
		# per symbol in row (per column)
		for x, symbol in enumerate(row):
			plt.text(x=x, y=y, s=symbol, fontdict=font)
	plt.savefig(f'{path}_new.jpg', format='jpg', dpi=200)


def main():
	# путь к файла
	# img_path = "/home/alex/Downloads/risovach.ru (3).jpg"
	img_path = 'C:/Users/124/Desktop/d9omjYWcCL0.jpg'
	# пикчу в список пикселей
	pixels_matrix, w, h = img2array(img_path)
	# пиксели в символы
	art = pixel2symbol(pixels_matrix, w, h)
	# отрисовка символов обратно в картинку :D (можно просто вывести на экран)
	save_art(art, path='C:/Users/124/Desktop/art_peppa.jpg')
	
	
if __name__ == "__main__":
	main()	





