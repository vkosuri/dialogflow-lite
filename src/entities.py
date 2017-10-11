
from .agent import Dialogflow


class Entities(Dialogflow):
    def get_entities(self):
        """
        Retrieves a list of all entities for the agent.
        :return: JSON response
        """
        pass

    def get_entitiy(self, id):
        """
        Retrieves the specified entity
        :param id: Entity ID
        :return: JSON response
        """
        pass

    def create_entities(self, data):
        """
        create a new entity
        :param data: A valid JSON data
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