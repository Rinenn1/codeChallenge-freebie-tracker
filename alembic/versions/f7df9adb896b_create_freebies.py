"""create freebies

Revision ID: f7df9adb896b
Revises: 
Create Date: 2025-03-05 18:53:16.500740

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7df9adb896b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('freebies',
    sa.Column('id', sa.Integer, nullable=False),
    sa.Column('item_name', sa.String, nullable=True),
    sa.Column('value', sa.Integer),
    sa.ForeignKeyConstraint(['dev_id'], ['devs.id']),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id']),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('freebies')
