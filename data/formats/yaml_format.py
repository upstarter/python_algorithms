import yaml
with open('tree.yaml') as f:
    # use safe_load instead load
    dataMap = yaml.safe_load(f)
