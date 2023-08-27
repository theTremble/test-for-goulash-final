import configparser
import ast
import os
from jinja2 import Environment, FileSystemLoader

# Create a ConfigParser instance
config = configparser.ConfigParser()

# Read the configuration file
config.read('config.toml')

# Define
section_name = 'sites.testpartner.db'
section_data = config[section_name]

# Extract IPs
db_main_ip = ast.literal_eval(section_data.get('host', fallback=None))
db_slave_ips = ast.literal_eval(section_data.get('slaves', fallback=None))

# Print the extracted IP addresses
print("Main IP ({section}):".format(section=section_name), db_main_ip)
print("Slave IPs ({section}):".format(section=section_name), db_slave_ips)

# Create a Jinja2 environment with the template folder
env = Environment(loader=FileSystemLoader('.'))

# Load the template
template = env.get_template('template.j2')

# Render the template with the extracted data
inventory_content = template.render(db_main_ip=db_main_ip, db_slave_ips=db_slave_ips)

# Write the rendered content to the 'inventory' file
with open('inventory', 'w') as f:
    f.write(inventory_content)
os.rename("/home/ubuntu/ansible/generator/inventory", "/home/ubuntu/ansible/inventory")

print("Inventory file has been generated and moved to the ansible dir")
