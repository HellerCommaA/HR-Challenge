from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
fake_data = Table('fake_data', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('slogan', VARCHAR),
    Column('time', DATETIME),
)

fake_data = Table('fake_data', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('rand', Integer),
    Column('time', DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['fake_data'].columns['slogan'].drop()
    post_meta.tables['fake_data'].columns['rand'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['fake_data'].columns['slogan'].create()
    post_meta.tables['fake_data'].columns['rand'].drop()
