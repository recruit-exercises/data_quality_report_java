# Copyright 2022 DoorDash, Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
import sys
sys.stdout = open("test.txt", "w")
import site
import numpy as np
import pandas as pd

from dataqualityreport import DataQualityReport, DataQualityRule, DataQualityWarning, dqr_compare

SALARIES_DF = pd.read_csv("tests/ds_salaries.csv", index_col=0)

MISSING_BY_COL = "missing_by_test"
TEST_RULES = [
    DataQualityRule(0, "perc_missing > 0.95", ["perc_missing"]),
    DataQualityRule(
        0, "(num_missing_partitions > 0)", ["num_missing_partitions", "min_missing_partition", "max_missing_partition"]
    ),
    DataQualityRule(1, "(perc_distinct > 0.99) & (perc_distinct < 1)", ["perc_distinct"]),
    DataQualityRule(1, "(perc_negative > 0) & (perc_negative < 0.05)", ["perc_negative", "num_negative", "min"]),
    DataQualityRule(2, "(perc_zeros > 0.5)", ["perc_zeros"]),
    DataQualityRule(2, "dtype == 'object'", ["dtype"]),
    DataQualityRule(2, "(perc_missing > 0.5) & (perc_missing <= 0.95)", ["perc_missing"]),
    DataQualityRule(3, "(num_low_10x_IQR_outliers > 0)", ["num_low_10x_IQR_outliers", "p05", "min"]),
    DataQualityRule(3, "(num_high_10x_IQR_outliers > 0)", ["num_high_10x_IQR_outliers", "p95", "max"]),
    DataQualityRule(3, "(perc_missing > 0) & (perc_missing <= 0.5)", ["perc_missing"]),
]

NUM_FIELDS = len(SALARIES_DF.columns)
NUM_WARNINGS = 1
NUM_WARNINGS_GTE_2 = 0
NUM_FIELDS_WITH_WARNINGS = 1
NUM_NON_OBJECT_FIELDS = len([ty for ty in SALARIES_DF.dtypes if str(ty) != "object"])

myDataQualityReport = data_quality_report = DataQualityReport(SALARIES_DF, missing_by=MISSING_BY_COL, rules=TEST_RULES, n_jobs=1)

print(myDataQualityReport) # prints warnings summary and detail
myDataQualityReport.warnings_report_str() # ^ same as above
myDataQualityReport.display_table().render() # renders HTML table in notebooks
sourceFile = open('demo.html', 'w')
print(myDataQualityReport.display_table().render(), file = sourceFile)
sourceFile.close()
sys.stdout.close()

