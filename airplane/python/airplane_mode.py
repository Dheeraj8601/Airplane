# Import necessary modules
from frappe import _

# Define the route handler function
def get_show_me_page(context):
    # Get the color value from the query parameter
    color = frappe.form_dict.get('color', 'black')  # Default to black if no color is provided
    
    # Render the HTML template with the color value
    context.update({
        'color': color
    })
    return {
        'template': 'show_me.html',
        'context': context
    }

# Define the route in the hooks.py file
# Assuming you are using Frappe framework
# Define the hook in your app's hooks.py file
# This will map the route to the route handler function
def get_website_routes():
    return [
        {
            'from_route': '/show-me',
            'to_method': 'path.to.your.module.get_show_me_page'
        }
    ]
