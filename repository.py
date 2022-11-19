from firebase_admin import firestore

class ExchangeRepository:

    collection = 'dolar_exchange'

    def __init__(self):
        self.db = firestore.client()

    def save(self, exchange_entity):
        doc_ref = self.db.collection(self.collection).document()
        doc_ref.set(exchange_entity)

