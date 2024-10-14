from cerberus import Validator
import re


class CustomValidator(Validator):
    def _validate_regex(self, regex, field, value):
        """Override the default regex validation error message"""
        if not re.match(regex, value):
            self._error(field, f"Invalid {field}")

    def _validate_gender(self, gender, field, value):
        """Custom validation for gender field with case insensitivity."""
        allowed_values = {"male", "female", "other"}
        if gender and value.lower() not in allowed_values:
            self._error(
                field,
                f"Invalid gender. Allowed values are: {', '.join(allowed_values)}",
            )
