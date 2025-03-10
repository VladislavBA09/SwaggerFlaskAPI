# SwaggerFlaskAPI

**SwaggerFlaskAPI** is a project for creating and documenting RESTful APIs using Flask and Swagger. This project demonstrates how to integrate Flask with Swagger to automatically generate and maintain up-to-date API documentation.

---

## 📌 Key Features

- **RESTful API Creation:** A straightforward and efficient way to build APIs using Flask, a popular Python web framework.
- **Automatic Documentation:** Seamless integration with Swagger (OpenAPI) for automatic generation of interactive API documentation accessible via Swagger UI.
- **Flexibility and Scalability:** Easily add new endpoints and functionality to meet evolving project requirements.
- **Clean and Maintainable Code:** Demonstrates structured and organized code with best practices for simplicity and maintainability.

---

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/VladislavBA09/SwaggerFlaskAPI.git

2. Navigate to the project directory:
    cd SwaggerFlaskAPI

3. Create and activate a virtual environment:
    python -m venv venv

    On macOS and Linux:
        source venv/bin/activate

    On Windows:
        venv\Scripts\activate

4. Install dependencies:
    pip install -r requirements.txt

5. Run the Flask server:
    python start.py

6. Open Swagger UI:
    http://localhost:5000/swagger

    Access the interactive API documentation and test the endpoints directly through the Swagger interface.
    
🚀 Usage

Main Endpoint:

Access your API through the primary URL:
    /apidocs/

Swagger Documentation:

View interactive API documentation at:
    http://localhost:5000/swagger

Example Request:

To open the documentation link via the command line:
    curl -X GET "http://localhost:5000/apidocs/" -H "accept: application/json"

📧 Contact
If you have any questions or suggestions, feel free to reach out to us at:
brunko.vladislav@gmail.com
