# fondeadora-test-app

Development evaluation project for the backend developer position at Fondeadora.

  Project Title: URL Shortener Service

  Overview:
  
The URL Shortener Service is a Python 3-based project that provides a RESTful API for shortening long URLs into short aliases The service includes two endpoints, one for accepting a URL via a POST request and returning a shortcode, and another for accepting a shortcode via a GET request and returning the original URL. The project aims to provide a simple and efficient solution for creating and managing shortened URLs.

-Technology stack:
  python 3.8.10
  fastapi 0.95.0
  unittest2 1.1.0

-Database:
  sqlite
  
  Features:

URL Shortening: The service allows users to submit long URLs via a POST request and generates a unique shortcode that represents the shortened URL. This shortcode can be used to redirect users to the original URL when accessed.

URL Expansion: The service also provides a GET endpoint that accepts a shortcode and returns the original URL associated with that shortcode. This allows users to expand the shortened URL and access the original long URL.

Customizable Architecture: The project allows for flexibility in choosing the technology stack, such as the option to use a simple DB like SQLite for storing mappings between shortcodes and URLs, and the use of FastAPI for building the RESTful API.

Clean Code and Testing: The project follows a clean, layered architecture and emphasizes clean coding practices. It includes comprehensive test coverage to ensure the reliability and robustness of the service. Git is used extensively, with clear commit messages to document the coding process.




The service was deployed on Heroku and can be easily accessed from the following URL:

  https://fondeadora-test-app.herokuapp.com/docs

in it we find the fast api swagger in which we can test the project methods.

To be able to test the project locally it is necessary to execute the following commands:

  docker build . -c -t fondeadora-test-app

  docker run -p 8000:8000 fondeadora-test-app

in order to run the unit tests the command is needed:

  python -m pytest test_services.py 
  python -m pytest test_providers.py 

