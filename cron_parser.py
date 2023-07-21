import sys

FIELDS = ["minute", "hour", "day of month", "month", "day of week"]

def parse_cron(cron_string):
    fields_and_command = cron_string.split(None, maxsplit=5)

    if len(fields_and_command) != 6:
        print("Error: Invalid cron string. Please provide a valid cron expression.")
        sys.exit(1)

    fields = fields_and_command[:5]
    command = fields_and_command[-1]

    expanded_fields = []

    def expand_field(field, min_val, max_val):
        if field == "*":
            return list(range(min_val, max_val + 1))
        values = []
        parts = field.split(",")
        for part in parts:
            if "-" in part:
                start, end = map(int, part.split("-"))
                values.extend(list(range(start, end + 1)))
            elif "/" in part:
                step = int(part.split("/")[1])
                values.extend(list(range(min_val, max_val + 1, step)))
            else:
                values.append(int(part))
        return sorted(set(values))

    range_limits = {
        0: (0,59),
        1: (0,23),
        2: (1, 31),
        3: (1, 12),
        4: (0, 7)
    }
    for i, field in enumerate(fields):
        min_val, max_val = range_limits.get(i)
        expanded_fields.append(expand_field(field, min_val, max_val))

    return expanded_fields, command

def print_schedule(expanded_fields, command):
    for field_name, field_values in zip(FIELDS, expanded_fields):
        print("{:<14}{}".format(field_name, " ".join(map(str, field_values))))
    print("{:<14}{}".format("command", command))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    cron_string = sys.argv[1]
    expanded_fields, command = parse_cron(cron_string)
    print_schedule(expanded_fields, command)
