import logging

import requests

from integrations.common.wrapper import AbstractBaseIdentityIntegrationWrapper

logger = logging.getLogger(__name__)

HEAP_API_URL = "https://heapanalytics.com"


class HeapWrapper(AbstractBaseIdentityIntegrationWrapper):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.url = f"{HEAP_API_URL}/api/track"

    def _identify_user(self, user_data: dict) -> None:
        response = requests.post(self.url, json=user_data)
        logger.debug("Sent event to Heap. Response code was: %s" % response.status_code)

    def generate_user_data(self, user_id, feature_states):
        feature_properties = {}

        for feature_state in feature_states:
            value = feature_state.get_feature_state_value()
            feature_properties[feature_state.feature.name] = (
                value if (feature_state.enabled and value) else feature_state.enabled
            )

        return {
            "app_id": self.api_key,
            "identity": user_id,
            "event": "Flagsmith Feature Flags",
            "properties": feature_properties,
        }
