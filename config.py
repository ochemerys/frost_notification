import configparser

# Create a configuration object
config = configparser.ConfigParser()

def get_configuration(key):
    # Load the configuration file
    config.read('app_config.ini')

    # Get the value associated with the key from the configuration file
    return config['APP_CONFIG'].get(key)