from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from api.database import get_db
from api.models import TradeRecord

router = APIRouter()


# Get all trade records
@router.get("/trades")
def get_all_trades(db: Session = Depends(get_db)):

    trades = db.query(TradeRecord).all()

    return trades


# Filter trade records
@router.get("/trades/filter")
def filter_trades(
    year: int | None = None,
    reporter: str | None = None,
    partner: str | None = None,
    product: str | None = None,
    flow: str | None = None,
    db: Session = Depends(get_db)
):

    query = db.query(TradeRecord)

    if year:
        query = query.filter(TradeRecord.period == year)

    if reporter:
        query = query.filter(
            TradeRecord.reporter_name.ilike(f"%{reporter}%")
        )

    if partner:
        query = query.filter(
            TradeRecord.partner_name.ilike(f"%{partner}%")
        )

    if product:
        query = query.filter(
            TradeRecord.cmd_desc.ilike(f"%{product}%")
        )

    if flow:
        query = query.filter(
            TradeRecord.flow_type.ilike(f"%{flow}%")
        )

    results = query.all()

    return results