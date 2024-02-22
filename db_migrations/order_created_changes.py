"""order_detail changes

Revision ID: 7a341d712aa5
Revises: 78da3a78bfd6
Create Date: 2023-09-29 13:22:35.204135

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "6hksd782js6u"
down_revision: Union[str, None] = "6hksd782jsn0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Make the vendor optional
    op.alter_column(
        "order_created",
        "order_id",
        nullable=True,
    )

    # Convert existing values to integers (for example, if representing cents)
    op.execute("UPDATE order_created SET total_amount = ROUND(total_amount * 100)")
    # op.execute("UPDATE order_created SET total_price = ROUND(total_price * 100)")

    # Alter the column type
    op.alter_column("order_created", "total_amount", type_=sa.Integer)
    # op.alter_column("order_details", "total_price", type_=sa.Integer)


# def downgrade() -> None:
#     op.alter_column(
#         "order_created",
#         "order_id",
#         nullable=False,
#     )

#     # Alter the column type back to Numeric
#     op.alter_column("order_created", "total_amount", type_=sa.Numeric(10, 2))
#     # op.alter_column("order_details", "total_price", type_=sa.Numeric(10, 2))

#     # Convert integer values back to their decimal representations
#     op.execute("UPDATE order_created SET total_amount = total_amount / 100.0")
#     # op.execute("UPDATE order_details SET total_price = total_price / 100.0")
