import random
import math
import matplotlib.pyplot as plt

random.seed(314159)
N = 10000
xs_in, ys_in, xs_out, ys_out = [], [], [], []
hit = 0

for _ in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x*x + y*y <= 1:
        hit += 1
        xs_in.append(x)
        ys_in.append(y)
    else:
        xs_out.append(x)
        ys_out.append(y)

pi_est = 4 * hit / N
abs_err = abs(pi_est - math.pi)

print("N =", N)
print("Hits =", hit)
print("Estimated pi =", pi_est)
print("Absolute error =", abs_err)

fig, ax = plt.subplots(figsize=(5, 5))
ax.scatter(xs_in, ys_in, s=3, alpha=0.6, label="Inside circle")
ax.scatter(xs_out, ys_out, s=3, alpha=0.6, label="Outside circle")

circle = plt.Circle((0, 0), 1, fill=False)
ax.add_patch(circle)

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect("equal", adjustable="box")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title(f"Monte Carlo estimation of pi (N={N}, estimate={pi_est:.6f})")
ax.legend()
fig.tight_layout()
fig.savefig("assets/monte_carlo_pi_plot.png", dpi=150, bbox_inches="tight")
print("Saved to assets/monte_carlo_pi_plot.png")
