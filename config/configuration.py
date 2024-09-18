import os
import yaml


class Configuration:
    """
    Configuration for base URLs.
    """

    def __init__(self):
        # Load the config file once during initialization
        current_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(current_dir, "config.yaml")

        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)

    def get_ui_test_automation_playground_base_url(self):
        # Return the base URL from the loaded config
        return self.config['base_urls']['ui_test_automation_playground_base_url']

    def get_device_name(self):
        # Return the selected device from loaded config
        return self.config['mobile_emulation_device']['device_name']
