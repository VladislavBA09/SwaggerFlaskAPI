SwaggerFlaskAPI

SwaggerFlaskAPI is a project for creating and documenting RESTful APIs using Flask and Swagger. This project demonstrates how to integrate Flask with Swagger to automatically 
generate and maintain up-to-date API documentation.

Key Features
* RESTful API Creation: A straightforward and efficient way to build APIs using Flask, a popular Python web framework.

* Automatic Documentation: Integration with Swagger (OpenAPI) for automatic generation of interactive API documentation available through Swagger UI.

* Flexibility and Scalability: Easy addition of new endpoints and functionality, with support for expanding the project to meet growing requirements.

* Clean and Maintainable Code: Example of structured code with best practices to ensure ease of development and maintenance.

* Installation

1. Clone the repository: bashCopy code  git clone https://github.com/VladislavBA09/SwaggerFlaskAPI.git

2. Navigate to the project directory: cd SwaggerFlaskAPI
   
3. Create and activate a virtual environment: python -m venv venv

4. source venv/bin/activate  # Use `venv\Scripts\activate` for Windows
   
5. Install dependencies: pip install -r requirements.txt
   
6. Run the Flask server: python start.py
   
7. Open Swagger UI: Visit http://localhost:5000/swagger to view and test the API through the interactive Swagger interface.

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
