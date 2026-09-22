"""Initial AgriSmart database schema."""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0001_initial_schema"
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    uuid = lambda: postgresql.UUID(as_uuid=False)
    op.create_table("users",
        sa.Column("id", uuid(), primary_key=True),
        sa.Column("full_name", sa.String(120), nullable=False),
        sa.Column("email", sa.String(255), nullable=False),
        sa.Column("password_hash", sa.String(255), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("created_at", sa.DateTime(), nullable=False))
    op.create_index("ix_users_email", "users", ["email"], unique=True)

    op.create_table("farms",
        sa.Column("id", uuid(), primary_key=True),
        sa.Column("owner_id", uuid(), sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
        sa.Column("name", sa.String(150), nullable=False),
        sa.Column("location", sa.String(255)), sa.Column("latitude", sa.Float()),
        sa.Column("longitude", sa.Float()), sa.Column("area_acres", sa.Float()),
        sa.Column("soil_type", sa.String(100)), sa.Column("created_at", sa.DateTime(), nullable=False))
    op.create_index("ix_farms_owner_id", "farms", ["owner_id"])

    for name, cols, fk, idx in [
        ("soil_records", [("nitrogen",sa.Float()),("phosphorus",sa.Float()),("potassium",sa.Float()),("ph",sa.Float()),("moisture",sa.Float())], "farms.id", "farm_id"),
        ("crop_recommendations", [("crop_name",sa.String(120)),("confidence",sa.Float()),("reason",sa.Text())], "farms.id", "farm_id"),
    ]:
        columns=[sa.Column("id",uuid(),primary_key=True),sa.Column("farm_id",uuid(),sa.ForeignKey(fk,ondelete="CASCADE"),nullable=False)]
        columns += [sa.Column(n,t) for n,t in cols] + [sa.Column("created_at" if name=="crop_recommendations" else "recorded_at",sa.DateTime(),nullable=False)]
        op.create_table(name,*columns)
        op.create_index(f"ix_{name}_{idx}",name,[idx])

    op.create_table("disease_predictions",
        sa.Column("id",uuid(),primary_key=True),sa.Column("user_id",uuid(),sa.ForeignKey("users.id",ondelete="CASCADE"),nullable=False),
        sa.Column("crop_name",sa.String(120),nullable=False),sa.Column("image_url",sa.Text()),
        sa.Column("disease_name",sa.String(160),nullable=False),sa.Column("confidence",sa.Float()),
        sa.Column("treatment",sa.Text()),sa.Column("created_at",sa.DateTime(),nullable=False))
    op.create_index("ix_disease_predictions_user_id","disease_predictions",["user_id"])

    op.create_table("yield_predictions",
        sa.Column("id",uuid(),primary_key=True),sa.Column("farm_id",uuid(),sa.ForeignKey("farms.id",ondelete="CASCADE"),nullable=False),
        sa.Column("crop_name",sa.String(120),nullable=False),sa.Column("predicted_yield",sa.Float(),nullable=False),
        sa.Column("unit",sa.String(30),nullable=False),sa.Column("confidence",sa.Float()),sa.Column("created_at",sa.DateTime(),nullable=False))
    op.create_index("ix_yield_predictions_farm_id","yield_predictions",["farm_id"])

    op.create_table("weather_records",
        sa.Column("id",uuid(),primary_key=True),sa.Column("farm_id",uuid(),sa.ForeignKey("farms.id",ondelete="CASCADE"),nullable=False),
        sa.Column("temperature",sa.Float()),sa.Column("humidity",sa.Float()),sa.Column("rainfall_mm",sa.Float()),
        sa.Column("wind_speed",sa.Float()),sa.Column("recorded_at",sa.DateTime(),nullable=False))
    op.create_index("ix_weather_records_farm_id","weather_records",["farm_id"])

    op.create_table("chat_sessions",
        sa.Column("id",uuid(),primary_key=True),sa.Column("user_id",uuid(),sa.ForeignKey("users.id",ondelete="CASCADE"),nullable=False),
        sa.Column("title",sa.String(200)),sa.Column("created_at",sa.DateTime(),nullable=False))
    op.create_index("ix_chat_sessions_user_id","chat_sessions",["user_id"])

    op.create_table("chat_messages",
        sa.Column("id",uuid(),primary_key=True),sa.Column("session_id",uuid(),sa.ForeignKey("chat_sessions.id",ondelete="CASCADE"),nullable=False),
        sa.Column("role",sa.String(30),nullable=False),sa.Column("content",sa.Text(),nullable=False),sa.Column("created_at",sa.DateTime(),nullable=False))
    op.create_index("ix_chat_messages_session_id","chat_messages",["session_id"])

def downgrade():
    for table in ["chat_messages","chat_sessions","weather_records","yield_predictions","disease_predictions","crop_recommendations","soil_records","farms","users"]:
        op.drop_table(table)
