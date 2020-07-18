/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 80015
Source Host           : localhost:3306
Source Database       : spider

Target Server Type    : MYSQL
Target Server Version : 80015
File Encoding         : 65001

Date: 2020-07-18 21:33:47
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for qcwyzp
-- ----------------------------
DROP TABLE IF EXISTS `qcwyzp`;
CREATE TABLE `qcwyzp` (
  `job_name` varchar(255) NOT NULL,
  `salary` varchar(255) DEFAULT NULL,
  `company` varchar(255) DEFAULT NULL,
  `degree` varchar(255) DEFAULT NULL,
  `demand` varchar(255) DEFAULT NULL,
  `experience` varchar(255) DEFAULT NULL,
  `want_numbers` varchar(255) DEFAULT NULL,
  `dateline` varchar(255) DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL,
  `keyword` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of qcwyzp
-- ----------------------------
