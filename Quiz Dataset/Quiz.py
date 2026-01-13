import pandas as pd

print("🔹 Step 1: Loading data...")

# ✅ Correct file path
file_path = r"D:\Data Analyst\Skill Foundation Project\Quizzes_Dataset.xlsx"

df = pd.read_excel(file_path)
print("✅ Data loaded successfully\n")
print("----------------------------------------------------------------------------")
print("🔹 Initial Data Check")

print("🔹 Step 2: First 5 rows")
print(df.head(), "\n")

print("🔹 Shape (Rows, Columns):")
print(df.shape, "\n")

print("🔹 Column Names:")
print(df.columns.tolist(), "\n")

print("🔹 Data Info:")
print(df.info(), "\n")

print("----------------------------------------------------------------------------")
print("🔹 Clean Column Names")
print("🔹 Step 3: Cleaning column names...")

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Standard column names
df.columns = df.columns.str.replace('quiztype', 'quiz_type')
df.columns = df.columns.str.replace('quizid', 'quiz_id')
df.columns = df.columns.str.replace('secperquestion', 'sec_per_question')
df.columns = df.columns.str.replace('creatorname', 'creator_name')
df.columns = df.columns.str.replace('creatorid', 'creator_id')
df.columns = df.columns.str.replace('resultsusers', 'results_users')
df.columns = df.columns.str.replace('winnername', 'winner_name')
df.columns = df.columns.str.replace('winnerscore', 'winner_score')
df.columns = df.columns.str.replace('winnertime', 'winner_time')
df.columns = df.columns.str.replace('winnerfinalscore', 'winner_final_score')
df.columns = df.columns.str.replace('createdat', 'create_date')
df.columns = df.columns.str.replace('startedat', 'start_date')
df.columns = df.columns.str.replace('completedat', 'complete_date')
df.columns = df.columns.str.replace('livequizlabel', 'livequiz_label')
df.columns = df.columns.str.replace('livequizsubject', 'livequiz_subject')
df.columns = df.columns.str.replace('livequiztopic', 'livequiz_topic')
df.columns = df.columns.str.replace('livequizdifficulty', 'livequiz_difficulty')
df.columns = df.columns.str.replace('livequizslot', 'livequiz_slot')

print("✅ Cleaned Column Names:")
print(df.columns.tolist(), "\n")

print("----------------------------------------------------------------------------")
print("🔹 Duplicate Removal")
print("🔹 Step 4: Checking duplicates...")
print("Duplicate rows:", df.duplicated().sum())

df = df.drop_duplicates()
print("✅ Duplicates removed\n")

print("----------------------------------------------------------------------------")
print("🔹 Missing Values Check (BEFORE)")
print("🔹 Step 5: Missing values before cleaning")
print(df.isnull().sum(), "\n")

print("----------------------------------------------------------------------------")
print("🔹 Winner Columns Handling")
print("🔹 Step 6: Filling winner related columns...")

winner_cols = ['winner_name', 'winner_score', 'winner_time', 'winner_final_score']

for col in winner_cols:
    if col in df.columns:
        df[col] = df[col].fillna('Not Declared')

print("✅ Winner columns cleaned\n")

print("----------------------------------------------------------------------------")
print("🔹 Live Quiz Columns Handling")
print("🔹 Step 7: Filling live quiz columns...")

live_quiz_cols = [
    'livequiz_label',
    'livequiz_subject',
    'livequiz_topic',
    'livequiz_difficulty',
    'livequiz_slot'
]

for col in live_quiz_cols:
    if col in df.columns:
        df[col] = df[col].fillna('Not Live')

print("✅ Live quiz columns cleaned\n")

print("----------------------------------------------------------------------------")
print("🔹 Date Columns Handling")
print("🔹 Step 8: Converting date columns...")

date_cols = ['create_date', 'start_date', 'complete_date']

for col in date_cols:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')

print("✅ Date columns converted\n")

print("----------------------------------------------------------------------------")
print("🔹 Quiz Status Column")
print("🔹 Step 9: Creating quiz_status column...")

df['quiz_status'] = 'Completed'

if 'start_date' in df.columns:
    df.loc[df['start_date'].isna(), 'quiz_status'] = 'Not Started'

if 'complete_date' in df.columns:
    df.loc[df['complete_date'].isna(), 'quiz_status'] = 'In Progress'

print("✅ quiz_status column created")
print(df['quiz_status'].value_counts(), "\n")

print("----------------------------------------------------------------------------")
print("🔹 Extra Dashboard Columns")
print("🔹 Step 10: Creating year & month columns...")

if 'create_date' in df.columns:
    df['created_year'] = df['create_date'].dt.year
    df['created_month'] = df['create_date'].dt.month_name()

print("✅ Year & Month columns added\n")

print("----------------------------------------------------------------------------")
print("🔹 Step 11A: Fixing data types for analysis")

if 'winner_score' in df.columns:
    df['winner_score'] = pd.to_numeric(df['winner_score'], errors='coerce')

if 'participants' in df.columns:
    df['participants'] = pd.to_numeric(df['participants'], errors='coerce')

if 'results_users' in df.columns:
    df['results_users'] = pd.to_numeric(df['results_users'], errors='coerce')

print("✅ Numeric columns fixed\n")

print("----------------------------------------------------------------------------")
print("🔹 Step 11B: Logical data validation")

if 'results_users' in df.columns and 'participants' in df.columns:
    invalid_rows = df[df['results_users'] > df['participants']].shape[0]
    print(f"Invalid rows found (results_users > participants): {invalid_rows}")
    df = df[df['results_users'] <= df['participants']]

print("✅ Logical validation applied\n")

print("----------------------------------------------------------------------------")
print("🔹 Step 11C: Text standardization")

text_cols = ['status', 'mode', 'language', 'school']

for col in text_cols:
    if col in df.columns:
        df[col] = df[col].astype(str).str.lower().str.strip()

print("✅ Text columns standardized\n")

print("----------------------------------------------------------------------------")
print("🔹 Missing Values Check (AFTER)")
print("🔹 Step 12: Missing values after cleaning")
print(df.isnull().sum(), "\n")

print("----------------------------------------------------------------------------")
print("🔹 Final Dataset Preview")
print("🔹 Step 13: Final cleaned data preview")
print(df.head(), "\n")

print("----------------------------------------------------------------------------")
print("🔹 Fixing timezone issue in date columns...")

for col in date_cols:
    if col in df.columns and pd.api.types.is_datetime64_any_dtype(df[col]):
        df[col] = df[col].dt.tz_localize(None)

print("✅ Timezone removed from date columns\n")

print("----------------------------------------------------------------------------")
print("🔹 Saving clean data to CSV...")

output_path = r"D:\Data Analyst\Skill Foundation Project\Final_Clean_Quiz_Data.csv"
df.to_csv(output_path, index=False)

print("✅ Final_Clean_Quiz_Data.csv saved successfully at:")
print(output_path)
