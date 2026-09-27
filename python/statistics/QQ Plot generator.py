# import numpy as np
# import matplotlib.pyplot as plt
# import scipy.stats as stats
#
# # হাতির ডাটা
# elephant_data = [3049.67, 2986.17, 3064.77, 3152.3, 2976.58, 2976.59, 3157.92, 3076.74, 2953.05, 3054.26]
#
# # QQ Plot তৈরি করা
# plt.figure(figsize=(6, 4))
# stats.probplot(elephant_data, dist="norm", plot=plt)
# plt.title("QQ Plot for Elephant Weights")
# plt.xlabel("Theoretical Quantiles")
# plt.ylabel("Ordered Values (Elephant Weights)")
# plt.grid(True)
# plt.show()

# import matplotlib.pyplot as plt
# import scipy.stats as stats
#
# # ১. হাতির ওজনের ডাটাসেট (কেজিতে)
# elephant_data = [3049.67, 2986.17, 3064.77, 3152.30, 2976.58, 2976.59, 3157.92, 3076.74, 2953.05, 3054.26]
#
# # ২. ইঁদুরের ওজনের ডাটাসেট (গ্রামে)
# mouse_data = [45.37, 45.34, 52.42, 30.87, 32.75, 44.38, 39.87, 53.14, 40.92, 35.88]
#
# # প্লটের আকার নির্ধারণ (পাশাপাশি দুটি গ্রাফ দেখার জন্য)
# fig, axes = plt.subplots(1, 2, figsize=(12, 5))
#
# # হাতির ডাটার জন্য QQ Plot
# stats.probplot(elephant_data, dist="norm", plot=axes[0])
# axes[0].set_title("QQ Plot: Elephant Weights")
# axes[0].grid(True)
#
# # ইঁদুরের ডাটার জন্য QQ Plot
# stats.probplot(mouse_data, dist="norm", plot=axes[1])
# axes[1].set_title("QQ Plot: Mouse Weights")
# axes[1].grid(True)
#
# # গ্রাফ সুন্দরভাবে সাজানো এবং প্রদর্শন করা
# plt.tight_layout()
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# ১. Right-Skewed Data তৈরি করা (Exponential Distribution ব্যবহার করে)
# উদাহরণ: মানুষের আয়ের ডাটা বা কল সেন্টারে অপেক্ষার সময় সাধারণত এমন হয়
skewed_data = np.random.exponential(scale=2, size=1000)

# প্লটের আকার নির্ধারণ
plt.figure(figsize=(8, 5))

# Skewed ডাটার জন্য QQ Plot তৈরি করা
stats.probplot(skewed_data, dist="norm", plot=plt)

# গ্রাফের টাইটেল ও অন্যান্য সেটিংস
plt.title("QQ Plot: Right-Skewed Data")
plt.xlabel("Theoretical Quantiles")
plt.ylabel("Ordered Values (Skewed Data)")
plt.grid(True)
plt.show()