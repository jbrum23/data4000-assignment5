import requests

# --- Functions ---

def get_student_key():
    student_key = input("Student key: ")
    seed = sum(ord(ch) for ch in student_key.strip())
    return seed

def get_sku():
    while True:
        sku = input("SKU: ").strip()
        if sku.upper() == "DONE":
            return "DONE"
        elif sku == "":
            print("SKU cannot be blank. Please try again.")
        else:
            return sku

def get_on_hand():
    while True:
        try:
            qty = int(input("On hand: "))
            if qty < 0:
                print("Quantity must be 0 or greater. Please try again.")
            else:
                return qty
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def get_threshold(seed):
    if seed % 3 == 0:
        return 15
    elif seed % 3 == 1:
        return 12
    else:
        return 9

def check_reorder(on_hand, threshold):
    if on_hand < threshold:
        return "REORDER"
    else:
        return "OK"

def get_search_term(seed):
    if seed % 2 == 0:
        return "weezer"
    else:
        return "drake"

def api_spot_check(term):
    try:
        response = requests.get(
            "https://itunes.apple.com/search",
            params={"entity": "song", "limit": 5, "term": term}
        )
        data = response.json()
        results = data.get("results", [])
        count = sum(1 for item in results if item.get("kind") == "song")
        return count, "OK"
    except requests.exceptions.RequestException:
        return "N/A", "FAILED"
    except (KeyError, ValueError):
        return "N/A", "INVALID_RESPONSE"

# --- Main Program ---

seed = get_student_key()
threshold = get_threshold(seed)

total_skus = 0
reorder_count = 0

while True:
    sku = get_sku()

    if sku == "DONE":
        break

    on_hand = get_on_hand()
    status = check_reorder(on_hand, threshold)

    total_skus += 1
    if status == "REORDER":
        reorder_count += 1

search_term = get_search_term(seed)
songs_returned, api_status = api_spot_check(search_term)

print(f"Seed: {seed}")
print(f"Threshold: {threshold}")
print(f"SKUs entered: {total_skus}")
print(f"Reorder flagged: {reorder_count}")
print(f"Spotcheck term: {search_term}")
print(f"Songs returned: {songs_returned}")
print(f"API status: {api_status}")