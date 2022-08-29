

># ENDPOINTS  
>
>> ### USERS
>>"/lgoin"   ==> POST  
>"/register"  ==> POST  
>"/user/:id" ==> PUT DELETE GET  
>"/user/:id/orders" ==> GET  
> "/user/:id/comments" ==> GET  
> 
>> ### PRODUCTS   
>>"/product" ==> POST              (?where:category_title="sport")
>"/product/:id" ==> PUT DELETE GET /PATCH/  
>
>>  ### COMMENTS
>>"/comments/:product_id"  ==> GET POST DELETE PUT  
> 
>> ### ORDERS
>>"/orders"  ==> GET /ADMIN/  
> "/orders/:id" ==> PUT /ADMIN/
> "/orders/:user_id"  ==> GET  
> 
>> ### WISHES
>> "/wishes/:user_id"  ==>  GET DELETE POST
> 
>> ### NEWSLETTER
>> "/newsletter"  ==> POST DELETE | GET  
>  
>> ### DISCOUNT
>> "/discount"  ==> POST GET  /ADMIN/   
>  "/discount/:id"  ==> PUT DELETE GET  /ADMIN/  
>  "/discount/check" ==> POST  {discount: discount, isValid: true}
>   
>> ### CATEGORY 
>> "/category"  ==> GET | POST /ADMIN/  
>  "/category/:id"  ==> GET PUT DELETE  /ADMIN/  
> 
>> ### BRAND
>> "/brand"  ==> GET | POST /ADMIN/  
>  "/brand/:id"  ==> GET PUT DELETE  /ADMIN/  

![Database schema](https://i.ibb.co/DMZmMtC/Shoecommerce-database-schema.png)


# REST API

The REST API to the app is described below.


- [Register](#register)

>## Register
>### Request
>`[POST] "/register"`
>
>```json
>{
>    "user_data":{
>        "f_name": "firstName",
>        "l_name": "lastName",
>        "phone": "0888429842"
>    },
>    "email": "some@email.com",
>    "password": "goodpassword1"
>}
>```
>### Response
> 
> ```json
> "{\"token\": \"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjM0LCJleHAiOjE2NzA0Mzg4OTd9.YVu0irTJl3ZOxdharUiMipaNhHQkAFe3RMd3JCD6iyc\", \"user_id\": 34, \"role\": \"user\"}"
>```
>Server validations are:   
> - Email must be correct email string.   
> - Password must be between 5 and 60 characters.   
> - Password must have atleast one number.   
> - First name must be between 2 and 60 characters.
> - Last name must be between 2 and 60 characters.
>
> Example error massages
>```json
>{
>    "message": {
>        "email": [
>            "Missing data for required field."
>        ],
>        "user_data": {
>            "l_name": [
>                "Length must be between 2 and 60."
>            ],
>            "f_name": [
>                "Length must be between 2 and 60."
>            ],
>            "phone": [
>                "Not a valid integer."
>            ]
>        },
>        "password": [
>            "Length must be between 5 and 60.",
>            "Password must have atleast one number."
>        ]
>    }
>}
>```

>## Login
>### Request
>`[POST] "/login"`
>```json
>{
>    "password": "23233223",
>    "email": "email@abv.bg"
>}
>``` 
>### Response
> ```json
>"{\"token\": \"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjM0LCJleHAiOjE2NzA0Mzg4OTd9.YVu0irTJl3ZOxdharUiMipaNhHQkAFe3RMd3JCD6iyc\", \"user_id\": 34, \"role\": \"user\"}"
>```
> Server validations are:
> - Must have sent all fields(email and password)
> - Email must be valid email string
> 
> Example error massages
> If email is valid email string:
> ```json
> {
>    "message": "Wrong email or password!"
> }
>```
>If email is not a valid email string or missing some key (email or password), error will be:
>```json
>{
>    "message": {
>        "email": [
>            "Not a valid email address."
>        ],
>        "password": [
>            "Missing data for required field."
>        ]
>    }
>}
>```