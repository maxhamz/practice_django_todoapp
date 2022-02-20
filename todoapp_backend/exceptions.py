from rest_framework.exceptions import ValidationError


def forbiddenInputError(request):
    noEditFields = ["id", "created_at", "last_modified_at"]
    invalidFields = []
    for i in request.keys():
        if i in noEditFields:
            invalidFields.append(i)
        
    if len(invalidFields) > 0:
        errorMessage = "FORBIDDEN INPUT FIELD: %s" % (invalidFields)
        raise ValidationError(detail=errorMessage)
    
    return None
