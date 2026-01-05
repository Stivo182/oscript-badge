import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# Настройка шрифта
fp = FontProperties(family='Verdana', size=11)

# Создаем фигуру и ось (без отображения)
fig, ax = plt.subplots()
ax.axis('off')  # Отключаем оси

# Список символов для расчета
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 №!@#$%^&*()_+-=[]{}|;:\'",.<>\\|/?`~АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'

# Словарь для хранения ширин
widths = {}

# Получаем рендерер после первого рисования
canvas = fig.canvas
canvas.draw()
renderer = canvas.get_renderer()

for char in chars:
    # Добавляем текст на ось
    text_obj = ax.text(0, 0, char, fontproperties=fp)
    
    # Получаем bounding box (границы текста)
    bbox = text_obj.get_window_extent(renderer=renderer)
    
    # Ширина в пикселях
    width = bbox.width
    
    widths[char] = round(width, 2)
    
    # Удаляем текст, чтобы не накапливать
    text_obj.remove()

# Закрываем фигуру
plt.close(fig)

# Расчет коэффициентов
coefficients = {}
for char, width in widths.items():
    coeff = round(width / 14, 1)
    coefficients[char] = coeff

# Группировка символов по коэффициентам
coeff_groups = {}
for char, coeff in coefficients.items():
    if coeff not in coeff_groups:
        coeff_groups[coeff] = []
    coeff_groups[coeff].append(char)

# Сортировка по коэффициенту (от большего к меньшему)
sorted_coeffs = sorted(coeff_groups.keys(), reverse=True)

# Вывод в формате 1C
print("КоэффициентыШириныСимволов = Новый Соответствие();")
for coeff in sorted_coeffs:
    chars_str = ''.join(coeff_groups[coeff])
    # Экранируем кавычки
    chars_str = chars_str.replace('"', '""')
    print(f'КоэффициентыШириныСимволов.Вставить("{chars_str}", {coeff});')