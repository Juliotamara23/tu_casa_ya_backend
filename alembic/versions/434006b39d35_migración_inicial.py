"""Migración inicial

Revision ID: 434006b39d35
Revises: 
Create Date: 2025-02-13 17:24:07.575288

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '434006b39d35'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('horarios')
    op.drop_table('empleados')
    op.drop_table('configuracion_salarios')
    op.drop_table('nominas')
    op.drop_table('registros_horas')
    op.drop_table('recargos')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recargos',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('porcentaje', sa.NUMERIC(precision=5, scale=2), autoincrement=False, nullable=False),
    sa.Column('valor_hora', sa.NUMERIC(precision=10, scale=2), autoincrement=False, nullable=False),
    sa.Column('horario', sa.TEXT(), autoincrement=False, nullable=True),
    sa.CheckConstraint("horario = ANY (ARRAY['Diurna'::text, 'Nocturna'::text, 'Dominical_Diurna'::text, 'Dominical_Nocturna'::text, 'Extra_Diurna'::text, 'Extra_Nocturna'::text, 'Dominical_Ext_Diurna'::text, 'Dominical_Ext_Nocturna'::text])", name='recargos_horario_check'),
    sa.PrimaryKeyConstraint('id', name='recargos_pkey'),
    sa.UniqueConstraint('nombre', name='recargos_nombre_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('registros_horas',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('empleado_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('fecha', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('hora_inicio', postgresql.TIME(), autoincrement=False, nullable=False),
    sa.Column('hora_fin', postgresql.TIME(), autoincrement=False, nullable=False),
    sa.Column('horas_trabajadas', sa.NUMERIC(precision=5, scale=2), autoincrement=False, nullable=False),
    sa.Column('horario_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('recargo_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('valor_pagado', sa.NUMERIC(precision=10, scale=2), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['empleado_id'], ['empleados.id'], name='registros_horas_empleado_id_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['horario_id'], ['horarios.id'], name='registros_horas_horario_id_fkey', ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['recargo_id'], ['recargos.id'], name='registros_horas_recargo_id_fkey', ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id', name='registros_horas_pkey')
    )
    op.create_table('nominas',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('trabajador_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('fecha_inicio', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('fecha_fin', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('dias_laborados', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('horas_extras', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('recargo_nocturno_semana', sa.NUMERIC(precision=10, scale=2), autoincrement=False, nullable=False),
    sa.Column('recargo_nocturno_domingos', sa.NUMERIC(precision=10, scale=2), autoincrement=False, nullable=False),
    sa.Column('recargo_dia_domingos_festivos', sa.NUMERIC(precision=10, scale=2), autoincrement=False, nullable=False),
    sa.Column('recargo_horas_extras_nocturnas', sa.NUMERIC(precision=10, scale=2), autoincrement=False, nullable=False),
    sa.Column('subsidio_transporte', sa.NUMERIC(precision=10, scale=2), autoincrement=False, nullable=False),
    sa.Column('descuento_salud', sa.NUMERIC(precision=10, scale=2), autoincrement=False, nullable=False),
    sa.Column('descuento_pension', sa.NUMERIC(precision=10, scale=2), autoincrement=False, nullable=False),
    sa.Column('otros_descuentos', sa.NUMERIC(precision=10, scale=2), autoincrement=False, nullable=False),
    sa.Column('total_pagado', sa.NUMERIC(precision=10, scale=2), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['trabajador_id'], ['empleados.id'], name='nominas_trabajador_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='nominas_pkey')
    )
    op.create_table('configuracion_salarios',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('año', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('salario_minimo', sa.NUMERIC(precision=10, scale=2), autoincrement=False, nullable=False),
    sa.Column('valor_hora', sa.NUMERIC(precision=10, scale=2), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='configuracion_salarios_pkey'),
    sa.UniqueConstraint('año', name='configuracion_salarios_año_key')
    )
    op.create_table('empleados',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('documento', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('cargo', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('fecha_ingreso', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('salario_base', sa.NUMERIC(precision=10, scale=2), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='empleados_pkey'),
    sa.UniqueConstraint('documento', name='empleados_documento_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('horarios',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('empleado_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('dia_semana', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('hora_inicio', postgresql.TIME(), autoincrement=False, nullable=False),
    sa.Column('hora_fin', postgresql.TIME(), autoincrement=False, nullable=False),
    sa.Column('tipo_jornada', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.CheckConstraint("dia_semana::text = ANY (ARRAY['Lunes'::character varying::text, 'Martes'::character varying::text, 'Miércoles'::character varying::text, 'Jueves'::character varying::text, 'Viernes'::character varying::text, 'Sábado'::character varying::text, 'Domingo'::character varying::text])", name='horarios_dia_semana_check'),
    sa.CheckConstraint("tipo_jornada::text = ANY (ARRAY['Diurna'::character varying::text, 'Nocturna'::character varying::text])", name='horarios_tipo_jornada_check'),
    sa.ForeignKeyConstraint(['empleado_id'], ['empleados.id'], name='horarios_empleado_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='horarios_pkey')
    )
    # ### end Alembic commands ###
