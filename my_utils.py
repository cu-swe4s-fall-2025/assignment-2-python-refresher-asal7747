def get_column(file_name, query_column, query_value, result_column=1):
    # Create an empty list to store matching values
    results = []

    # Open the file and read it line by line
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            # Remove new line and extra spaces
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            # Split the line into a list by commas
            parts = line.split(",")

            # Make sure the indices exist before using them
            if query_column >= len(parts) or result_column >= len(parts):
                continue

            # Check if the value in query_column matches query_value
            if parts[query_column].strip() == query_value:
                # Add the value from result_column to the results
                results.append(parts[result_column].strip())

    # Return the collected values
    return results

