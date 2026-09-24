import cv2
import numpy as np
import turtle

image_path = 'sitaram.jpg'
img = cv2.imread(image_path)

if img is None:
    print("Error: 'sitaram.jpg' nahi mili! Check karein ki photo sahi folder me hai.")
    exit()

# Aspect ratio setup
width, height = 550, 720
img = cv2.resize(img, (width, height))

# Grayscale & Blur
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3, 3), 0)

# Canny Edge Detection tuned for clean silhouettes
edges = cv2.Canny(blur, 40, 140)

# Extract contours
contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# Screen setup (Pure Black Background like your video)
screen = turtle.Screen()
screen.setup(width=720, height=850)
screen.bgcolor("black")
screen.title("Python Line Sketch Drawing")
turtle.colormode(255)

# Turtle Cursor setup
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.shape("classic")
t.showturtle()
t.pensize(1.8)

# Smooth drawing speed
screen.tracer(2)

print("Drawing start ho rahi hai...")

# Sort from bottom-to-top so cursor draws upwards like your video
sorted_contours = sorted(contours, key=lambda c: -np.min(c[:, :, 1]))

for cnt in sorted_contours:
    if len(cnt) < 6:
        continue

    t.penup()
    first_pt = cnt[0][0]

    # Pure white line art sketch
    t.pencolor(255, 255, 255)

    start_x = first_pt[0] - width // 2
    start_y = height // 2 - first_pt[1]

    t.goto(start_x, start_y)
    t.pendown()

    for pt in cnt[1:]:
        x = pt[0][0] - width // 2
        y = height // 2 - pt[0][1]
        t.goto(x, y)

t.penup()
t.goto(width // 2 - 40, -height // 2 + 40)
screen.update()

print("Drawing Complete!")
turtle.done()