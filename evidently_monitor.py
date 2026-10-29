import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset

reference_data = pd.DataFrame({
    "feature": [10, 12, 11, 13, 12, 14, 11, 10, 13, 12]
})

current_data = pd.DataFrame({
    "feature": [20, 22, 21, 23, 22, 24, 21, 20, 23, 22]
})

report = Report(metrics=[DataDriftPreset()])

result = report.run(
    reference_data=reference_data,
    current_data=current_data
)

result.save_html("evidently_report.html")

print("Evidently monitoring report generated successfully.")