"""Initial migration

Revision ID: 171c8ba8b7d2
Revises: 0b9c622a987b
Create Date: 2024-07-31 15:08:50.852048

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '171c8ba8b7d2'
down_revision: Union[str, None] = '0b9c622a987b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
