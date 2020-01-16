import cherrypy

from app.views import IndexViewset
from cms.views import ArticleViewset, ArticleDetailsViewset

def url_mapper():
    mapper = cherrypy.dispatch.RoutesDispatcher()
    mapper.connect('index', '/', controller=IndexViewset(), action='index')

    mapper.connect('article_create_list', '/articles/', controller=ArticleViewset(), action='index')
    mapper.connect('article_details_fetch_update_delete', '/articles/{article_id}/', controller=ArticleDetailsViewset(), action='index')

    return mapper
