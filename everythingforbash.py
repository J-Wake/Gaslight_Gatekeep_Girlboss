import pandas as pd


df2023 = pd.read_csv('All_Assistance_PrimeTransactions_2023.csv')
df2024 = pd.read_csv('assistance_prime_transaction_2024.csv')
df2025 = pd.read_csv('assistprime2026.csv')
state_spending = pd.read_csv('per-pupil-spending-by-state-2023-26.csv')
actdf = pd.read_csv('AVG_ACT_STAGE.csv')
satdf= pd.read_csv('avg_sat_state.csv')

usa_spending_csvs = [df2023,df2024,df2025]
for df in usa_spending_csvs:
    
