SwaggerFlaskAPI
SwaggerFlaskAPI is a project for creating and documenting RESTful APIs using Flask and Swagger. This project demonstrates how to integrate Flask with Swagger to automatically generate and maintain up-to-date API documentation.
Key Features
* RESTful API Creation: A straightforward and efficient way to build APIs using Flask, a popular Python web framework.
* Automatic Documentation: Integration with Swagger (OpenAPI) for automatic generation of interactive API documentation available through Swagger UI.
* Flexibility and Scalability: Easy addition of new endpoints and functionality, with support for expanding the project to meet growing requirements.
* Clean and Maintainable Code: Example of structured code with best practices to ensure ease of development and maintenance.
Installation
1. Clone the repository: bashCopy code  git clone https://github.com/VladislavBA09/SwaggerFlaskAPI.git
2.   
3. Navigate to the project directory: bashCopy code  cd SwaggerFlaskAPI
4.   
5. Create and activate a virtual environment: bashCopy code  python -m venv venv
6. source venv/bin/activate  # Use `venv\Scripts\activate` for Windows
7.   
8. Install dependencies: bashCopy code  pip install -r requirements.txt
9.   
10. Run the Flask server: bashCopy code  flask run
11.   
12. Open Swagger UI: Visit http://localhost:5000/swagger to view and test the API through the interactive Swagger interface.
Usage
* Main Endpoint: /apidocs/ — the primary URL to access your API.
* Swagger Documentation: Available at http://localhost:5000/swagger.
Example Request
To open the documentation link:
bash
Copy code
curl -X GET "http://localhost:5000/apidocs/" -H "accept: application/json"
Contact
If you have any questions or suggestions, feel free to reach out to us at [brunko.vladislav@gmail.com].
