# socket-rest
Why? Why not.

```bash
$ docker run -p 8000:8000 -e TOKEN="123" lilja/socket-rest
```

```bash
$ curl -X POST "localhost:8000/?token=123&domain=google.com&port=80"
{"status":"Online","domain":"google.com","port":80}
$ curl -X POST "localhost:8000/?token=123&domain=google.com&port=1337"
{"status":"Offline","domain":"google.com","port":1337}

```


