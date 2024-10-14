from PIL import Image, ImageFilter

# Загружаем изображение
image = Image.open("hopper.jpg")

# Увеличиваем резкость на 5.0
for _ in range(5):
    image = image.filter(ImageFilter.SHARPEN)

# Изменяем размер изображения
new_size = (500, 200)
resized_image = image.resize(new_size)

# Преобразуем в черно-белый
grayscale_image = resized_image.convert("L")

# Сохраняем изображение с увеличенной резкостью, измененным размером и черно-белым эффектом
grayscale_image.save("hopper_sharpened_resized_grayscale.png")