from peewee import SqliteDatabase, Model, IntegerField, DoubleField, DateTimeField, datetime as peewee_datetime

from config import DB_NAME

db = SqliteDatabase(DB_NAME)


class XRate(Model):
    class Meta:
        database = db
        db_table = "xrates"
        indexes = (
            (("from_currency", "to_currency"), True),
        )

    from_currency = IntegerField()
    to_currency = IntegerField()
    rate = DoubleField()
    updated = DateTimeField(default=peewee_datetime.datetime.now)

    def __repr__(self):
        return "XRate(%s=>%s): %s" % (self.from_currency, self.to_currency, self.rate)


def init_db():
    db.drop_table(XRate, True)
    XRate.create_table()
    XRate.create(from_currency=840, to_currency=980, rate=1)
    print("db created!")
