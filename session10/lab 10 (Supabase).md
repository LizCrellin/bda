### Tutorial supabase

1. Register at: https://supabase.com/ and log in. Complete your name if you like.

![Screenshot 2025-06-30 at 13.48.13](/Users/steliossotiriadis/Desktop/Screenshot 2025-06-30 at 13.48.13.png)

2. Create a password.

![Screenshot 2025-06-30 at 13.48.54](/Users/steliossotiriadis/Desktop/Screenshot 2025-06-30 at 13.48.54.png)

3. You are ready!

![Screenshot 2025-06-30 at 13.49.23](/Users/steliossotiriadis/Desktop/Screenshot 2025-06-30 at 13.49.23.png)

4. Create a new table, I called it `test` and default fields.
5. Go to Authentication and polciies click `Disable RLS`

![Screenshot 2025-06-30 at 14.02.15](/Users/steliossotiriadis/Desktop/Screenshot 2025-06-30 at 14.02.15.png)

6. Open VSC and create a new project.
7. Create a new `venv`

```
python -m venv venv

- Mac: source venv/bin/activate
- Windows: venv\Scripts\activate

pip3 install supabase
```

8. Go back to `supabase` and locate your API key in the `Project settings` and `API keys`.
   * You will need to use the `anon` `public` key. 

![image-20250630140757632](/Users/steliossotiriadis/Library/Application Support/typora-user-images/image-20250630140757632.png)

8. Check your supabase URL and find out your URI.

![image-20250630140928931](/Users/steliossotiriadis/Library/Application Support/typora-user-images/image-20250630140928931.png)

8. Find your test table and insert yoru first row.
9. Run the following script.

```
from supabase import create_client, Client
from pprint import pprint  # or use json.dumps if you prefer

url = "https://mkqumcpmiwszcxzbrsle.supabase.co"
key = "your_key_goes_here"

supabase: Client = create_client(url, key)

response = supabase.table("test").select("*").execute()
pprint(response.data)
```

10. You are now connected!

11. Go to bucket and load a file, e.g. the Biostats.csv from the previous classes.

12. Run the following script to load data in Python.

```
from supabase import create_client, Client
import pandas as pd
import requests
from io import StringIO
import certifi

# Load CSV using requests with SSL verification using certifi
csv_url = "https://mkqumcpmiwszcxzbrsle.supabase.co/storage/v1/object/public/stelios-bucket/Biostats.csv"
headers = {"Authorization": f"Bearer {key}"}

r = requests.get(csv_url, headers=headers, verify=certifi.where())

if r.status_code == 200:
    df = pd.read_csv(StringIO(r.text))
    print(df.head())
else:
    print("Failed to load CSV:", r.status_code, r.text)
```

