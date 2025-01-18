# Amazon Bedrock code agent

This repo creates a code generating agent using Amazon Bedrock. We do this in the following steps:

1. Create prompt templates using Amazon Bedrock Prompt Management.
1. Create an AWS Lambda function that acts as tool for generating the code given the user input.
1. (Optional) create a Amazon Bedrock Knowledge Base that contains content relevant for code generation.
1. Create the agent using the Lambda and the knowledge base.

## Installation

This repo uses `uv` for package management. Follow the steps below to install `uv` and get the required Python packages installed.

```{.bashrc}
git clone https://github.com/aarora79/bedrock-code-agent.git
cd  bedrock-code-agent.git
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv && source .venv/bin/activate && uv pip sync pyproject.toml
```

Run the notebooks in the following order:

1. `0_create_prompt.ipynb`: this notebook creates the prompt templates for code generation. 

1. `1_create_lambda.ipynb`: this notebook creates the AWS Lambda function that is used by the Amazon Bedrock Agent as a tool to generate code.

1. `2_create_knowledge_base.ipynb`: this notebook creates an Amazon Bedrock Knowledge Base with data relevant for code generation.

1. `3_create_agent.ipynb`: this notebook creates the Amazon Bedrock Agent that uses the Lambda and Amazon Bedrock Knowledge Base created earlier.

1. `4_code_generation.ipynb`: this notebook tests the created agent on various code generation tasks.

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the [LICENSE](./LICENSE) file.