# main.py
import top_50_books 

# Load dataset from top_50_books.py
df = top_50_books.get_dataset()

def get_autocomplete_options(df, category, first_letter):
    options = df[category].str.startswith(first_letter, na=False)
    suggestions = df[options][category].unique()
    return suggestions

def recommend_books(df, category, selection):
    recommendations = df[df[category] == selection]
    return recommendations[['title', 'author', 'genre']]

def match_partial_input(selection_text, suggestions):
    selection_text = selection_text.lower()

    for suggestion in suggestions:
        if selection_text in suggestion.lower():
            return suggestion
    return None


def main():
    while True:
        # Category selection
        category = input("Choose a category to filter by (author or genre) or 'exit' to quit ").strip().lower()
        if category == 'exit':
            print("Goodbye!")
            break
        if category not in ['author', 'genre']:
            print("Invalid category. Please choose 'author' or 'genre'.")
            continue

        # First letter input and autocomplete suggestions
        while True:
            first_letter = input(f"Enter the first letter of the {category} name: ").strip().upper()
            suggestions = get_autocomplete_options(df, category, first_letter)
            if len(suggestions) == 0:
                print(f"No matches found for {category} starting wit '{first_letter}'. Try another letter.")
                continue

            # Selection and recommendations 
            print(f"Suggestions for {category} starting with '{first_letter}': {suggestions}")
            selection_input = input(f"Choose one of the above suggestions (partial input allowed): ").strip()

            #Match user's input with suggestions
            matched_selection = match_partial_input(selection_input, suggestions)
            if not matched_selection:
                print("Invalid selection. Please choose from the suggestions provided.")
                continue

            # If valid selection is made, display recommendations and break loop
            recommendations = recommend_books(df, category, matched_selection)
            print("Here are your book recommendations:")
            print(recommendations)
            break

# Run the program
main()