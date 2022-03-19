import pymongo
import os

client = pymongo.MongoClient("mongodb://127.0.0.1:27017")

DATABASE = os.getenv("DATABASE")

db = client[DATABASE]


class Posts:
    def __init__(self, id, created_at, updated_at, **kwargs):
        self.title = kwargs["title"]
        self.author = kwargs["author"]
        self.tags = kwargs["tags"]
        self.content = kwargs["content"]
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at


    def get_posts_models():
        get_all = db.posts.find()

        return get_all

    
    def get_posts_by_id_models(id):
        get_post_by_id = db.posts.find_one({"id": id})

        return get_post_by_id


    def create_posts_models(data):
        create_post = db.posts.insert_one(data)

        found = db.posts.find_one({"_id": create_post.inserted_id})

        return found


    def delete_post_models(id):
        deleted_post = db.posts.find_one_and_delete({"id": id})

        return deleted_post


    def update_post_models(data, id):
        updated_post = db.posts.find_one_and_update({"id": id}, {"$set": data})
        
        return updated_post