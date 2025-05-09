"""access_token_nullable_2

Revision ID: c8fe2a643016
Revises: 734d371938e2
Create Date: 2025-05-08 20:42:25.774823

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c8fe2a643016'
down_revision: Union[str, None] = '734d371938e2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
