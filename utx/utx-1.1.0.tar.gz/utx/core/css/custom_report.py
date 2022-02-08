#!/usr/bin/python
# encoding=utf-8

"""
@Author  :  Lijiawei
@Date    :  9/14/2021 4:36 PM
@Desc    :  Custom Report line.
"""
import io
import os
import time

import jinja2

CUSTOM_HTML_TPL = "summary_template_v2.html"
CUSTOM_STATIC_DIR = os.path.dirname(__file__)


def gen_report(results, report_path):
    """
    gen_report
    :param results: results list
    :param report_path: report_path
    :return: custom report html
    """
    format_list = []
    for i in results:
        if i not in format_list:
            format_list.append(i)

    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(CUSTOM_STATIC_DIR),
        extensions=(),
        autoescape=True
    )
    template = env.get_template(CUSTOM_HTML_TPL, CUSTOM_STATIC_DIR)
    html = template.render({"results": format_list})
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    output_file = os.path.join(report_path, now + '_' + "utx_summary.html")
    with io.open(output_file, 'w', encoding="utf-8") as f:
        f.write(html)
    print(output_file)
