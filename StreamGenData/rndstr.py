import uuid
import time
def random_string(string_length):
    random=str(uuid.uuid4())
    random=random.upper()
    random=random.replace("-","")
    return random[0:string_length]
