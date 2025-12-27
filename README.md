# LearnFastApi
FastApi is modern, high-performance web Frame for building APIs with Python
- will get uvicorn web server (which is Asyn. nature handle multiple parallel req.)
- to create virtual environment use cmd ( python -m venv myEnv) => it will create one folder and in folder there is scripts folder in which Activate.ps1 copy path and run
- source myEnv/bin/activate
- uvicorn main:app --reload 
- 127.0.0.1:8000/docs  --> Swagger 
- myenv/scripts/activate

=> FastApi (2 famous lib ka use kr k bna hai) 
1. Starlette (send response and recieve request through api http)
2. Pydantic (data validation) (It is use to check if the data is coming into your api is correct and right format)
=> Why FastApi is fast to run? http req. ko python understable code format me convert krna hai (SGI - server gateway interface) SGI kaam krta h 
FastApi me ASGI (Asyn server..) use hota hai. Asynchronous interface that better suited for web modern application like those using Websocket and real-time feature. 
Flask me WSGI (web server...) Sync. nature ka hota hai jo slower req. process  krta hai...
=> Why FastApi is fast to code?  
1. Automatic input validation 
2. Auto-Generated Interactive Document
3. Seamless Integration with modern Ecosystem (ML/DL Lib., OAuth, JWT, SQL Alchemy, Docker, kubernetes etc..)
=> Path() fun in FastApi is use to provide metaData, validation and documentation hint in Swagger

=> By defatult Python me type validation nahi hai
=>Python me type hinting ache se kaam ni krta basically yee just hint dane k liye we are using (name: str, age: int)  BUT app age ko str pass kroge to error ni aayega everything works well Soo we use Pydantic  to fix the issue dataValidation typeValidation, typeCasting 
1. ya to manually type validation kr lo like if type(age)==int: 
2. Will solve by Pydantic  (pip install pydantic)
- will make class of Pydantic (model) 
- Instantiate the model with raw input data 
- Pass the validated model object
=> agar list -> []  --> List[str] ->list k under only str allow (iske liye import krna padhta hai)

=> In FastApi, a response model define the structure of data that your API will return. It help in:
- Generate clean API doc
- Validate output (so your API doesn't return malformed response)
- Filtering unnecessary data

=> patient1 = Patient(**patient_info) # '**' Take all key–value pairs from the dictionary and pass them as named arguments to the function or class.