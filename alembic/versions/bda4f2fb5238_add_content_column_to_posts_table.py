"""add content column to posts table

Revision ID: bda4f2fb5238
Revises: f47f42bc223a
Create Date: 2024-03-11 11:19:39.510097

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bda4f2fb5238'
down_revision: Union[str, None] = 'f47f42bc223a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
