CREATE DATABASE Skill_Guru_Foundation1;				--create database
GO 
USE  Skill_Guru_Foundation1;						--use that database
GO


-------------------------------------------------------------------------------------
--CREATE TABLE FINAL QUIZ DATA 
DROP TABLE IF EXISTS Final_Clean_Quiz_Data;
GO

CREATE TABLE Final_Clean_Quiz_Data (
    quiz_type           VARCHAR(50),
    quiz_id             VARCHAR(100),
    status              VARCHAR(50),
    mode                VARCHAR(50),
    language            VARCHAR(50),
    questions           VARCHAR(100),
    sec_per_question    VARCHAR(100),
    creator_name        VARCHAR(150),
    creator_id          VARCHAR(100),
    school              VARCHAR(150),
    participants        VARCHAR(100),
    results_users       VARCHAR(100),
    winner_name         VARCHAR(150),
    winner_score        VARCHAR(100),
    winner_time         VARCHAR(100),
    winner_final_score  VARCHAR(100),
    create_date         VARCHAR(100),
    start_date          VARCHAR(100),
    complete_date       VARCHAR(100),
    description         VARCHAR(MAX),
    livequiz_label      VARCHAR(MAX),
    livequiz_subject    VARCHAR(150),
    livequiz_topic      VARCHAR(150),
    livequiz_difficulty VARCHAR(MAX),
    livequiz_slot       VARCHAR(100),
    quiz_status         VARCHAR(MAX),
    created_year        VARCHAR(20),
    created_month       VARCHAR(MAX)
);


BULK INSERT Final_Clean_Quiz_Data
FROM 'D:\Data Analyst\Skill Foundation Project\Final_Clean_Quiz_Data.csv'
WITH (
    FIRSTROW = 2,              -- Header row skip
    FIELDTERMINATOR = ',',     -- Column separator
    ROWTERMINATOR = '\n',      -- New line
    TABLOCK
);



--------------------------------------------------------------------------------------
--CREATE TABLE FINAL USER DATA
DROP TABLE IF EXISTS Final_User_Data;
GO
CREATE TABLE Final_User_Data (
    user_id VARCHAR(100),
    user_name VARCHAR(200),
    user_email VARCHAR(300),
    gender VARCHAR(MAX),
    city VARCHAR(150),
    state VARCHAR(150),
    school VARCHAR(200),
    class_level VARCHAR(100),
    language VARCHAR(100),
    rating_as_learner VARCHAR(100),   -- FLOAT → VARCHAR (safe for bulk)
    rating_as_guru VARCHAR(100),      -- FLOAT → VARCHAR
    wallet_balance VARCHAR(100),      -- FLOAT → VARCHAR
    referred_users VARCHAR(100),      -- INT → VARCHAR
	 create_date VARCHAR(100),         -- DATETIME → VARCHAR
    update_date VARCHAR(MAX)          -- DATETIME → VARCHAR
);
TRUNCATE TABLE Final_User_Data;
--INSERT BULK DATA
BULK INSERT Final_User_Data
FROM 'D:\Data Analyst\Skill Foundation Project\Final_User_data_CLEANED.csv'
WITH (
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    TABLOCK
);

---------------------------------------------------------------------------------------

