"""
Write a function taking in a string like WOW this is REALLY
 amazing and returning Wow this is really amazing. 
 String should be capitalized and properly spaced.
  Using re and string is not allowed.
"""


def filter_words(st):
    
    st = ' '.join(st.split())
    st = list(st.lower())
    first_up  = st[0].upper()
    st.pop(0)
    st =  "".join(list(first_up)+st)
    
    return(st)
    
print(filter_words("this   will   no    Pass")) 

