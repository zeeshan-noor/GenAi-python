# How to get started with langchain
- Python Base dev container with using remote explorer
- Poetry Installation : https://python-poetry.org/docs/#installing-with-the-official-installer
```
curl -sSL https://install.python-poetry.org | python3 -
```
Langchain intallation https://python.langchain.com/v0.1/docs/get_started/installation/

```
poetry add langchain-core
poetry add langchain-community

https://python.langchain.com/docs/integrations/llms/openai/#installation

    -  poetry add langchain-openai   
```


- First create openAi platfrom account & purchase api key plan.
```https://platform.openai.com/docs/overview```


- Environment Package Installation to access env variable
```poetry add python_dotenv```
``` 
   from dotenv import load_dotenv 
   load_dotenv()
   ```