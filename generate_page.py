import yaml
from jinja2 import Template

# Load the ruleset YAML file
with open('ruleset.yaml') as file:
    ruleset = yaml.safe_load(file)

# Extract rule names, descriptions, severities, and values to the respective lists
rules = []
updated_rules = []
disabled_rules = []

for rule_name, rule_details in ruleset['rules'].items():
    if isinstance(rule_details, bool):
        # Rule only has a bool value
        rule = {
            'name': rule_name,
            'toggle': "Enabled" if rule_details is True else "Disabled"
        }
        disabled_rules.append(rule)

    elif isinstance(rule_details, str):
        # Rule only has a string value
        rule = {
            'name': rule_name,
            'severity': rule_details
        }
        updated_rules.append(rule)

    elif isinstance(rule_details, dict) and 'description' in rule_details and 'severity' in rule_details:
        # Rule that have a description and severity
        rule = {
            'name': rule_name,
            'description': rule_details['description'],
            'severity': rule_details['severity']
        }
        rules.append(rule)

# Sort the rules by severity
severity_order = {'error': 0, 'warn': 1, 'info': 2, 'hint': 3}
rules.sort(key=lambda x: severity_order.get(x['severity'], 999))
updated_rules.sort(key=lambda x: severity_order.get(x['severity'], 999))

# Render the template
with open('template.html') as file:
    template = Template(file.read())
    rendered = template.render(rules=rules, updated_rules=updated_rules, disabled_rules=disabled_rules)

# Write the rendered output to index.html
with open('index.html', 'w') as file:
    file.write(rendered)
    print("Page generated successfully!")
