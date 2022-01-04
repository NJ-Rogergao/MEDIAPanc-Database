/*
CREATE database pancreas
*/
CREATE DATABASE `pancreas` CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
use pancreas;

/*
CREATE TABLE admission
*/
CREATE TABLE `admission` (
  `ROW_ID` int(11) unsigned NOT NULL COMMENT 'row number',
  `PATIENT_ID` varchar(20) NOT NULL COMMENT 'an identifier which specifies an individual patient',
  `HOSPITAL_ID` varchar(20) NOT NULL COMMENT 'an identifier which specifies a single patient''s admission to the hospital',
  `ICU_ID` varchar(20) DEFAULT NULL COMMENT 'an identifier which specifies a single patient''s admission to the ICU',
  `DOB` date NOT NULL COMMENT 'shifted date of birth for the patient',
  `GENDER` varchar(10) NOT NULL COMMENT 'the genotypical sex of the patient',
  `PATIENT_HEIGHT` decimal(6,2) unsigned DEFAULT NULL COMMENT 'height for the patient in centimeters',
  `PATIENT_WEIGHT` decimal(6,2) unsigned DEFAULT NULL COMMENT 'weight for the patient in kilograms',
  `BLOOD_TYPE` varchar(10) DEFAULT NULL COMMENT 'blood type for the patient',
  `APACHE2` smallint(5) unsigned DEFAULT NULL COMMENT 'APACHE II score on the ICU-admission day',
  `ADMISSION_TIME` datetime NOT NULL COMMENT 'shifted hospital-admission time for the patient',
  `DISCHARGE_TIME` datetime NOT NULL COMMENT 'shifted hospital-discharge time for the patient',
  `ICU_IN_TIME` datetime DEFAULT NULL COMMENT 'shifted ICU-admission time for the patient',
  `ICU_OUT_TIME` datetime DEFAULT NULL COMMENT 'shifted ICU-discharge time for the patient',
  `DISCHARGE_STATUS` varchar(20) DEFAULT NULL COMMENT 'survival status which indicates whether the patient died within the given hospitalization',
  PRIMARY KEY (`ROW_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Demographic and administrative information regarding the patients and their ICU or hospital stay';

/*
CREATE TABLE vitalsign
*/
CREATE TABLE `vitalsign` (
  `ROW_ID` int(11) unsigned NOT NULL COMMENT 'row number',
  `PATIENT_ID` varchar(20) NOT NULL COMMENT 'an identifier which specifies an individual patient',
  `HOSPITAL_ID` varchar(20) NOT NULL COMMENT 'an identifier which specifies a single patient''s admission to the hospital',
  `ICU_ID` varchar(20) NOT NULL COMMENT 'an identifier which specifies a single patient''s admission to the ICU',
  `TIME_POINT` datetime NOT NULL COMMENT 'time point for the measurement of a certain vital sign',
  `ITEM_CODE` varchar(20) NOT NULL COMMENT 'local code for a certain monitoring item',
  `VALUE` varchar(20) DEFAULT NULL COMMENT 'value of a certain item_code',
  PRIMARY KEY (`ROW_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Continuous vital sign measurements for patients receiving intensive care and ventilatory support measurements for patients undergoing mechanical ventilation';

/*
CREATE TABLE fluidbalance
*/
CREATE TABLE `fluidbalance` (
  `ROW_ID` int(11) unsigned NOT NULL COMMENT 'row number',
  `PATIENT_ID` varchar(20) NOT NULL COMMENT 'an identifier which specifies an individual patient',
  `HOSPITAL_ID` varchar(20) NOT NULL COMMENT 'an identifier which specifies a single patient''s admission to the hospital',
  `ICU_ID` varchar(20) NOT NULL COMMENT 'an identifier which specifies a single patient''s admission to the ICU',
  `TIME_POINT` datetime NOT NULL COMMENT 'time point for a certain intake or output event documented in nursing records',
  `ITEM_CODE` varchar(20) NOT NULL COMMENT 'local code for a certain intake or output event',
  `VALUE` decimal(8,2) DEFAULT NULL COMMENT 'value of a certain item_code',
  `IN_OR_OUT_TYPE` varchar(20) NOT NULL COMMENT 'an identifier of intake or output event for the patient',
  PRIMARY KEY (`ROW_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Intake and output information recorded for patients in ICU';

/*
CREATE TABLE lab
*/
CREATE TABLE `lab` (
  `ROW_ID` int(11) unsigned NOT NULL COMMENT 'row number',
  `PATIENT_ID` varchar(20) NOT NULL COMMENT 'an identifier which specifies an individual patient',
  `HOSPITAL_ID` varchar(20) NOT NULL COMMENT 'an identifier which specifies a single patient''s admission to the hospital',
  `TIME_POINT` datetime NOT NULL COMMENT 'report time of a certain laboratary test',
  `SPEC` varchar(50) DEFAULT NULL COMMENT 'specimen',
  `ITEM_CODE` varchar(20) NOT NULL COMMENT 'local code for a certain laboratory item',
  `VALUE` varchar(50) DEFAULT NULL COMMENT 'value of a certain item_code',
  PRIMARY KEY (`ROW_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Laboratory measurements for patient derived specimens';

/*
CREATE TABLE microlab
*/
CREATE TABLE `microlab` (
  `ROW_ID` int(11) unsigned NOT NULL COMMENT 'row number',
  `PATIENT_ID` varchar(20) NOT NULL COMMENT 'an identifier which specifies an individual patient',
  `HOSPITAL_ID` varchar(20) NOT NULL COMMENT 'an identifier which specifies a single patient''s admission to the hospital',
  `TIME_POINT` datetime NOT NULL COMMENT 'report time of microbiology culture results and antibiotic sensitivities',
  `SPEC` varchar(50) DEFAULT NULL COMMENT 'specimen',
  `MB_ITEM_CODE` varchar(20) NOT NULL COMMENT 'local code for a certain microorganism',
  `AB_ITEM_CODE` varchar(20) NOT NULL COMMENT 'local code for a certain antibiotic',
  `KB` varchar(20) DEFAULT NULL COMMENT 'value of inhibition zone diameters using Kirby-Bauer method',
  `MIC` varchar(20) DEFAULT NULL COMMENT 'value of the minimum inhibitory concentration',
  `INTERPRETATION` varchar(10) DEFAULT NULL COMMENT 'results of the susceptibility for a certain antibiotic: S short for susceptible, I short for intermediate, R short for resistance, SDD short for susceptible-dose dependent',
  PRIMARY KEY (`ROW_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Microbiology culture results and antibiotic sensitivities';

/*
CREATE TABLE PATIENTASSESS
*/
CREATE TABLE `patientassess` (
  `ROW_ID` int(11) unsigned NOT NULL COMMENT 'row number',
  `PATIENT_ID` varchar(20) NOT NULL COMMENT 'an identifier which specifies an individual patient',
  `HOSPITAL_ID` varchar(20) NOT NULL COMMENT 'an identifier which specifies a single patient''s admission to the hospital',
  `DBC` varchar(20) DEFAULT NULL COMMENT 'determinant-based classification',
  `RAC` varchar(20) DEFAULT NULL COMMENT 'revised Atlanta classification',
  `ETIOLOGY` varchar(200) DEFAULT NULL COMMENT 'causes of acute pancrestitis',
  `LC` varchar(200) DEFAULT NULL COMMENT 'local complication',
  `OF` varchar(200) DEFAULT NULL COMMENT 'organ failure',
  `MC` varchar(200) DEFAULT NULL COMMENT 'major complication',
  `CM` varchar(200) DEFAULT NULL COMMENT 'pre-existing co-morbid disease',
  `TI` smallint(5) unsigned DEFAULT NULL COMMENT 'days from the onset of symptoms to admission',
  PRIMARY KEY (`ROW_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='AP-specific assessment of patient in a hospital stay';

/*
CREATE TABLE intervention
*/
CREATE TABLE `intervention` (
  `ROW_ID` int(11) unsigned NOT NULL COMMENT 'row number',
  `PATIENT_ID` varchar(20) NOT NULL COMMENT 'an identifier which specifies an individual patient',
  `HOSPITAL_ID` varchar(20) NOT NULL COMMENT 'an identifier which specifies a single patient''s admission to the hospital',
  `PROCEDURE_DATE` date NOT NULL COMMENT 'date of a certain procedure event',
  `PROCEDURE` varchar(50) DEFAULT NULL COMMENT 'specific name for a certain prcedure event',
  PRIMARY KEY (`ROW_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Treatment information for minimally invasive step-up approach';

/*
CREATE TABLE d_item
*/
CREATE TABLE `d_item` (
  `ROW_ID` int(11) unsigned NOT NULL COMMENT 'row number',
  `ITEM_CODE` varchar(20) NOT NULL COMMENT 'local code for a certain monitoring item',
  `LABEL` varchar(200) DEFAULT NULL COMMENT 'specific name for a certain item_code',
  `LINKS_TO` varchar(50) NOT NULL COMMENT 'a certain table which links to the item',
  `PARAM_TYPE` varchar(20) DEFAULT NULL COMMENT 'basic data types including number or text',
  `VALUEUOM` varchar(20) DEFAULT NULL COMMENT 'unit of a certain value',
  PRIMARY KEY (`ROW_ID`),
  UNIQUE KEY `ITEM_CODE_UNIQUE` (`ITEM_CODE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Dictionary of local codes (’ITEM_CODE’) appearing in the AP database, except those that relate to laboratory tests';

/*
CREATE TABLE d_labitem
*/
CREATE TABLE `d_labitem` (
  `ROW_ID` int(11) unsigned NOT NULL COMMENT 'row number',
  `ITEM_CODE` varchar(20) NOT NULL COMMENT 'local code for a certain laboratory item',
  `LABEL` varchar(200) DEFAULT NULL COMMENT 'specific name for a certain item_code',
  `PARAM_TYPE` varchar(20) DEFAULT NULL COMMENT 'basic data types including number or text',
  `LAB_NAME` varchar(200) DEFAULT NULL COMMENT 'specific name for a certain laboratory test',
  `REFERENCE_RANGES` varchar(200) DEFAULT NULL COMMENT 'reference range of a certain value',
  `VALUEUOM` varchar(20) DEFAULT NULL COMMENT 'unit of a certain value',
  PRIMARY KEY (`ROW_ID`),
  UNIQUE KEY `ITEM_CODE_UNIQUE` (`ITEM_CODE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Dictionary of local codes (’ITEM_CODE’) appearing in the AP database that relate to laboratory tests';

/*
CREATE TABLE d_microitem
*/
CREATE TABLE `d_microitem` (
  `ROW_ID` int(11) unsigned NOT NULL COMMENT 'row number',
  `ITEM_CODE` varchar(20) NOT NULL COMMENT 'local code for a certain laboratory item',
  `LABEL` varchar(200) DEFAULT NULL COMMENT 'specific name for a certain item_code',
  PRIMARY KEY (`ROW_ID`),
  UNIQUE KEY `ITEM_CODE_UNIQUE` (`ITEM_CODE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Dictionary of local codes (’ITEM_CODE’) appearing in the AP database that relate to microorganisms and antibiotics';


-- CREATE FUNCTION SPLITSTR_BLOCKS
DROP FUNCTION IF EXISTS SPLITSTR_BLOCKS;
DELIMITER $$ 
CREATE FUNCTION SPLITSTR_BLOCKS 
(S_STRING VARCHAR(200),S_DELIMITER VARCHAR(10)) RETURNS int(11) 
BEGIN 
    return 1+(length(S_STRING) - length(replace(S_STRING,S_DELIMITER,''))); 
END$$ 
DELIMITER ; 

-- CREATE FUNCTION SPLITSTR
DROP FUNCTION IF EXISTS SPLITSTR;
DELIMITER $$ 
CREATE FUNCTION SPLITSTR 
(S_STRING VARCHAR(200),S_DELIMITER varchar(10),I_ORDER int) RETURNS VARCHAR(200)
BEGIN 
        DECLARE RESULT VARCHAR(200) default ''; 
        set RESULT = REVERSE(SUBSTRING_INDEX(REVERSE(SUBSTRING_INDEX(S_STRING,S_DELIMITER,I_ORDER)),S_DELIMITER,1)); 
        return result; 
END$$ 
DELIMITER ;

-- CREATE PROCEDURE CALC_ETIOLOGY_NUMS
DROP PROCEDURE IF EXISTS CALC_ETIOLOGY_NUMS;
DELIMITER $$ 
CREATE PROCEDURE CALC_ETIOLOGY_NUMS() 
BEGIN
DECLARE ETIOLOGY VARCHAR(200); 
DECLARE FLAG INT DEFAULT 0;
DECLARE CNT INT DEFAULT 0;
DECLARE FIND_COUNT INT DEFAULT 0;
DECLARE ROW_ID VARCHAR(100);
DECLARE LAST_ROW_ID INT DEFAULT 0;
DECLARE ITEM CURSOR FOR SELECT T.ETIOLOGY,T.ROW_ID FROM PATIENTASSESS T INNER JOIN
(SELECT MIN(M.HOSPITAL_ID) AS HOSPITAL_ID FROM PATIENTASSESS M GROUP BY M.PATIENT_ID ORDER BY M.PATIENT_ID,M.HOSPITAL_ID) P
ON T.HOSPITAL_ID = P.HOSPITAL_ID
WHERE T.ETIOLOGY IS NOT NULL AND T.ETIOLOGY != '';
DECLARE CONTINUE HANDLER FOR NOT FOUND SET FLAG=1;

DROP TEMPORARY TABLE IF EXISTS UNIQUE_ETIOLOGY;
-- CREATE TEMPORARY TABLE UNIQUE_ETIOLOGY
CREATE TEMPORARY TABLE UNIQUE_ETIOLOGY(
ROW_ID INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
ETIOLOGY VARCHAR(200),
PRIMARY KEY (`ROW_ID`),
NUM INT(11) NULL DEFAULT 0
);
-- DELETE UNIQUE_ETIOLOGY
DELETE FROM UNIQUE_ETIOLOGY;
OPEN ITEM;
	READ_LOOP: REPEAT
		IF NOT FLAG THEN
			FETCH ITEM INTO ETIOLOGY,ROW_ID;
            IF LAST_ROW_ID <> ROW_ID THEN
				SET CNT = SPLITSTR_BLOCKS (ETIOLOGY,';'); 
				IF CNT > 1 THEN
					SET FIND_COUNT = (SELECT COUNT(1) FROM UNIQUE_ETIOLOGY T WHERE T.ETIOLOGY = 'Mixed');
					IF FIND_COUNT = 0 THEN
						INSERT INTO UNIQUE_ETIOLOGY(`ETIOLOGY`,`NUM`) VALUES('Mixed',1);
						COMMIT;
					ELSE
						UPDATE UNIQUE_ETIOLOGY T SET T.NUM = T.NUM + 1 WHERE T.ETIOLOGY = 'Mixed';
						COMMIT;
					END IF;
				ELSE
					SET FIND_COUNT = (SELECT COUNT(1) FROM UNIQUE_ETIOLOGY T WHERE T.ETIOLOGY = ETIOLOGY);
					IF FIND_COUNT = 0 THEN
						INSERT INTO UNIQUE_ETIOLOGY(`ETIOLOGY`,`NUM`) VALUES(ETIOLOGY,1);
						COMMIT;
					ELSE
						UPDATE UNIQUE_ETIOLOGY T SET T.NUM = T.NUM + 1 WHERE T.ETIOLOGY = ETIOLOGY;
						COMMIT;
					END IF;
				END IF;
                SET LAST_ROW_ID = ROW_ID;
            END IF;
        END IF;
	UNTIL FLAG END REPEAT READ_LOOP;CLOSE ITEM;
END$$ 
DELIMITER ; 

-- CREATE PROCEDURE CALC_LC_NUMS
DROP PROCEDURE IF EXISTS CALC_LC_NUMS;
DELIMITER $$ 
CREATE PROCEDURE CALC_LC_NUMS() 
BEGIN
DECLARE LC VARCHAR(200); 
DECLARE FLAG INT DEFAULT 0;
DECLARE CNT INT DEFAULT 0;
DECLARE i INT DEFAULT 0;
DECLARE PARTSTR VARCHAR(200);
DECLARE FIND_COUNT INT DEFAULT 0;
DECLARE ROW_ID INT DEFAULT 0;
DECLARE LAST_ROW_ID INT DEFAULT 0;
DECLARE ITEM CURSOR FOR SELECT T.LC,T.ROW_ID FROM PATIENTASSESS T WHERE T.LC IS NOT NULL AND T.LC != '';
DECLARE CONTINUE HANDLER FOR NOT FOUND SET FLAG=1;
DROP TEMPORARY TABLE IF EXISTS UNIQUE_LC;
-- CREATE TEMPORARY TABLE UNIQUE_LC
CREATE TEMPORARY TABLE UNIQUE_LC(
ROW_ID INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
LC VARCHAR(200),
PRIMARY KEY (`ROW_ID`),
NUM INT(11) NULL DEFAULT 0
);
DELETE FROM UNIQUE_LC;
OPEN ITEM;
	REPEAT
		FETCH ITEM INTO LC,ROW_ID;
        IF ROW_ID <> LAST_ROW_ID THEN
			SET CNT = SPLITSTR_BLOCKS (LC,';'); 
			WHILE i < cnt 
			DO 
				SET i = i + 1; 
				SET PARTSTR = SPLITSTR (LC,';',i);
				SET FIND_COUNT = (SELECT COUNT(1) FROM UNIQUE_LC T WHERE T.LC = PARTSTR);
				IF FIND_COUNT = 0 THEN
					INSERT INTO UNIQUE_LC(`LC`,`NUM`) VALUES(PARTSTR,1);
					COMMIT;
				ELSE
					UPDATE UNIQUE_LC T SET T.NUM = T.NUM + 1 WHERE T.LC = PARTSTR;
					COMMIT;
				END IF;
			END WHILE; 
			SET i = 0;
            SET LAST_ROW_ID = ROW_ID;
        END IF;
	UNTIL FLAG END REPEAT;
CLOSE ITEM;
END$$
DELIMITER ; 
