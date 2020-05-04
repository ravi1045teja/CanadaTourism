"""initial database migration

Revision ID: 9ed86537fbb9
Revises: 
Create Date: 2020-03-13 16:38:58.145000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ed86537fbb9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blacklist_tokens',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('token', sa.String(length=500), nullable=False),
    sa.Column('blacklisted_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('package',
    sa.Column('packageId', sa.Integer(), nullable=False),
    sa.Column('source', sa.String(length=45), nullable=True),
    sa.Column('destination', sa.String(length=45), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('transportMode', sa.String(length=45), nullable=True),
    sa.PrimaryKeyConstraint('packageId')
    )
    op.create_table('ticket',
    sa.Column('ticketId', sa.Integer(), nullable=False),
    sa.Column('packageId', sa.Integer(), nullable=True),
    sa.Column('bookingUserId', sa.Integer(), nullable=False),
    sa.Column('ticketPrice', sa.Integer(), nullable=True),
    sa.Column('dicountPriceApplied', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('ticketId')
    )
    op.create_table('transaction',
    sa.Column('transactionId', sa.Integer(), nullable=False),
    sa.Column('paymentMethod', sa.String(length=45), nullable=True),
    sa.Column('transactionSuccess', sa.String(length=45), nullable=True),
    sa.Column('ticketId', sa.String(length=45), nullable=True),
    sa.PrimaryKeyConstraint('transactionId')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('registered_on', sa.DateTime(), nullable=False),
    sa.Column('admin', sa.Boolean(), nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=True),
    sa.Column('password_hash', sa.String(length=100), nullable=True),
    sa.Column('activated', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('userdetails',
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.Column('firstName', sa.String(length=45), nullable=True),
    sa.Column('lastName', sa.String(length=45), nullable=True),
    sa.Column('gender', sa.String(length=45), nullable=True),
    sa.Column('email', sa.String(length=45), nullable=True),
    sa.Column('phoneNo', sa.String(length=45), nullable=True),
    sa.PrimaryKeyConstraint('userId')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('userdetails')
    op.drop_table('user')
    op.drop_table('transaction')
    op.drop_table('ticket')
    op.drop_table('package')
    op.drop_table('blacklist_tokens')
    # ### end Alembic commands ###
