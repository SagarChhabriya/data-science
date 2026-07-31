- https://www.kaggle.com/code/servetkara/diabetes-prediction-classification
- https://github.com/npradaschnor/Pima-Indians-Diabetes-Dataset/blob/master/diabetes.csv


### 1. Pregnancies: The number of times a woman has been pregnant.

Example
- A woman who has had two babies and one miscarriage has had 3 pregnancies.
- A woman who has never been pregnant has 0 pregnancies.
Can it be zero?

Yes

Zero is perfectly normal.

Notes
- Mean = 3.85
- Median = 3
- Max = 17

Some women had many pregnancies, but most had around 3–4.

### 2. Glucose: The amount of glucose (sugar) in the blood.

Usually measured after a glucose tolerance test.

Example

Healthy person:

Glucose = 95 mg/dL


Diabetic patient:

Glucose = 180 mg/dL

Can it be zero?

No

A living person cannot have 0 blood sugar.

If glucose becomes extremely low, it causes unconsciousness or death—not a recorded value of zero.

Therefore

In this dataset,

Glucose = 0


usually means

Missing value.

### 3. BloodPressure: The force of blood pushing against artery walls.

Measured in mmHg.

Example:

120/80


This dataset mainly records the diastolic pressure.

Example

Normal:

80 mmHg


High:

95 mmHg

Can it be zero?

No.

A person with 0 blood pressure is not alive (bro is in the flight to hell I mean heaven 🤣).

Therefore

BloodPressure = 0


means

Missing measurement.

### 4. SkinThickness

Thickness of the skin fold measured using calipers.

Doctors pinch the skin (usually on the upper arm) to estimate body fat.

Example

Person A

SkinThickness = 25 mm


Person B

SkinThickness = 35 mm

Can it be zero?

No.

Everyone has skin.

Zero means

Skin was not measured (missing value).

### 5. Insulin: Amount of insulin hormone in the blood.

Insulin helps move sugar from blood into body cells.

Example

Healthy:

80 µU/mL


High:

250 µU/mL

Can it be zero?

No.

Living people naturally produce some insulin (or, in diabetes treatment, receive insulin). A measured value of exactly zero in this dataset is not realistic.

Therefore

Insulin = 0


usually means

Missing value.

### 6. BMI (Body Mass Index): A measure of body weight relative to height.

Formula

BMI = Weight (kg)
      ----------
      Height² (m²)

Example
- Weight = 70 kg
- Height = 1.75 m
- BMI = 22.9

Can it be zero?

No.

A living person cannot have

BMI = 0


Therefore

Zero indicates

Missing value.

### 7. Diabetes Pedigree Function (DPF): A score representing family history (genetic risk) of diabetes.

Higher value

↓

Greater inherited risk.

Example
- Person A: DPF = 0.20 Low family history.
- Person B: DPF = 1.50 Strong family history.

Can it be zero?

Almost never.

In this dataset

Minimum is

0.078


No missing zeros here.

### 8. Age: Age of the participant. (Time spent on this GOLA 🫡)

Example
- 22 years
- 35 years
- 61 years

Can it be zero?

No.

Adults cannot have: Age = 0

Fortunately, Minimum age is: 21


### 9. Outcome: Target variable.

Whether the patient has diabetes.

Values
- 0 = No Diabetes
- 1 = Diabetes

- Columns that should NEVER be zero
Column	Can be 0?	Why?
- Pregnancies: Yes	A woman may never have been pregnant.
- Glucose: No	A living person cannot have zero blood sugar.
- BloodPressure: No	Zero blood pressure is incompatible with life.
- SkinThickness: No	Everyone has measurable skin thickness.
- Insulin: No	A measured value of exactly zero is not realistic here; it usually indicates missing data.
- BMI: No	BMI cannot be zero for a living person.
- DiabetesPedigreeFunction:	Usually No	Represents a calculated risk score; this dataset has no zeros.
- Age: No	Participants are adults (minimum is 21).

- Notes on Skewness 

- Rule 1: Mean ≈ Median ➡ Distribution is approximately symmetric.
  - Example: BMI
    - Mean = 31.99
    - Median = 32
    - Very close.
    - Not much skew.

- Rule 2: Mean > Median ➡ Right (positive) skew.
- Reason: Large values pull the average upward.
  - Example: Insulin
    - Mean = 79.8
    - Median = 30.5
    - Huge difference.
    - A few patients have extremely high insulin values.
    - Those values increase the mean.
    - Tail goes to the right.

- Rule 3: Mean < Median ➡ Left (negative) skew.
- Reason: Small values pull the average downward.
  - Example
    - Median = 50
    - Mean = 40
    - Tail goes to the left.
    - Another Trick: Compare Mean, Median, and Max/Min
    
    - Right Skew
    - Usually you'll see: Mean > Median
    - Maximum is much farther from the median than the minimum is.
    - Example (Insulin):
      - Mean = 79.8
      - Median = 30.5
      - Max = 846
      - The maximum is extremely far from the center, indicating a long right tail.

    - Left Skew
      - Usually you'll see: Mean < Median
      - Minimum is much farther from the median than the maximum is.

- Mean ≈ Median	Approximately symmetric
- Mean > Median	Right (positive) skew
- Mean < Median	Left (negative) skew
- Very large Standard Deviation	Data is widely spread
- Max much larger than Mean	Possible high-end outliers
- Min = 0 for impossible medical values	Likely missing values encoded as zero
- Mean of a 0/1 column	Proportion of 1s (e.g., Outcome mean = 0.349 → about 35% have diabetes)

