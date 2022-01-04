# We developed a MySQL database (version 5.7) for data management.
# Scripts were written in Python (version 3.7.3) to generate statistical graphics.
# Packages pymysql (version 1.0.2) and pyecharts (version 1.9.1) for python were used.
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Pie
from pyecharts.charts import Line
from pyecharts.charts import Grid
from pyecharts.commons.utils import JsCode
import pymysql
from pymysql.constants import CLIENT

# connect to MySQL database
set_host=""
set_user=""
set_password=""
set_database="pancreas"
conn = pymysql.connect(
    host=set_host,
    user=set_user,
    password=set_password,
    database=set_database,
    client_flag=CLIENT.MULTI_STATEMENTS
)
cursor = conn.cursor()
# query the frequency of hospitalizations in different age groups
sql="""
SELECT CASE
        WHEN ROUND(DATEDIFF(T.ADMISSION_TIME, T.DOB) / 365.25,2) < 11 THEN '0-10'
        WHEN ROUND(DATEDIFF(T.ADMISSION_TIME, T.DOB) / 365.25,2) < 21 THEN '11-20'
        WHEN ROUND(DATEDIFF(T.ADMISSION_TIME, T.DOB) / 365.25,2) < 31 THEN '21-30'
        WHEN ROUND(DATEDIFF(T.ADMISSION_TIME, T.DOB) / 365.25,2) < 41 THEN '31-40'
        WHEN ROUND(DATEDIFF(T.ADMISSION_TIME, T.DOB) / 365.25,2) < 51 THEN '41-50'
        WHEN ROUND(DATEDIFF(T.ADMISSION_TIME, T.DOB) / 365.25,2) < 61 THEN '51-60'
        WHEN ROUND(DATEDIFF(T.ADMISSION_TIME, T.DOB) / 365.25,2) < 71 THEN '61-70'
        WHEN ROUND(DATEDIFF(T.ADMISSION_TIME, T.DOB) / 365.25,2) < 81 THEN '71-80'
        WHEN ROUND(DATEDIFF(T.ADMISSION_TIME, T.DOB) / 365.25,2) < 91 THEN '81-90'
        ELSE '>=91'
    END AGE_RANGE,COUNT(1) AS AGE_GROUP_COUNT
FROM ADMISSION T
INNER JOIN 
(SELECT M.HOSPITAL_ID,MIN(M.ROW_ID) AS ROW_ID FROM ADMISSION M GROUP BY M.HOSPITAL_ID) P
ON T.ROW_ID = P.ROW_ID
GROUP BY AGE_RANGE
ORDER BY AGE_RANGE;
"""
cursor.execute(sql)
data = cursor.fetchall()
age_classes=[]
male_classes_count=[]
female_classes_count=[]
for name,val in data:
    age_classes.append(name)
# query the frequency of hospitalizations in different genders and age groups
sql="""
SELECT IFNULL(SUM(CASE C1.GENDER WHEN 'F' THEN C1.GENDER_COUNT ELSE 0 END),0) AS FEMALE,
	   IFNULL(SUM(CASE C1.GENDER WHEN 'M' THEN C1.GENDER_COUNT ELSE 0 END),0) AS MALE,
        '0-10' AS GENDER_TYPE
FROM 
(SELECT  T.GENDER, COUNT(*) AS GENDER_COUNT 
FROM ADMISSION T
INNER JOIN 
(SELECT HOSPITAL_ID,MIN(ROW_ID) AS ROW_ID FROM ADMISSION GROUP BY HOSPITAL_ID) M
ON T.ROW_ID = M.ROW_ID
WHERE ROUND(DATEDIFF(T.ADMISSION_TIME, T.DOB) / 365.25,2) < 11
GROUP BY T.GENDER) C1
UNION 
SELECT IFNULL(SUM(CASE C2.GENDER WHEN 'F' THEN C2.GENDER_COUNT ELSE 0 END),0) AS FEMALE,
	   IFNULL(SUM(CASE C2.GENDER WHEN 'M' THEN C2.GENDER_COUNT ELSE 0 END),0) AS MALE,
        '11-20' AS GENDER_TYPE
        FROM 
(SELECT  T.GENDER, COUNT(*) AS GENDER_COUNT 
FROM ADMISSION T
INNER JOIN 
(SELECT HOSPITAL_ID,MIN(ROW_ID) AS ROW_ID FROM ADMISSION GROUP BY HOSPITAL_ID) M
ON T.ROW_ID = M.ROW_ID
WHERE ROUND(DATEDIFF(T.ADMISSION_TIME, T.DOB) / 365.25,2) >= 11 && ROUND(DATEDIFF(T.ADMISSION_TIME, T.DOB) / 365.25,2) < 21 
GROUP BY T.GENDER) C2
UNION
SELECT IFNULL(SUM(CASE C3.GENDER WHEN 'F' THEN C3.GENDER_COUNT ELSE 0 END),0) AS FEMALE,
	   IFNULL(SUM(CASE C3.GENDER WHEN 'M' THEN C3.GENDER_COUNT ELSE 0 END),0) AS MALE,
        '21-30' AS GENDER_TYPE
        FROM 
(SELECT  T.GENDER, COUNT(*) AS GENDER_COUNT 
FROM ADMISSION T
INNER JOIN 
(SELECT HOSPITAL_ID,MIN(ROW_ID) AS ROW_ID FROM ADMISSION GROUP BY HOSPITAL_ID) M
ON T.ROW_ID = M.ROW_ID
WHERE ROUND(DATEDIFF(T.ADMISSION_TIME, T.DOB) / 365.25,2) >= 21 && ROUND(DATEDIFF(T.ADMISSION_TIME, T.DOB) / 365.25,2) < 31 
GROUP BY T.GENDER) C3
UNION
SELECT IFNULL(SUM(CASE C4.GENDER WHEN 'F' THEN C4.GENDER_COUNT ELSE 0 END),0) AS FEMALE,
	   IFNULL(SUM(CASE C4.GENDER WHEN 'M' THEN C4.GENDER_COUNT ELSE 0 END),0) AS MALE,
        '31-40' AS GENDER_TYPE
        FROM 
(SELECT  T.GENDER, COUNT(*) AS GENDER_COUNT 
FROM ADMISSION T
INNER JOIN 
(SELECT HOSPITAL_ID,MIN(ROW_ID) AS ROW_ID FROM ADMISSION GROUP BY HOSPITAL_ID) M
ON T.ROW_ID = M.ROW_ID
WHERE ROUND(DATEDIFF(T.ADMISSION_TIME, T.DOB) / 365.25,2) >= 31 && ROUND(DATEDIFF(T.ADMISSION_TIME, T.DOB) / 365.25,2) < 41 
GROUP BY T.GENDER) C4
UNION
SELECT IFNULL(SUM(CASE C5.GENDER WHEN 'F' THEN C5.GENDER_COUNT ELSE 0 END),0) AS FEMALE,
	   IFNULL(SUM(CASE C5.GENDER WHEN 'M' THEN C5.GENDER_COUNT ELSE 0 END),0) AS MALE,
        '41-50' AS GENDER_TYPE
        FROM 
(SELECT  T.GENDER, COUNT(*) AS GENDER_COUNT 
FROM ADMISSION T
INNER JOIN 
(SELECT HOSPITAL_ID,MIN(ROW_ID) AS ROW_ID FROM ADMISSION GROUP BY HOSPITAL_ID) M
ON T.ROW_ID = M.ROW_ID
WHERE ROUND(DATEDIFF(T.ADMISSION_TIME, T.DOB) / 365.25,2) >= 41 && ROUND(DATEDIFF(T.ADMISSION_TIME, T.DOB) / 365.25,2) < 51 
GROUP BY T.GENDER) C5
UNION
SELECT IFNULL(SUM(CASE C6.GENDER WHEN 'F' THEN C6.GENDER_COUNT ELSE 0 END),0) AS FEMALE,
	   IFNULL(SUM(CASE C6.GENDER WHEN 'M' THEN C6.GENDER_COUNT ELSE 0 END),0) AS MALE,
        '51-60' AS GENDER_TYPE
        FROM 
(SELECT  T.GENDER, COUNT(*) AS GENDER_COUNT 
FROM ADMISSION T
INNER JOIN 
(SELECT HOSPITAL_ID,MIN(ROW_ID) AS ROW_ID FROM ADMISSION GROUP BY HOSPITAL_ID) M
ON T.ROW_ID = M.ROW_ID
WHERE ROUND(DATEDIFF(T.ADMISSION_TIME, T.DOB) / 365.25,2) >= 51 && ROUND(DATEDIFF(T.ADMISSION_TIME, T.DOB) / 365.25,2) < 61 
GROUP BY T.GENDER) C6
UNION
SELECT IFNULL(SUM(CASE C7.GENDER WHEN 'F' THEN C7.GENDER_COUNT ELSE 0 END),0) AS FEMALE,
	   IFNULL(SUM(CASE C7.GENDER WHEN 'M' THEN C7.GENDER_COUNT ELSE 0 END),0) AS MALE,
        '61-70' AS GENDER_TYPE
        FROM 
(SELECT  T.GENDER, COUNT(*) AS GENDER_COUNT 
FROM ADMISSION T
INNER JOIN 
(SELECT HOSPITAL_ID,MIN(ROW_ID) AS ROW_ID FROM ADMISSION GROUP BY HOSPITAL_ID) M
ON T.ROW_ID = M.ROW_ID
WHERE ROUND(DATEDIFF(T.ADMISSION_TIME, T.DOB) / 365.25,2) >= 61 && ROUND(DATEDIFF(T.ADMISSION_TIME, T.DOB) / 365.25,2) < 71 
GROUP BY T.GENDER) C7
UNION
SELECT IFNULL(SUM(CASE C8.GENDER WHEN 'F' THEN C8.GENDER_COUNT ELSE 0 END),0) AS FEMALE,
	   IFNULL(SUM(CASE C8.GENDER WHEN 'M' THEN C8.GENDER_COUNT ELSE 0 END),0) AS MALE,
        '71-80' AS GENDER_TYPE
        FROM 
(SELECT  T.GENDER, COUNT(*) AS GENDER_COUNT 
FROM ADMISSION T
INNER JOIN 
(SELECT HOSPITAL_ID,MIN(ROW_ID) AS ROW_ID FROM ADMISSION GROUP BY HOSPITAL_ID) M
ON T.ROW_ID = M.ROW_ID
WHERE ROUND(DATEDIFF(T.ADMISSION_TIME, T.DOB) / 365.25,2) >= 71 && ROUND(DATEDIFF(T.ADMISSION_TIME, T.DOB) / 365.25,2) < 81 
GROUP BY T.GENDER) C8
UNION
SELECT IFNULL(SUM(CASE C9.GENDER WHEN 'F' THEN C9.GENDER_COUNT ELSE 0 END),0) AS FEMALE,
	   IFNULL(SUM(CASE C9.GENDER WHEN 'M' THEN C9.GENDER_COUNT ELSE 0 END),0) AS MALE,
        '81-90' AS GENDER_TYPE
        FROM 
(SELECT  T.GENDER, COUNT(*) AS GENDER_COUNT 
FROM ADMISSION T
INNER JOIN 
(SELECT HOSPITAL_ID,MIN(ROW_ID) AS ROW_ID FROM ADMISSION GROUP BY HOSPITAL_ID) M
ON T.ROW_ID = M.ROW_ID
WHERE ROUND(DATEDIFF(T.ADMISSION_TIME, T.DOB) / 365.25,2) >= 81 && ROUND(DATEDIFF(T.ADMISSION_TIME, T.DOB) / 365.25,2) < 91 
GROUP BY T.GENDER) C9
ORDER BY GENDER_TYPE
"""
cursor.execute(sql)
data = cursor.fetchall()
for fc,mc,cs in data:
    female_classes_count.append(fc)
    male_classes_count.append(mc)
# query the total hospitalizations in different genders
sql="""
SELECT T.GENDER,COUNT(*) AS GENDER_COUNT FROM ADMISSION T
INNER JOIN
(SELECT HOSPITAL_ID,MIN(ROW_ID) AS ROW_ID FROM ADMISSION GROUP BY HOSPITAL_ID) M
ON T.ROW_ID = M.ROW_ID
GROUP BY T.GENDER
ORDER BY GENDER;
"""
male_total=0
female_total=0
cursor.execute(sql)
data = cursor.fetchall()
for t,v in data:
    if t == 'F':
        female_total=v
    else:
        male_total=v
# draw graph for the distribution of gender and age
bar = Bar()
bar.add_xaxis(age_classes)
bar.add_yaxis(
    "Female",
    female_classes_count,
    stack="stack",
    label_opts=opts.LabelOpts(is_show=False)
)
bar.add_yaxis(
    "Male",
    male_classes_count,
    stack="stack",
    label_opts=opts.LabelOpts(is_show=False)
)
bar.set_global_opts(
    xaxis_opts=opts.AxisOpts(name="years")
)
pie = Pie()
pie.add(
    series_name="gender rate",
    data_pair=[
        ["Female",female_total],
        ["Male",male_total]
    ],
    center=["85%","18%"],
    radius=[0,"30%"],
    label_opts=opts.LabelOpts(
        position="inner",
        formatter=JsCode(
            "function(x){if(x.name==='Male'){return'Male\\n'+x.percent+'%'}else{return'Female\\n'+x.percent+'%'}}"
        )
    )
)
bar.overlap(pie)
bar.set_global_opts(
    title_opts=opts.TitleOpts(title="Age and gender",pos_left="center",pos_top = "bottom"),
    legend_opts=opts.LegendOpts(is_show=False)
)
bar.set_colors(["brown","#2F4554"])
bar.render("Ageandgender.html")

# etiologies
cursor.callproc("CALC_ETIOLOGY_NUMS")
# query the etiologies of individuals
sql="""
SELECT T.ETIOLOGY,T.NUM FROM UNIQUE_ETIOLOGY T ORDER BY T.NUM DESC;
"""
cursor.execute(sql)
data=cursor.fetchall()
etiology_names=[]
etiology_vals=[]
for name,val in data:
    etiology_names.append(name)
    etiology_vals.append(val)
# draw graph for the rank of etiologies
bar_etilogy=Bar(init_opts=opts.InitOpts(width="1800px"))
bar_etilogy.add_xaxis(etiology_names)
bar_etilogy.add_yaxis("etiology",etiology_vals)
bar_etilogy.reversal_axis()
bar_etilogy.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
bar_etilogy.set_global_opts(
    title_opts=opts.TitleOpts(title="Etiology",pos_left="center",pos_top="bottom"),
    yaxis_opts=opts.AxisOpts(
        is_inverse=True
    ),
    legend_opts=opts.LegendOpts(is_show=False)
)
bar_etilogy.render("Etiology.html")

# local complications
cursor.callproc("CALC_LC_NUMS")
# query local complications of patients in every hospitalization
sql="""
SELECT T.LC,T.NUM FROM UNIQUE_LC T ORDER BY T.NUM DESC;
"""
cursor.execute(sql)
data=cursor.fetchall()
lc_pair=[]
for name,val in data:
    lc_pair.append([name,val])
# draw graph for the distribution of local complications
pie_lc=Pie()
pie_lc.add(
    series_name="LC",
    data_pair=lc_pair,
    label_opts=opts.LabelOpts(is_show=False)
)
pie_lc.set_global_opts(
    title_opts=opts.TitleOpts(title="Local complications",pos_left="center",pos_top="bottom"),
    legend_opts=opts.LegendOpts(
        is_show=True,
        pos_left="right",
        pos_top="middle",
        orient="vertical",
        align="left"
    ),
)
pie_lc.render("Local_complications.html")

# severity
# query severity of patients evaluated by DBC in every hospitalization
sql="""
SELECT T.DBC,
		(CASE WHEN T.DBC='Mild' THEN 1
			 WHEN T.DBC='Moderate' THEN 2
             WHEN T.DBC='Severe'  THEN 3
             ELSE 4
		END) AS SORT_NO,
		COUNT(1) AS NUM 
FROM PATIENTASSESS T 
GROUP BY T.DBC 
ORDER BY SORT_NO;
"""
cursor.execute(sql)
data=cursor.fetchall()
dbc_names=[]
dbc_vals=[]
for n,s,v in data:
    dbc_names.append('DBC ' +n)
    dbc_vals.append(v)
# query severity of patients evaluated by RAC in every hospitalization 
sql="""
SELECT T.RAC,
		(CASE WHEN T.RAC='Mild' THEN 1
			 WHEN T.RAC='Moderate severe' THEN 2
             ELSE 3
		END) AS SORT_NO,
COUNT(1) AS NUM FROM PATIENTASSESS T GROUP BY T.RAC;
"""
cursor.execute(sql)
data=cursor.fetchall()
rac_names=[]
rac_vals=[]
for n,s,v in data:
    rac_names.append('RAC '+ n)
    rac_vals.append(v)
dbcdata_pair=[]
dbcnames=dbc_names
dbcvals=dbc_vals
for k,v,c in zip(dbcnames,dbcvals,["green","orange","red","darkred"]):
    dbcdata_pair.append(opts.PieItem(
        name=k,
        value=v,
        itemstyle_opts=opts.ItemStyleOpts(color=c)
    ))

racdata_pair=[]
racnames=rac_names
racvals=rac_vals
for k,v,c in zip(racnames,racvals,["green","orange","red"]):
    racdata_pair.append(opts.PieItem(
        name=k,
        value=v,
        itemstyle_opts=opts.ItemStyleOpts(color=c)
    ))
# draw graph for the distribution of severity
pie_dbcrac=Pie()
pie_dbcrac.add(
    series_name="DBC",
    data_pair=dbcdata_pair,
    radius=[0,"30%"],
    label_opts=opts.LabelOpts(
        is_show=True,
        position="inside",
        formatter=JsCode(
            "function(x){return x.name.split(' ')[1];}"
        ),
        color="black"
    )
)
pie_dbcrac.add(
    series_name="RAC",
    data_pair=racdata_pair,
    radius=["45%", "60%"],
    label_opts=opts.LabelOpts(
        is_show=True,
        position="inside",
        formatter=JsCode(
            "function(x){return x.name.split(' ')[1];}"
        ),
        color="black"
    )
)
pie_dbcrac.set_global_opts(
    title_opts=opts.TitleOpts(
        title="Severity",
        subtitle="(doughnut: RAC, pie: DBC)",
        pos_left="center",
        pos_top="85%"
    ),
    legend_opts=opts.LegendOpts(is_show=False)
)
pie_dbcrac.render("Severity.html")

# query top 10 microorganisms cultured in blood specimen
sql="""
SELECT M.LABEL AS MB_NAME,COUNT(1) AS MB_COUNT FROM (
SELECT T.HOSPITAL_ID,D.LABEL
FROM MICROLAB T 
INNER JOIN D_MICROITEM D ON T.MB_ITEM_CODE = D.ITEM_CODE 
WHERE T.SPEC = 'blood' 
GROUP BY T.HOSPITAL_ID,D.LABEL
) M 
GROUP BY M.LABEL 
ORDER BY MB_COUNT DESC LIMIT 10;
"""
cursor.execute(sql)
data=cursor.fetchall()
blood_names=[]
blood_vals=[]
for name,val in data:
    blood_names.append(name)
    blood_vals.append(-val)
# query top 10 microorganisms cultured in pacreatic/peripancreatic   necrosis tissue
sql="""
SELECT M.LABEL AS MB_NAME,COUNT(1) AS MB_COUNT FROM (
SELECT T.HOSPITAL_ID,D.LABEL
FROM MICROLAB T 
INNER JOIN D_MICROITEM D ON T.MB_ITEM_CODE = D.ITEM_CODE 
WHERE T.SPEC = 'pacreatic/peripancreatic necrosis tissue' 
GROUP BY T.HOSPITAL_ID,D.LABEL
) M 
GROUP BY M.LABEL 
ORDER BY MB_COUNT DESC LIMIT 10;
"""
cursor.execute(sql)
data=cursor.fetchall()
pacreatic_names=[]
pacreatic_vals=[]
for name,val in data:
    pacreatic_names.append(name)
    pacreatic_vals.append(val)
# draw graph for the rank of microorganisms cultured in different specimens
bar_mb1=Bar()
bar_mb1.add_yaxis(
    series_name="blood",
    y_axis=blood_vals,
    xaxis_index=0,
    label_opts=opts.LabelOpts(
        is_show=False
    )
)
bar_mb1.add_xaxis(blood_names)
bar_mb1.reversal_axis()
bar_mb1.set_global_opts(
    yaxis_opts=opts.AxisOpts(
        axislabel_opts=opts.LabelOpts(
            margin=-20
        ),
        is_inverse=True
    ),
    xaxis_opts=opts.AxisOpts(
        axislabel_opts=opts.LabelOpts(
            formatter=JsCode(
                "function(x){if(x < 0)return -x;else return x;}"
            )
        )
    ),
    legend_opts=opts.LegendOpts(
        pos_left="40%"
    )
)

bar_mb2=Bar()
bar_mb2.add_yaxis(
    series_name="pacreatic/peripancreatic necrosis tissue",
    y_axis=pacreatic_vals,
    label_opts=opts.LabelOpts(
        is_show=False
    )
)
bar_mb2.add_xaxis(pacreatic_names)
bar_mb2.reversal_axis()
bar_mb2.set_global_opts(
    xaxis_opts=opts.AxisOpts(
        position="bottom",
        grid_index=0
    ),
    yaxis_opts=opts.AxisOpts(
        position="right",
        axislabel_opts=opts.LabelOpts(
            margin=-20
        ),
        is_inverse=True
    ),
    legend_opts=opts.LegendOpts(
        pos_left="55%"
    ),
    title_opts=opts.TitleOpts(
        title="Microbiology",
        pos_left="center",
        pos_top="bottom"
    )
)

grid_mb=Grid(init_opts=opts.InitOpts(width="1800px",height="600px"))
grid_mb.add(bar_mb1,grid_opts=opts.GridOpts(pos_right="50%"))
grid_mb.add(bar_mb2,grid_opts=opts.GridOpts(pos_left="50%"))
grid_mb.render("Microbiology.html")

# query the lengths of hospitalization
sql="""
SELECT  (CASE WHEN DATEDIFF(T.DISCHARGE_TIME,T.ADMISSION_TIME) <= 7 THEN '<=1w'
			 WHEN DATEDIFF(T.DISCHARGE_TIME,T.ADMISSION_TIME) <= 14 THEN '1-2w'
             WHEN DATEDIFF(T.DISCHARGE_TIME,T.ADMISSION_TIME) <= 21 THEN '2-3w'
             WHEN DATEDIFF(T.DISCHARGE_TIME,T.ADMISSION_TIME) <= 28 THEN '3-4w'
             ELSE
				'>4w'
		 END) AS HOS_DAYS,
         (CASE WHEN DATEDIFF(T.DISCHARGE_TIME,T.ADMISSION_TIME) <= 7 THEN 1
			 WHEN DATEDIFF(T.DISCHARGE_TIME,T.ADMISSION_TIME) <= 14 THEN 2
             WHEN DATEDIFF(T.DISCHARGE_TIME,T.ADMISSION_TIME) <= 21 THEN 3
             WHEN DATEDIFF(T.DISCHARGE_TIME,T.ADMISSION_TIME) <= 28 THEN 4
             ELSE
				5
		 END) AS SORT_NO,
         COUNT(1) AS DAYS_COUNT FROM ADMISSION T
INNER JOIN 
(SELECT M.HOSPITAL_ID,MIN(M.ROW_ID) AS ROW_ID FROM ADMISSION M GROUP BY M.HOSPITAL_ID) P
ON T.ROW_ID = P.ROW_ID
GROUP BY HOS_DAYS
ORDER BY SORT_NO;
"""
cursor.execute(sql)
data=cursor.fetchall()
days_names=[]
days_vals=[]
for n,s,v in data:
    days_names.append(n)
    days_vals.append(v)
# draw graph for the distribution of lengths of hospitalization
bar_days = Bar()
bar_days.add_xaxis(days_names)
bar_days.add_yaxis("In Hospital Days",days_vals,label_opts=opts.LabelOpts(is_show=False))
bar_days.set_global_opts(
    title_opts=opts.TitleOpts(
        title="Lengths of hospitalization",
        pos_left="center",
        pos_top = "bottom"
    ),
    yaxis_opts=opts.AxisOpts(
        splitline_opts=opts.SplitLineOpts(
            is_show=True
        )
    ),
    legend_opts=opts.LegendOpts(
        is_show=False
    )
)
bar_days.render("Lengths_of_hospitalization.html")
