import math
import cv2
import cvzone
from cvzone.ColorModule import ColorFinder
import numpy as np
import matplotlib.pyplot as plt

# Initialize the Video
cap = cv2.VideoCapture('Videos/vid (4).mp4')

# Create the color Finder object
myColorFinder = ColorFinder(False)
hsvVals = {'hmin': 8, 'smin': 96, 'vmin': 115, 'hmax': 14, 'smax': 255, 'vmax': 255}

# Variables
posListX, posListY = [], []
xList = [item for item in range(0, 1300)]
prediction = False

# Initialize plot
plt.ion()
fig, ax = plt.subplots()
scatter_plot, = ax.plot([], [], 'go')
regression_plot, = ax.plot([], [], 'm--')
ax.set_xlim(0, 1300)
ax.set_ylim(800, 0)  # Inverted Y for image-like display
ax.set_title('Live Ball Trajectory')
ax.set_xlabel('X Position')
ax.set_ylabel('Y Position')

def update_plot():
    scatter_plot.set_data(posListX, posListY)
    if len(posListX) > 2:
        A, B, C = np.polyfit(posListX, posListY, 2)
        y_vals = [A * x ** 2 + B * x + C for x in xList]
        regression_plot.set_data(xList, y_vals)
    fig.canvas.draw()
    fig.canvas.flush_events()

while True:
    success, img = cap.read()
    if not success:
        break

    img = img[0:900, :]

    imgColor, mask = myColorFinder.update(img, hsvVals)
    imgContours, contours = cvzone.findContours(img, mask, minArea=500)

    if contours:
        posListX.append(contours[0]['center'][0])
        posListY.append(contours[0]['center'][1])

    if posListX:
        A, B, C = np.polyfit(posListX, posListY, 2)

        for i, (posX, posY) in enumerate(zip(posListX, posListY)):
            pos = (posX, posY)
            cv2.circle(imgContours, pos, 10, (0, 255, 0), cv2.FILLED)
            if i > 0:
                cv2.line(imgContours, pos, (posListX[i - 1], posListY[i - 1]), (0, 255, 0), 5)

        for x in xList:
            y = int(A * x ** 2 + B * x + C)
            cv2.circle(imgContours, (x, y), 2, (255, 0, 255), cv2.FILLED)

        if len(posListX) < 10:
            a = A
            b = B
            c = C - 590
            x = int((-b - math.sqrt(b ** 2 - (4 * a * c))) / (2 * a))
            if 330 < x < 430:
                prediction = True

        if prediction:
            cvzone.putTextRect(imgContours, "Basket", (50, 150),
                               scale=5, thickness=5, colorR=(0, 200, 0), offset=20)
        else:
            cvzone.putTextRect(imgContours, "No Basket", (50, 150),
                               scale=5, thickness=5, colorR=(0, 0, 200), offset=20)

    update_plot()

    imgContours = cv2.resize(imgContours, (0, 0), None, 0.7, 0.7)
    cv2.imshow("Prediction", imgContours)
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
