from util.general import return_pretty_message
from bson import ObjectId

class MongoFunctions:

    def __init__(self, db, collection):
        self.db = db
        self.collection = collection

    async def list_data(self):
        collection = self.collection.find({})
        if not collection:
            return return_pretty_message({})

        any_collection = await collection.to_list(length=10)
        return any_collection

    async def list_one(self, id):
        return await self.collection.find_one({
            "_id": ObjectId(id)
        })

    def insert_data(self, data):
        self.collection.insert_one(data)

    def update_data(self, **kwargs):
        _id = kwargs["id"]
        kwargs.pop("id")
        self.collection.update_one(
            {"_id": ObjectId(_id)},
            {
                "$set": {
                    **kwargs
                }
            }
        )

    def delete_data(self, _id):
        self.collection.delete_one({
            "_id": ObjectId(_id)
        })