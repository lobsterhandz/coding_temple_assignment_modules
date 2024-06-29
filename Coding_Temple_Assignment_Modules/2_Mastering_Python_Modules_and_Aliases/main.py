# main.py
import text_utils as tu

def main():
    # Sample strings to manipulate
    sample_string = "hello"
    another_string = "world"

    # Using functions from text_utils module via alias
    reversed_string = tu.reverse_string(sample_string)
    capitalized_string = tu.capitalize_string(another_string)

    # Display the results
    print(f"Original: {sample_string} | Reversed: {reversed_string}")
    print(f"Original: {another_string} | Capitalized: {capitalized_string}")

if __name__ == "__main__":
    main()
