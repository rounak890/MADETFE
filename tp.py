import matplotlib.pyplot as plt
import numpy as np

# --- Data from the table ---
variants = [
    "Feature-based",
    "Resolution-based",
    "Masked Downshuffle",
    "UNet",
    "Denoised LaMa + UNet",
    "Final (LaMa + MAT + UNet + denoiser)"
]
P = np.array([16.6, 0.46, 0.76, 125.0, 125.2, 125.3])                    # Params in millions
FID = np.array([65.63, 60.23, 35.6, 19.23, 18.43, 0.9873])
SSIM = np.array([0.03, 0.18, 0.892, 0.928, 0.9398, 0.9764])
FP = SSIM / FID                                                           # Fitting performance (SSIM/FID)

# X-axis: Parameter change (from reference point)
X = P - 125.3                                           # X-axis: P - 125.3

# Y-axis: Fitting performance FP
Y = FP                                                  # Y-axis: FP = SSIM/FID

# --- Figure setup ---
fig, ax = plt.subplots(figsize=(9, 6))

# Axis limits
x_min, x_max = -130, 5
y_min, y_max = -0.05, 1.0

# Draw axes (origin at (0,0))
ax.axvline(0.0, color='k', linewidth=1.0)
ax.axhline(0.0, color='k', linewidth=1.0)

# Quadrant colored backgrounds
# Quadrant I (OER): x>0, y>0 - Upper right (Decreasing performance) - light blue
ax.fill_betweenx([0, y_max], 0, x_max, color='#d9eaf7', alpha=0.6)
# Quadrant II (OAR): x<0, y>0 - Upper left (Promoting performance) - light orange
ax.fill_betweenx([0, y_max], x_min, 0, color='#ffe6cc', alpha=0.6)
# Quadrant III (UER): x<0, y<0 - Lower left (Decreasing performance) - light blue
ax.fill_betweenx([y_min, 0], x_min, 0, color='#d9eaf7', alpha=0.6)
# Quadrant IV (UAR): x>0, y<0 - Lower right (Promoting performance) - light orange
ax.fill_betweenx([y_min, 0], 0, x_max, color='#ffe6cc', alpha=0.6)

# Plot connecting path with arrows
ax.plot(X, Y, linestyle='--', linewidth=1, color='gray', zorder=2)
for i in range(len(X)-1):
    # small arrow between consecutive points
    dx = X[i+1] - X[i]
    dy = Y[i+1] - Y[i]
    ax.arrow(X[i], Y[i], dx, dy,
             length_includes_head=True, head_width=0.02, head_length=2,
             fc='gray', ec='gray', alpha=0.8, zorder=2)

# Scatter points
colors = ['tab:purple', 'tab:orange', 'tab:blue', 'tab:green', 'tab:olive', 'tab:red']
markers = ['o','s','^','D','v','*']
sizes = np.clip((FP / FP.max()) * 300 + 50, 60, 400)  # scale marker sizes by FP for emphasis
for i, label in enumerate(variants):
    ax.scatter(X[i], Y[i], s=sizes[i], color=colors[i], edgecolor='k', zorder=5, marker=markers[i])
    ax.text(X[i] + 2, Y[i] + 0.03, label, fontsize=9, fontweight='bold', zorder=6)

# Axis labels and ticks
ax.set_xlabel('Parameter change (X = P − 125.3)', fontsize=11)
ax.set_ylabel('Fitting performance (Y = SSIM / FID)', fontsize=11)
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)
ax.set_title('PQS-FP diagram — MADETFE variants', fontsize=13, fontweight='bold')

# Quadrant labels: place them in the center of each quadrant
ax.text(-65, 0.70, 'Quadrant II\nOAR', fontsize=11, color='maroon', ha='center', weight='bold', 
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#ffe6cc', alpha=0.7, edgecolor='maroon', linewidth=2))
ax.text(2.5, 0.70, 'Quadrant I\nOER', fontsize=11, color='navy', ha='center', weight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#d9eaf7', alpha=0.7, edgecolor='navy', linewidth=2))
ax.text(-65, 0.25, 'Quadrant III\nUER', fontsize=11, color='navy', ha='center', weight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#d9eaf7', alpha=0.7, edgecolor='navy', linewidth=2))
ax.text(2.5, 0.25, 'Quadrant IV\nUAR', fontsize=11, color='maroon', ha='center', weight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#ffe6cc', alpha=0.7, edgecolor='maroon', linewidth=2))

# Grid and annotation for ideal model
ax.grid(alpha=0.4, linestyle=':')
ax.scatter(0.0, FP[-1], s=250, facecolor='none', edgecolor='black', linewidth=1.2, zorder=7)
ax.text(5, FP[-1] + 0.03, 'Ideal (O)', fontsize=9, fontstyle='italic', weight='bold')

# Legend for markers - placed on the left side to avoid covering data
from matplotlib.lines import Line2D
legend_elements = [Line2D([0],[0], marker=markers[i], color='w', markerfacecolor=colors[i],
                          markeredgecolor='k', markersize=8, label=variants[i]) for i in range(len(variants))]
ax.legend(handles=legend_elements, loc='upper left', fontsize=8, framealpha=0.95)

plt.tight_layout()
plt.savefig('pqs_fp_diagram.png', dpi=300, bbox_inches='tight')
plt.show()
