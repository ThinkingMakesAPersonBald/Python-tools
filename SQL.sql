CREATE TABLE `audio_robot` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `script_id` bigint(20) unsigned NOT NULL COMMENT '话术ID',
  `recorder_tone_id` bigint(20) unsigned NOT NULL COMMENT '录音员ID',
  `scene` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '场景',
  `country` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '国家',
  `language` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '语言',
  `text` text COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '音频翻译',
  `from` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '音频来源：机器人知识库/通用话术音频/为空(客户上传)',
  `source_id` bigint(20) unsigned DEFAULT NULL COMMENT '来源ID，机器人知识库/通用话术音频/为空(客户上传)',
  `filename` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '上传文件名称，不可重复',
  `realname` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '真实文件存放地址，规则：Robot/secne/country/language/robot_id/',
  `version_id` int(11) NOT NULL COMMENT '版本id',
  `type` int(1) NOT NULL COMMENT '音频文件类型，1:tts 0:fixed',
  `duration` int(11) NOT NULL DEFAULT '0' COMMENT '音频时长，默认0',
  `robot_id` bigint(20) unsigned NOT NULL COMMENT '机器人ID',
  `dec` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '录音文件描述',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `filename` (`robot_id`,`version_id`,`filename`) USING BTREE,
  KEY `audio_robot_scene_created` (`scene`,`created_at`) USING BTREE,
  KEY `audio_robot_country_created` (`country`,`created_at`) USING BTREE,
  KEY `audio_robot_robot_id_created` (`robot_id`,`created_at`) USING BTREE,
  KEY `audio_robot_created` (`created_at`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=191648 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='机器人所有的音频';

CREATE TABLE
IF
	NOT EXISTS `interest_rate` (
		`id` INT NOT NULL AUTO_INCREMENT COMMENT '自增id',
		`country` VARCHAR ( 64 ) NOT NULL COMMENT '国家',
		`commodity` VARCHAR ( 128 ) NOT NULL COMMENT '商品',
		`date` DATE NOT NULL COMMENT '发布日期',
		`current_value` FLOAT ( 16 ) NOT NULL COMMENT '当前值',
		`predictive_value` FLOAT ( 16 ) NOT NULL COMMENT '预测值',
		`former_value` FLOAT ( 16 ) NOT NULL COMMENT '前值',
		PRIMARY KEY ( `id` ),
	CONSTRAINT `unique_data` UNIQUE ( `country`, `date` ) 
	) ENGINE = INNODB DEFAULT CHARSET = utf8 COMMENT = '世界主要国家的央行利率'
