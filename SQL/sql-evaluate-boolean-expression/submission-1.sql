select c.left_operand, c.operator, c.right_operand,
    case
        when operator = '<' then c.left_value < c.right_value
        when operator = '=' then c.left_value = c.right_value
        else c.left_value > c.right_value
    end as value
from (
    SELECT
        e.left_operand,
        e.operator,
        e.right_operand,
        left_var.value AS left_value,
        right_var.value AS right_value
    FROM expressions AS e
    JOIN variables AS left_var
        ON left_var.name = e.left_operand
    JOIN variables AS right_var
        ON right_var.name = e.right_operand
) as c;