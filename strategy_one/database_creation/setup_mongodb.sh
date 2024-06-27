#!/bin/bash

# Install Homebrew if not already installed
if ! command -v brew &> /dev/null
then
    echo "Homebrew not found, installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
    echo "Homebrew already installed"
fi

# Add the MongoDB tap
echo "Adding MongoDB Homebrew tap..."
brew tap mongodb/brew

# Install MongoDB
echo "Installing MongoDB..."
brew install mongodb-community@5.0

# Start MongoDB service
echo "Starting MongoDB service..."
brew services start mongodb/brew/mongodb-community

# Verify installation
echo "Verifying MongoDB installation..."
if command -v mongo &> /dev/null
then
    echo "MongoDB installed successfully"
else
    echo "MongoDB installation failed"
fi

# Install Python dependencies
echo "Installing Python dependencies..."
pip install pymongo

echo "Setup complete"

