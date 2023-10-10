# Import necessary modules and classes
from uagents import Context
from messages.query_messages import QueryUserRequest, QueryTemperatureResponse, TemperatureStatus

# Import the 'agent' object from the 'temperature_query' module
from agents.temperature_query.temperature_query import agent as query_agent

# Prompt the user for input for location, temperature thresholds, and period
query_location = input("Enter the location for temperature query: ")
query_min_temperature = float(input("Enter the minimum acceptable temperature: "))
query_max_temperature = float(input("Enter the maximum acceptable temperature: "))
query_period = float(3600)

# Define an interval handler for sending periodic temperature queries
@query_agent.on_interval(period=query_period, messages=QueryUserRequest)
async def handle_interval(ctx: Context):
    
    # Send a QueryUserRequest to query the temperature in specified location with specified temperature thresholds
    await ctx.send(query_agent.address, QueryUserRequest(location=query_location, min_temperature=query_min_temperature, max_temperature=query_max_temperature))

# Define a message handler for handling QueryTemperatureResponse messages
@query_agent.on_message(QueryTemperatureResponse)
async def handle_query_response(ctx: Context, _, msg: QueryTemperatureResponse):
    
    # Check the temperature status and log appropriate messages
    if msg.status == TemperatureStatus.COLD or msg.status == TemperatureStatus.HOT:
        ctx.logger.warning(f"{msg.status.value} at {msg.time}!! Current Temperature is {msg.temp}°C.")
        
    else:
        ctx.logger.info(f"{msg.status.value} at {msg.time}!! Current Temperature is {msg.temp}°C.")

# Entry point for the script
if __name__ == "__main__":
    
    # Run the query agent
    query_agent.run()
