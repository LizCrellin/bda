### Tutorial MongoDB

1. Register and login: https://www.mongodb.com

![Screenshot 2025-06-30 at 19.12.57](/Users/steliossotiriadis/Desktop/Screenshot 2025-06-30 at 19.12.57.png)

2. Skip the personalization in the next screen
3. Select `Free` and click on `Create Deployment`

![Screenshot 2025-06-30 at 19.13.22](/Users/steliossotiriadis/Desktop/Screenshot 2025-06-30 at 19.13.22.png)

4. Create a new user with your desired password - **do not forge to press on Create Database User button**.

![Screenshot 2025-06-30 at 19.13.49](/Users/steliossotiriadis/Desktop/Screenshot 2025-06-30 at 19.13.49.png)

5. You are now ready!

![Screenshot 2025-06-30 at 19.14.08](/Users/steliossotiriadis/Desktop/Screenshot 2025-06-30 at 19.14.08.png)

6. Go to `Network Access`, click on `+Add IP Address` and allow access from anywhere.

![image-20250630191909676](/Users/steliossotiriadis/Library/Application Support/typora-user-images/image-20250630191909676.png)

7. Go to `Clusters` and `Browse Collections`. Let's connect to `sample_mflix`.

![image-20250630191954925](/Users/steliossotiriadis/Library/Application Support/typora-user-images/image-20250630191954925.png)

8. Let's try to connect using Python. Go to `Clusters`, then `Connect` , then click on `Drivers` and select `Python`.

![image-20250630192138279](/Users/steliossotiriadis/Library/Application Support/typora-user-images/image-20250630192138279.png)

9. That's the link to the driver.

![image-20250630192253655](/Users/steliossotiriadis/Library/Application Support/typora-user-images/image-20250630192253655.png)

10. Go to VSC, create a new project and a new `venv`.

```
python -m pip install "pymongo[srv]"
```

10. Then create a new file and add the following code.
    * Use the following code and adjust your `uri`
    * Make sure you change:
      * Your name
      * Your password
      * Add the collection name: `sample_mflix`

> mongodb+srv://`ssotiriadis`:`1234`@cluster0.1fqzpnv.mongodb.net/`sample_mflix`?retryWrites=...

```
from pymongo import MongoClient
import certifi
from pprint import pprint

uri = "mongodb+srv://ssotiriadis:1234@cluster0.1fqzpnv.mongodb.net/sample_mflix?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, tlsCAFile=certifi.where())
db = client["sample_mflix"]
users_collection = db["users"]

user = users_collection.find_one()
pprint(user)
```

