from scipy.stats import shapiro

# আমাদের হাতির ডাটা
elephant_data = [3049.67, 2986.17, 3064.77, 3152.30, 2976.58, 2976.59, 3157.92, 3076.74, 2953.05, 3054.26]

# Shapiro-Wilk Test করা
stat, p_value = shapiro(elephant_data)

print(f"W-Statistic: {stat:.4f}")
print(f"P-Value: {p_value:.4f}")

if p_value > 0.05:
    print("সিদ্ধান্ত: ডাটাটি Normal Distribution মেনে চলে।")
else:
    print("সিদ্ধান্ত: ডাটাটি Normal Distribution মেনে চলে না।")