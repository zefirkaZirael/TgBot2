import cv2

def process_image(image_path, output_path):
    # Загрузка предобученного классификатора для детектирования лиц
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Загрузка изображения
    image = cv2.imread(image_path)
    if image is None:
        print("Ошибка загрузки изображения")
    # Преобразование изображения в оттенки серого для улучшения производительности детектора
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Обнаружение лиц в изображении
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))


    # Размытие области вокруг каждого обнаруженного лица
    for (x, y, w, h) in faces:
        # Извлечение области лица
        face_region = image[y:y+h, x:x+w]

        # Применение размытия
        blurred_face = cv2.GaussianBlur(face_region, (99, 99), 30)

        # Замена области лица размытым изображением
        image[y:y+h, x:x+w] = blurred_face

    # Сохранение обработанного изображения
    cv2.imwrite(output_path, image)


def capture_video():
    # Открываем первый подключенный источник видео (обычно это веб-камера)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Ошибка: Не удалось открыть камеру.")
        return

    # Загрузка предобученного классификатора для обнаружения лиц
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while True:
        # Захват кадра
        ret, frame = cap.read()

        if not ret:
            print("Ошибка: Не удалось захватить кадр.")
            break

        # Преобразование изображения в серые оттенки для улучшения производительности детектора
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Обнаружение лиц
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Размытие лица и отрисовка прямоугольников вокруг лиц
        for (x, y, w, h) in faces:
            # Извлечение области лица
            face_region = frame[y:y+h, x:x+w]

            # Применение размытия
            blurred_face = cv2.GaussianBlur(face_region, (99, 99), 30)

            # Замена области лица на размытое изображение
            frame[y:y+h, x:x+w] = blurred_face

            # Отображение прямоугольника вокруг обнаруженного лица
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Отображение кадра с размазанными лицами
        cv2.imshow('Видео с камеры', frame)

        # Выход при нажатии клавиши 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Освобождение ресурсов
    cap.release()
    cv2.destroyAllWindows()

# Запуск функции захвата видео
capture_video()
# Проверяем работу кода
#process_image("face.png", "output.png")
