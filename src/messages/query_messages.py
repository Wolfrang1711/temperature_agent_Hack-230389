from enum import Enum
from uagents import Model

class TemperatureStatus(str, Enum):
    COLD = "Temperature Alert: It's Cold"
    HOT = "Temperature Alert: It's Hot"
    NORMAL = "Temperature is Normal"
    
class QueryUserRequest(Model):
    location: str
    max_temperature: float
    min_temperature: float
    
class QueryTemperatureResponse(Model):
    status: TemperatureStatus
    time: str
    temp: float
