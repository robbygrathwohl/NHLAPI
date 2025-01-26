import re

def camel_to_snake(name: str) -> str:
    """Convert a camelCase string to snake_case."""
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

def convert_keys_to_snake_case(obj):
    """Convert all keys in a dictionary to snake_case."""
    if isinstance(obj, dict):
        return {camel_to_snake(key): convert_keys_to_snake_case(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [convert_keys_to_snake_case(item) for item in obj]
    else:
        # Base case: return the value as is if it's not a dict or list
        return obj