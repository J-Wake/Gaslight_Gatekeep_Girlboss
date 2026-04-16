import pandas as pd 
actdf = pd.read_csv('Avg_ACT_STATE.csv')
satdf = pd.read_csv('avg_sat_state.csv')

actandsat = pd.merge(actdf, satdf, on='State', how='outer')
print(actandsat.head(10))

# to rename col names in avg act scores 
renamed_act1 = actdf.rename(columns={'Avg Sc 2021': '2021 ACT Avg'})
renamed_act2 = renamed_act1.rename(columns={'Avg Sc 2022': '2022 ACT Avg'})
renamed_act3 = renamed_act2.rename(columns={'Avg Sc 2023': '2023 ACT Avg'})
renamed_act4 = renamed_act3.rename(columns={'Avg Sc 2024': '2024 ACT Avg'})
renamed_act = renamed_act4.rename(columns={'Avg Sc 2025': '2025 ACT Avg'})


# to rename col names in avg sat scores
renamed_sat1 = satdf.rename(columns={'2021 Mean scr': '2021 SAT Avg'})
renamed_sat2 = renamed_sat1.rename(columns={'2022 Mean scr': '2022 SAT Avg'})
renamed_sat3 = renamed_sat2.rename(columns={'2023 Mean scr': '2023 SAT Avg'})
renamed_sat4 = renamed_sat3.rename(columns={'2024 Mean scr': '2024 SAT Avg'})
renamed_sat = renamed_sat4.rename(columns={'2025 Mean scr': '2025 SAT Avg'})

print(f'the length of the orginal dataset for 2024 is 578888')
