from playsound import playsound
import string
import sys

def main():
	if len(sys.argv) != 2:
		print("Error! just send one argument.")
		return
	for char in sys.argv[1]:
		if char.lower() not in string.ascii_lowercase: continue
		playsound(f"./sounds/{char.lower()}.wav")

if __name__ == "__main__":
	main()