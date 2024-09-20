#!/usr/bin/env python3

import os
from pathlib import Path
import openai

# Ensure the 'audio' directory exists
OUTPUT_DIR = Path('audio')
OUTPUT_DIR.mkdir(exist_ok=True)

# Ensure the OPENAI_API_KEY environment variable is set
api_key = os.environ.get('OPENAI_API_KEY')
if not api_key:
    print("Error: The OPENAI_API_KEY environment variable is not set.")
    print("Please export your API key as an environment variable and try again.")
    exit(1)

openai.api_key = api_key

# Define the scenes with their text content
scenes = {
    'scene_start.mp3': "You find yourself at the edge of a serene landscape, the sky ablaze with hues of orange, yellow, and red transitioning into pink and purple. A dark green tree with flowing branches stands to your right, and a rocky formation looms to your left. A small bird flies overhead. Do you wish to follow the bird or explore the tree?",
    'scene_followBird.mp3': "You decide to follow the bird. It leads you towards the glowing horizon where the sun is partially visible. As you approach, you notice a path leading into the mountains. Do you take the mountain path or continue following the bird?",
    'scene_exploreTree.mp3': "You walk towards the abstract tree. Its branches seem to whisper ancient secrets. As you touch the bark, you feel a surge of energy. Do you climb the tree or listen to the whispers?",
    'scene_mountainPath.mp3': "You take the path into the mountains. The air grows cooler, and the colors of the sky deepen. Suddenly, you reach a cave entrance. Do you enter the cave or turn back?",
    'scene_birdFlight.mp3': "You continue to follow the bird, but it flies higher until it disappears into the sun. You're left standing alone as the sky darkens. Do you wait for the bird to return or seek shelter?",
    'scene_climbTree.mp3': "You climb the tree and reach a vantage point where the entire landscape unfolds before you. You see a hidden valley behind the rocky formation. Do you descend towards the valley or stay in the tree?",
    'scene_listenWhispers.mp3': "You listen closely, and the whispers reveal a riddle about the sun and moon. Solving it could grant you a wish. Do you attempt to solve the riddle or ignore it?",
    'scene_enterCave.mp3': "Inside the cave, you find glowing crystals that illuminate ancient drawings. The drawings depict a portal. Do you touch the crystals or study the drawings?",
    'scene_turnBack.mp3': "You decide to turn back, but the path has vanished. The landscape shifts, and you're now in an unfamiliar place. Do you call out for help or try to find a new path?",
    'scene_waitBird.mp3': "You wait patiently, and as night falls, the bird returns, transforming into a luminous creature. It offers to guide you to a place of wonder. Do you accept its offer?",
    'scene_seekShelter.mp3': "You seek shelter and find a small cabin near the rocky formation. Inside, there's a warm fire and a mysterious book. Do you read the book or rest by the fire?",
    'scene_hiddenValley.mp3': "You descend into the hidden valley, where time seems to stand still. Do you explore the ancient ruins or rest by the sparkling lake?",
    'scene_stayTree.mp3': "You decide to stay in the tree, enjoying the serene view. As the sun sets, you feel at peace. The End.",
    'scene_solveRiddle.mp3': "You attempt to solve the riddle. As you speak the answer, the landscape transforms, and your wish is granted. The End.",
    'scene_ignoreRiddle.mp3': "You choose to ignore the whispers. The tree's energy fades, and you return to where you started. The adventure ends here. The End.",
    'scene_touchCrystals.mp3': "You touch the crystals, and a portal opens. You're transported to a new world filled with wonders. The End.",
    'scene_studyDrawings.mp3': "You study the drawings and learn the secrets of the ancients. You gain wisdom beyond measure. The End.",
    'scene_callHelp.mp3': "You call out for help, and an echo responds. A mysterious figure appears to guide you back. The End.",
    'scene_newPath.mp3': "You try to find a new path and discover hidden wonders you never imagined. The adventure continues.",
    'scene_acceptOffer.mp3': "You accept the creature's offer and are taken to a realm of endless sunsets. You've found a place of eternal beauty. The End.",
    'scene_declineOffer.mp3': "You decline, and the creature vanishes. You're left alone as the world around you fades. The adventure ends here. The End.",
    'scene_readBook.mp3': "You read the mysterious book and unlock secrets of the universe. Knowledge fills your mind. The End.",
    'scene_restFire.mp3': "You rest by the fire, feeling warmth and comfort. You drift into a peaceful sleep. The End.",
    'scene_exploreRuins.mp3': "You explore the ancient ruins and uncover artifacts of immense power. Your journey has just begun.",
    'scene_restLake.mp3': "You rest by the sparkling lake, and its waters rejuvenate you. A sense of tranquility envelops you. The End.",
    'scene_followNewPath.mp3': "You follow the new path and find yourself back at the starting point, but with a newfound appreciation for the journey. The End.",
    'scene_restWait.mp3': "You decide to rest and wait. As you relax, the environment around you changes subtly. The adventure ends here. The End."
}

print("Starting audio generation using OpenAI Text-to-Speech API...")

for filename, text in scenes.items():
    print(f"Generating audio for {filename}...")

    # Prepare the output file path
    speech_file_path = OUTPUT_DIR / filename

    try:
        # Generate the speech
        response = openai.audio.speech.create(
            model="tts-1",
            voice="alloy",  # Adjust the voice as needed
            input=text
        )

        # Save the audio to a file
        response.stream_to_file(speech_file_path)
        print(f"Saved {filename} to {speech_file_path}")

    except Exception as e:
        print(f"Error generating audio for {filename}: {e}")

print("Audio generation completed.")

