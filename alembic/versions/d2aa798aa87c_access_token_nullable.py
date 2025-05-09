"""access_token_nullable

Revision ID: d2aa798aa87c
Revises: a63ef3e57c7b
Create Date: 2025-05-08 20:32:31.236862

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd2aa798aa87c'
down_revision: Union[str, None] = 'a63ef3e57c7b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
