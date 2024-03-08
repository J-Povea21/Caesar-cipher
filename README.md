# Caesar-cipher
Hi! Welcome to the Caesar Cipher API :). This API it's an implementation of this basic
encryption algorithm.

## How to use it
It's really simple. The API expects a **json** with the following structure
```json
{
    "shift": int,
    "content": str
}
```
where `shift` it's the shift you want to apply to the alphabet and `content` the message you want to encrypt/decrypt

> **Important**: We only support **messages in spanish** with letters. If you use a number or special mark such as `! @ # ...` the API will return an error. Another thing to mention is that all the messages are capitalized.

## Endpoints
This API has two endpoints - or 3 if you count the root one - which are: **encrypt** and **decrypt**. I think it's
clear what each endpoint do. For both, you just need to pass a json with the structure we already saw


## Example
Let's say we want to encrypt the message "HELLO" with a shift=10. In that case we just need to POST to **encrypt** the following json
```json
{
    "shift":10,
    "content":"ZAPATO"
}
```
And we'll get this response from the API
```json
{
    "message":"JKZKDY"
}
```
If now we want to decrypt that message we need to do the same thing, but with **decrypt**
```json
{
    "shift":10,
    "content":"JKZKDY"
}
```
And the API will return
```json
{
    "message": "ZAPATO"
}
```
That's all! Enjoy using our API :D


