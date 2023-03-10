"""init

Revision ID: 8e0d93278ca6
Revises: 
Create Date: 2023-02-26 20:23:21.448386

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e0d93278ca6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('certificate',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('given_date', sa.String(), nullable=False),
    sa.Column('expire_date', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('drive',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('given_date', sa.String(), nullable=True),
    sa.Column('is_accepted', sa.Boolean(), nullable=False),
    sa.Column('is_destroyed', sa.Boolean(), nullable=False),
    sa.Column('destroy_date', sa.String(), nullable=True),
    sa.Column('destroy_document', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('inn',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('series', sa.Integer(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('given_by', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('license',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('given_date', sa.String(), nullable=False),
    sa.Column('given_by', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('passport',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('series', sa.Integer(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('given_by', sa.String(), nullable=False),
    sa.Column('register_address', sa.String(), nullable=False),
    sa.Column('birthday_address', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sign',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('owner', sa.String(), nullable=False),
    sa.Column('given_date', sa.String(), nullable=False),
    sa.Column('given_by', sa.String(), nullable=False),
    sa.Column('expire_date', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('snils',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('series', sa.Integer(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('given_by', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('app',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('version', sa.String(), nullable=False),
    sa.Column('license_number', sa.Integer(), nullable=False),
    sa.Column('license_expire_date', sa.String(), nullable=False),
    sa.Column('certificate_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['certificate_id'], ['certificate.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('organization',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('INN', sa.Integer(), nullable=False),
    sa.Column('OGRN', sa.Integer(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('license_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['license_id'], ['license.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('surname', sa.String(), nullable=False),
    sa.Column('patronimic', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('passport_id', sa.Integer(), nullable=False),
    sa.Column('INN_id', sa.Integer(), nullable=False),
    sa.Column('SNILS_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['INN_id'], ['inn.id'], ),
    sa.ForeignKeyConstraint(['SNILS_id'], ['snils.id'], ),
    sa.ForeignKeyConstraint(['passport_id'], ['passport.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_drive',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('drive_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['drive_id'], ['drive.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('drive_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_drive')
    op.drop_table('user')
    op.drop_table('organization')
    op.drop_table('app')
    op.drop_table('snils')
    op.drop_table('sign')
    op.drop_table('passport')
    op.drop_table('license')
    op.drop_table('inn')
    op.drop_table('drive')
    op.drop_table('certificate')
    # ### end Alembic commands ###
