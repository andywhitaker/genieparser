# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/cipher' resources
# =============================================


class LtmCipherSchema(MetaParser):

    schema = {}


class LtmCipher(LtmCipherSchema):
    """ To F5 resource for /mgmt/tm/ltm/cipher
    """

    cli_command = "/mgmt/tm/ltm/cipher"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
