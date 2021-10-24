from typing import List

from models.user import User

from fastapi import APIRouter, Depends

# importing custom dependencies
from api.deps import pwd_context, oauth2_scheme, basic_auth
from api.deps import get_current_active_user

from models.vultr_instance import ServerInstance

router = APIRouter()

@router.get("/list", response_model=List[ServerInstance])
async def list_vultr_instances(current_user: User = Depends(get_current_active_user)):
    vultr_instances = [
        ServerInstance(**{
            "id": 1,
            "serverInfo": {
                "name": "MFS Prod",
                "ip": "127.0.0.1"
            },
            "operatingSystem": "Ubuntu",
            "status": 'Running',
        }),
        ServerInstance(**{
            "id": 2,
            "serverInfo": {
                "name": "MFS Prod",
                "ip": "127.0.0.1"
            },
            "operatingSystem": "CentOS",
            "status": 'Stopped',
        })
    ]
    return vultr_instances
