-- Logging In to the Database
```mysql
mysql -uUserName -pPassword
use pancreas;
```


-- import data

```mysql
-- import admission data
load data infile 'admission.csv' into table admission fields terminated by "," lines terminated by "\r\n" IGNORE 1 LINES (ROW_ID,PATIENT_ID,HOSPITAL_ID,ICU_ID,DOB,GENDER,@PATIENT_HEIGHT,@PATIENT_WEIGHT,BLOOD_TYPE,@APACHE2,ADMISSION_TIME,DISCHARGE_TIME,@ICU_IN_TIME,@ICU_OUT_TIME,DISCHARGE_STATUS) SET PATIENT_HEIGHT = NULLIF(@PATIENT_HEIGHT,''),PATIENT_WEIGHT = NULLIF(@PATIENT_WEIGHT,''),APACHE2 = NULLIF(@APACHE2,''),ICU_IN_TIME = NULLIF(@ICU_IN_TIME,''),ICU_OUT_TIME = NULLIF(@ICU_OUT_TIME,'');

-- import patientassess data
load data infile 'patientassess.csv' into table patientassess fields terminated by "," lines terminated by "\n" IGNORE 1 LINES (ROW_ID,PATIENT_ID,HOSPITAL_ID,DBC,RAC,ETIOLOGY,LC,OF,MC,CM,@TI) SET TI = NULLIF(@TI,'');

-- import vitalsign data
load data infile 'vitalsign.csv' into table vitalsign fields terminated by "," lines terminated by "\r\n" IGNORE 1 LINES ;

-- import lab data
load data infile 'lab.csv' into table lab fields terminated by "," lines terminated by "\r\n" IGNORE 1 LINES ;

-- import microlab data
load data infile 'microlab.csv' into table microlab fields terminated by "," lines terminated by "\r\n" IGNORE 1 LINES ;

-- import fluidbalance data
load data infile 'fluidbalance.csv' into table fluidbalance fields terminated by "," lines terminated by "\r\n" IGNORE 1 LINES ;

-- import intervention data
load data infile 'intervention.csv' into table intervention fields terminated by "," lines terminated by "\r\n" IGNORE 1 LINES ;

-- import d_item data
load data infile 'd_item.csv' into table d_item fields terminated by "," lines terminated by "\r\n" IGNORE 1 LINES ;

-- import d_labitem data
load data infile 'd_labitem.csv' into table d_labitem fields terminated by "," lines terminated by "\r\n" IGNORE 1 LINES ;

-- import d_microitem data
load data infile 'd_microitem.csv' into table d_microitem fields terminated by "," lines terminated by "\r\n" IGNORE 1 LINES ;
```
