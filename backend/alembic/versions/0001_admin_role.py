"""Add admin role to users.
Revision ID: 0001_admin_role
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import inspect

revision = "0001_admin_role"
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    bind = op.get_bind()
    inspector = inspect(bind)
    tables = inspector.get_table_names()
    if "users" not in tables:
        from app.db.session import Base
        from app import models  # noqa
        Base.metadata.create_all(bind=bind)
        return
    columns = {c["name"] for c in inspector.get_columns("users")}
    if "is_admin" not in columns:
        op.add_column("users", sa.Column("is_admin", sa.Boolean(), nullable=False, server_default=sa.false()))
        op.alter_column("users", "is_admin", server_default=None)

def downgrade():
    bind = op.get_bind()
    inspector = inspect(bind)
    if "users" in inspector.get_table_names():
        columns = {c["name"] for c in inspector.get_columns("users")}
        if "is_admin" in columns:
            op.drop_column("users", "is_admin")
