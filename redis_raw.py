import redis


redis_conn = redis.Redis(host="localhost", port=6379, db=0)


#insert e update
redis_conn.set("chave_1", "mudar_valor")

# select
meu_valor = redis_conn.get("chave_1").decode("utf-8")
print(meu_valor)
print(type(meu_valor))

#delete
redis_conn.delete("chave_1")



# commands for hast
meu_hash={
    "nome":"joao",#field value
    "idade":22,
    "cidade":"salvador"
}

redis_conn.hset("meu_hash", "nome", "joao")
redis_conn.hset("meu_hash", "idade", "30")
redis_conn.hset("meu_hash", "cidade", "salvador")


valor_1 = redis_conn.hget("meu_hash", "nome").decode("utf-8")
print(valor_1)

redis_conn.hdel("meu_hash","cidade")


## buscar por existencia

elem = redis_conn.exists("chave_1")
print(elem)


elem2 = redis_conn.hexists("meu_hast","idade")
print(elem2)


#### expiraçao de dados
#dados -> TTL -> Time To Live [segundos]
redis_conn.set("chave_del", "esse valor sera deletado", 12)
redis_conn.expire("meu_hash",30)
