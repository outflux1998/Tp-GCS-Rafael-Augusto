# Usa uma imagem base do Python
FROM python:'3.9'

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências do projeto
RUN pip install -r requirements.txt

# Copia todo o conteúdo do diretório atual para o diretório de trabalho
COPY . .

# Expõe a porta 8000 para acesso externo
EXPOSE 8000

# Define o comando de inicialização do contêiner
CMD ["python", "main.py"]