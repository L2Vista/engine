# import warnings
# warnings.filterwarnings('ignore')

from langchain.chat_models import ChatOpenAI

from typing import Tuple

import templetes
import check


"""LLM"""
llm = ChatOpenAI(
    # model_name="gpt-4",
    model_name='gpt-3.5-turbo-16k',
    temperature=0.9
)  # Can be any valid LLM
# https://platform.openai.com/docs/models/gpt-4


# [LLM output, (from_chain, to_chain, category, address, tx_hash)]
def conversation(human_input: str) -> Tuple[str, Tuple[str, str, str, str, str]]:
    """check input"""
    ai_output = llm.predict(
        templetes.l2vista_prompt.format(
            input=human_input
        )
    )

    """parsing"""
    parsed_output = llm.predict(
        templetes.parsing_prompt.format(
            human_input=human_input,
            ai_response=ai_output,
        )
    )
    # print(parsed_output)

    return (
        ai_output.replace("L2Vista Chatbot:", ""),
        check.parse(parsed_output)
    )


if __name__ == "__main__":
    while True:
        human_input = input("🥰: ")
        print("💻:", conversation(human_input))
