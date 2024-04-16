import json
import sys

def fill_values(tests, values):
    for test in tests:
        test_id = test["id"]
        for value in values["values"]:
            if value["id"] == test_id:
                test["value"] = value["value"]
                break
        if "values" in test:
            fill_values(test["values"], values)

def generate_report(values_file_path, tests_file_path, report_file_path):
    with open(values_file_path, "r") as values_file:
        values = json.load(values_file)
    
    with open(tests_file_path, "r") as tests_file:
        tests = json.load(tests_file)
    
    fill_values(tests["tests"], values)
    
    with open(report_file_path, "w") as report_file:
        json.dump(tests, report_file, indent=2)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("How to use: python3 task3.py <values.json> <tests.json> <report.json>")
        sys.exit(1)

    tests_file_path = sys.argv[1]
    values_file_path = sys.argv[2]
    report_file_path = sys.argv[3]

    generate_report(tests_file_path, values_file_path, report_file_path)