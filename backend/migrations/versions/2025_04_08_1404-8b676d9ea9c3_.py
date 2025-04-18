"""empty message

Revision ID: 8b676d9ea9c3
Revises:
Create Date: 2025-04-08 14:04:57.968336

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "8b676d9ea9c3"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "events",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("date", sa.Date(), nullable=False),
        sa.Column("time", sa.Time(), nullable=False),
        sa.Column("met_place", sa.String(), nullable=False),
        sa.Column("route", sa.String(), nullable=True),
        sa.Column("guid", sa.String(), nullable=False),
        sa.Column("cost", sa.Float(), nullable=True),
        sa.Column("time_of_the_event", sa.Float(), nullable=True),
        sa.Column("max_participants", sa.Integer(), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_events")),
        sa.UniqueConstraint("guid", name=op.f("uq_events_guid")),
    )
    op.create_table(
        "participants",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("surname", sa.String(), nullable=False),
        sa.Column("patronymic", sa.String(), nullable=False),
        sa.Column("phone", sa.String(), nullable=False),
        sa.Column("tg_username", sa.String(), nullable=False),
        sa.Column("comment", sa.String(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("event_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["event_id"],
            ["events.id"],
            name=op.f("fk_participants_event_id_events"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_participants")),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("participants")
    op.drop_table("events")
