from src.agents.react_agent import agent


def main():
    question = "What is 15 multiplied by 8 and divided by 3?"

    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": question
                }
            ]
        }
    )

    print(response["messages"][-1].content)


if __name__ == "__main__":
    main()