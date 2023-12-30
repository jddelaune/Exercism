def leap_year(year):
    div_by_four = year % 4 == 0
    not_div_by_hundred = year % 100 != 0
    div_by_four_hundred = year % 400 == 0

    return div_by_four and (not_div_by_hundred or div_by_four_hundred) 
        
