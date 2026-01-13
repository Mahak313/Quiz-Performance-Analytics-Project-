CREATE OR ALTER VIEW vw_quiz_dashboard_analytics_mine AS
SELECT
    -- =========================
    -- IDENTIFIERS
    -- =========================
    f.quiz_id,
    f.quiz_type,
    f.quiz_status,
    f.status,
    f.mode,
    f.language,
    f.school,

    -- =========================
    -- CONTENT METADATA
    -- =========================
    f.livequiz_subject,
    f.livequiz_topic,
    f.livequiz_difficulty,

    -- =========================
    -- RAW METRICS
    -- =========================
    f.questions,
    f.sec_per_question,
    f.participants       AS reported_participants,
    f.results_users     AS reported_results_users,

    -- 👇 SCORES: NO LOGIC, NO CAST, NO CASE
    f.winner_score,            -- AS-IS
    f.winner_final_score,      -- AS-IS

    -- =========================
    -- KPI MEASURES (NO SCORE MATH)
    -- =========================
    CASE
        WHEN f.results_users > f.participants THEN f.results_users
        ELSE f.participants
    END AS effective_participants,

    f.results_users AS completed_users,

    CASE
        WHEN f.participants IS NULL OR f.participants = 0 THEN NULL
        ELSE ROUND((f.results_users * 100.0) / f.participants, 2)
    END AS completion_rate,

    CASE
        WHEN f.winner_score IS NULL AND f.winner_final_score IS NULL THEN 'Not Declared'
        ELSE 'Declared'
    END AS result_status,

    CASE 
        WHEN f.results_users > f.participants THEN 1
        ELSE 0
    END AS has_participant_mismatch,

    -- =========================
    -- TIME ANALYTICS
    -- =========================
    f.create_date,
    CAST(f.create_date AS DATE)        AS quiz_date,
    YEAR(f.create_date)               AS quiz_year,
    MONTH(f.create_date)              AS quiz_month,
    DATENAME(MONTH, f.create_date)    AS quiz_month_name,
    DATENAME(WEEKDAY, f.create_date)  AS quiz_day,
    DATEPART(HOUR, f.create_date)     AS quiz_hour

FROM fact_quiz f;



-- =========================================
-- Final view 
-- ========================================


SELECT * FROM vw_quiz_dashboard_analytics_mine


