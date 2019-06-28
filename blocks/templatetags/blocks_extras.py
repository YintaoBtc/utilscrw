from django import template
from blocks.models import Block

register = template.Library()

@register.simple_tag
def get_block_list():
    blocks = Block.objects.all()
    return blocks