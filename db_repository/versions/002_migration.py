from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
theA = Table('theA', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('count', INTEGER),
)

fake_data = Table('fake_data', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('slogan', String),
    Column('time', DateTime, default=ColumnDefault(datetime.datetime(2015, 5, 14, 22, 23, 48, 701030))),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['theA'].drop()
    post_meta.tables['fake_data'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['theA'].create()
    post_meta.tables['fake_data'].drop()
