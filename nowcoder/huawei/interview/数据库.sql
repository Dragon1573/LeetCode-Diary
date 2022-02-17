/* 一张表有10条相同数据，删除其中9条 */
DELETE FROM `tableName`
LIMIT 9;
/* 对于数据表 dataset(name, subject, score) ，选出所有科目都大于80分的学生姓名 */
SELECT `name`
FROM dataset
WHERE `name` NOT IN (
        SELECT `name`
        FROM dataset
        WHERE score < 80
    );
/* 每班总成绩前10 */
SELECT *
FROM (
        SELECT T.*,
            ROW_NUMBER() OVER(
                PARTITION BY 班级
                ORDER BY 成绩 DESC
            ) RN
        FROM T
    )
WHERE RN <= 10
