
# Projeto: Extração de Dados de Termos de Compromisso em PDF

## Visão Geral
Este projeto foi criado para extrair dados estruturados de termos de compromisso em formato PDF e transformá-los em um dicionário JSON utilizando bibliotecas Python modernas e modelos de inteligência artificial. 

Com este projeto, é possível processar documentos de forma automática e eficiente, gerando resultados prontos para uso em aplicações ou análises.

---

## Funcionalidades
- **Conversão de PDF para Markdown:** O texto do documento é extraído e formatado como Markdown.
- **Limpeza de Dados:** Ajusta a formatação para uma apresentação consistente e estruturada.
- **Geração de JSON:** Utiliza modelos de IA para extrair informações específicas do termo de compromisso.
- **Cálculo Automático:** Calcula valores totais com base nos dados extraídos.

---

## Pré-requisitos
- **Python:** 3.11
- **Bibliotecas Necessárias:** 
  - `pymupdf4llm` para manipulação de PDFs.
  - `ollama` para geração de respostas inteligentes.
  - `re` para processamento de texto.
  - `json` para manipulação de dados estruturados.

Instale as dependências utilizando:
```bash
pip install pymupdf4llm ollama
```

---

## Como Usar

### 1. Configuração Inicial
Certifique-se de que o Python 3.11 está instalado em sua máquina e instale as bibliotecas listadas nos pré-requisitos.

### 2. Preparar o Documento
Coloque o arquivo PDF que deseja processar na pasta `data/` e nomeie-o como `termo3.pdf`.

### 3. Executar o Script
Rode o script principal para processar o PDF e gerar o JSON:
```bash
python script.py
```

### 4. Acessar os Resultados
Os dados extraídos estarão disponíveis no console e serão salvos em um arquivo JSON na pasta `output/`.

---

## Estrutura do JSON
O JSON gerado seguirá o modelo abaixo:

```json
{
    "nome_projeto": "Nome do projeto",
    "numero_do_processo": "Número do processo",
    "nome_do_bolsista": "Nome do bolsista",
    "CPF": "CPF do bolsista",
    "vigencia_inicio": "DD-MM-YYYY",
    "vigencia_fim": "DD-MM-YYYY",
    "quantidade_parcelas": 12,
    "valor_parcela": 1500.00,
    "valor_total": 18000.00
}
```

---

## Exemplo de Uso
Após rodar o script com um arquivo de exemplo, o seguinte resultado poderá ser gerado:
```json
{
    "nome_projeto": "Projeto de Pesquisa ABC",
    "numero_do_processo": "12345/2024",
    "nome_do_bolsista": "João da Silva",
    "CPF": "123.456.789-00",
    "vigencia_inicio": "01-01-2024",
    "vigencia_fim": "31-12-2024",
    "quantidade_parcelas": 12,
    "valor_parcela": 1500.00,
    "valor_total": 18000.00
}
```

---

## Estrutura do Projeto
```plaintext
.
├── data/
│   └── termo3.pdf           # Arquivo PDF a ser processado
├── output/
│   └── dados_extraidos.json # JSON gerado após o processamento
├── script.py                # Script principal do projeto
├── README.md                # Este arquivo
```

---
