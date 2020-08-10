import os
from typing import *
def get_token() -> Optional[str]:
    return os.getenv('CHEEMSBOT_TOKEN')