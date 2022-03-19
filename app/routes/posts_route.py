from app.controllers.posts_controllers import delete_post_controller, get_posts_by_id_controller, get_posts_controller, create_posts_controller, update_post_controller


def get_posts_route(app):
    @app.get("/posts")
    def read_posts():
        return get_posts_controller()


    @app.get("/posts/<int:id>")
    def read_post_by_id(id):
        return get_posts_by_id_controller(id)


    @app.post("/posts")
    def create_post():
        return create_posts_controller()


    @app.delete("/posts/<int:id>")
    def delete_post(id):
        return delete_post_controller(id)


    @app.patch("/posts/<int:id>")
    def update_post(id):
        return update_post_controller(id)