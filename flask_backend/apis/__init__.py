from flask_restx imort Api
from .community import community
from .home import home
from .profile import profile

api = Api(
        title="Mission Together",
        version="1.0",
        description="Review application for students",
        )

api.add_namespace(home)
api.add_namespace(community)
api.add_namespace(profile)
