🌐 AWS Resource Dashboard



⚡ Monitor, Visualize & Manage Your AWS Resources Like a Pro — in Style.

The AWS Resource Dashboard is a modern, lightweight, and user-centric monitoring tool tailored for developers, DevOps engineers, and system administrators who work with Amazon Web Services. With this dashboard, you can gain a centralized view of your cloud infrastructure — providing real-time visibility into the status of your EC2 instances, RDS databases, Lambda functions, and ECS clusters.

No more switching between AWS service tabs or wrestling with the CLI — this dashboard offers a clean, dynamic, and responsive web interface that brings clarity to your cloud.

Whether you’re managing production workloads or experimenting in a sandbox environment, this tool simplifies your experience, accelerates your insights, and puts control back in your hands.

🎬 Demo Video

🎥 https://drive.google.com/file/d/1zFCuyO6-zjOJd8AaygI_XuP_0PWiBtIz/view?usp=drive_link — See it in action!

🖼️ Dashboard Preview
![Screenshot 2025-05-27 160113](https://github.com/user-attachments/assets/7e81cb19-f43c-419e-a0b5-a8c40c777ab9)



✨ Key Features

🌍 Live Resource Sync: Real-time monitoring of EC2, RDS, Lambda & ECS🎨 Beautiful UI: Clean, dark-themed interface with smooth transitions⚙️ One-Click Refresh: Instantly pull latest AWS status with the Refresh button🧩 Modular Architecture: Separate components for flexibility & scaling🚀 Performance Optimized: Lightweight frontend with rapid API responses

## 🛠️ Tech Stack Breakdown

| Layer         | Tools & Frameworks        |
| ------------- | ------------------------- |
| 🎨 Frontend   | HTML5, CSS3, Vanilla JS   |
| 🔧 Backend    | Python, Flask, Flask-CORS |
| ☁️ AWS SDK    | Boto3                     |
| 🧪 Testing    | Postman, Browser DevTools |
| 🔍 API Format | RESTful JSON              |


📁 Project Layout

📦 AWS Resource Dashboard

├── 🧠 aws_monitor.py             →  Flask-based API service

├── 🌐 index.html                 → Frontend UI template

├── 📘 README.md                  → Project documentation

├── 🛠️ tempCodeRunnerFile.py      → Cors testing helper

├── 🖼️ data-center-image.webp     → Background visual

⚙️ Getting Started

🖥️ Backend Setup (Python)

# Step 1: Install required libraries
pip install flask boto3 flask-cors

# Step 2: Run the API server
python aws_monitor.py

✅ Flask app running on: http://localhost:5000/aws-resources

🌐 Frontend Setup (HTML)

Simply open index.html in your browser

Select services: EC2 | RDS | Lambda | ECS

Hit 🔄 Refresh to update data from AWS live

🧾 Sample Output:

{
  "EC2": [{"id": "i-0abcd1234", "type": "t3.micro", "state": "running"}],
  "RDS": [{"id": "prod-db", "state": "available"}],
  "Lambda": [{"name": "handler-fn", "state": "Active"}],
  "ECS": [{"name": "cluster-a", "status": "ACTIVE"}]
}

👨‍💻 Author

Kunal Guha 📫 kunalguh2003@gmail.com.com 🔗 GitHub 

📝 License

Licensed under the MIT License — Use it. Tweak it. Share it.

🌟 Star, Fork & Contribute

✨ If this project made your cloud journey easier:

⭐ Star this repo to support the project

🍴 Fork it to add new ideas or improvements

📬 Submit issues or pull requests

“Build dashboards that do more than display — they inspire.” 🚀

