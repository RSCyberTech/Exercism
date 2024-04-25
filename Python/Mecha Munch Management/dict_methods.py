"""Functions to manage a users shopping cart items."""

from collections import OrderedDict


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    for i in items_to_add:
        if i not in current_cart.keys():
            current_cart[i] = 1
        else:
            current_cart[i] = current_cart[i] + 1
    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    toRet = {}
    for n in notes:
        toRet[n] = 1
    return toRet


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    for k, v in recipe_updates:
        ideas[k] = v
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items(), key=lambda x: x[0]))


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    for k in cart.keys():
        cart[k] = [cart[k]] + aisle_mapping[k]
    return OrderedDict(sorted(cart.items(), key=lambda x: x[0], reverse=True))


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    for f, v in fulfillment_cart.items():
        store_inventory[f][0] -= v[0]
        if store_inventory[f][0] == 0:
            store_inventory[f][0] = "Out of Stock"
    return store_inventory
