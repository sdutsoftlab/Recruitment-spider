/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 80015
Source Host           : localhost:3306
Source Database       : spider

Target Server Type    : MYSQL
Target Server Version : 80015
File Encoding         : 65001

Date: 2020-07-18 21:35:11
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for rczp
-- ----------------------------
DROP TABLE IF EXISTS `rczp`;
CREATE TABLE `rczp` (
  `job_name` varchar(255) DEFAULT NULL,
  `salary` varchar(255) DEFAULT NULL,
  `want_numbers` varchar(255) DEFAULT NULL,
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
-- Records of rczp
-- ----------------------------
INSERT INTO `rczp` VALUES ('远洋捕鱼工、船员普工', '10-15k', '10人', '经验不限', '初中以上', '全职', '2020-07-18更新', '五险一金 提供食宿 绩效奖金 年终奖金 年底双薪  年终分红 弹性工作 岗位晋升 带薪年假 定期体检', '浙江 湖州', '宁波市北仑区大碶街道坝头路257号', '宁波佲洋船务有限公司', 'https://www.cjol.com/jobs/job-10863406');
INSERT INTO `rczp` VALUES ('高薪船员', '10-15k', '18人', '经验不限', '初中以上', '全职', '2020-07-18更新', '五险一金 提供食宿 绩效奖金 年终奖金 年底双薪  年终分红 弹性工作 岗位晋升 带薪年假 定期体检', '广东 深圳', '宁波市北仑区大碶街道坝头路257号', '宁波佲洋船务有限公司', 'https://www.cjol.com/jobs/job-10858073');
INSERT INTO `rczp` VALUES ('近海船员', '10-15k', '18人', '经验不限', '初中以上', '全职', '2020-07-18更新', '五险一金 提供食宿 绩效奖金 年终奖金 年底双薪  年终分红 弹性工作 岗位晋升 带薪年假 定期体检', '浙江 宁波', '宁波市北仑区大碶街道坝头路257号', '宁波佲洋船务有限公司', 'https://www.cjol.com/jobs/job-10855329');
INSERT INTO `rczp` VALUES ('出海捕鱼工、船员普工', '10-15k', '18人', '经验不限', '初中以上', '全职', '2020-07-18更新', '五险一金 提供食宿 绩效奖金 年终奖金 年底双薪  年终分红 弹性工作 岗位晋升 带薪年假 定期体检', '浙江 宁波', '宁波市北仑区大碶街道坝头路257号', '宁波佲洋船务有限公司', 'https://www.cjol.com/jobs/job-10855336');
INSERT INTO `rczp` VALUES ('急招普工-捕鱼工-货船船员-海员水手  年薪10万  包吃住', '10-15k', '18人', '经验不限', '初中以上', '全职', '2020-07-18更新', '五险一金 提供食宿 绩效奖金 年终奖金 年底双薪  年终分红 弹性工作 岗位晋升 带薪年假 定期体检', '浙江 杭州', '宁波市北仑区大碶街道坝头西路257号', '宁波佲洋船务有限公司', 'https://www.cjol.com/jobs/job-10845790');
INSERT INTO `rczp` VALUES ('山东、青岛打鱼船员招聘、山东出海打渔捕鱼招聘、温州出海打渔船员、广东出海船员海员捕鱼工、', '10-15k', '89人', '经验不限', '初中以上', '全职', '2020-07-18更新', '提供食宿 提供住宿 年终奖金 带薪年假', '广东 惠州', '宁波市海曙区灵桥路159号、宁波宏远船务有限公司', '宁波宏远船务有限公司', 'https://www.cjol.com/jobs/job-10805744');
INSERT INTO `rczp` VALUES ('招聘捕鱼工-货船海员-出海普工-机工水手-分拣员', '10-15k', '20人', '经验不限', '初中以上', '全职', '2020-07-18更新', '五险一金 提供食宿 绩效奖金 年终奖金 年底双薪  年终分红 弹性工作 岗位晋升 带薪年假 定期体检', '浙江 杭州', '宁波市北仑区大碶街道坝头西路257号', '宁波佲洋船务有限公司', 'https://www.cjol.com/jobs/job-10846434');
INSERT INTO `rczp` VALUES ('公司招聘普工-搬运工-分拣工-电焊工-捕鱼工-船员水手', '10-15k', '18人', '经验不限', '初中以上', '全职', '2020-07-18更新', '五险一金 提供食宿 绩效奖金 年终奖金 年底双薪  年终分红 弹性工作 岗位晋升 带薪年假 定期体检', '浙江 杭州', '宁波市北仑区大碶街道坝头西路257号', '宁波佲洋船务有限公司', 'https://www.cjol.com/jobs/job-10846432');
INSERT INTO `rczp` VALUES ('最新招聘捕鱼工-货船船员-出海普工-电焊工-分拣员', '10-15k', '20人', '经验不限', '初中以上', '全职', '2020-07-18更新', '五险一金 提供食宿 绩效奖金 年终奖金 年底双薪  年终分红 弹性工作 岗位晋升 带薪年假 定期体检', '浙江 杭州', '宁波市北仑区大碶街道坝头西路257号', '宁波佲洋船务有限公司', 'https://www.cjol.com/jobs/job-10846430');
