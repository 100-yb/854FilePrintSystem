CREATE DATABASE printshop;
USE printshop;

CREATE TABLE `printfile` (
  `filename` VARCHAR(255) NOT NULL COMMENT '文件名',
  `filesize` DOUBLE DEFAULT NULL COMMENT '文件大小',
  `filetype` VARCHAR(255) DEFAULT NULL COMMENT '文件类型',
  `createtime` DATETIME DEFAULT NULL COMMENT '创建时间',
  `userid` INT NOT NULL COMMENT '用户id',
  `copies` INT NOT NULL COMMENT '数量',
  `side` VARCHAR(10) NOT NULL COMMENT '单双面',
  `color` VARCHAR(10) NOT NULL COMMENT '黑白',
  `file` LONGBLOB NOT NULL COMMENT '文件',
  PRIMARY KEY (`filename`)
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `printuser` (
  `userid` VARCHAR(255) NOT NULL COMMENT '用户id',
  `username` VARCHAR(255) DEFAULT NULL COMMENT '用户名',
  `password` VARCHAR(255) NOT NULL COMMENT '用户密码',
  `permission` VARCHAR(10) DEFAULT NULL COMMENT '权限',
  PRIMARY KEY (`userid`)
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `printuser` (`userid`, `username`, `password`, `permission`) VALUES ('202100203029', '江海程', '854867', 'vip');
INSERT INTO `printuser` (`userid`, `username`, `password`, `permission`) VALUES ('202100203030', '蔡坤龙', '854867', 'vip');
INSERT INTO `printuser` (`userid`, `username`, `password`, `permission`) VALUES ('202100203032', '陈泓宇', '854867', 'vip');
INSERT INTO `printuser` (`userid`, `username`, `password`, `permission`) VALUES ('202100203099', '陈礼伟', '123456', 'common');
INSERT INTO `printuser` (`userid`, `username`, `password`, `permission`) VALUES ('202100203100', '蔡海升', '854867', 'vip');
INSERT INTO `printuser` (`userid`, `username`, `password`, `permission`) VALUES ('202100203103', '陈奕柏', '854867', 'vip');
INSERT INTO `printuser` (`userid`, `username`, `password`, `permission`) VALUES ('202100203106', '于梦洋', '123456', 'common');
