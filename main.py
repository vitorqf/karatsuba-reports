import time
from tabulate import tabulate
import csv

def solve_by_brute_force(x, y):
    return x * y

def solve_by_karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    
    x_high, x_low = divmod(x, 10 ** m)
    y_high, y_low = divmod(y, 10 ** m)
    
    z0 = solve_by_karatsuba(x_high, y_high)
    z1 = solve_by_karatsuba(x_low, y_low)
    z2 = solve_by_karatsuba(x_high + x_low, y_high + y_low)
    
    return z0 * 10 ** (2 * m) + (z2 - z0 - z1) * 10 ** m + z1

def run_test(test_case, x, y):
    start_time = time.time()
    result = test_case(x, y)
    end_time = time.time()
    elapsed_time = end_time - start_time
    test_name = test_case.__name__
    
    return [test_name, f"{len(str(x))}, {len(str(y))}", f"{elapsed_time:.10f} seconds", result]

# Collect results
results = []

# First test battery
results.append(run_test(solve_by_karatsuba, 1234, 5678))
results.append(run_test(solve_by_karatsuba, 11111111, 22222222))
results.append(run_test(solve_by_karatsuba, 12345678, 87654321))

# Second test battery
results.append(run_test(solve_by_karatsuba, 123, 456789))
results.append(run_test(solve_by_karatsuba, 12345, 678))
results.append(run_test(solve_by_karatsuba, 123456, 78901234))

# Third test battery
results.append(run_test(solve_by_karatsuba, 1234567890,1987654321))
results.append(run_test(solve_by_brute_force, 1234567890, 1987654321))

results.append(run_test(solve_by_karatsuba, 71920384891650729830476295813467091238475902387461, 48293017659487236091578302476198345092813467501928))
results.append(run_test(solve_by_brute_force, 71920384891650729830476295813467091238475902387461, 48293017659487236091578302476198345092813467501928))

results.append(run_test(solve_by_karatsuba, 8472036192850347192837465028371984501982374650192384702193845760563291847039812456708431975208139427565, 1029384756019273845610928374650192837465029384756102938475601927384561092837465019283746501928374650192))
results.append(run_test(solve_by_brute_force, 8472036192850347192837465028371984501982374650192384702193845760563291847039812456708431975208139427565, 1029384756019273845610928374650192837465029384756102938475601927384561092837465019283746501928374650192))

# Display results in a single table
table = tabulate(results, headers=["Test Name", "Total Digits (x,y)", "Elapsed Time", "Result"], tablefmt="fancy_grid", colalign=("left", "center", "center", "left"))

# Write the table to a text file
with open("results_table.txt", "w") as text_file:
    text_file.write(table)

# Prompt user for export to CSV
export_to_csv = input("Should export to CSV? (y/n): ").lower()
if export_to_csv == 'y':
    # Write the table to a CSV file
    with open("results_table.csv", "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Test Name", "Total Digits (x,y)", "Elapsed Time", "Result"])
        csv_writer.writerows(results)