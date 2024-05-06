-- 创建表的SQL语句，包含SET和BOOLEAN类型
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age TINYINT,
    salary DECIMAL(10, 2),
    started_on DATE,
    last_login DATETIME,
    emails SET('email1@example.com', 'email2@example.com', 'email3@example.com'), -- SET类型提供可选值的列表
    isFemale BOOLEAN
);


-- 插入数据，包含SET和BOOLEAN类型的值
INSERT INTO employees (name, age, salary, started_on, last_login, emails, isFemale)
VALUES ('Jane Doe', 28, 65000.00, '2022-02-02', '2024-04-20 09:00:00', 'email1@example.com,email3@example.com', TRUE);

-- 查询数据
SELECT * FROM employees;
