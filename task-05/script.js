const terminalOutput = document.querySelector('.terminal-output');
const terminalInput = document.querySelector('input[type="text"]');

function handleInput(command) {

    const detailsMatch = command.match(/^details\s+(\d+)$/);
    const addMatch = command.match(/^add\s+(\d+)$/);
    const removeMatch = command.match(/^remove\s+(\d+)$/);
    const searchMatch = command.match(/^search\s+(.+)$/);
    const sortMatch = command.match(/^sort\s+(price|name)$/);

    if (detailsMatch) {
        const productId = detailsMatch[1];
        details(productId);
    }
    else if (addMatch) {
        const productId = addMatch[1];
        Add(productId);
    } 
    else if (removeMatch) {
        const productId = removeMatch[1];
        Remove(productId);
    } 
    else if (searchMatch) {
        const productName = searchMatch[1];
        viewSearch(productName);
    } 
    else if (sortMatch) {
        const criteria = sortMatch[1];
        sort(criteria);
    }
    else {
        switch (command) {
            case 'help':
                viewCommand();
                break;

            case 'list':
                viewList();
                break;

            case 'cart':
                viewCart();
                break;

            case 'buy':
                viewBuy();
                break;

            case 'clear':
                viewClear();
                break;

            default:
                terminalOutput.textContent += `Invalid command: ${command}\n`;
                break;
        }
    }

    terminalInput.value = '';  
}


const imgElements = document.querySelectorAll('.rows img');

imgElements.forEach((imgElement, index) => {
    const productId = index + 1;
    fetch('https://fakestoreapi.com/products/' + productId)
        .then(res => res.json())
        .then(json => {
            const img = json.image;
            imgElement.src = img;
        })
        .catch(error => console.error('Error fetching product:', error));
});


function viewCommand() {
    terminalOutput.textContent += `
    - list: "Display all available products."
    - details: "'product_id': View details of a specific product identified by its ID."
    - add: "'product_id': Add a specific product to your cart using its ID."
    - remove: "'product id': To remove the product from the cart."
    - cart: "View the current items in your cart."
    - buy: "Proceed to a new webpage where you can review items in your cart along with the total price, enabling you to finalize your purchase."
    - clear: "Clear the terminal screen."
    - search: "'product_name': Search a product by name."
    - sort: "'price/name': Sort the products based on the price or the name."`;
}


function viewList() {
    fetch("https://fakestoreapi.com/products")
        .then(res => res.json())
        .then(data => {
            data.forEach(item => {
                terminalOutput.textContent += `- ${item.title}\n`;
            });
        });
}


function details(productId) {
    fetch(`https://fakestoreapi.com/products/${productId}`)
        .then(res => res.json())
        .then(json => {
            terminalOutput.textContent += `- ${json.title}\n` +
                                          `- ${json.category}\n` +
                                          `- ${json.description}\n` +
                                          `- $${json.price}\n`;
        });
}


let cart = [];
let total = 0;


function Add(productId) {
    fetch(`https://fakestoreapi.com/products/${productId}`)
        .then(res => res.json())
        .then(json => {
            cart.push(json);
            total += json.price;
        });
}


function Remove(productId) {
    const index = cart.findIndex(product => product.id == productId);
    if (index !== -1) {
        total -= cart[index].price;
        cart.splice(index, 1);
    }
}


function viewCart() {
    terminalOutput.textContent += "Current items in cart:\n";
    cart.forEach(item => {
        terminalOutput.textContent += `${item.title} - $${item.price.toFixed(2)}\n`;
    });
    terminalOutput.textContent += `Total: $${total.toFixed(2)}\n`;
}


function viewClear() {
    terminalOutput.textContent = ''; 
}


function viewSearch(productName) {
    fetch("https://fakestoreapi.com/products")
        .then(res => res.json())
        .then(data => {
            const searchResults = data.filter(item => 
                item.title.toLowerCase().includes(productName.toLowerCase())
            );

            if (searchResults.length > 0) {
                terminalOutput.textContent += `Search results for "${productName}":\n`;
                searchResults.forEach(item => {
                    terminalOutput.textContent += `- ${item.title} - $${item.price.toFixed(2)}\n`;
                });
            } else {
                terminalOutput.textContent += `No products found matching "${productName}".\n`;
            }
        });
}


function sort(criteria) {
    const url = 'https://fakestoreapi.com/products?sort=desc';

    fetch(url)
        .then(res => res.json())
        .then(data => {
            if (criteria === 'price') {
                data.sort((a, b) => a.price - b.price);
            } else if (criteria === 'name') {
                data.sort((a, b) => a.title.localeCompare(b.title));
            }

            terminalOutput.textContent += `Products sorted by ${criteria}:\n`;
            data.forEach(item => {
                terminalOutput.textContent += `- ${item.title} - $${item.price.toFixed(2)}\n`;
            });
        })
        .catch(error => console.error('Error fetching products:', error));
}


function viewBuy() {
    const queryString = new URLSearchParams({ cart: JSON.stringify(cart), total }).toString();
    window.location.href = `checkout.html?${queryString}`;
}



document.getElementById('command').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        const command = e.target.value.trim();
        handleInput(command); 
    }
});
