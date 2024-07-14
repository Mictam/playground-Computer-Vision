#!/bin/bash

chmod +x set_openai_api_key.sh

SHELL_PROFILE=""

if [ -n "$ZSH_VERSION" ]; then
    SHELL_PROFILE="$HOME/.zshrc"
elif [ -n "$BASH_VERSION" ]; then
    SHELL_PROFILE="$HOME/.bashrc"
else
    echo "Unsupported shell. Please add the API key to your shell profile manually."
    exit 1
fi

source ./set_openai_api_key.sh

source $SHELL_PROFILE


if [ -z "$OPENAI_API_KEY" ]; then
    echo "Failed to set the OpenAI API key. Please check your setup."
    exit 1
else
    echo "OpenAI API key has been successfully set."
fi
