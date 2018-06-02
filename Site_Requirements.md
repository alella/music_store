Website Requirements
=====================

- **User signup**: Register a new user to the system.
 - Check the new username or email address if it’s already registered to the system using AJAX.
  - Form validation: Check if all mandatory fields are filled out. (JQuery)
  - Check if password is strong enough. Define the rules of having a strong password. (JQuery). User passwords should be hashed and hashed version of passwords should be stored in the database.
- User login
- List available products/services in the system. User should be able to filter the results based on at least one criterion (i.e.category). Also, should be able to search for a specific item. Search and filtering should be integrated together.
- Implement a page for listing products/services.
- Add item(s) to the cart and checkout. For the online shopping sites, pricing will be included but payment functionality doesn't need to be implemented. However, you will keep track of inventory. For websites where a shopping cart does not exist, you can implement Wish list or Favorites and save those listings.
- For the websites where shopping cart is implemented, user should be able to update items in the cart (remove items from the cart, update their quantity)
- Show the history of purchases or saved lists for the user.
- For Admin user(s):
  - List all items
  - Add new item
  - Delete item
  - Update item

- Admin user will have the same interface with regular users, except that he/she will be provided extra features (buttons/links) for update and deletion of products/services.

- While adding items to the system, admin user should be able to upload pictures for the items and while updating items, should be able to change pictures.

- For delete, soft-delete should be implemented.
