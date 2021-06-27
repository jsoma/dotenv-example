Install dotenv, create a `.env` file, then use it!

```python
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('PROJECT_API_KEY')
```