import pandas as pd

# ================================
# STEP 1: LOAD DATA
# ================================
print("🔹 Step 1: Loading data...")
df = pd.read_excel(r'D:\Data Analyst\Skill Foundation Project\User_data.xlsx')
print("✅ Data loaded successfully\n")

# ================================
# STEP 2: BASIC DATA CHECK
# ================================
print("----------------------------------------------------------------------------")
print("🔹 STEP 2: Basic Data Understanding")

print("First 5 rows:")
print(df.head(), "\n")

print("Shape (Rows, Columns):")
print(df.shape, "\n")

print("Column Names:")
print(df.columns.tolist(), "\n")

print("Data Info:")
print(df.info(), "\n")

# ================================
# STEP 3: CLEAN COLUMN NAMES
# ================================
print("----------------------------------------------------------------------------")
print("🔹 STEP 3: Cleaning column names into snake_case...")

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(' ', '_', regex=False)
    .str.replace('__+', '_', regex=True)
    .str.replace('[^a-z0-9_]', '', regex=True)
)

# Fix specific column names
df.columns = df.columns.str.replace('userid', 'user_id', regex=False)
df.columns = df.columns.str.replace('useremail', 'user_email', regex=False)
df.columns = df.columns.str.replace('companyid', 'company_id', regex=False)
df.columns = df.columns.str.replace('schoolid', 'school_id', regex=False)
df.columns = df.columns.str.replace('classlevel', 'class_level', regex=False)
df.columns = df.columns.str.replace('walletbalance', 'wallet_balance', regex=False)
df.columns = df.columns.str.replace('createdat', 'create_date', regex=False)
df.columns = df.columns.str.replace('updatedat', 'update_date', regex=False)
df.columns = df.columns.str.replace('username', 'user_name', regex=False)
df.columns = df.columns.str.replace('callids', 'call_ids', regex=False)
df.columns = df.columns.str.replace('calllinks', 'call_links', regex=False)
df.columns = df.columns.str.replace('biotitle', 'bio_title', regex=False)
df.columns = df.columns.str.replace('referralcode', 'referral_code', regex=False)
df.columns = df.columns.str.replace('userphone', 'user_phone', regex=False)
df.columns = df.columns.str.replace('countrycode', 'country_code', regex=False)
df.columns = df.columns.str.replace('wallettransactions', 'wallet_transactions', regex=False)
df.columns = df.columns.str.replace('currentguruid', 'current_guru_id', regex=False)
df.columns = df.columns.str.replace('screenid', 'screen_id', regex=False)
print("✅ Cleaned Column Names:")
print(df.columns.tolist())

# ================================
# STEP 4: REMOVE DUPLICATES
# ================================
print("----------------------------------------------------------------------------")
print("🔹 STEP 4: Duplicate Rows Check")

print("Duplicate rows before:", df.duplicated().sum())
df = df.drop_duplicates()
print("Duplicate rows after:", df.duplicated().sum())



# ================================
# STEP 5: MISSING VALUES CHECK
# ================================
print("----------------------------------------------------------------------------")
print("🔹 STEP 5: Missing Values (NULL) Analysis")
print(df.isnull().sum())
print("----------------------------------------------------------------------------")
print("🔹 STEP 5.5: Checking duplicate column names")

print("Duplicate column names:")
print(df.columns[df.columns.duplicated()])

# Remove duplicate columns (keep first)
df = df.loc[:, ~df.columns.duplicated()]

print("✅ Duplicate columns removed")

print("----------------------------------------------------------------------------")



# ================================
# STEP 6: HANDLE MISSING VALUES
# ================================
print("----------------------------------------------------------------------------")
print("🔹 STEP 6: Handling missing values safely...")

# 1️⃣ Numeric columns (int, float)
num_cols = df.select_dtypes(include=['int64', 'float64']).columns

for col in num_cols:
    total_rows = len(df[col])           # total rows in column
    null_count = df[col].isna().sum()   # number of missing values

    # Agar poora column NULL hai
    if null_count == total_rows:
        df[col] = df[col].fillna(0)
    else:
        # Agar kuch values NULL hain to median se fill karo
        df[col] = df[col].fillna(df[col].median())

# 2️⃣ Text / Object columns
text_cols = df.select_dtypes(include=['object']).columns

for col in text_cols:
    df[col] = df[col].fillna("Not Available")

print("✅ Missing values handled successfully")


# ================================
# STEP 7: DATE COLUMN FORMATTING
# ================================
print("----------------------------------------------------------------------------")
print("🔹 STEP 7: Converting date columns to datetime...")

date_cols = [col for col in df.columns if 'date' in col or 'created' in col or 'updated' in col]

for col in date_cols:
    df[col] = pd.to_datetime(df[col], errors='coerce')

print("✅ Date columns formatted")


# ================================
# STEP 8: CLEAN TEXT SPACES
# ================================
print("----------------------------------------------------------------------------")
print("🔹 STEP 8: Removing extra spaces from text columns...")

text_cols = df.select_dtypes(include=['object']).columns

for col in text_cols:
    df[col] = df[col].str.strip()

print("✅ Extra spaces removed")
print("----------------------------------------------------------------------------")

# ================================
# STEP 9: OUTLIER TREATMENT (IQR METHOD)
# ================================
print("----------------------------------------------------------------------------")
print("🔹 STEP 9: Handling outliers in numeric columns...")

num_cols = df.select_dtypes(include=['int64', 'float64']).columns

for col in num_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    df[col] = df[col].clip(lower_bound, upper_bound)

print("✅ Outliers handled")
print("----------------------------------------------------------------------------")

# ================================
# STEP 10: OPTIMIZE DATA TYPES
# ================================
print("----------------------------------------------------------------------------")
print("🔹 STEP 10: Optimizing data types...")

for col in num_cols:
    df[col] = pd.to_numeric(df[col], downcast='integer')

print("✅ Data types optimized")


# ================================
# STEP 11: FINAL DATA CHECK
# ================================
print("----------------------------------------------------------------------------")
print("🔹 STEP 11: Final Clean Data Summary")

print(df.info())

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("----------------------------------------------------------------------------")
print("🎉 DATA FULLY CLEANED & READY FOR ANALYSIS")

# ================================
# STEP 11.5: REMOVE TIMEZONE FROM DATETIME COLUMNS
# ================================
print("----------------------------------------------------------------------------")
print("🔹 STEP 11.5: Removing timezone info from datetime columns...")

datetime_cols = df.select_dtypes(include=['datetime64[ns, UTC]', 'datetime64[ns]']).columns

for col in datetime_cols:
    try:
        df[col] = df[col].dt.tz_localize(None)
    except:
        pass

print("✅ Timezone removed from datetime columns")

print("----------------------------------------------------------------------------")
# ================================
# STEP 12: SAVE CLEANED DATA
# ================================
print("----------------------------------------------------------------------------")
print("🔹 STEP 12: Saving cleaned data to new Excel file...")

output_path = r'D:\Data Analyst\Skill Foundation Project\User_data_CLEANED.xlsx'
df.to_excel(output_path, index=False)

print("✅ Cleaned file saved successfully at:")
print(output_path)


# ================================
# STEP 13: SAVE AS CSV (OPTIONAL)
# ================================
print("----------------------------------------------------------------------------")
print("🔹 STEP 13: Saving cleaned data as CSV for SQL / Power BI...")

csv_path = r'D:\Data Analyst\Skill Foundation Project\Final_User_data_CLEANED.csv'
df.to_csv(csv_path, index=False)

print("✅ CSV file saved successfully at:")
print(csv_path)

