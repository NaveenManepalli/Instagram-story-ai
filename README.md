# AI-Powered Instagram Story Template Generator

## Overview

AI-Powered Instagram Story Template Generator is a platform that automatically creates aesthetically designed **Instagram Story templates (1080 × 1920)** using artificial intelligence.

Users can upload their images and generate visually appealing story layouts based on:

* Natural language prompts
* Reference images (Pinterest, Instagram, Google Images)
* YouTube template videos

The system analyzes design styles, layouts, overlays, and text placements to automatically generate **ready-to-post Instagram story designs**.

---

## Key Features

* AI-generated Instagram story templates
* Prompt-based story design generation
* Pinterest / reference image template replication
* YouTube template style extraction
* AI-agent driven design workflow
* Automatic layout and styling
* Instagram optimized output (9:16 – 1080 × 1920)
* Downloadable story images
* Template preset saving
* Direct Instagram sharing (future feature)

---

## Example Workflow

1. User uploads an image
2. User provides one of the following inputs:

   * Design prompt
   * Reference image
   * YouTube template link
3. AI analyzes layout and style
4. Template is automatically generated
5. Final story image is rendered
6. User downloads or shares the story

---

## System Architecture

```
Frontend (React)
        │
        ▼
Backend API (Spring Boot)
        │
        ▼
AI Processing Service (Flask)
        │
        ├── Ollama (LLM Prompt Processing)
        ├── Stable Diffusion (Image Generation)
        ├── ControlNet (Template Replication)
        ├── OpenCV (Image Processing)
        └── Pillow (Story Rendering)
        │
        ▼
Storage + Database
MinIO + PostgreSQL
```

---

## Tech Stack

### Frontend

* React
* Tailwind CSS
* Axios
* Fabric.js

### Backend

* Spring Boot
* Spring Security
* Spring Data JPA

### AI / ML

* Flask
* Ollama
* Stable Diffusion
* ControlNet
* OpenCV
* Pillow
* CLIP
* Segment Anything

### Database & Storage

* PostgreSQL
* MinIO
* Redis (optional cache)

### Infrastructure

* Docker
* Git
* VS Code

---

## Project Structure

```
instagram-story-ai
│
├── frontend
│   └── react-app
│
├── backend
│   └── spring-boot-api
│
├── ai-service
│   └── flask-ai-engine
│
├── infra
│   └── docker
│
└── docs
```

---

## Installation (Development Setup)

Clone the repository:

```
git clone https://github.com/yourusername/instagram-story-ai.git
cd instagram-story-ai
```

Start backend:

```
cd backend
mvn spring-boot:run
```

Start frontend:

```
cd frontend
npm install
npm start
```

Start AI service:

```
cd ai-service
pip install -r requirements.txt
python app.py
```

Run Ollama:

```
ollama serve
```

---

## Future Improvements

* Direct Instagram story publishing
* Advanced template editor
* Template marketplace
* AI template recommendation
* Multi-image collage generation
* Video story templates

---

## License

This project is currently under development.
License will be added in future releases.

---

## Contributors

* Project Author
* Collaborators
    