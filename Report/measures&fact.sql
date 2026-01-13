DROP TABLE IF EXISTS dim_user;
GO

CREATE TABLE dim_user (
    user_key INT IDENTITY(1,1) PRIMARY KEY,
    user_id VARCHAR(100) UNIQUE,

    user_name VARCHAR(200),
    user_email VARCHAR(300),
    gender VARCHAR(50),

    city VARCHAR(150),
    state VARCHAR(150),
    school VARCHAR(200),
    class_level VARCHAR(100),
    language VARCHAR(100),

    rating_as_learner FLOAT,
    rating_as_guru FLOAT,
    wallet_balance FLOAT,
    referred_users INT,

    create_date DATETIME,
    update_date DATETIME
);
GO


TRUNCATE TABLE dim_user;
GO
INSERT INTO dim_user (
    user_id,
    user_name,
    user_email,
    gender,
    city,
    state,
    school,
    class_level,
    language,
    rating_as_learner,
    rating_as_guru,
    wallet_balance,
    referred_users,
    create_date,
    update_date
)
SELECT DISTINCT
    user_id,
    user_name,
    user_email,

    -- ✅ FIX: Keep only valid gender values
    CASE 
        WHEN LOWER(gender) IN ('male','female','m','f','other') THEN gender
        ELSE 'Unknown'
    END AS gender,

    city,
    state,
    school,
    class_level,
    language,
    TRY_CAST(rating_as_learner AS FLOAT),
    TRY_CAST(rating_as_guru AS FLOAT),
    TRY_CAST(wallet_balance AS FLOAT),
    TRY_CAST(referred_users AS INT),
    TRY_CAST(create_date AS DATETIME),
    TRY_CAST(update_date AS DATETIME)
FROM Final_User_Data;





----------------------------------------------------------------------
DROP TABLE IF EXISTS fact_quiz;
GO
CREATE TABLE fact_quiz (
    quiz_id             VARCHAR(100),
    quiz_type           VARCHAR(50),
    quiz_status         VARCHAR(MAX),
    status              VARCHAR(50),
    mode                VARCHAR(50),
    language            VARCHAR(50),
	questions           INT,
    sec_per_question    INT,
    participants        INT,
    results_users       INT,
	winner_score        INT,
    winner_time         INT,
    winner_final_score  INT,
    create_date         DATETIME,
    start_date          DATETIME,
    complete_date       DATETIME,
    created_year        INT,
    created_month       VARCHAR(50),
    livequiz_subject    VARCHAR(150),
    livequiz_topic      VARCHAR(150),
    livequiz_difficulty VARCHAR(MAX),
    school              VARCHAR(150)
);


TRUNCATE TABLE fact_quiz;
GO
INSERT INTO fact_quiz (
    quiz_id,
    quiz_type,
    quiz_status,
    status,
    mode,
    language,
    questions,
    sec_per_question,
    participants,
    results_users,
    winner_score,           -- AS-IS
    winner_time,
    winner_final_score,     -- AS-IS
    create_date,
    start_date,
    complete_date,
    created_year,
    created_month,
    livequiz_subject,
    livequiz_topic,
    livequiz_difficulty,
    school,
    user_id
)
SELECT
    quiz_id,
    quiz_type,
    quiz_status,
    [status],
    [mode],
    [language],

    TRY_CAST(questions AS INT),
    TRY_CAST(sec_per_question AS INT),
    TRY_CAST(participants AS INT),
    TRY_CAST(results_users AS INT),

    -- 👇 SCORES: INSERT EXACTLY AS THEY ARE
    winner_score,
    winner_time,
    winner_final_score,

    TRY_CAST(create_date AS DATETIME),
    TRY_CAST(start_date AS DATETIME),
    TRY_CAST(complete_date AS DATETIME),

    CASE 
        WHEN created_year = '2026.0' THEN 2026
        WHEN created_year = '2025.0' THEN 2025
        ELSE TRY_CAST(created_year AS INT)
    END,

    created_month,
    livequiz_subject,
    livequiz_topic,
    livequiz_difficulty,
    school,

    creator_id     -- user_id mapping
FROM Final_Clean_Quiz_Data;

--==========================================
ALTER TABLE fact_quiz
ALTER COLUMN winner_score VARCHAR(100);

ALTER TABLE fact_quiz
ALTER COLUMN winner_final_score VARCHAR(100);


-- ===============================================


SELECT
    q.quiz_id,
    q.creator_id,

    TRY_CAST(q.participants AS INT),
    TRY_CAST(q.results_users AS INT),
    TRY_CAST(q.winner_score AS INT),

    CASE 
        WHEN TRY_CAST(q.participants AS INT) > 0 
        THEN TRY_CAST(q.results_users AS FLOAT) 
             / TRY_CAST(q.participants AS FLOAT)
        ELSE 0
    END,

    TRY_CAST(q.create_date AS DATETIME),
    TRY_CAST(q.start_date AS DATETIME),
    TRY_CAST(q.complete_date AS DATETIME)

FROM Final_Clean_Quiz_Data q;








------------------------------------------------------------------------------------
SELECT COUNT(*) AS total_users FROM dim_user;
SELECT COUNT(*) AS total_quiz_records FROM fact_quiz;

SELECT TOP 10 * FROM dim_user;
SELECT TOP 10 * FROM fact_quiz;


SELECT
    COUNT(*) AS total_quizzes,
    SUM(CASE WHEN results_users > participants THEN 1 ELSE 0 END) AS mismatched_rows
FROM fact_quizzes;

