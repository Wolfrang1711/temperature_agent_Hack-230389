from uagents import Agent, Context
from messages.query_messages import QueryUserRequest, QueryTemperatureResponse, TemperatureStatus
from uagents.setup import fund_agent_if_low
from utils import weather_api

agent = Agent(name="temperature_query", port=8000, seed="temperature_query_seed", endpoint="http://127.0.0.1:8000/submit")

fund_agent_if_low(agent.wallet.address())

@agent.on_message(model=QueryUserRequest, replies={QueryTemperatureResponse})
async def handle_query_request(ctx: Context, sender: str, msg: QueryUserRequest):

    api_status, api_time, api_temp = weather_api.fetch_data(msg.location)
    
    if api_status is True:
           
        if api_temp <= msg.min_temperature:
            status = TemperatureStatus.COLD
            
        elif api_temp >= msg.max_temperature:
            status = TemperatureStatus.HOT
            
        else:
            status = TemperatureStatus.NORMAL           
            
    await ctx.send(sender, QueryTemperatureResponse(status=status, time=api_time, temp=api_temp))           