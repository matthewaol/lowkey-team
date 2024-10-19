import openai
from uagents import Agent, Context, Model

# Define the message model for receiving dish names
class DishMessage(Model):
    dish_name: str

# Set up OpenAI API key (replace with your OpenAI key)

# Define the agent with a name and seed phrase
agent = Agent(name="alice", seed="secret_seed_phrase", port=8001)

# Event handler for when the agent starts
@agent.on_event("startup")
async def introduce_agent(ctx: Context):
    ctx.logger.info(f"Hello, I'm agent {agent.name} and my address is {agent.address}.")

# Function to generate a recipe using OpenAI's API
def generate_recipe(dish_name):
    # Send the dish name to ChatGPT to generate a recipe
    prompt = f"Generate a recipe for {dish_name}."
    
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can choose the engine (e.g., GPT-4 if available)
        prompt=prompt,
        max_tokens=300  # Adjust token limit based on how detailed you want the response to be
    )
    
    recipe = response.choices[0].text.strip()  # Get the generated text
    return recipe

# Event handler for receiving dish names and returning generated recipes
@agent.on_message(model=DishMessage, replies=set())
async def get_recipe(ctx: Context, sender: str, msg: DishMessage):
    dish_name = msg.dish_name.strip()  # Get the dish name from the message
    ctx.logger.info(f"Received request for recipe: {dish_name}")

    # Generate a recipe using the LLM
    recipe = generate_recipe(dish_name)
    
    # Send the generated recipe back to the sender
    await ctx.send(sender, DishMessage(dish_name=recipe))

if __name__ == "__main__":
    agent.run()
