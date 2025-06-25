import cv2
import mediapipe as mp
import random
import time

# Initialize MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Constants
WIDTH, HEIGHT = 800, 600

class Fruit:
    def __init__(self):
        self.x = random.randint(100, WIDTH - 100)
        self.y = 0
        self.speed = random.randint(5, 10)
        self.r = 30
        self.color = (0, 255, 0)  # Green (safe) by default
        self.is_bad = False
        if random.random() < 0.2:  # 20% chance to be red (bad)
            self.color = (0, 0, 255)
            self.is_bad = True
        self.alive = True

    def move(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.alive = False

    def draw(self, frame):
        cv2.circle(frame, (self.x, self.y), self.r, self.color, -1)

    def is_sliced(self, point):
        px, py = point
        return (self.x - px) ** 2 + (self.y - py) ** 2 < self.r ** 2

def run_game():
    cap = cv2.VideoCapture(0)
    cap.set(3, WIDTH)
    cap.set(4, HEIGHT)

    fruits = []
    score = 0
    last_spawn = time.time()
    game_over = False

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        fingertip = None
        if result.multi_hand_landmarks:
            for hand in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)
                tip = hand.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                h, w, _ = frame.shape
                fingertip = (int(tip.x * w), int(tip.y * h))
                cv2.circle(frame, fingertip, 10, (255, 0, 255), -1)

        if time.time() - last_spawn > 1 and not game_over:
            fruits.append(Fruit())
            last_spawn = time.time()

        for fruit in fruits:
            fruit.move()
            if fingertip and fruit.is_sliced(fingertip):
                fruit.alive = False
                if fruit.is_bad:
                    game_over = True
                else:
                    score += 1
            if fruit.alive:
                fruit.draw(frame)

        fruits = [f for f in fruits if f.alive]

        cv2.putText(frame, f'Score: {score}', (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 200, 255), 3)

        if game_over:
            cv2.putText(frame, "Game Over!", (WIDTH // 2 - 150, HEIGHT // 2),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)
            cv2.putText(frame, "Press 'r' to play again or 'q' to quit",
                        (WIDTH // 2 - 250, HEIGHT // 2 + 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

        cv2.imshow("Fruit Slicer", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            break
        if game_over and key == ord('r'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return key

def main():
    while True:
        key = run_game()
        if key != ord('r'):
            print("Thanks for playing! 🍉")
            break

main()
