from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy import String


class Base(DeclarativeBase):
    pass


class HistModel(Base):
    __tablename__ = "hist"
    date: Mapped[str] = mapped_column(String(30), primary_key=True)
    ticker: Mapped[str] = mapped_column(String(30), primary_key=True)
    close: Mapped[float] = mapped_column()



    # __tablename__ = "hist"
    # # id = db.Column(db.Integer, primary_key=True)
    # # analyst_id = db.Column(db.Integer, db.ForeignKey("analysts.id"), nullable=False)
    #
    # data = db.Column(db.String(30), primary_key=True, nullable=False)
    # ticker = db.Column(db.String(30), primary_key=True, nullable=False)
    #
    # # type = db.Column(
    # #     db.Enum(AnalysisType), server_default=AnalysisType.analysis.name, nullable=False
    # # )
    # # created_on = db.Column(db.DateTime, nullable=False, server_default=func.now())
    # # updated_on = db.Column(db.DateTime, onupdate=func.now())
    # # relationship = db.relationship("AnalystsModel")
