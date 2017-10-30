import requests;
import time;

response = requests.get("https://jsonplaceholder.typicode.com/posts/1");
print (response.elapsed);