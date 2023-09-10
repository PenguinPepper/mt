rom flask_restx import Namespace, Resource, fields
from flask import request
from models.user import User
from models.review import Review

communit_ns = Namespace('Community',
                        description='Community related operations')

community = api.model('Community', {
    'name': fields.String(),
    'surname': fields.String(),
    'cohort_no': fields.Integer(),
    'prodile-id': fields.Integer(),
    'review_percent': fields.Integer(),
    })


@communit_ns.route('/')
class CommunityList(Resource):
    """"Retrieve a list of all users from database
    from that list capture the profile_id
    use the profile_id to query the table for reviews and get the
    lastest review text
    Return: the name of users, surname, cohort_no and review percentage
    """

    @api.doc('Community_list')
    @marshal_list_with(comunity)
    def get(self):
        all_users = storage.all(User).values()
        list_users = []
        for user in all_users:
            list_users.append(user.to_dict())

        review = ""        for people in list_users:
            """How about i create a link between profile_id
            in user table with review tabele and query that instead"""
            review = storage.get(Review, list_users[people][profile_id])

        objects = {"name": list_users.name,
                   "surname": list_users.surname,
                   "cohort-no": list_users.cohort_no,
                   "review_percentage": review.percent}

        return objects


@communit_ns.route("/community/<int:profile_id>")
class CommunityReview(Resource):
    """"Review a comunity memebers profile"""

    @api.doc(description="Review a users profile")
    @api.marshal_with(community)
    def post(self):
        """"Leave a review"""
        if not request.get_json():
            api.abort(400, "This is not valid JSON")

        data = request.get_json()

        new_review = Review(
                )
