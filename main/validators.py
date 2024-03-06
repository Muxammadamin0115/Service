from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
import re
from django.core.validators import RegexValidator


class ImageFileValidator(FileExtensionValidator):
    def init(self, allowed_extensions=None, message=None):
        self.allowed_extensions = allowed_extensions or ['jpg', 'jpeg', 'png', 'gif', 'bmp']
        self.message = message or 'File must be an image with a valid extension'


    def call(self, value):
        # Get the file extension using a regular experession
        match = re.search(r'\.([a-zA-Z0-9]+)$', str(value))
        if not match or match.group(1).lower() not in self.allowed_extensions:
            raise ValidationError(self.message, code='Invalid')