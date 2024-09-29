from textblob import TextBlob

# Function to analyze the tone of the email
def analyze_tone(email_content):
    # Create a TextBlob object
    blob = TextBlob(email_content)
    
    # Analyze sentiment polarity (-1 = negative, 0 = neutral, 1 = positive)
    sentiment_polarity = blob.sentiment.polarity
    
    if sentiment_polarity > 0:
        return "Positive"
    elif sentiment_polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Function to display tone analysis
def display_tone_analysis(email_content):
    print("\nAnalyzing the tone of your email...\n")
    tone = analyze_tone(email_content)
    print(f"The tone of the email is: {tone}")
    
# Main function to run the program
def main():
    print("Welcome to the Email Tone Checker!\n")
    
    # Ask the user to input their email content
    email_content = input("Please enter the content of your email:\n")
    
    # Display the tone analysis
    display_tone_analysis(email_content)
    
    # Give the user advice based on tone
    tone = analyze_tone(email_content)
    if tone == "Negative":
        print("\nIt seems like the email has a negative tone. You might want to revise it to sound more positive or neutral.")
    elif tone == "Neutral":
        print("\nThe email has a neutral tone, which is appropriate for professional communication.")
    else:
        print("\nThe email has a positive tone. Great job in maintaining a polite and friendly tone!")

# Run the program
if __name__ == "__main__":
    main()
