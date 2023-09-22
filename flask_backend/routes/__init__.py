#!/usr/bin/env python3
""""Namespaces for app"""

from flask_restx import Api
from .community import communit_ns
from .home import home_ns
from .profile import profile_ns

api = Api(
        title="Mission Together",
        version="1.0",
        description="Review application for students"
        )

api.add_namespace(home_ns, path='/missiontogether/home/')
api.add_namespace(communit_ns, path='/missiontogether/community/')
api.add_namespace(profile_ns, path='/missiontogether/profile/')

