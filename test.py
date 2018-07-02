import utils, sys

projects = [(2, "Timesheets"), (12312, "Wirtualna Mennica"), (5234234, "CBInsights")]

parsed_csv = utils.read_csv_as_array("czerwiec.txt", 0, "	")
filtered_csv = []
total_duration_hours = 0

def reformat_date(date):
    date = date.split("/")
    reformatted_date = "{}-{}-{}".format(date[2],
                                         date[1],
                                         date[0])
    return reformatted_date

for row in parsed_csv:
    if (len(row) > 1) and (len(row) < len(projects) * 2):
        raise ValueError("Line {} is invalid!".format(1 + parsed_csv.index(row)))

    if len(row) <= 1:
        continue
    elif len(row) == len(projects) * 2:  # if last project has empty description
        row.append("")

    filtered_csv.append(row)

result_report = []

for row in filtered_csv:
    date = row[0]

    for project in projects:
        index = projects.index(project) * 2 + 1

        duration_hours = row[index]
        if duration_hours == "":
            duration_hours = 0
            continue
        else:
            duration_hours = float(duration_hours)

        description = row[index + 1]
        if description == "":
            description = "No description"

        if duration_hours == 0:
            continue

        total_duration_hours += duration_hours

        task = dict(projectId=project[0],
                    projectName=project[1],
                    date=date,
                    duration=duration_hours,
                    description=description)
        result_report.append(task)

        if "wiesiek" in sys.argv:
            to_print = "{0}\tWykonanie testów: {1}\t{2}".format(date,
                                                                task['projectName'],
                                                                task["duration"])
            print(to_print)

utils.save_json_to_file(result_report, "czerwiec_report.json")

print("Total duration [hours]: %d" % total_duration_hours)