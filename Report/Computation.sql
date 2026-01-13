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
	winner_name         VARCHAR(150),
    winner_score        INT,
    winner_time         VARCHAR(50),
    winner_final_score  INT,
	create_date         DATETIME,
    start_date          DATETIME,
    complete_date       DATETIME,
	created_year        INT,
    created_month       VARCHAR(MAX),
	livequiz_subject    VARCHAR(150),
    livequiz_topic      VARCHAR(150),
    livequiz_difficulty VARCHAR(MAX),
    school              VARCHAR(150)
);
GO

TRUNCATE TABLE fact_quiz;
-------------------------------------------------------------------
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
    winner_name,
    winner_score,
    winner_time,
    winner_final_score,
    create_date,
    start_date,
    complete_date,
    created_year,
    created_month,
    livequiz_subject,
    livequiz_topic,
    livequiz_difficulty,
    school
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

    -- Winner Name (as-is except Not Declared)
    CASE 
        WHEN winner_name = 'Not Declared' OR winner_name IS NULL THEN NULL
        ELSE winner_name
    END,

    -- 🏆 Winner Score (AS-IS, NO CONVERSION)
    winner_score,

    -- ⏱ Winner Time (AS-IS)
    CASE 
        WHEN winner_time = 'Not Declared' OR winner_time IS NULL THEN NULL
        ELSE winner_time
    END,

    -- 🎯 Winner Final Score (AS-IS, NO CONVERSION)
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
    school
FROM Final_Clean_Quiz_Data;



































