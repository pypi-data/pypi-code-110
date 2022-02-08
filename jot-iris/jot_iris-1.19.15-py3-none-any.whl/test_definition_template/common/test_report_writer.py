"""
Handles the creation of the result files and directories
"""

import datetime
import pathlib
import json2html


def create_report(
    report_json,
    report_dict,
    test_positions,
    parameters,
    local_db,
    common_definitions,
    progress_reporter,
):
    """Creates and stores report for DUT(s)"""

    if common_definitions.OPERATOR_INTRODUCTIONS:
        progress_reporter.show_operator_instructions("Take finished DUT away from tester.")

    # Get root level items on report
    root_items = {}

    for key, value in report_dict.items():
        if not isinstance(value, dict) or key == 'operator' or key == 'tester':
            root_items[key] = value

    # Extract each DUT and add to database
    for key, value in test_positions.items():

        dut = value.dut

        if dut is not None:
            dut_sn = dut.serial_number

            result_db = {'serialnumber': dut_sn}

            result_db['result'] = dut.pass_fail_result

            result_db['failedCases'] = dut.failed_steps

            result_db['passedCases'] = [
                case_name for case_name, case in dut.test_cases.items() if case['result']
            ]
            # The actual results
            result_db['testCases'] = report_dict[dut_sn]

            # Add also root level items
            result_db.update(root_items)
            local_db.db_client[local_db.db_name].test_reports.insert_one(result_db)

    filename = '_'.join(
        [
            '%s-%s' % (test_position_name, test_position_value.dut.serial_number)
            for (test_position_name, test_position_value) in test_positions.items()
        ]
    )

    report_path = create_report_path()

    report_file_path = report_path / (filename + '.html')

    report_file_path.write_text(json2html.json2html.convert(json=report_json))

    remove_old_reports()

def remove_old_reports(timespan=7*24*60*60):
    report_base_path = (
        pathlib.Path.cwd() / 'results'
    )

    remove_tree(report_base_path, timespan)

def remove_tree(path, timespan):
    if timespan <= 0:
        return

    path = pathlib.Path(path)
    for child in path.glob('*'):
        if child.is_file():
            time_diff = datetime.datetime.now().timestamp() - child.stat().st_mtime
            if time_diff > timespan:
                child.unlink()
        else:
            remove_tree(child, timespan)
    try:
        path.rmdir()
    except OSError:
        pass

def create_report_path():
    current = datetime.datetime.now()

    report_path = (
        pathlib.Path.cwd() / 'results' / str(current.year) / str(current.month) / str(current.day)
    )
    report_path.mkdir(parents=True, exist_ok=True)

    return report_path
