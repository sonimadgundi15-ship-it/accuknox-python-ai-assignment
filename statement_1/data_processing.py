import matplotlib.pyplot as plt
import requests
import statistics

url = "https://reqres.in"
print("Attempting to connect to public API endpoint...")

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    data_payload = response.json()
    student_records = data_payload.get("data", [])
    print("✅ Success: Fetched data live from the API.")

except requests.exceptions.RequestException as error:
    print(f" Network error occurred: {error}")
    print("🔄 Automatically switching to local backup student dataset...\n")

    student_records = [
        {"id": 1, "first_name": "John", "last_name": "Doe"},
        {"id": 2, "first_name": "Jane", "last_name": "Smith"},
        {"id": 3, "first_name": "Alex", "last_name": "Jones"},
        {"id": 4, "first_name": "Emily", "last_name": "Brown"},
        {"id": 5, "first_name": "Michael", "last_name": "Davis"},
    ]

student_names = []
calculated_averages = []
all_individual_averages = []

for student in student_records:
    student_id = student.get("id", 0)
    full_name = (
        f"{student.get('first_name', '')} {student.get('last_name', '')}"
    )

    marks = {
        "Mathematics": 65 + ((student_id * 8) % 31),
        "Science": 60 + ((student_id * 12) % 36),
        "English": 70 + ((student_id * 5) % 26),
    }

    student_average = statistics.mean(list(marks.values()))
    all_individual_averages.append(student_average)

    student_names.append(full_name)
    calculated_averages.append(student_average)

if student_names and calculated_averages:
    class_average = statistics.mean(all_individual_averages)

    print(f"\n📊 Overall Class Average calculated: {class_average:.2f}%")
    print("🎨 Rendering performance bar chart visualization...")

    plt.figure(figsize=(10, 6))

    bars = plt.bar(
        student_names,
        calculated_averages,
        color="skyblue",
        edgecolor="navy",
        alpha=0.85,
    )

    plt.axhline(
        y=class_average,
        color="crimson",
        linestyle="--",
        linewidth=1.5,
        label=f"Class Average ({class_average:.1f}%)",
    )

    plt.title(
        "Individual Student Performance Metrics (Average Score)",
        fontsize=14,
        fontweight="bold",
        pad=15,
    )
    plt.xlabel("Student Profiles", fontsize=12, labelpad=10)
    plt.ylabel("Average Performance Score (%)", fontsize=12, labelpad=10)
    plt.ylim(0, 105)
    plt.grid(axis="y", linestyle=":", alpha=0.6)
    plt.legend(loc="lower right")

    for bar in bars:
        yval = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            yval + 1.5,
            f"{yval:.1f}%",
            ha="center",
            va="bottom",
            fontsize=9,
            fontweight="bold",
        )

    plt.tight_layout()
    plt.show()
