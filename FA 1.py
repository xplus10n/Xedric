{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "57dac9d2-07b4-41a0-90cc-3731a03eb06a",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''Programming Set 1\n",
    "\n",
    "This assignment will familiarize you with Python's basics.\n",
    "'''\n",
    "\n",
    "def savings(gross_pay, tax_rate, expenses):\n",
    "    '''Savings.\n",
    "\n",
    "    This function calculates the money remaining\n",
    "        for an employee after taxes and expenses.\n",
    "\n",
    "    To get the take-home pay of an employee, we will\n",
    "        follow the following process:\n",
    "        1. Apply the tax rate to the gross pay of the employee; round down\n",
    "        2. Subtract the expenses from the after-tax pay of the employee\n",
    "\n",
    "    Parameters\n",
    "    ----------\n",
    "    gross_pay: int\n",
    "        the gross pay of an employee for a certain time period, expressed in centavos\n",
    "    tax_rate: float\n",
    "        the tax rate for a certain time period, expressed as a number between 0 and 1 (e.g., 0.12)\n",
    "    expenses: int\n",
    "        the expenses of an employee for a certain time period, expressed in centavos\n",
    "\n",
    "    Returns\n",
    "    -------\n",
    "    int\n",
    "        the number of centavos remaining from an employee's pay after taxes and expenses\n",
    "    '''\n",
    "    # Replace `pass` with your code.\n",
    "    # Stay within the function. Only use the parameters as input. The function should return your answer.\n",
    "    \n",
    "    return int(int(gross_pay)*float(1-tax_rate))-(int(expenses))\n",
    "    \n",
    "def material_waste(total_material, material_units, num_jobs, job_consumption):\n",
    "    '''Material Waste.\n",
    "\n",
    "    This function calculates how much material input will be wasted\n",
    "        after running a certain number of jobs that consume\n",
    "        a set amount of material.\n",
    "\n",
    "    To get the waste of a set of jobs:\n",
    "        1. Multiply the number of jobs by the material consumption per job.\n",
    "        2. Subtract the total material consumed from the total material available.\n",
    "\n",
    "    The users of this function also want you to format the output as a string, annotated with the\n",
    "        units in which the material is expressed. Do not add a space between the number and the unit.\n",
    "\n",
    "    Parameters\n",
    "    ----------\n",
    "    total_material: int\n",
    "        the total material available\n",
    "    material_units: str\n",
    "        the units used to express a quantity of the material (e.g., \"kg\", \"L\", etc.)\n",
    "    num_jobs: int\n",
    "        the number of jobs to run\n",
    "    job_consumption: int\n",
    "        the amount of material consumed per job\n",
    "\n",
    "    Returns\n",
    "    -------\n",
    "    str\n",
    "        the amount of remaining material expressed with its unit (e.g., \"10kg\").\n",
    "    '''\n",
    "    # Replace `pass` with your code.\n",
    "    # Stay within the function. Only use the parameters as input. The function should return your answer.\n",
    "\n",
    "    return str(int(total_material)-(int(num_jobs)*int(job_consumption)))+str(material_units)\n",
    "\n",
    "def interest(principal, rate, periods):\n",
    "    '''Interest.\n",
    "\n",
    "    This function calculates the final value of an investment after\n",
    "        gaining simple interest over a number of periods.\n",
    "\n",
    "    To calculate simple interest, simply multiply the principal to the quantity (rate * time).\n",
    "        Add this amount to the principal to get the final value.\n",
    "\n",
    "    Round down the final amount.\n",
    "\n",
    "    Parameters\n",
    "    ----------\n",
    "    principal: int\n",
    "        the principal (i.e., starting) amount invested, expressed in centavos\n",
    "    rate: float\n",
    "        the interest rate per period, expressed as a decimal representation of a percentage (e.g., 3% is 0.03)\n",
    "    periods: int\n",
    "        the number of periods invested\n",
    "\n",
    "    Returns\n",
    "    -------\n",
    "    int\n",
    "        the final value of the investment\n",
    "    '''\n",
    "    # Replace `pass` with your code.\n",
    "    # Stay within the function. Only use the parameters as input. The function should return your answer.\n",
    "\n",
    "    return int(int(principal)+(int(principal)*float(rate)*int(periods)))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "32c25dec-0f34-4fb1-b969-82d75a69d311",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
