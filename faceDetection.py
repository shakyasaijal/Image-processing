import cv2

cascade = cv2.CascadeClassifier("C:/Users/User/Desktop/python/cascade.xml")

image = cv2.imread("C:/Users/User/Desktop/python/photo.jpg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = cascade.detectMultiScale(gray_image, scaleFactor = 1.05, minNeighbors=5)

print(type(faces))
print(faces)

for x,y,w,h in faces:
    img = cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 3)

cv2.imshow("Title", img)

cv2.waitKey()

cv2.destroyAllWindows()
