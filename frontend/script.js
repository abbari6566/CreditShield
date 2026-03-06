const getForm = document.getElementById("credit-form");
const predictBtn = document.getElementById("predict-btn");

predictBtn.addEventListener("click", async () => {
  const data = {
    RevolvingUtilizationOfUnsecuredLines: Number(
      document.getElementById("RevolvingUtilizationOfUnsecuredLines").value,
    ),
    age: Number(document.getElementById("age").value),
    NumberOfTime3059DaysPastDueNotWorse: Number(
      document.getElementById("NumberOfTime3059DaysPastDueNotWorse").value,
    ),
    DebtRatio: Number(document.getElementById("DebtRatio").value),
    MonthlyIncome: Number(document.getElementById("MonthlyIncome").value),
    NumberOfOpenCreditLinesAndLoans: Number(
      document.getElementById("NumberOfOpenCreditLinesAndLoans").value,
    ),
    NumberOfTimes90DaysLate: Number(
      document.getElementById("NumberOfTimes90DaysLate").value,
    ),
    NumberRealEstateLoansOrLines: Number(
      document.getElementById("NumberRealEstateLoansOrLines").value,
    ),
    NumberOfTime6089DaysPastDueNotWorse: Number(
      document.getElementById("NumberOfTime6089DaysPastDueNotWorse").value,
    ),
    NumberOfDependents: Number(
      document.getElementById("NumberOfDependents").value,
    ),
  };
  const response = await fetch("http://127.0.0.1:8000/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });
  const result = await response.json();
  document.getElementById("result").innerText =
    "Default Probability: " +
    (result.default_probability * 100).toFixed(1) +
    "%";
});
