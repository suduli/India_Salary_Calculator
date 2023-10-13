import os

# Constants
BASIC_MULTIPLIER = 2
PF_MULTIPLIER = 12 / 100
HRA_MULTIPLIER = 40 / 100
GRATUITY_MULTIPLIER = 4.81 / 100

def calculate_annual_salary_based_on_basic(monthly_basic):
    return monthly_basic * 12 * BASIC_MULTIPLIER

def calculate_annual_salary_based_on_pf(monthly_pf):
    annual_basic = monthly_pf / PF_MULTIPLIER
    return annual_basic * BASIC_MULTIPLIER

def calculate_annual_salary_based_on_hra(monthly_hra):
    annual_basic = monthly_hra / HRA_MULTIPLIER
    return annual_basic * BASIC_MULTIPLIER

def calculate_annual_salary_based_on_gratuity(monthly_gratuity):
    annual_basic = monthly_gratuity / GRATUITY_MULTIPLIER
    return annual_basic * BASIC_MULTIPLIER

def main():
    # User Input
    user_data = input("Choose component:\n1.Basic\n2.PF\n3.HRA\n4.Gratuity\nEnter your Option: ")
    user_input_data_type = input("1.Monthly\n2.Annually\nEnter your Option: ")

    if user_input_data_type == "1":
        data = float(input("Enter Monthly Amount: ")) * 12
    elif user_input_data_type == "2":
        data = float(input("Enter Annually Amount: "))
    else:
        print("Please Enter Valid Input!!!")
        return

    # Calculate CTC based on user input
    if user_data == "1":
        ctc = calculate_annual_salary_based_on_basic(data)
    elif user_data == "2":
        ctc = calculate_annual_salary_based_on_pf(data)
    elif user_data == "3":
        ctc = calculate_annual_salary_based_on_hra(data)
    elif user_data == "4":
        ctc = calculate_annual_salary_based_on_gratuity(data)
    else:
        print("Please Enter Valid Input!!!")
        return

    print(f"Current salary is: {ctc}")

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
