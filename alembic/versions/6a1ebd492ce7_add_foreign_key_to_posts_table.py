"""add foreign key to posts table

Revision ID: 6a1ebd492ce7
Revises: e2a42506228b
Create Date: 2026-01-13 11:15:34.122958

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6a1ebd492ce7'
down_revision: Union[str, Sequence[str], None] = 'e2a42506228b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    op.add_column('posts',sa.Column('published',sa.Boolean(),nullable=False,server_default='TRUE'))
    op.add_column('posts',sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('now()')))
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('posts_users_fk',source_table="posts", referent_table="users",
                          local_cols=['owner_id'],remote_cols=['id'],ondelete="CASCADE")
    


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('post_users_fk',table_name="posts")
    op.drop_column('posts','owner_id')
    op.drop_column('posts','content')
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
