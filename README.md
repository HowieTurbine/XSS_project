# XSS attack demo


## Reflected Attack
To start the reflected attack, 
use the link:
```
http://127.0.0.1:5000/demo1
```

This page would show us a demo comment board, in order to attack this page, try a script like this:
```
<script>alert('You are attacked!')</script>
```

## Stored Attack:
To start the stored attack,first go to the link:
```
http://127.0.0.1:5000/demo2
```
Type your username and password(whatever it is)
and then check button 'Remember Me'.
Then go to the page:
```
http://127.0.0.1:5000/demo2_2
```
You would see there is a image, if you check the URL link for this image, then you could be able to find that your
cookie is appended as GET parameter.
