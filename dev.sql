-- prepares databse for development

CREATE DATABASE IF NOT EXISTS missiont_dev;
CREATE USER IF NOT EXISTS dev_user@localhost IDENTIFIED BY 'mistodev_pwdv1';
GRANT ALL PRIVILEGES ON missiont_dev.* TO 'dev_user'@'localhost';
