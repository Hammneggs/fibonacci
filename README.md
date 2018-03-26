# Fibonacci RESTful web service
This is a very simple RESTful web service that accepts a given number as input and outputs that given set of numbers from the Fibonacci sequence, starting with 0.  Only positive numbers are accepted. 

For example: 5
would output
[0, 1, 1, 2, 3] 

## Requirements

- python (verified with version 2.7.13)
- Flask web framework  (install with: pip install flask) 

```
sudo pip install -r requirements.txt
```

## Installation
After you install Flask, clone this github repository.  Make sure the app.py script is at the same location as your flask directory and start the app with

      $  chmod 755 app.py
      $ ./app.py &

The application is set to listen on port 5000.  

To send a request, you can go to your web browser at:
```
      http://127.0.0.1:5000/fibonacci/<number you choose>
```
or use curl:
```
      $ curl http://127.0.0.1:5000/fibinacci/<number you choose>
```


