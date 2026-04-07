# Findings Report

## Dataset Overview

- The dataset contains ~2000 student records across multiple departments.
- Key variables include GPA, study hours, attendance, internship status, and scholarship type.
- Missing values were present in:
  - `commute_minutes` (~10%) → filled with median
  - `study_hours_weekly` (~5%) → rows removed
- Overall data quality is good after preprocessing.

---

## Distribution Insights

- GPA distribution is slightly left-skewed, with most students between 2.5 and 3.5.  
  (See output/gpa_distribution.png)

- Study hours show moderate spread, with some high-study outliers.  
  (See output/study_hours_distribution.png)

- Attendance is generally high, with most students above 70%.  
  (See output/attendance_distribution.png)

- GPA across departments appears similar, with no major differences in median values.  
  (See output/gpa_by_department.png and output/gpa_violin.png)

---

## Correlation Analysis

- Study hours and GPA show a moderate positive correlation.
- Attendance also positively correlates with GPA.
- These relationships suggest that effort and engagement contribute to academic success.

(See output/correlation_heatmap.png, output/study_vs_gpa.png)

> Note: Correlation does not imply causation.

---

## Hypothesis Testing

### 1. Internship vs GPA (t-test)

- t-statistic: **13.56**
- p-value: **3.68e-40**
- Result: Statistically significant (p < 0.05)

**Interpretation:**
Students with internships have significantly higher GPAs than those without.  
The effect size (Cohen’s d ≈ 0.71) indicates a moderate to large practical impact.

---

### 2. GPA Across Departments (ANOVA)

- F-statistic: **0.67**
- p-value: **0.61**
- Result: Not statistically significant

**Interpretation:**
There is no significant difference in GPA across departments.

---

### 3. Post-hoc Analysis (Bonferroni)

- All pairwise comparisons between departments were not significant.

**Interpretation:**
This confirms that academic performance is consistent across departments.

---

## Advanced Statistical Validation (Tier 3)

- **Bootstrap Confidence Intervals:**
  - Internship GPA: ~2.95 to 3.01
  - No Internship GPA: ~2.68 to 2.72  
    → Minimal overlap confirms strong group differences.

- **Power Analysis:**
  - Required sample size ≈ 32 per group  
    → Dataset size is more than sufficient, increasing confidence in results.

- **Simulation:**
  - False positive rate ≈ 0.049  
    → Confirms statistical tests behave as expected.

---

## Recommendations

1. **Encourage internships**
   - Strong statistical evidence shows internships are associated with higher GPA.

2. **Promote structured study programs**
   - Positive correlation between study hours and GPA suggests academic support programs could improve performance.

3. **Improve attendance monitoring**
   - Attendance is positively linked to GPA, so reinforcing attendance policies may boost outcomes.

---

## Key Takeaway

Internships are the strongest predictor of higher academic performance, supported by multiple statistical methods and validation techniques.
