/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 80015
Source Host           : localhost:3306
Source Database       : spider

Target Server Type    : MYSQL
Target Server Version : 80015
File Encoding         : 65001

Date: 2020-07-18 21:25:50
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for lgzp
-- ----------------------------
DROP TABLE IF EXISTS `lgzp`;
CREATE TABLE `lgzp` (
  `job_name` varchar(255) DEFAULT NULL,
  `salary` varchar(255) DEFAULT NULL,
  `place` varchar(255) DEFAULT NULL,
  `experience` varchar(255) DEFAULT NULL,
  `degree` varchar(255) DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL,
  `update_time` varchar(255) DEFAULT NULL,
  `tag` varchar(255) DEFAULT NULL,
  `workplace` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `company` varchar(255) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of lgzp
-- ----------------------------
