def caesar_cipher(text, shift):
	"""Return text shifted forward by shift positions in the alphabet."""
	lowercase_alphabet = "abcdefghijklmnopqrstuvwxyz"
	uppercase_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	encrypted_text = ""

	shift = shift % 26

	for index in range(len(text)):
		character = text[index]

		if character in lowercase_alphabet:
			letter_index = lowercase_alphabet.index(character)
			shifted_index = (letter_index + shift) % 26
			encrypted_text += lowercase_alphabet[shifted_index]
		elif character in uppercase_alphabet:
			letter_index = uppercase_alphabet.index(character)
			shifted_index = (letter_index + shift) % 26
			encrypted_text += uppercase_alphabet[shifted_index]
		else:
			encrypted_text += character

	return encrypted_text


def caesar_decipher(cyphertext, shift):
	"""Return the original text by shifting cyphertext backward."""
	return caesar_cipher(cyphertext, -shift)


def letter_frequency(text):
	"""Return the number of times each letter appears in text."""
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	frequency = {}

	for index in range(len(alphabet)):
		frequency[alphabet[index]] = 0

	for index in range(len(text)):
		character = text[index].lower()
		if character in alphabet:
			frequency[character] += 1

	return frequency


def main():
	"""Run the Caesar cipher terminal program."""
	print("Caesar Cipher")
	print("---------------")

	message = None
	shift = 0

	while True:
		print("\nMenu")
		print("1. Enter a message and shift")
		print("2. See the encrypted text")
		print("3. See the letter frequencies")
		print("4. See the decrypted text")
		print("5. Quit")

		choice = input("Choose an option: ")

		if choice == "1":
			message = input("Enter a message: ")
			shift = int(input("Enter a shift number: "))
			print("Message and shift saved.")
		elif choice == "2":
			if message is None:
				print("Please enter a message and shift first.")
			else:
				print("Encrypted text:", caesar_cipher(message, shift))
		elif choice == "3":
			if message is None:
				print("Please enter a message and shift first.")
			else:
				print("Letter frequencies:", letter_frequency(message))
		elif choice == "4":
			if message is None:
				print("Please enter a message and shift first.")
			else:
				encrypted_message = caesar_cipher(message, shift)
				print("Decrypted text:", caesar_decipher(encrypted_message, shift))
		elif choice == "5":
			print("Goodbye!")
			break
		else:
			print("Please choose a number from 1 to 5.")


if __name__ == "__main__":
	main()
