from pynput.keyboard import Key, Listener
import matplotlib.pyplot as plt # type: ignore
import string

# Initialize counters
letter_counts = {char: 0 for char in string.ascii_lowercase}
word_lengths = {}

def on_press(key):
    global current_word
    if hasattr(key, 'char'):
        char = key.char.lower()
        # Count individual letters
        if char in string.ascii_lowercase:
            letter_counts[char] += 1
        
        # If separator character is pressed, consider it as the end of a word
        if char in [' ', ',', '.', ':']:
            word_length = len(current_word)
            if word_length in word_lengths:
                word_lengths[word_length] += 1
            else:
                word_lengths[word_length] = 1
            current_word = ''
        else:
            current_word += char

def on_release(key):
    if key == Key.esc:
        # Stop the listener
        return False

current_word = ''

# Start the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Data analysis and plotting
# Plot letter frequencies
letters = list(letter_counts.keys())
counts = list(letter_counts.values())
plt.bar(letters, counts)
plt.xlabel('Letter')
plt.ylabel('Frequency')
plt.title('Letter Frequencies')
plt.show()

# Plot word lengths
word_lengths_sorted = sorted(word_lengths.items(), key=lambda x: x[0])
lengths = [x[0] for x in word_lengths_sorted]
word_counts = [x[1] for x in word_lengths_sorted]
plt.bar(lengths, word_counts)
plt.xlabel('Word Length')
plt.ylabel('Frequency')
plt.title('Word Length Frequencies')
plt.show()
