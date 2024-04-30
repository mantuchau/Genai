from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secret_key import openapi_key
import os
os.environ['OPENAI_API_KEY']=openapi_key
llm=OpenAI(temperature=0.7)

def generate_software_servicename(software_company):
    prompt_template_name=PromptTemplate(input_variables=['software_company'],
                                    template="I want to know the different types of services of {software_company}")
    name_chain=LLMChain(llm=llm,prompt=prompt_template_name,output_key='service')
    prompt_template_items=PromptTemplate(input_variables=['service'],
                                    template="Different kinds of software {service} provide by thr company")
    name_chain_item=LLMChain(llm=llm,prompt=prompt_template_items,output_key='Domain_name')
    chain=SequentialChain(
    chains=[name_chain,name_chain_item],
    input_variables=['software_company'],
    output_variables=['service','Domain_name']  # Changed 'services' to 'service'
    )
    response=chain({'software_company':software_company})
    return response


if __name__== "__main__":
    print(generate_software_servicename("TCS"))