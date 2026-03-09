import tkinter as tk
from tkinter import messagebox, ttk

class UnitConverter:
    def __init__(self, root):
        # root - это главное окно нашего приложения
        self.root = root
        self.root.title("Конвертер физических величин")  # Заголовок окна

        # НАСТРОЙКА ОКНА
        self.root.resizable(True, True) # Изменение размера окна
        self.root.geometry("400x300")
        self.create_menu() # меню
        self.create_widgets() # эл-ты интерфейса



