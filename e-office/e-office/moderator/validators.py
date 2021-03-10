from django.core.exceptions import ValidationError



def validate_file_size(value):

    try:
        filesize= value.size
        
        if filesize > 1485760:
            raise ValidationError("Size must be less than 1 MB")
        else:
            return value
    except:
        pass

def empty_file(value):
    
    if value:
        pass
    else:
        raise ValidationError('You must choose a file')

