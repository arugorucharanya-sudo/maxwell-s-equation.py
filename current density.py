 Maxwell's Law Calculation
 Calculation of displacement current density

 Permittivity of free space
epsilon_0 = 8.854e-12

 Input values
dE_dt = float(input("Enter rate of change of electric field (V/m/s): "))

 Calculate displacement current density
Jd = epsilon_0 * dE_dt

 Display result
print("\n--- Maxwell's Law Calculation ---")
print("Rate of change of electric field =", dE_dt, "V/m/s")
print("Displacement Current Density =", Jd, "A/m^2")
