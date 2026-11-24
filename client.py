import uuid
import secrets

def create_query(domain, record_type="A"):
  query = {
    "type": "DNS_QUERY",
    "transaction_id": str(uuid.uuid4),
    "name": domain,
    "record_type": record_type,
    "nonce": secrets.token_hex(16)
  }

  return query

query = create_query("www.example.com")

print(query)