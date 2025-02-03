# FINE 3300 - Assignment #1
# Mortgage Payment Calculator

def mortgage_payments(principal, rate, amortization):
    """
    Function to calculate mortgage payments for different payment frequencies.    
    """

    # Calculate periodic interest rates for different payment frequencies
    r_monthly = (1 + rate / 200) ** (2/12) - 1          
    r_semi_monthly = (1 + rate / 200) ** (2/24) - 1    
    r_bi_weekly = (1 + rate / 200) ** (2/26) - 1      
    r_weekly = (1 + rate / 200) ** (2/52) - 1          

    # Number of total payments over the amortization period
    n_monthly = amortization * 12      
    n_semi_monthly = amortization * 24 
    n_bi_weekly = amortization * 26    
    n_weekly = amortization * 52       

    # Function to calculate the annuity payment using the present value formula
    def pmt(r, n):
        """
        Compute periodic mortgage payments using the present value of annuity formula.        
        """
        return principal * r / (1 - (1 + r) ** -n)

    # Calculate payments for different frequencies
    monthly = pmt(r_monthly, n_monthly)                
    semi_monthly = pmt(r_semi_monthly, n_semi_monthly)  
    bi_weekly = pmt(r_bi_weekly, n_bi_weekly)         
    weekly = pmt(r_weekly, n_weekly)                   

    # Accelerated payment calculations:
    rapid_bi_weekly = monthly / 2 
    rapid_weekly = monthly / 4    

    # Return rounded payment values as a tuple
    return round(monthly, 2), round(semi_monthly, 2), round(bi_weekly, 2), round(weekly, 2), round(rapid_bi_weekly, 2), round(rapid_weekly, 2)


# Prompt the user to enter mortgage details
principal = float(input("Enter the mortgage principal ($): "))  # Loan amount
rate = float(input("Enter the quoted interest rate (%): "))     # Annual interest rate
amortization = int(input("Enter the amortization period (years): "))  # Loan duration in years

monthly, semi_monthly, bi_weekly, weekly, rapid_bi_weekly, rapid_weekly = mortgage_payments(principal, rate, amortization)

print("\nMortgage Payment Schedule:")
print(f"Monthly Payment: ${monthly}")
print(f"Semi-monthly Payment: ${semi_monthly}")
print(f"Bi-weekly Payment: ${bi_weekly}")
print(f"Weekly Payment: ${weekly}")
print(f"Rapid Bi-weekly Payment: ${rapid_bi_weekly}")
print(f"Rapid Weekly Payment: ${rapid_weekly}")
