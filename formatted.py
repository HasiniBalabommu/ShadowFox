def format_number(value, representation):
    result = format(value, representation)
    return result

# Using 145 and 'o' as arguments
formatted_result = format_number(145, 'o')
print("Formatted result:", formatted_result)
