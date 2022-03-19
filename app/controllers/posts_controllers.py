from app.models.posts_models import Posts
from flask import jsonify, request
from datetime import datetime
import os

ACCEPTED_KEYS = os.getenv("ACCEPTED_KEYS")


def get_posts_controller():
    get_posts = Posts.get_posts_models()

    get_posts_list = list(get_posts)

    for i in get_posts_list:
        del i["_id"]


    return jsonify(get_posts_list), 200


def get_posts_by_id_controller(id):
    try:
        get_post_by_id = Posts.get_posts_by_id_models(id)

        del get_post_by_id["_id"]


        return get_post_by_id, 200
    except:
        return {"msg": f"ID {id} not found"}, 404


def create_posts_controller():
    try:
        date = datetime.now()
        actual_date = date.strftime("%d/%m/%y %H:%M:%S")

        data = request.get_json()

        get_posts = Posts.get_posts_models()

        get_posts_list = list(get_posts)

        if(len(get_posts_list) == 0):
            new_id = 1
        else:
            previous_object = get_posts_list[-1]
            new_id = previous_object["id"] + 1


        new_data = Posts(new_id, actual_date, actual_date, **data)

        found = Posts.create_posts_models(new_data.__dict__)

        del found["_id"]


        return found, 201

    except:
        return {
            "error": "wrong fields", 
            "required_fields": [
                {"title": "Title"},
                {"author": "Author"},
                {"tags": "Tags"},
                {"content": "Content"}
            ]
        }, 400


def delete_post_controller(id):
    try:
        deleted_post = Posts.delete_post_models(id)

        del deleted_post["_id"]


        return deleted_post, 200

    except:
        return {"error": f"ID {id} not found"}, 404


def update_post_controller(id):
    try:
        data = request.get_json()

        accepted = ACCEPTED_KEYS.split(", ")
        
        for key in data.keys():
            if(key not in accepted):
                return {
                    "error": f"field '{key}' doesn't exists and cannot be updated!"
                }, 400

        if(len(data) == 0):
            return {
                "error": "You must pass the data!"
            }, 400


        date = datetime.now()
        actual_date = date.strftime("%d/%m/%y %H:%M:%S")

        data.update({"updated_at": actual_date})

        updated_post = Posts.update_post_models(data, id)

        show_updated_post = Posts.get_posts_by_id_models(id)
        
        del show_updated_post["_id"]
        

        return show_updated_post, 200

    except:
        return {
            "error": f"ID {id} not found!"
        }, 404