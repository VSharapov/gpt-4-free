#!/bin/sh

# Create a virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
  echo "Creating virtual environment..."
  virtualenv venv
fi

# Activate the virtual environment
echo "Activating virtual environment..."
. venv/bin/activate

# Install required Python packages
echo "Installing required Python packages..."
pip install -r requirements.txt

# Create OPENAI_API_KEY.env if it doesn't exist
if [ ! -f "OPENAI_API_KEY.env" ]; then
  echo "Creating OPENAI_API_KEY.env ..."
  touch OPENAI_API_KEY.env
  echo "OPENAI_API_KEY=" >> OPENAI_API_KEY.env

  # Open the OPENAI_API_KEY.env file in an editor
  ${EDITOR:-vi} OPENAI_API_KEY.env
fi

# Done
echo "Setup complete. To activate the virtual environment, run the following command:"
echo ". venv/bin/activate"