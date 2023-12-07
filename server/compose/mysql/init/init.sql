# compose/mysql/init/init.sql
-- 创建数据库
CREATE DATABASE `homepage_dev` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- 创建普通用户
GRANT ALL PRIVILEGES ON homepage_dev.* TO 'hpuser'@'%' IDENTIFIED BY '12345678';
FLUSH PRIVILEGES;
use homepage_dev;