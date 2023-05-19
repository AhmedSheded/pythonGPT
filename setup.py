import setuptools

with open("README.md", "r", encoding ="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "pythonGPT",
    version = "1.0.0",
    author = "Ahmed Sheded",
    author_email = "sheded222@gmail.com",
    description = "The ChatGPT Requests module is a Python package that provides a convenient interface for making requests to the ChatGPT language model. It abstracts away the complexity of interacting with the model's API, allowing developers to easily integrate ChatGPT into their applications.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "package URL",
    project_urls = {
        "Bug Tracker": "package issues URL",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6"
)

