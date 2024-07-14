#!/bin/bash

echo "Please enter your OpenAI API key: "
read -s OPENAI_API_KEY

export OPENAI_API_KEY

echo "export OPENAI_API_KEY='$OPENAI_API_KEY'" >> ~/.bashrc
# For zsh users, use ~/.zshrc instead
# echo "export OPENAI_API_KEY='$OPENAI_API_KEY'" >> ~/.zshrc

echo "OpenAI API key has been set and added to your shell profile."