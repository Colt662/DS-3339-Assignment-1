from product_data import products

#Create a customer_preferences list and store the user preference in this list.
customer_preferences = []
response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
    # Add the customer preference to the list
    customer_preferences.append(preference)

    response = input("Do you want to add another preference? (Y/N): ").upper()


# Convert customer preferences and product tag lists to set to eliminate duplicates and allow for fast comparisons.
customer_preferences = set(customer_preferences)

for product in products:
    product["tags"] = set(product["tags"])


# Function to calculate the number of matching tags for a product
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    return len(customer_tags.intersection(product_tags))


#Function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A sorted list of products containing product names and their match counts.
    '''
    matches = []

    for product in products:
        num_matches = count_matches(product["tags"],customer_tags)
        if num_matches > 0:
            matches.append({"product": product["name"],"matches": num_matches})
    #sorted in descending order by number of matches
    matches.sort(reverse=True, key=lambda x:x["matches"])
    return matches


#Get the recommendations and print the results
matched_products = recommend_products(products, customer_preferences)

print("Recommended Products:")
for match in matched_products:
    print(f"- {match["product"]:30} {match["matches"]} match(es)")



# DESIGN MEMO (write below in a comment): 200-300 words
# 1. What core operations did you use (e.g., intersections, loops)? Why?
# 2. How might this code change if you had 1000+ products?

# 1. What core operations did you use (e.g., intersections, loops)? Why?
# A while loop was used to input user preferences so that any amount of tags may be entered.
# For-in loops were used to access the products list so that the whole list could be accessed.
# An intersection was used to count product tag matches because it is a fast way to compare.
# Both the user preferred tags and the product tags are converted to and kept as sets since for the purposes of recommendations it isn't necessary to have duplicate or ordered tags, and they would both likely be used primarily for comparisons even in other situations.

#2. How might this code change if you had 1000+ products?
# If there were 1000+ products the underlying logic wouldn't need much if any change, since the for-in loops work for any sized list, but additional effort would be needed to make the output more useful to the user, since there would be more products recommended for a given number of preferred tags.
# There would likely be many products that would have the same number of matches, with many having all their tags matching user preferences, so additional sorting of those top products would be desired, as well either a possible culling of the bottom options after the first ~100 or so matches, or a GUI which only show a certain amount of matches per page.
# A possible solution to apply additional sorting to the output would be by inputting user priority of preferred tags. E.G. the user would prefer to see products that have the "lightweight" tag over ones that have the "durable" tag, so for products that have the same number of matches, those with the "lightweight" tag would be higher up in the list.
# If the list of products was long enough to run into the limitations of storing or accessing lists in Python (I am unsure of how large that would be), they might need to be stored in such a way that would necessitate additional logic to properly import and convert the list.
# In such a circumstance the list might even need to be compared in chunks of a certain amount of products at a time which would require additional logic to make sure the results were only shown once all comparisons were made.
# If the list of products were even longer such that comparing the tags of all products was infeasible, the products would have to be stored in such a way that only a fraction of them had to be compared to the users preferences, which I would have to research more into, perhaps using hash tables