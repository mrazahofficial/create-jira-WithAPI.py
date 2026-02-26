GitHub-Jira Automation Bridge
A Python-based automation service hosted on AWS EC2 that integrates GitHub Issue comments with Jira Cloud. It uses a Flask-based REST API to listen for webhooks and triggers ticket creation when a specific command is used.

🌟 Overview
This project automates the transition from "Bug Discussion" to "Project Management." Instead of manually creating tickets, developers can simply type /jira in any GitHub issue comment to instantly generate a Jira ticket containing the issue title, the commenter's name, and a link back to the source.

🛠️ Architecture
Frontend: GitHub Webhooks (Issue Comment events)

Middleware: Flask API running on Python 3.12

Cloud Infrastructure: AWS EC2 (Ubuntu 24.04)

Backend: Jira Cloud REST API v3

🚀 Installation & Setup
1. AWS EC2 Preparation
Ensure your Security Group has Port 5000 open for inbound TCP traffic from 0.0.0.0/0.

2. Environment Setup
To maintain system stability and follow modern Python standards (PEP 668), this project uses a Virtual Environment.

Bash
# Update Ubuntu and install venv
sudo apt update && sudo apt install python3-venv -y

# Create the virtual environment
python3 -m venv myenv

# ACTIVATE the environment (Crucial Step)
source myenv/bin/activate

# Install required dependencies inside the environment
pip install flask requests
3. Configuration
Update the github_jira.py file with your credentials:

Jira URL: https://your-domain.atlassian.net/rest/api/3/issue

Email: Your Atlassian email

API Token: Your Atlassian API Token

Project Key: (e.g., "KAN")

🖥️ Usage
While inside the (myenv), run the script:

Bash
# Run in the background so it stays alive after you exit SSH
nohup python3 github_jira.py &
🔗 Webhook Configuration
In your GitHub Repository:

Go to Settings > Webhooks > Add webhook.

Payload URL: http://<your-ec2-public-ip>:5000/create_jira

Content type: application/json

Which events? Select Issue comments.

🧪 How to Trigger
Open any Issue in your GitHub repository.

Type a comment containing the string: /jira.

Check your Jira board—a new ticket will be created automatically with the GitHub details!

🛡️ Best Practices Applied
Isolation: Used python3-venv to prevent system-wide package corruption.

Binding: Configured Flask to bind to 0.0.0.0 for cloud visibility.

Resilience: Implemented nohup for process persistence.
