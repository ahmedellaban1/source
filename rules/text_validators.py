from django.core.validators import RegexValidator


BLOG_COMMENT_PATTERN = RegexValidator(
    regex = r'^.{20,1000}$',
    message = 'comment should be at least 20 characters and at most 1000 characters',
    code = 'invalid_comment'
)


REVIEW_PATTERN = RegexValidator(
    regex = r'^.{20,200}$',
    message = 'review should be at least 20 characters and at most 200 characters',
    code = 'invalid_review'
)


PRODUCT_DESCRIPTION = RegexValidator(
    regex = r'^.{20,1000}$',
    message = 'product description should be at least 20 characters and at most 1000 characters',
    code = 'invalid_description'
)
