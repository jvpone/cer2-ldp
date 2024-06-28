from rest_framework.renderers import TemplateHTMLRenderer

class PokemonHTMLRenderer(TemplateHTMLRenderer):
    template_name = 'pokemon_list.html'

