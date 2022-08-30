
from playsound import playsound
import string

message = "Hello world"

for char in message:
	if char.lower() not in string.ascii_lowercase: continue
	playsound(f"./sounds/{char.lower()}.wav")