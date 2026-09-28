def main():
    """Run the WhatsApp chat analyzer program."""
    raw_lines = get_messages()
    messages = parse_messages(raw_lines)

    while True:
        show_menu()
        choice = input("Choose an option (0-19): ").strip()

        if choice == "1":
            count_total_messages(messages)
        elif choice == "2":
            find_unique_users(messages)
        elif choice == "3":
            count_total_words(messages)
        elif choice == "4":
            average_words_per_message(messages)
        elif choice == "5":
            find_longest_message(messages)
        elif choice == "6":
            find_most_active_user(messages)
        elif choice == "7":
            count_messages_by_user(messages)
        elif choice == "8":
            most_frequent_word_by_user(messages)
        elif choice == "9":
            first_and_last_message_by_user(messages)
        elif choice == "10":
            check_user_presence(messages)
        elif choice == "11":
            find_commonly_repeated_words(messages)
        elif choice == "12":
            longest_average_message_length_user(messages)
        elif choice == "13":
            count_mentions(messages)
        elif choice == "14":
            remove_duplicate_messages(messages)
        elif choice == "15":
            sort_messages_alphabetically(messages)
        elif choice == "16":
            extract_questions(messages)
        elif choice == "17":
            reply_ratio(messages)
        elif choice == "18":
            delete_message(messages)
        elif choice == "19":
            count_deleted_messages(messages)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please pick a number from the menu.")

def show_menu():
    """Print the list of analysis options for the user to choose from."""
    print("\n----- WhatsApp Chat Analyzer Menu -----")
    print("1.  Count total number of messages")
    print("2.  Identify unique users in the chat")
    print("3.  Count total words in the chat")
    print("4.  Calculate average words per message")
    print("5.  Find the longest message sent")
    print("6.  Find the most active user")
    print("7.  Get message count for a specific user")
    print("8.  Find the most frequent word used by a specific user")
    print("9.  Retrieve the first and last message by a user")
    print("10. Check if a user is present in the chat")
    print("11. Find commonly repeated words")
    print("12. Identify the user with the longest average message length")
    print("13. Count how many messages mention a specific user")
    print("14. Remove duplicate messages")
    print("15. Sort messages alphabetically")
    print("16. Extract all questions asked in the chat")
    print("17. Calculate the reply ratio between two users")
    print("18. Delete a message")
    print("19. Count total deleted messages")
    print("0.  Exit")

def get_messages():
    """Ask the user how many messages there are and read them one by one."""
    count = int(input("Enter the number of messages: "))
    raw_lines = []
    for i in range(count):
        line = input()
        raw_lines.append(line)
    return raw_lines


def parse_messages(raw_lines):
    """Turn each 'Name: message' line into a (user, message) tuple. returns a list of tuples."""
    parsed = []
    for line in raw_lines:
        user, message = line.split(":")
        user = user.strip()
        message = message.strip()
        parsed.append((user, message))
    return parsed


def clean_word(word):
    """Lowercase a word and strip common punctuation from it."""
    cleaned = word.lower()
    punctuation = "!?.,;:\"'()[]{}"
    for ch in punctuation:
        cleaned = cleaned.replace(ch, "")
    return cleaned

def count_total_messages(messages):
    """Option 1: Count and print the total number of messages."""
    total = len(messages)
    print(f"Total messages: {total}")


def find_unique_users(messages):
    """Option 2: Find and print the set of unique users in the chat."""
    users = set()
    for user, message in messages:
        users.add(user)
    print(f"Unique users: {users}")


def count_total_words(messages):
    """Option 3: Count and print the total number of words in the chat."""
    total_words = 0
    for user, message in messages:
        total_words += len(message.split())
    print(f"Total words in the chat: {total_words}")


def average_words_per_message(messages):
    """Option 4: Calculate and print the average words per message."""
    if len(messages) == 0:
        print("No messages to analyze.")
        return

    total_words = 0
    for user, message in messages:
        total_words += len(message.split())

    average = total_words / len(messages)
    print(f"Average words per message: {average:.2f}")


def find_longest_message(messages):
    """Option 5: Find and print the longest message (by characters)."""
    if not messages:
        print("No messages to analyze.")
        return

    longest_user, longest_message = messages[0]
    for user, message in messages:
        if len(message) > len(longest_message):
            longest_user, longest_message = user, message

    print(f"Longest message: {longest_user}: {longest_message}")


def find_most_active_user(messages):
    """Option 6: Find and print the user who sent the most messages."""
    message_counts = {}
    for user, message in messages:
        if user in message_counts:
            message_counts[user] += 1
        else:
            message_counts[user] = 1

    most_active_user = None
    most_active_count = 0
    for user, count in message_counts.items():
        if count > most_active_count:
            most_active_user = user
            most_active_count = count

    print(f"Most active user: {most_active_user} ({most_active_count} messages)")


def count_messages_by_user(messages):
    """Option 7: Ask for a username and print how many messages they sent."""
    username = input("Enter the username: ").strip()
    count = 0
    for user, message in messages:
        if user == username:
            count += 1
    print(f"Messages sent by {username}: {count}")


def most_frequent_word_by_user(messages):
    """Option 8: Ask for a username and print their most frequent word."""
    username = input("Enter the username: ").strip()
    word_counts = {}

    for user, message in messages:
        if user == username:
            for word in message.split():
                clean = clean_word(word)
                if clean == "":
                    continue
                if clean in word_counts:
                    word_counts[clean] += 1
                else:
                    word_counts[clean] = 1

    if not word_counts:
        print(f"No messages found for user '{username}'.")
        return

    top_word = None
    top_count = 0
    for word, count in word_counts.items():
        if count > top_count:
            top_word = word
            top_count = count

    print(f"Most frequent word used by {username}: \"{top_word}\"")


def first_and_last_message_by_user(messages):
    """Option 9: Ask for a username and print their first and last message."""
    username = input("Enter the username: ").strip()
    user_messages = []
    for user, message in messages:
        if user == username:
            user_messages.append(message)

    if not user_messages:
        print(f"No messages found for user '{username}'.")
        return

    print(f"First message by {username}: {user_messages[0]}")
    print(f"Last message by {username}: {user_messages[-1]}")


def check_user_presence(messages):
    """Option 10: Ask for a username and check if they are in the chat."""
    username = input("Enter the username: ").strip()
    found = False
    for user, message in messages:
        if user == username:
            found = True
            break

    if found:
        print(f"User '{username}' is present in the chat.")
    else:
        print(f"User '{username}' not found in the chat.")


def find_commonly_repeated_words(messages):
    """Option 11: Find and print words that appear more than once overall."""
    word_counts = {}
    for user, message in messages:
        for word in message.split():
            clean = clean_word(word)
            if clean == "":
                continue
            if clean in word_counts:
                word_counts[clean] += 1
            else:
                word_counts[clean] = 1

    repeated_words = set()
    for word, count in word_counts.items():
        if count > 1:
            repeated_words.add(word)

    print(f"Common repeated words: {repeated_words}")


def longest_average_message_length_user(messages):
    """Option 12: Find the user with the highest average words per message."""
    word_totals = {}
    message_counts = {}

    for user, message in messages:
        word_count = len(message.split())
        word_totals[user] = word_totals.get(user, 0) + word_count
        message_counts[user] = message_counts.get(user, 0) + 1

    top_user = None
    top_average = 0
    for user in word_totals:
        average = word_totals[user] / message_counts[user]
        if average > top_average:
            top_average = average
            top_user = user

    print(f"{top_user} (avg {top_average:.1f} words)")


def count_mentions(messages):
    """Option 13: Ask for a username and count messages that mention it."""
    username = input("Enter the username to search for: ").strip()
    count = 0
    for user, message in messages:
        cleaned_words = [clean_word(word) for word in message.split()]
        if username.lower() in cleaned_words:
            count += 1
    print(f"Messages mentioning '{username}': {count}")


def remove_duplicate_messages(messages):
    """Option 14: Remove duplicate messages and print how many remain."""
    seen = set()
    unique_messages = []
    for user, message in messages:
        full_message = f"{user}: {message}"
        if full_message not in seen:
            seen.add(full_message)
            unique_messages.append(full_message)

    print(f"Unique messages count: {len(unique_messages)}")


def sort_messages_alphabetically(messages):
    """Option 15: Sort all messages alphabetically and print them."""
    full_messages = []
    for user, message in messages:
        full_messages.append(f"{user}: {message}")

    sorted_messages = sorted(full_messages)

    print("All messages sorted A-Z:")
    for msg in sorted_messages:
        print(msg)


def extract_questions(messages):
    """Option 16: Find and print all messages containing a question mark."""
    questions = []
    for user, message in messages:
        if "?" in message:
            questions.append(f"{user}: {message}")

    if questions:
        print("Questions found in the chat:")
        for q in questions:
            print(q)
    else:
        print("No questions found in the chat.")


def reply_ratio(messages):
    """Option 17: Count how many times one user replied right after another."""
    user_a = input("Enter the username that is replying: ").strip()
    user_b = input("Enter the username being replied to: ").strip()

    reply_count = 0
    for i in range(1, len(messages)):
        previous_sender = messages[i - 1][0]
        current_sender = messages[i][0]
        if previous_sender == user_b and current_sender == user_a:
            reply_count += 1

    print(f"Reply ratio from {user_a} to {user_b}: {reply_count} replies")


def delete_message(messages):
    """Option 18: Deletes the content from the list of messages and replaces it with "this message is deleted"""
    if not messages:
        print("No messages to delete.")
        return

    print("Current messages:")
    for i in range(len(messages)):
        user, message = messages[i]
        print(f"{i + 1}. {user}: {message}")

    choice = input("Enter the message number to delete: ").strip()

    if not choice.isdigit():
        print("Please enter a valid message number.")
        return

    index = int(choice) - 1

    if index < 0 or index >= len(messages):
        print("That message number does not exist.")
        return

    user, message = messages[index]
    messages[index] = (user, "This message was deleted")
    print(f"Message {index + 1} from {user} has been deleted.")


def count_deleted_messages(messages):
    """Option 19: Count and print how many messages have been deleted."""
    deleted_markers = ["this message was deleted", "<deleted>", "[deleted]"]
    deleted_count = 0

    for user, message in messages:
        if message.strip() == "":
            deleted_count += 1
            continue
        lowered = message.lower()
        for marker in deleted_markers:
            if marker in lowered:
                deleted_count += 1
                break

    print(f"Total deleted messages: {deleted_count}")


if __name__ == "__main__":
    main()