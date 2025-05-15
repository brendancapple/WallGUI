# Wall GUI
# Displays an interactive GUI for the NCSSM CS Department Corkboard.



import tkinter as tk
import random

# Apps
class App:
	def __init__(self, name, image_path, app_code):
		self.name = name
		self.image_path = image_path
		self.code = app_code
	
	def run(self, root):
		self.code(root)



def return_home(root, frame):
	frame.destroy()
	create_title(root, tk.Frame(root))

fortune_list = [
		"You have a long, happy life ahead of you...\nUnless you ate the fish last friday.", 
		"Why're ya asking me?",
		"I don't care what you said.\nYou're wrong."
		]

def app_fortune_request(label):
	fortune_index = random.randint(0, len(fortune_list)-1)
	label.config(text=fortune_list[fortune_index])

def app_fortune(root):
	fortune_frame = tk.Frame(root)
	
	fortune_topbar = tk.Frame(fortune_frame)
	fortune_home = tk.Button(fortune_topbar, text="X",
				command=lambda: return_home(root, fortune_frame))
	fortune_label = tk.Label(fortune_topbar, text="READ YOUR FORTUNE!")
	fortune_home.pack(side=tk.LEFT)
	fortune_label.pack(side=tk.RIGHT)

	fortune_mainframe = tk.Frame(fortune_frame)
	fortune_output = tk.Label(fortune_mainframe)
	fortune_request = tk.Button(fortune_mainframe, text="What's My\nFortune?", 
								command=lambda: app_fortune_request(fortune_output))
	tk.Label(fortune_mainframe, text="\n\n").pack()
	fortune_output.pack()
	fortune_request.pack()

	fortune_topbar.pack(side=tk.TOP)
	fortune_mainframe.pack(side=tk.TOP)
	
	fortune_frame.pack()




# General GUI
app_list = [
	App("Fortune", "fortune.png", app_fortune)
	]

def clear_and_run(frame, func):
	frame.destroy()
	func()


def clear_and_open(root, frame, app):
	frame.destroy()
	app.run(root)


def create_apps_menu(root, app_root):
	menu_frame = tk.Frame(root)
	
	menu_topbar = tk.Frame(menu_frame)
	menu_topbar.configure(background="gray")
	menu_title = tk.Label(menu_topbar, text="App Menu")
	menu_return = tk.Button(menu_topbar, text="<", command=menu_frame.destroy)
	menu_title.pack(side=tk.RIGHT)
	menu_return.pack(side=tk.LEFT)
	
	menu_app_list = tk.Frame(menu_frame)
	for app in app_list:
		menu_app_frame = tk.Frame(menu_app_list)
		menu_app_image_file = tk.PhotoImage(file=app.image_path).subsample(50,50)
		menu_app_image = tk.Label(menu_app_frame, image=menu_app_image_file)
		menu_app = tk.Button(menu_app_frame, text=app.name, 
							command=lambda: clear_and_open(app_root, root, app))
		menu_app_image.pack(side=tk.LEFT)
		menu_app.pack(side=tk.RIGHT)
		menu_app_image.menu_app_image_file = menu_app_image_file
		menu_app_frame.pack()
	
	menu_topbar.pack()
	menu_app_list.pack()
	
	menu_frame.pack(side=tk.RIGHT)



def create_title(root, main_frame):
	title_frame = tk.Frame(main_frame)
	
	# Title Labels
	image_wall = tk.PhotoImage(file="wall.png").subsample(5,5)
	main_title = tk.Label(title_frame, text="Wall GUI")
	main_subtitle = tk.Label(title_frame, text= "Brought to You By the Durham CS TA Team")
	main_image = tk.Label(title_frame, image=image_wall)
	
	main_buttons = tk.Frame(title_frame)
	main_button = tk.Button(main_buttons, text="Apps", command=lambda: create_apps_menu(main_frame, root))
	main_exit = tk.Button(main_buttons, text="Exit", command=root.destroy)
	main_button.pack(side=tk.LEFT)
	main_exit.pack(side=tk.RIGHT)
	
	main_title.pack()
	main_subtitle.pack()
	main_image.pack()
	main_buttons.pack()
	
	main_image.image_wall = image_wall
	
	title_frame.pack(side=tk.LEFT)
	main_frame.pack()



# Set up Main Window
root = tk.Tk()

root.title("Wall GUI")
root.configure(background="blue")
root.minsize(200, 200)
root.maxsize(1000, 500)
root.geometry("700x400+50+50") # <width>x<height>+<x>+<y> default screen position

main_frame = tk.Frame(root)
create_title(root, main_frame)

#Start the program
root.mainloop()