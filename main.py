import pymupdf4llm
import re
import  ollama 



md_text = pymupdf4llm.to_markdown("data/termo3.pdf")
#convert string to markdown

context = re.sub(r"(?<!\n)\n(?!\n)", " ", md_text) # remove \n only 
context = context.replace("\n\n", "  \n") # replace \n\n with 2 spaces and \n
context = f"""{context}""" 



prompt_gpt = f"""
Gere um dicionário JSON com as seguintes chaves e valores extraídos do termo de compromisso fornecido:

{context}

nome_projeto: o nome do projeto indicado no termo de compromisso.
numero_do_processo: o número do processo indicado no termo de compromisso.
nome_do_bolsista: o nome do bolsista indicado no termo de compromisso.
CPF: o número do CPF do bolsista, localizado logo após o nome,  indicado no termo de compromisso.
vigencia_inicio: a data inicial do termo de compromisso (formato DD-MM-YYYY).
vigencia_fim: a data final do termo de compromisso (formato DD-MM-YYYY).
quantidade_parcelas: a quantidade de bolsas que o bolsista receberá.
valor_parcela: o valor unitário de cada bolsa.
valor_total: o valor total recebido pelo bolsista, calculado como quantidade_parcelas multiplicado pelo valor_parcela.
Importante: Apenas forneça o dicionário completo com base nas informações do termo de compromisso, sem qualquer informação adicional. 
"""	
response = ollama.generate(model="llama3.2:3b", prompt=prompt_gpt, options={'num_ctx':8096, 'temperature':0} )
print(response['response'])




import json
data = json.loads(response['response'])
data['numero_do_processo']
data['valor_total']

