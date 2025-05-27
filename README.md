🚀 AWS Resource Dashboard



A real-time AWS Resource Monitoring Dashboard built with Flask and HTML/CSS/JS, enabling you to visualize and manage EC2, RDS, Lambda, and ECS resources from a single intuitive UI.

🎥 Demo

https://drive.google.com/file/d/1zFCuyO6-zjOJd8AaygI_XuP_0PWiBtIz/view?usp=drive_link 

📸 UI Snapshot

![Screenshot 2025-05-27 160113](https://github.com/user-attachments/assets/e3da1b81-b578-4d89-b3b3-1e5b890b0432)


🧠 Features

🌐 Real-time resource monitoring via REST API

💽 EC2 instance status display

🟔 RDS instance monitoring

⚙️ Lambda function listing

🧵 ECS cluster details

🔁 Refresh resource status dynamically from UI

🌈 Fully responsive and elegant front-end interface

🛠️ Tech Stack

Backend: Python, Flask, Boto3

Frontend: HTML, CSS (with custom styling), JavaScript

Deployment Ready: Docker-compatible Flask server (localhost:5000)

📁 Project Structure

├── aws_monitor.py              # Flask API server
├── index.html                  # Frontend UI
├── README.md                   # Project documentation
├── tempCodeRunnerFile.py       # Temporary Flask-CORS reference
├── data-center-image.webp      # Background image for the UI

⚙️ Setup Instructions

🐍 Backend

Install dependencies

pip install flask boto3 flask-cors

Run the Flask server

python aws_monitor.py

The API will be available at http://localhost:5000/aws-resources

🌐 Frontend

Open index.html in any modern browser.

Ensure backend (aws_monitor.py) is running before interacting with the UI.

📡 API Endpoint

Endpoint

Method

Description

/aws-resources

GET

Returns all AWS resource statuses

Sample Response:

{
  "EC2": [{"id": "i-012345", "type": "t2.micro", "state": "running"}],
  "RDS": [{"id": "mydb", "state": "available"}],
  "Lambda": [{"name": "my-function", "state": "Active"}],
  "ECS": [{"name": "cluster-name", "status": "ACTIVE"}]
}

🙇‍♂️ Author

Kunal Guha📧 [kunalguh2003@gmail.com]  🔗 LinkedIn/GitHub/Portfolio

📃 License

This project is licensed under the MIT License.

✨ Have suggestions or improvements? Feel free to fork and PR!
