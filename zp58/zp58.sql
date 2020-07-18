/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 80015
Source Host           : localhost:3306
Source Database       : spider

Target Server Type    : MYSQL
Target Server Version : 80015
File Encoding         : 65001

Date: 2020-07-18 21:35:26
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for zp58
-- ----------------------------
DROP TABLE IF EXISTS `zp58`;
CREATE TABLE `zp58` (
  `job_name1` varchar(255) NOT NULL,
  `job_name2` varchar(255) DEFAULT NULL,
  `salary` varchar(255) DEFAULT NULL,
  `want_numbers` varchar(255) DEFAULT NULL,
  `degree` varchar(255) DEFAULT NULL,
  `experience` varchar(255) DEFAULT NULL,
  `address1` varchar(255) DEFAULT NULL,
  `address2` varchar(255) DEFAULT NULL,
  `url` varchar(510) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of zp58
-- ----------------------------
INSERT INTO `zp58` VALUES (' 前台/总机/接待', '前台接待 ', '2500-3000', '  招1人 ', '学历不限', ' 经验不限 ', '鞍山 铁东', '华艺大厦12楼1207鼎信文化', 'https://as.58.com/renli/42840544957442x.shtml?psid=138355662209069097369364171&entinfo=42840544957442_j&ytdzwdetaildj=0&finalCp=finalCp=000001250000000000000000000000000000_138355662209069097369364171&tjfrom=pc_list_left_jp__138355662209069097369364171__183295397044387840__jp__1__18____');
INSERT INTO `zp58` VALUES (' 汽车美容', '（鞍山店）太阳膜技师 ', '4000-8000', '  招6人 ', '学历不限', ' 1-2年 ', '鞍山 铁西', '千山西路94栋1层13-14号', 'http://as.58.com/zpqiche/42854324891536x.shtml?adtype=1&finalCp=finalCp%3D000001230000000000000000000000000000_138355662209069097369364171&adact=3&psid=138355662209069097369364171&ytdzwdetaildj=0&entinfo=42854324891536_q&tjfrom=pc_list_left_jz__138355662209069097369364171__183295397044387840__jz__5%2C0%2C8__0____');
INSERT INTO `zp58` VALUES (' 客服专员/助理', '客服-底薪2500-五险 ', '4000-8000', '  招10人 ', '大专', ' 经验不限,可接收应届生 ', '鞍山 铁东', '鞍山市站前四隆大厦36楼397', 'https://as.58.com/kefu/42156637247384x.shtml?psid=138355662209069097369364171&entinfo=42156637247384_j&ytdzwdetaildj=0&finalCp=finalCp=000001250000000000000000000000000000_138355662209069097369364171&tjfrom=pc_list_left_jp__138355662209069097369364171__183295397044387840__jp__1__17____');
INSERT INTO `zp58` VALUES (' 汽车修理工', '新开店招聘汽车修理工 ', '3000-5000', '  招若干人 ', '学历不限', ' 经验不限 ', '鞍山 铁西', '中国辽宁省鞍山市铁西区西民生路152号', 'https://as.58.com/zpqiche/37305206775066x.shtml?psid=138355662209069097369364171&entinfo=37305206775066_j&ytdzwdetaildj=0&finalCp=finalCp=000001250000000000000000000000000000_138355662209069097369364171&tjfrom=pc_list_left_jp__138355662209069097369364171__183295397044387840__jp__1__16____');
INSERT INTO `zp58` VALUES (' 娱乐休闲其他', '带货主播 ', null, '  招20人 ', '学历不限', ' 经验不限 ', '鞍山 铁西', '辽宁省鞍山市铁西区交通路', 'https://as.58.com/zpwentiyingshi/39071019849998x.shtml?psid=138355662209069097369364171&entinfo=39071019849998_j&ytdzwdetaildj=0&finalCp=finalCp=000001250000000000000000000000000000_138355662209069097369364171&tjfrom=pc_list_left_jp__138355662209069097369364171__183295397044387840__jp__1__15____');
INSERT INTO `zp58` VALUES (' 文员', '文员/工作轻松不累 ', null, '  招5人 ', '学历不限', ' 经验不限 ', '鞍山 铁东', '鞍山铁东山南建国南路53号邮局附近', 'https://as.58.com/renli/42729465351454x.shtml?psid=138355662209069097369364171&entinfo=42729465351454_j&ytdzwdetaildj=0&finalCp=finalCp=000001250000000000000000000000000000_138355662209069097369364171&tjfrom=pc_list_left_jp__138355662209069097369364171__183295397044387840__jp__1__14____');
INSERT INTO `zp58` VALUES (' 销售代表', '销售 ', null, '  招10人 ', '学历不限', ' 经验不限,可接收应届生 ', '鞍山 铁东', '鞍山铁东四海酒店附近', 'https://as.58.com/yewu/42420920861702x.shtml?psid=138355662209069097369364171&entinfo=42420920861702_j&ytdzwdetaildj=0&finalCp=finalCp=000001250000000000000000000000000000_138355662209069097369364171&tjfrom=pc_list_left_jp__138355662209069097369364171__183295397044387840__jp__1__13____');
INSERT INTO `zp58` VALUES (' 财务总监', '高薪诚聘财务总监助理 ', '8000-10000', '  招1人 ', '本科', ' 3-5年 ', '鞍山 铁西', '鞍山铁西区通尊科技园一号楼C座二楼', 'https://as.58.com/zpcaiwushenji/42675293226905x.shtml?psid=138355662209069097369364171&entinfo=42675293226905_j&ytdzwdetaildj=0&finalCp=finalCp=000001250000000000000000000000000000_138355662209069097369364171&tjfrom=pc_list_left_jp__138355662209069097369364171__183295397044387840__jp__1__12____');
