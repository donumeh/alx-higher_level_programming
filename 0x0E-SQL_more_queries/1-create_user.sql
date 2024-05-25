-- Script that creates a user in Mysql

-- UNINSTALL COMPONENT 'validate_password';

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED WITH mysql_native_password BY 'user_0d_1_pwd';
