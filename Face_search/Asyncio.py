import cv2
import time
import os
import asyncio

time_start = time.time()
list_image = ['faces0.jpg', 'faces1.jpg', 'faces2.jpg', 'faces3.jpg', 'faces4.jpg', 'faces5.jpg',
              'faces6.jpg', 'faces7.jpg', 'faces8.jpg', 'faces9.jpg']

async def find_faces(images):
    image_path = images
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    image = cv2.imread(image_path)
    faces_detected = 0

    for i in range(4):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor= 1.1,
            minNeighbors= 30,
            minSize=(4, 4)
        )
        faces_detected += len(faces)
        # Рисуем квадраты вокруг лиц
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 0), 2)
        (h, w, d) = image.shape
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, 90, 1.0)
        image = cv2.warpAffine(image, M, (w, h))
    cv2.imwrite(f"_{images}_processed.jpg", image)
    print(f'На фотографии {images} Лиц обнаружено: {faces_detected}')




async def main():
    os.chdir('face_library')
    tasks = []
    for images in list_image:
        tasks.append(asyncio.create_task(find_faces(images)))

    for task in tasks:
        await task



time_start = time.time()

asyncio.run(main())  #  #запуск основной функции

time_end = time.time()

print(f'Время, затраченное на выполнение программы с использованием Asyncio:, '
      f'{time_end - time_start} сек.') #фиксация времени на получение результатов: 1.07 секунд

