
from .agent import ApiAi


class Intent(ApiAi):
    def get_intents(self):
        pass

    def get_intents_by_id(self, id):
        pass

    def create_intents(self, data):
        """
        Creates a new intent.
        :param data: JSON data
        :return: JSON response
        """
        pass

    def update_intent(self, id, data):
        """
        Update given intents
        :param id: Intent ID
        :param data: A valid JSON data
        :return: JSON response
        """
        pass

    def delete_intent(self, id, data):
        """
        Delete specific intent
        :param id: Intent ID
        :param data: A valid JSON data
        :return: JSON response
        """
        pass
