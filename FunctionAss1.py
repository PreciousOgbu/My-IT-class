# A function showing seasons, with return function


def run_season_check():


 #Defines and returns list for each season,
    autumn_months = ['Sept', 'Oct', 'Nov']

    winter_months = [ 'Dec', 'Jan', 'Feb']

    spring_months = [ 'Mar', 'Apr', 'May']

    summer_months = [ 'Jun', 'Jul', 'Aug'] 

    return autumn_months,  winter_months, spring_months, summer_months

def get_user_input():
     # Prompts the user to input the month 
    month = input('Enter the month(e.g., Jan, Feb, Mar): ').strip().capitalize()
    return month
    
def determine_season(month, autumn_months, winter_months,  spring_months,  summer_months):
        # Determine the season based on the corresponding month
    if month in autumn_months:
     return 'Autumn'
       
    elif month in winter_months:
     return 'Winter'
       
    elif month in spring_months:
      return 'Spring'
       
    elif month in summer_months:
      return 'Summer'
    
    else:
      return None
       
def print_season(season):
       #Prints season if it's valid, throws an error message if it's none
    if season:
          print(f'The season is {season}')
    else:
          print('Invalid month Input')

          

if  __name__ == "__main__":
   autumn_months, winter_months, spring_months, summer_months = run_season_check()
   month = get_user_input()
   season = determine_season (month, autumn_months, winter_months, spring_months, summer_months)
   print_season(season)