import cv2

img = cv2.imread('C:\\davabase\\Code\\computer_vision\\Computer-Vision-with-Python\\Computer-Vision-with-Python\\DATA\\00-puppy.jpg')

while True:

    cv2.imshow('Puppy',img)

    # IF we've waited at least 1 millesecond AND we've pressed the Esc key
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
        