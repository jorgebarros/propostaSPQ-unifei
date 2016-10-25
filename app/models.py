from flask.ext.appbuilder import Model
from flask.ext.appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""

class CategoriaProjeto(Model):
    __tablename__ = "categoria"

    id = Column(Integer, primary_key=True)
    nome = Column(String(48), nullable=False, unique=True)


    def __repr__(self):
        return self.nome

class Projeto(Model):
    __tablename__ = "projeto"

    id = Column(Integer, primary_key=True)
    nome = Column(String(80), nullable=False)
    duracao = Column(DateTime)
    valor_previsto = Column(Float)
    status = ""


    categoria_id = Column(Integer, ForeignKey('categoria.id'), nullable=False)
    categoria = relationship("CategoriaProjeto")

    def __init__(self):
        status_list = ["candidato", "aprovado",
                       "reprovado", "finalizado"]

        self.status_list = status_list
        self.status = Column(String(18), default=status_list[0])

    def __repr__(self):
        return self.nome
