# WeLoveTrees - Mahir Riki, Ravindra Mangar, Kevin Liu
### SoftDev
### K19: Sessions Greetings
### 2022-11-03
### time spent: 0.5 hr

## DISCO
* To generate a token, we used:
```
$ python3 -c 'import secrets; print(secrets.token_hex())'
```
* In Jinja HTML, to show the username we couldn't use {{username}}, instead, we had to use {{session['username']}}.

## QCC
* Can we use the token we generated in any way to keep track of the user?