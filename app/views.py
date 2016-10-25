#coding: utf-8
from flask import render_template
from flask.ext.appbuilder.models.sqla.interface import SQLAInterface
from flask.ext.appbuilder import ModelView
from app import appbuilder, db
from models import Projeto, CategoriaProjeto

"""
    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(MyModelView, "My View", icon="fa-folder-open-o", category="My Category", category_icon='fa-envelope')
"""
def preenche_categorias():
    try:
        categorias = [
            'Pesquisa',
            u'Competição Tecnológica',
            u'Inovação no Ensino',
            u'Manutenção e Reforma',
            'Pequenas Obras']

        for categoria in categorias:
            db.session.add(CategoriaProjeto(nome=categoria))

        db.session.commit()
    except:
        db.session.rollback()


class ProjetoModelView(ModelView):

    datamodel = SQLAInterface(Projeto)

    list_columns = []




appbuilder.add_view(ProjetoModelView, "Projeto", icon="fa-database")



"""
    Application wide 404 error handler
"""
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404

db.create_all()
preenche_categorias()


