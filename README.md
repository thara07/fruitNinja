🍉 Fruit Slicer Game with Hand Tracking
A fun, real-time computer vision game powered by MediaPipe and OpenCV. Use your index finger to slice the falling fruits. Green fruits give you points, but beware of the red ones—they end the game!

🎮 Features
Hand tracking using MediaPipe Hands

Real-time fruit slicing with finger gestures

Dynamic fruit spawning and game loop

Score tracking with Game Over and replay functionality

Simple and engaging visual feedback
____________________________________________

📦 Requirements
Python 3.7+

OpenCV

MediaPipe
____________________________________________

Install dependencies with:

bash
pip install opencv-python mediapipe
🚀 How to Run
Run the game using:

bash
python fruit_slicer.py
Controls
Move your index finger in front of the webcam to slice fruits.

Press q to quit.

After game over, press r to restart.
_____________________________________________

🧠 How It Works
MediaPipe tracks your index fingertip.

Fruits fall from the top of the screen at random positions and speeds.

Touching (slicing) a fruit:

✅ Green fruit: +1 point

❌ Red fruit: ends the game

✏️ Code Overview
Fruit class handles fruit state, position, and behavior.

run_game() sets up the game loop and detects collision with the fingertip.

Game loop resets when the player chooses to replay.

📸 Screenshot
Coming soon! (Feel free to add an in-game screenshot here.)

🙏 Acknowledgements
MediaPipe for real-time hand tracking

OpenCV for video and drawing utilities
