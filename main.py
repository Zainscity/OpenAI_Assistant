from dotenv import load_dotenv
import os
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI
load_dotenv()



def main():
    MODEL_NAME = "gemini-2.0-flash"
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    external_client = AsyncOpenAI(
        api_key = GEMINI_API_KEY,
        base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
    )
    model = OpenAIChatCompletionsModel(
        model = MODEL_NAME,
        openai_client=external_client
        )
    assistant = Agent(
        name="Gemini Assistant",
        instructions="You are a helpful assistant.",
        model=model
        )
    result = Runner.run_sync(
        assistant,
        "What is the capital of Pakistan?"
    )
    print(result.final_output)

if __name__ == "__main__":
    main()
