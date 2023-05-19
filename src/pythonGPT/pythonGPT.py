import os
import requests
import time
import json


class PythonGPT:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = 'https://api.openai.com/v1/chat/completions'
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def request(self, prompt):
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,

        }
        try:
            response = requests.post(self.api_url, headers=self.headers, json=data)
            response.raise_for_status()
            response_json = response.json()
            conversation_id = response.json()['id']
            return conversation_id, response_json['choices'][0]['message']['content'].strip()
        except requests.exceptions.RequestException as err:
            print('An error occurred:', err)
            return None

    def requests(self, file_path):
        with open(file_path, 'r') as f:
            content = f.readlines()

        questions = [a.split('?') for a in content]
        questions = set([j.strip() + '?' for i in questions for j in i if len(j)>2])

        dir_path = os.path.join(os.getcwd(), 'GPT responses')
        if not os.path.exists(dir_path): os.mkdir(dir_path)
        out_file_name = file_path.split('/')[-1].split('.')[0]+f'_response{len(os.listdir(dir_path))}.txt'
        out_path = os.path.join(dir_path, out_file_name)

        for i, question in enumerate(questions):
            answer = self.request(question)
            with open(out_path, 'a') as f:
                f.write(question + '\n\n' + str(answer) + '\n\n')
            print(f'Question No.{i} has been answered')
            time.sleep(1)
        return 'See '+out_path+'!'


