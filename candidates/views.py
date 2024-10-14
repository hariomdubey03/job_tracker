import logging
from django.db import IntegrityError
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from job_tracker.utils import custom_exceptions as ce
from job_tracker.utils.custom_validator import CustomValidator
from candidates import schemas
from candidates.models import Candidate

logger = logging.getLogger("candidates")
c_validator = CustomValidator({}, allow_unknown=True)


class CandidatesAPIView(APIView):
    """
    Handles CRUD candidates on Candidate data.
    """

    permission_classes = (AllowAny,)

    def get(self, request):
        """
        Retrieve candidates based on search criteria.
        """
        try:
            is_valid = c_validator.validate(
                request.query_params, schemas.CANDIDATE_GET
            )

            if is_valid:
                return retrieve_candidates(request)
            else:
                raise ce.ValidationFailed(
                    {
                        "message": "Some validations have failed",
                        "data": c_validator.errors,
                    }
                )

        except ce.ValidationFailed as vf:
            logger.error("CANDIDATES API VIEW - GET: {}".format(vf))
            raise

        except Exception as e:
            logger.error("CANDIDATES API VIEW - GET: {}".format(e))
            raise ce.InternalServerError

    def post(self, request):
        """
        Create a new Candidate.
        """
        try:
            is_valid = c_validator.validate(
                request.data, schemas.CANDIDATE_POST
            )

            if is_valid:
                return create_candidate_instance(request)
            else:
                raise ce.ValidationFailed(
                    {
                        "message": "Some validations have failed",
                        "data": c_validator.errors,
                    }
                )

        except ce.ValidationFailed as vf:
            logger.error("CANDIDATES API VIEW - POST: {}".format(vf))
            raise

        except Exception as e:
            logger.error("CANDIDATES API VIEW - POST: {}".format(e))
            raise ce.InternalServerError

    def patch(self, request, candidate_id):
        """
        Partially update a Candidate's information.
        """
        try:
            is_valid = c_validator.validate(
                request.data, schemas.CANDIDATE_PATCH
            )

            if is_valid:
                return update_candidate_instance(candidate_id, request)
            else:
                raise ce.ValidationFailed(
                    {
                        "message": "Some validations have failed",
                        "data": c_validator.errors,
                    }
                )

        except ce.ValidationFailed as vf:
            logger.error("CANDIDATES API VIEW - PATCH: {}".format(vf))
            raise

        except Exception as e:
            logger.error("CANDIDATES API VIEW - PATCH: {}".format(e))
            raise ce.InternalServerError

    def delete(self, request, candidate_id):
        """
        Delete a Candidate by their ID.
        """
        try:
            return delete_candidate_instance(candidate_id)

        except ce.ValidationFailed as vf:
            logger.error("CANDIDATES API VIEW - DELETE: {}".format(vf))
            raise

        except Exception as e:
            logger.error("CANDIDATES API VIEW - DELETE: {}".format(e))
            raise ce.InternalServerError


def retrieve_candidates(request) -> Response:
    """
    Retrieve candidate data based on search criteria.
    """
    try:
        """Using Full-text index here.
        Using Full-text indexing offers better performance and scalability than icontains, as it's optimized for
        large datasets and supports advanced search features like tokenization and relevance ranking.
        """

        name = request.query_params.get("name")
        query = f"""
            SELECT
                id,
                name
            FROM
                candidates_candidate
            WHERE
                MATCH(name) AGAINST('{name}')
            order by
                MATCH(name) AGAINST('{name}') desc;
        """

        candidates = Candidate.objects.raw(query)
        if candidates:
            results = [
                {"candidate_id": candidate.id, "name": candidate.name}
                for candidate in candidates
            ]
            return Response(
                {
                    "message": "Candidates found successfully",
                    "data": results,
                },
                status=status.HTTP_200_OK,
            )

        return Response(
            {
                "message": "No candidates found",
                "data": None,
            },
            status=status.HTTP_404_NOT_FOUND,
        )

    except Exception as e:
        logger.error("RETRIEVE CANDIDATES: {}".format(e))
        raise ce.InternalServerError


def create_candidate_instance(request) -> Response:
    """
    Create a new Candidate instance.
    """
    try:
        candidate = Candidate.objects.create(
            name=request.data.get("name").title(),
            age=request.data.get("age"),
            gender=request.data.get("gender").lower(),
            email=request.data.get("email"),
            phone_number=request.data.get("phone_number"),
        )
        return Response(
            {
                "message": "Candidate created successfully",
                "data": {"id": candidate.id},
            },
            status=status.HTTP_201_CREATED,
        )

    except IntegrityError:
        return Response(
            {
                "message": "Candidate already exists.",
                "data": None,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    except Exception as e:
        logger.error("CREATE CANDIDATE INSTANCE: {}".format(e))
        raise ce.InternalServerError


def update_candidate_instance(candidate_id, request) -> Response:
    """
    Partially update a Candidate instance.
    """
    try:
        candidate = Candidate.objects.get(id=candidate_id)

        for key, value in request.data.items():
            setattr(candidate, key, value)

        candidate.save()
        return Response(
            {
                "message": "Candidate updated successfully",
                "data": {
                    "candidate_id": candidate.id,
                    "name": candidate.name,
                },
            },
            status=status.HTTP_200_OK,
        )

    except IntegrityError:
        return Response(
            {
                "message": "Candidate already exists.",
                "data": None,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    except Candidate.DoesNotExist:
        return Response(
            {
                "message": "Candidate not found",
            },
            status=status.HTTP_404_NOT_FOUND,
        )

    except Exception as e:
        logger.error("UPDATE CANDIDATE INSTANCE: {}".format(e))
        raise ce.InternalServerError


def delete_candidate_instance(candidate_id) -> Response:
    """
    Delete a Candidate by their ID.
    """
    try:
        candidate = Candidate.objects.filter(id=candidate_id).first()
        if candidate:
            candidate.delete()
            return Response(
                {
                    "message": "Candidate deleted successfully",
                    "data": None,
                },
                status=status.HTTP_200_OK,
            )

        return Response(
            {
                "message": "Candidate does not exist",
                "data": None,
            },
            status=status.HTTP_404_NOT_FOUND,
        )

    except Exception as e:
        logger.error("DELETE CANDIDATE: {}".format(e))
        raise ce.InternalServerError
