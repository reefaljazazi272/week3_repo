from langchain_core.prompts import PromptTemplate

template="You are a  tech expert.Explain {concept}  simply."

prompt= PromptTemplate(input_variables=["concept"],template=template)

formatted_prompt=prompt.format(concept="Generative AI")

print(formatted_prompt)