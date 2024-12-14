import cv2
import os
import time
import uuid

IMAGEPATH = "Dataset"

labels = ['glasses', 'hat', 'religious_cap']

number_of_images = 10

for label in labels:

    image_path = os.path.join(IMAGEPATH, label)

    if not os.path.exists(image_path):
        os.makedirs(image_path)

        # Open camera
        cap = cv2.VideoCapture(1)
        print(f"Collecting images for {label}")
        time.sleep(3)

        for imgnum in range(number_of_images):
            ret, frame = cap.read()
            imagename = os.path.join(IMAGEPATH, label, label + '.'+ '{}.jpg'.format(str(uuid.uuid1())))
            cv2.imwrite(imagename, frame)
            cv2.imshow('frame', frame)
            time.sleep(2)

            if cv2.waitKey(1) & 0xFF==ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
