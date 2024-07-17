# A Script showing seasons 

# Define lists for each season

autumn_months = ['Sept', 'Oct', 'Nov']

winter_months = [ 'Dec', 'Jan', 'Feb']

spring_months = [ 'Mar', 'Apr', 'May']

summer_months = [ 'Jun', 'Jul', 'Aug']

# # Get user input
month = input('Enter the month (e.g., Jan, Feb, Mar): ').strip().capitalize()

# To Determine the season based on the month

if month in autumn_months:
    season = 'Autumn'

elif month in winter_months:
    season = 'Winter'

elif month in spring_months:
    season = 'Spring'

elif month in summer_months:
    season = 'Summer'

else:
    season = 'None'

# Print the result
    
if season: 
    print(f'The season is {season}')

else: 
    print('Invalid month input')


 

# Dictionary to check Seasons

# seasons = {
#     'Sept': 'Autumn', 
#     'Oct' : 'Autumn',
#     'Nov': 'Autumn',
#     'Dec': 'Winter',
#     'Jan': 'Winter',
#     'Feb': 'Winter',
#     'March': 'Spring',
#     'April': 'Spring',
#     'May':  'Spring',
#     'June': 'Summer',
#     'July': 'Summer',
#     'August': 'Summer'
# }

# #Get User Input
# month= input('Enter the month (e.g., Jan, Feb, March): ').capitalize()

# # Check if the input is valid and print the corresponding season

# season = seasons.get(month)
# if season:
#     print(f'The season is {season}')

# else:
#     print('Invalid month input')