# SQL Interview Revision

## Joins
- INNER JOIN returns matches; LEFT JOIN preserves all left rows.
- Grain describes what one row represents.
- One-to-many joins can inflate totals.
- Aggregate detail rows before joining when needed.
- NULL does not match NULL with `=`.
- Duplicate-key matches multiply row counts.
- MySQL has no direct FULL OUTER JOIN.

## Window Functions
- GROUP BY collapses rows; windows preserve rows.
- ROW_NUMBER is unique; RANK has gaps; DENSE_RANK has no gaps.
- PARTITION BY creates independent groups.
- LAG returns a previous row; LEAD returns a following row.
- Filter window results in a CTE/subquery because WHERE is evaluated earlier.

## CTEs
- A CTE is a temporary named result set for one statement.
- Syntax: `WITH name AS (...) SELECT ...`.
- Multiple CTEs use commas.
- Later CTEs can reference earlier CTEs.
- CTEs improve readability but are not automatically faster than subqueries.
