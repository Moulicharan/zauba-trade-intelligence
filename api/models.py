from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String

from api.database import Base


class TradeRecord(Base):
    __tablename__ = "trade_records"

    id = Column(Integer, primary_key=True, index=True)

    period = Column(Integer, nullable=False)

    reporter_code = Column(Integer, nullable=False)
    reporter_name = Column(String, nullable=False)

    flow_code = Column(String, nullable=False)
    flow_type = Column(String, nullable=False)

    partner_code = Column(Integer, nullable=False)
    partner_name = Column(String, nullable=False)

    cmd_code = Column(Integer, nullable=False)
    cmd_desc = Column(String, nullable=False)

    trade_value_usd = Column(Float, nullable=False)

    net_weight_kg = Column(Float, nullable=False)

    quantity = Column(Float, nullable=False)

    scraped_at = Column(DateTime, nullable=False)

    cleaned_at = Column(DateTime, nullable=False)