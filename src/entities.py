
from .agent import Dialogflow


class Entities(Dialogflow):
    def __init__(self):
        self.entity_url = self.base_url + '/entities'
        self.headers = {
            'Authorization': 'Bearer ' + self.developer_access_token,
        }
        self.session.headers.update(self.headers)

    def get_entities(self):
        """
        Retrieves a list of all entities for the agent.
        :return: JSON response
        """
        params = (
            ('v', self.api_version),
            ('lang', self.language),
            ('sessionId', self.session_id),
            ('timezone', self.timezone),
        )

        return self.session.get(url=self.entity_url, params=params).json()

    def get_entitiy(self, entity_id):
        """
        Retrieves the specified entity
        :param id: Entity ID
        :return: JSON response
        """
        params = (
            ('v', self.api_version),
            ('lang', self.language),
            ('sessionId', self.session_id),
            ('timezone', self.timezone),
        )
        entity_url = self.entity_url + "/{}".format(entity_id)
        return self.session.get(url=entity_url, params=params).json()

    def create_entities(self, data):
        """
        create a new entity
        :param data: A valid JSON data, example data
        {
            "name": "Appliances",
            "entries": [{
                "value": "Coffee Maker",
                "synonyms": ["coffee maker", "coffee machine", "coffee"]
            }, {
                "value": "Thermostat",
                "synonyms": ["Thermostat", "heat", "air conditioning"]
            }, {
                "value": "Lights",
                "synonyms": ["lights", "light", "lamps"]
            }, {
                "value": "Garage door",
                "synonyms": ["garage door", "garage"]
            }]
        }
        :return: JSON response
        """
        pass

    def add_entities(self, id, data):
        """
        Adds an array of entity entries to the specified entity.
        :param id: Entity ID
        :param data: A valid JSON data
        :return: JSON response
        """
        pass

    def update_entities(self, data):
        """
        Creates or updates multiple entities
        :param data: A valid JSON data
        :return: JSON response
        """
        pass

    def update_entity_entries(self, id, data):
        """
        Updates an array of entity entries in the specified entity
        :param id: Entity ID
        :param data: A valid JSON data
        :return: JSON response
        """
        pass

    def delete_entity(self, id):
        """
        Deletes the specified entity
        :param id: Entity ID
        :return: JSON response
        """
        pass

    def delete_entity_entries(self, id, data):
        """
        Deletes an array of entity entries from the specified entity
        :param id: Entity ID
        :param data: A valid JSON data
        :return: JSON response
        """
        pass