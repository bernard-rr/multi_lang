#!/bin/bash

# Install Python dependencies from requirements.txt
pip install -r requirements.txt

# Create .env file with ACCESS_TOKEN=""
echo "ACCESS_TOKEN=\"\"" > .env

# Install VS Code extension: Google Cloud Code
code --install-extension GoogleCloudTools.cloudcode

# Install Google Cloud SDK
curl https://sdk.cloud.google.com | bash

# Reload VS Code environment (assuming you are in a VS Code terminal)
code .

# Install Google Cloud CLI components
gcloud components install alpha beta skaffold minikube kubectl gke-gcloud-auth-plugin
