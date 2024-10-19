from uagents import Agent, Context, Model

# Define a message model for sending dish names
class DishMessage(Model):
    dish_name: str

# Set the address for "alice" agent
ALICE_ADDRESS = "agent1qtu6wt5jphhmdjau0hdhc002ashzjnueqe89gvvuln8mawm3m0xrwmn9a76"  # Replace with actual address from alice's log

# Define bob agent
agent = Agent(name="bob", seed="bob_secret_seed")

@agent.on_interval(period=2.0)
async def send_message(ctx: Context):
    ctx.logger.info(f"Sending a dish name to alice at {ALICE_ADDRESS}")
    await ctx.send(ALICE_ADDRESS, DishMessage(dish_name="spaghetti"))

@agent.on_message(model=DishMessage, replies=set())
async def on_recipe_received(ctx: Context, sender: str, msg: DishMessage):
    ctx.logger.info(f"Received recipe from {sender}: {msg.dish_name}")

if __name__ == "__main__":
    agent.run()
