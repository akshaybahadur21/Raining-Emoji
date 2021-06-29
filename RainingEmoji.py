import mediapipe as mp
import cv2
from utils.cv_utils import rescale_frame, get_emojis, overlay
from utils.physics_utils import add_emojis_to_space, add_fingers_to_space, create_static_line
import pymunk
import numpy as np


class RainingEmoji:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.emoji_list = get_emojis()
        self.space = pymunk.Space()
        self.emoji_radius = 30
        self.number_of_emojis = 100
        self.fingers_radius = 20
        self.cap = cv2.VideoCapture(0)

    def rain(self):
        self.space.gravity = 0, -500
        emojis = [(600 + np.random.uniform(-300, 300), 400 + 50 * i + 0.5 * i ** 2) for i in
                  range(self.number_of_emojis)]
        emojis_body = [pymunk.Body(100.0, 1666, body_type=pymunk.Body.DYNAMIC) for _ in emojis]
        add_emojis_to_space(self.space, emojis_body, emojis, self.emoji_radius)

        fingers = [pymunk.Body(1000, 16660, body_type=pymunk.Body.KINEMATIC) for _ in range(21)]
        add_fingers_to_space(self.space, fingers, self.fingers_radius)

        create_static_line(self.space, 0, 100, 1200, 100)
        create_static_line(self.space, 0, 100, 0, 800)
        create_static_line(self.space, 1200, 100, 1200, 800)

        with self.mp_hands.Hands(
                min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
            while True:
                success, image = self.cap.read()
                image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
                image.flags.writeable = False
                results = hands.process(image)
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        for i, finger in enumerate(fingers):
                            x = int(hand_landmarks.landmark[i].x * image.shape[1])
                            y = image.shape[0] - int(hand_landmarks.landmark[i].y * image.shape[0])
                            fingers[i].velocity = 20.0 * (x - fingers[i].position[0]), 20.0 * (
                                    y - fingers[i].position[1])

                for i, emoji in enumerate(emojis_body):
                    xb = int(emoji.position[0])
                    yb = int(image.shape[0] - emoji.position[1])
                    image = overlay(image, self.emoji_list[i % len(self.emoji_list)], xb, yb, 60, 60)

                self.space.step(0.02)

                cv2.imshow("Raining Emoji", rescale_frame(image, percent=100))
                if cv2.waitKey(5) & 0xFF == 27:
                    break


if __name__ == '__main__':
    raining_emoji = RainingEmoji()
    raining_emoji.rain()
