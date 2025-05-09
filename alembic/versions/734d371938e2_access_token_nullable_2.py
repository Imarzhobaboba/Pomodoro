"""access_token_nullable_2

Revision ID: 734d371938e2
Revises: d2aa798aa87c
Create Date: 2025-05-08 20:35:10.459860

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '734d371938e2'
down_revision: Union[str, None] = 'd2aa798aa87c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
