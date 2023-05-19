# pythonGPT

ChatGPT Requests Module

The ChatGPT Requests module is a Python package that provides a convenient interface for making requests to the ChatGPT language model. It abstracts away the complexity of interacting with the model's API, allowing developers to easily integrate ChatGPT into their applications.

Key Features:
- Simple API: The module provides a high-level API that simplifies the process of sending messages and receiving responses from the ChatGPT model.
- Stateful Conversations: It supports stateful conversations, enabling users to have multi-turn interactions by maintaining context across messages.
- Error Handling: The module includes robust error handling to gracefully handle API errors and timeouts, ensuring a reliable integration.

Usage Example:
```python
from pythonGPT import PythonGPT

chatgpt = ChatGPT(api_key='your-api-key')

# Making a request
response = chatgpt.request("Hello, how are you?")
print(response)

# Submit multiple requests by txt file
response = chatgpt.requests('file.txt')
print(response)



