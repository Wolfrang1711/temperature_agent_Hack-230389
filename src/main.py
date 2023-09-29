from uagents import Context
from messages.query_messages import QueryUserRequest, QueryTemperatureResponse, TemperatureStatus

from agents.temperature_query.temperature_query import agent as query_agent

@query_agent.on_interval(period=3600.0, messages=QueryUserRequest)
async def interval(ctx: Context):
    
    await ctx.send(query_agent.address, QueryUserRequest(location='New Delhi', min_temperature=20.0, max_temperature=50.0))

@query_agent.on_message(QueryTemperatureResponse)
async def handle_query_response(ctx: Context, _, msg: QueryTemperatureResponse):
    
    if msg.status == TemperatureStatus.COLD or msg.status == TemperatureStatus.HOT:
        ctx.logger.warn(f"{msg.status.value} at {msg.time}!! Current Temperature is {msg.temp}°C.") 
        
    else:
        ctx.logger.info(f"{msg.status.value} at {msg.time}!! Current Temperature is {msg.temp}°C.")   
             
if __name__ == "__main__":
    
    query_agent.run()
