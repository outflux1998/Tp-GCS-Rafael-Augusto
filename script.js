// Exemplo de código JavaScript para inicializar o banco de dados

db.createCollection("users");
db.users.insertOne({ number: "124234", address: "EIRUWOEJI", zipcode: "345-345"});
db.users.insertOne({ number: "124234", address: "EIRUWOEJI", zipcode: "345-345"});
print("Dados inseridos com sucesso!");
