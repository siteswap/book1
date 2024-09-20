#!/bin/bash

# Script to generate images for the Sunset Quest game using OpenAI's Image Generation API

# Ensure the OPENAI_API_KEY environment variable is set
if [ -z "$OPENAI_API_KEY" ]; then
  echo "Error: The OPENAI_API_KEY environment variable is not set."
  echo "Please export your API key as an environment variable and try again."
  echo "Example: export OPENAI_API_KEY='your-api-key-here'"
  exit 1
fi

# Create the img directory if it doesn't exist
OUTPUT_DIR="img"
mkdir -p "$OUTPUT_DIR"

# Declare an associative array with filenames as keys and prompts as values
declare -A scenes=(
  ["scene_start.jpg"]="An abstract landscape at sunset with vivid colors transitioning from orange to purple; a dark green tree with flowing branches on the right, a dark brown rocky formation on the left, and a small dark bird flying overhead"
  ["scene_followBird.jpg"]="Following a small dark bird towards a glowing horizon with a partially visible sun; a path leading into distant mountains under a colorful sky"
  ["scene_exploreTree.jpg"]="Close-up of a dark green abstract tree with flowing branches that seem to whisper, set against a vivid sunset sky"
  ["scene_mountainPath.jpg"]="A path winding into mountains under a deepening sky, with cooler colors and a cave entrance appearing ahead"
  ["scene_birdFlight.jpg"]="The small dark bird flying higher into a bright sun, the sky beginning to darken as it ascends"
  ["scene_climbTree.jpg"]="View from atop the abstract tree, overlooking a vast landscape with a hidden valley revealed behind rocky formations"
  ["scene_listenWhispers.jpg"]="Close-up of the tree's bark with ethereal whispers represented as subtle glowing patterns, under a colorful sky"
  ["scene_enterCave.jpg"]="Inside a cave illuminated by glowing crystals, ancient drawings depicting a portal on the walls"
  ["scene_turnBack.jpg"]="An unfamiliar shifting landscape with vanishing paths under a surreal sky, a sense of being lost"
  ["scene_waitBird.jpg"]="Night falls over the landscape, the bird returns transformed into a luminous creature emitting a gentle glow"
  ["scene_seekShelter.jpg"]="A small cozy cabin near a rocky formation, warm light from the windows contrasting with the darkening sky"
  ["scene_acceptOffer.jpg"]="A realm of endless sunsets with vivid colors, the luminous creature guiding you through a breathtaking landscape"
  ["scene_declineOffer.jpg"]="The creature vanishing into thin air, the world around fading into darkness, symbolizing the end of the journey"
)

# Check if 'jq' is installed for JSON parsing
if ! command -v jq &> /dev/null; then
  echo "Error: 'jq' is not installed. Please install it to run this script."
  echo "On Ubuntu/Debian: sudo apt-get install jq"
  echo "On macOS: brew install jq"
  exit 1
fi

echo "Starting image generation..."

# Loop through each scene and generate the image
for filename in "${!scenes[@]}"; do
  prompt="${scenes[$filename]}"
  echo "Generating image for $filename..."

  # Make the API request to generate the image
  response=$(curl -s https://api.openai.com/v1/images/generations \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    -d '{
      "prompt": "'"${prompt//\"/\\\"}"'",
      "n": 1,
      "size": "1024x1024"
    }')

  # Check if the response contains an error
  if echo "$response" | jq -e '.error' > /dev/null; then
    error_message=$(echo "$response" | jq -r '.error.message')
    echo "Error generating image for $filename: $error_message"
    continue
  fi

  # Extract the image URL from the response
  url=$(echo "$response" | jq -r '.data[0].url')

  # Check if the URL is valid
  if [ -z "$url" ] || [ "$url" == "null" ]; then
    echo "Failed to retrieve image URL for $filename."
    continue
  fi

  # Download the image
  curl -s "$url" -o "$OUTPUT_DIR/$filename"
  echo "Downloaded $filename to $OUTPUT_DIR/$filename"
done

echo "Image generation completed."

