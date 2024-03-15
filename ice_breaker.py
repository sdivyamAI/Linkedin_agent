from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from third_parties.linkedin import scrape_linkedin_profile
from langchain_core.prompts import PromptTemplate
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from output_parser import person_intel_parser, PersonIntel


def ice_break(name: str) -> tuple[PersonIntel, str]:
    linkedin_profile_url = linkedin_lookup_agent(name=name)

    summary_template = """
    given the information {information} about a person I want you to create:
    1. A short summary 
    2. two interesting facts about them
    \n{format_instructions}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": person_intel_parser.get_format_instructions()
        },
    )
    llm = ChatOpenAI(temperature=0, model_name="gpt-4-0125-preview")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)
    result = chain.run(information=linkedin_data)
    print(result)

    return person_intel_parser.parse(result), linkedin_data.get("profile_pic_url")


if __name__ == "__main__":
    load_dotenv()
    # ice_break(name="Harrison Chase")
