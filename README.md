# Annual Salary Calculator

This script calculates the annual salary (CTC - Cost to Company) based on different components of the salary structure. The user can choose a specific component (Basic, PF, HRA, Gratuity) and provide the monthly or annual amount for that component. The script then calculates the annual salary based on the chosen component and displays the result.

## Features

- Calculate annual salary based on various components: Basic, PF, HRA, Gratuity.
- User-friendly prompts guide the user through the process.
- Error handling for invalid inputs.

## How to Use

1. Navigate to the directory containing the script.
2. Run the script using Python:
   ```
   python script_name.py
   ```
3. Follow the on-screen prompts to choose a salary component and specify the amount (either monthly or annually).
4. The script will display the calculated annual salary based on the provided input.

## Code Structure

- **Constants**: Defined constants for fixed values used in calculations.
- **Function Definitions**:
   - `calculate_annual_salary_based_on_basic`: Calculates annual salary based on the basic component.
   - `calculate_annual_salary_based_on_pf`: Calculates annual salary based on the Provident Fund (PF) component.
   - `calculate_annual_salary_based_on_hra`: Calculates annual salary based on the House Rent Allowance (HRA) component.
   - `calculate_annual_salary_based_on_gratuity`: Calculates annual salary based on the Gratuity component.
- **Main Function**: Orchestrates the entire process, from taking user input to displaying the result.

## Notes

- The script uses predefined multipliers for each component to calculate the annual salary.
- The calculations assume that the provided amount for each component is either monthly (which is then annualized) or already annual.

---

You can save the above content in a file named `README.md` and place it alongside the script for documentation purposes.
