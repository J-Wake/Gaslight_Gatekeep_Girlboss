import pandas as pd
import plotly.express as px

bigone = pd.read_csv('./data/clean/finaltables.csv')
#print(bigone)

ogsheet2023 = bigone[bigone['action_date_fiscal_year'] == 2023]
ogsheet2024 = bigone[bigone['action_date_fiscal_year'] == 2024]
ogsheet2025 = bigone[bigone['action_date_fiscal_year'] == 2025]

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

def data(sheet):
    sheet = sheet.dropna()
    sheet['state_code'] = sheet['recipient_state_name'].map(state_to_code)
    sheet_act = sheet.sort_values(by='ACT_Score', ascending=False)
    sheet_sat = sheet.sort_values(by='SAT_Score', ascending=False)
    return sheet_act,sheet_sat

actdata2023,satdata2023 = data(ogsheet2023)
actdata2024,satdata2024 = data(ogsheet2024)
actdata2025,satdata2025 = data(ogsheet2025)



fig_SAT = px.scatter(actdata2023, 
                 x='money_per_student_per_state', 
                 y='total_obligated_amount',  # Use the exact column name for your SAT scores
                 text='recipient_state_name',    # This labels the'pi dots with state names
                 title='Dept. of Edu. Funds vs. money Per Student 2023',
                 
                 trendline="ols",
                 color_discrete_sequence=['hotpink'])

graph = fig_SAT.write_html('state_scores.html')

fig_fedspend = px.choropleth(satdata2025,
                    locations='state_code', 
                    locationmode="USA-states",
                    color='total_obligated_amount',
                    scope="usa",
                    color_continuous_scale="RdPu",title='Federal Spending 2025')
fig_fedspend.write_html('fedspend.html')