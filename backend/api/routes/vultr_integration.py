from typing import List
import requests
import json

from models.user import User
from models.vultr_instance import ServerInstance

from fastapi import APIRouter, Depends

# importing custom dependencies
from api.deps import pwd_context, oauth2_scheme, basic_auth
from api.deps import get_current_active_user

from core.config import settings

router = APIRouter()

def get_vltr_instances():
    url = "https://api.vultr.com/v2/instances"

    payload={}
    headers = {
        'Authorization': f'Bearer {settings.V_API_KEY}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    json_object = json.loads(response.text)

    return json_object

@router.get("/list", response_model=List[ServerInstance])
async def list_vultr_instances(current_user: User = Depends(get_current_active_user)):
    vultr_instances = []
    for instance in get_vltr_instances()["instances"]:
        id = instance["id"]
        name = instance["label"]
        ip = instance["main_ip"]
        operating_system = instance["os"]
        power_status = instance["power_status"]
        server_instance = ServerInstance(**{
            "id": id,
            "server_info": {
                "name": name,
                "ip": ip
            },
            "operating_system": operating_system,
            "status": power_status,
        })
        vultr_instances.append(server_instance)

    return vultr_instances
