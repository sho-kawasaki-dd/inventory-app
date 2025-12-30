"""add_category_usage_manufacturer_to_items

Revision ID: 207aaed68472
Revises: 62c77c157476
Create Date: 2025-12-30 21:18:04.226047

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '207aaed68472'
down_revision = '62c77c157476'
branch_label = None
depends_on = None


def upgrade() -> None:
    # Add category, usage, manufacturer columns to items table
    op.add_column('items', sa.Column('category', sa.Text(), nullable=True))
    op.add_column('items', sa.Column('usage', sa.Text(), nullable=True))
    op.add_column('items', sa.Column('manufacturer', sa.Text(), nullable=True))


def downgrade() -> None:
    # Remove category, usage, manufacturer columns from items table
    op.drop_column('items', 'manufacturer')
    op.drop_column('items', 'usage')
    op.drop_column('items', 'category')
