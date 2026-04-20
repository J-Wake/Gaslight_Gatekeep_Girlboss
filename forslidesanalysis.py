import pandas as pd
import plotly.express as px

bigone = pd.read_csv('./data/clean/finaltables.csv')
percs = pd.read_csv('./data/clean/participation.csv')
biggerone = pd.merge(bigone,percs, left_on=['recipient_state_name','action_date_fiscal_year'],right_on=['STATE','YEAR'], how='inner')
biggerone = biggerone.drop(columns=['YEAR'])
#print(bigone)

ogsheet2023 = biggerone[biggerone['action_date_fiscal_year'] == 2023]
ogsheet2024 = biggerone[biggerone['action_date_fiscal_year'] == 2024]
ogsheet2025 = biggerone[biggerone['action_date_fiscal_year'] == 2025]

state_to_code = {
    'ALABAMA': 'AL', 'ALASKA': 'AK', 'ARIZONA': 'AZ', 'ARKANSAS': 'AR', 'CALIFORNIA': 'CA',
    'COLORADO': 'CO', 'CONNECTICUT': 'CT', 'DELAWARE': 'DE', 'DISTRICT OF COLUMBIA': 'DC',
    'FLORIDA': 'FL', 'GEORGIA': 'GA', 'HAWAII': 'HI', 'IDAHO': 'ID', 'ILLINOIS': 'IL',
    'INDIANA': 'IN', 'IOWA': 'IA', 'KANSAS': 'KS', 'KENTUCKY': 'KY', 'LOUISIANA': 'LA',
    'MAINE': 'ME', 'MARYLAND': 'MD', 'MASSACHUSETTS': 'MA', 'MICHIGAN': 'MI', 'MINNESOTA': 'MN',
    'MISSISSIPPI': 'MS', 'MISSOURI': 'MO', 'MONTANA': 'MT', 'NEBRASKA': 'NE', 'NEVADA': 'NV',
    'NEW HAMPSHIRE': 'NH', 'NEW JERSEY': 'NJ', 'NEW MEXICO': 'NM', 'NEW YORK': 'NY',
    'NORTH CAROLINA': 'NC', 'NORTH DAKOTA': 'ND', 'OHIO': 'OH', 'OKLAHOMA': 'OK',
    'OREGON': 'OR', 'PENNSYLVANIA': 'PA', 'RHODE ISLAND': 'RI', 'SOUTH CAROLINA': 'SC',
    'SOUTH DAKOTA': 'SD', 'TENNESSEE': 'TN', 'TEXAS': 'TX', 'UTAH': 'UT', 'VERMONT': 'VT',
    'VIRGINIA': 'VA', 'WASHINGTON': 'WA', 'WEST VIRGINIA': 'WV', 'WISCONSIN': 'WI', 'WYOMING': 'WY'
}


flor = [ogsheet2023,ogsheet2024,ogsheet2025]
def fixit(f):
    f = f.dropna()
    f = f.drop(columns=['recipient_state_name'])
    f['state_code'] = f['STATE'].map(state_to_code)
    f['effectivness_act$1000'] = ((f['ACT_Score'] * (f['PARTICIPATION PERCENTAGE FOR ACT'] / 100 )) / f['money_per_student_per_state']) * 1000
    f['effectivness_sat$1000'] = ((f['SAT_Score'] * (f['PARTICIPATION AVERAGE FOR SAT'] / 100 )) / f['money_per_student_per_state'])* 1000
    return f

newsheet2023=fixit(ogsheet2023)
newsheet2024 = fixit(ogsheet2024)
newsheet2025 = fixit(ogsheet2025)

flor = [newsheet2023,newsheet2024,newsheet2025]
for b in flor:
    sheet_act = b.sort_values(by='effectivness_act$1000', ascending=False)
    sheet_sat = b.sort_values(by='effectivness_sat$1000', ascending=False)
    b['rank_act'] = b['effectivness_act$1000'].rank(ascending=False)
    b['rank_sat'] = b['effectivness_sat$1000'].rank(ascending=False)
    b['rank_diff'] = abs(b['rank_act'] - b['rank_sat'])
    b['master_rank'] = (b['rank_act'] + b['rank_sat']) / 2
    g = b[['STATE','action_date_fiscal_year','rank_act','rank_sat','rank_diff','master_rank']]
    best_overall = g.sort_values('master_rank', ascending=False)
    print(best_overall[['STATE','action_date_fiscal_year', 'master_rank', 'rank_act', 'rank_sat']].head(10))



fig_SAT = px.scatter(newsheet2023, 
                 x='money_per_student_per_state', 
                 y='total_obligated_amount',  # Use the exact column name for your SAT scores
                 text='STATE',    # This labels the'pi dots with state names
                 title='Dept. of Edu. Funds vs. money Per Student 2023',
                 
                 trendline="ols",
                 color_discrete_sequence=['hotpink'])

graph = fig_SAT.write_html('state_scores.html')

fig_fedspend = px.choropleth(newsheet2023,
                    locations='state_code', 
                    locationmode="USA-states",
                    color='total_obligated_amount',
                    scope="usa",
                    color_continuous_scale="RdPu",title='Federal Spending 2025')
fig_fedspend.write_html('fedspend.html')
