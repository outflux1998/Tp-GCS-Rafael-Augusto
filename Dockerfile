# Define a imagem base
FROM mongo

# Copia o arquivo JavaScript para o diretório correto no contêiner
COPY script.js /docker-entrypoint-initdb.d/

# Define o comando a ser executado quando o contêiner for iniciado
CMD ["mongod"]