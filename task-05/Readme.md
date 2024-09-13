# TerminalTrolly


## Features

- **list**: Displays all available products.
- **details _product_id_**: View details of a specific product identified by its ID.
- **add _product_id_**: Add a specific product to your cart using its ID.
- **remove _product_id_**: Remove a product from your cart by its ID.
- **cart**: View the current items in your cart.
- **buy**: Redirect to a new page to review items in your cart and finalize your purchase.
- **clear**: Clear the terminal screen.
- **search _product_name_**: Search for a product by its name.
- **sort _price/name_**: Sort the products based on the price or name.

## Key features

1. The important functions such as sort were already present in the documentation of the api store and it only had to be adjusted to be seen in the output of terminal present in the webpage instead of the console.
2. The viewbyu() method converts the cart and price into query string to pass on the data and is accessed by the checkout.html
3. Query string helps you to pass data between different pages without server-side strorage requirement and the data is part of the url so its simple to access as it is visible to all(not beneficial for sensitive information)