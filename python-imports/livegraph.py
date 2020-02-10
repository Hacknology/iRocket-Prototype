import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from threading import Thread
from random import randrange
from time import sleep

#Gönlümü süsler hayalinin berdevam yolu
#Kutsal yüzün ki bir gece yıldızlara dolu

style.use("fivethirtyeight")
def thread1():
	sleep(3)
	fig = plt.figure()
	ax1 = fig.add_subplot(1,1,1)

	def animate(i):
		
		graph_data = open('heights.txt','r').read()
		lines = graph_data.split('\n')
		xs = []
		ys = []
		for line in lines:

			if len(line) > 1:
				x, y = line.split(',')
				xs.append(float(x))
				ys.append(float(y))
		ax1.clear()
		ax1.plot(xs, ys, 'ro')
	ani = animation.FuncAnimation(fig, animate, interval=1000)
	plt.show()

def thread2():
	i=1
	while 1:

		heights = randrange(20)
		text_to_write = str(i) + "," + str(heights) + "\n"

		file = open("heights.txt","a")
		file.write(text_to_write)
		file.close()

		i +=1
		sleep(3)
def run():
	Thread(target=thread2).start()
	Thread(target=thread1).start()

