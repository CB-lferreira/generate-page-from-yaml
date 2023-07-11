import yaml
from jinja2 import Template

# Load the ruleset YAML file
with open('ruleset.yaml') as file:
    ruleset = yaml.safe_load(file)

# Extract rule names, descriptions, and severities
rules = []

for rule_name, rule_details in ruleset['rules'].items():
    if isinstance(rule_details, dict) and 'description' in rule_details and 'severity' in rule_details:
        rule = {
            'name': rule_name,
            'description': rule_details['description'],
            'severity': rule_details['severity']
        }
        rules.append(rule)

# Render the template
with open('template.html') as file:
    template = Template(file.read())
    rendered = template.render(rules=rules)

# Write the rendered output to index.html
with open('index.html', 'w') as file:
    file.write(rendered)
