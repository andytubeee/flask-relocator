# Flask Relocator

Flask Relocator is a reusable Flask application designed to inform users of a server's new IP address or location. If you've migrated your server and don't want to take your application offline, Flask Relocator can dynamically inform users where to find the new site.

## Features

- **Simple Integration**: Easily integrate with any existing Flask application.
- **Dynamic Redirection**: Customize the message and redirection URL based on your new server location.
- **Security Focused**: Ensures that redirection notices are handled securely to prevent misuse.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

```bash
pip install flask
```

### Installing

A step-by-step series of examples that tell you how to get a development environment running:

1. Clone the repository:

```bash
git clone https://github.com/andytubeee/flask-relocator.git
cd flask-relocator
```

2. Setup virtualenv and activate it

```bash
python -m venv venv
source venv\bin\activate # or whatever OS you are using
```

3. Install requirements:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python app.py
```

### Usage

Here is how to use Flask Relocator in your project:

```python
from relocator.relocator import relocator_blueprint
app = Flask(__name__)
app.register_blueprint(relocator_blueprint, url_prefix='/')
```

## Contributing

Feel free to modify and contribute if you feel additional features are necessary

## License

This project is licensed under the MIT License

## Acknowledgments

- Me
- [Spirito@LottieFiles](https://lottiefiles.com/j6p1augtuu5fbu5y)
