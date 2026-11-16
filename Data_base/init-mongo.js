const database = db.getSiblingDB("cadastro_clientes");

if (!database.getCollectionNames().includes("clientes")) {
    database.createCollection("clientes");
    print("Coleção clientes criada!");
} else {
    print("Coleção clientes já existe.");
}

print("Banco cadastro_clientes preparado!");