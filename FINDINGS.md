# Findings Report

## Dataset Overview

- ~2000 student records
- Missing values handled for commute and study hours

## Distribution Insights

- GPA is slightly left-skewed
- Most students fall between 2.5 and 3.5 GPA
- Some departments show higher median GPA
  (See output/gpa_distribution.png)
  (See output/gpa_by_department.png)

## Correlations

- Study hours positively correlate with GPA
- Attendance also shows positive relationship with GPA
- Correlation does not imply causation
  (See output/correlation_heatmap.png)

## Hypothesis Testing

### Internship vs GPA (t-test)

- t = 13.56
- p < 0.001
- Result is statistically significant
- Students with internships have higher GPA
- Effect size (Cohen’s d ≈ 0.71) indicates a moderate to large effect

### GPA across Departments (ANOVA)

- F = 0.67
- p = 0.61
- Result is not statistically significant
- GPA does not differ significantly across departments

## Recommendations

1. Encourage internships, as students with internships have significantly higher GPAs (t-test results).

2. Promote study habit programs, since study hours show a positive correlation with GPA.

3. Improve attendance monitoring, as higher attendance is associated with better academic performance.
