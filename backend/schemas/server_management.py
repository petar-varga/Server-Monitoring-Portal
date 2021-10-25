from typing import List, Optional
from pydantic import BaseModel

class ExecuteMysqlQueryResponse(BaseModel):
    query_response: Optional[List[dict]]
    query_time_ms: float