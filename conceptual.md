### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

    - Python has wider usage 
    - Javascript is a client-side scripting language and Python is used for both desktop and web applications
    - python uses class-based inheritance model and Js uses a prototype-based inheritance model
  
  ---

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  
  - ``` if "c" in x```
  -  ```x.get('c', 'not found')```

---
- What is a unit test?

  - Unit test is a test that used to test small pieces of code
  ---

- What is an integration test?

  - Integration test used for when different pieces of code modules integrated and tested as a group
---

- What is the role of web application framework, like Flask?

  - Frameworks support the development of web applications. 
  ---

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  - Query param generally used for form parameters and the usage of route url is for a general subject of page.
  ___

- How do you collect data from a URL placeholder parameter using Flask?
    
    - We can use request.args.get() method.
  
  ---

- How do you collect data from the query string using Flask?
  
    - We can use request.args[] method.
  
---
- How do you collect data from the body of the request using Flask?
  
    - We can use request.form
---
- What is a cookie and what kinds of things are they commonly used for?

  - Cookies used for saving a small bits of info on the client. Commonly, it's used for one time selection to prevent repetitive code.
---
- What is the session object in Flask?

  - Flask session is a dictionary that uses cookies. Flask session preserve type.

---
- What does Flask's `jsonify()` do?

  -`jsonify()` is function to convert JSON format to a Response object 
