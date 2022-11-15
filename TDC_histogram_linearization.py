import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

n_bin = 2**3
n_bin1 = 2**10

count = 100
count1 = 10**4
probabilities = [0.32, .06, .06, .06, .06, .06, .06, .32]
#probabilities = [0, 0, 0, 0, 0, 0, 0, 1]

data = np.random.choice(n_bin, count, p=probabilities)
#data = np.random.randint(0,n_bin, size=count)

fig, axes= plt.subplots(ncols=4, nrows=1, figsize=(12,4), tight_layout=True, sharey=False, sharex=False)

n, bins, patches = axes[0].hist(data, bins=np.arange(n_bin+1), edgecolor='k')
print(bins)
axes[0].set_xlim(-1,9)
axes[0].set_ylim(0,None)
axes[0].set_xlabel(f'bins')
axes[0].set_ylabel(f'counts')
axes[0].set_title(f'fig1, bins={n_bin}, count={count}', fontsize=10)

avg = np.average(n[1:-1])
print(avg)
print(n)
effbins = bins[1:-2]
effcounts = n[1:-1].copy()
effcounts_norm = effcounts / avg
print(effcounts_norm)

axes[1].bar(effbins, effcounts_norm, width=1, align='edge', edgecolor='k')
axes[1].set_xlim(-1,9)
axes[1].set_ylim(0, None)
axes[1].set_xlabel(f'bins')
axes[1].set_ylabel(f'norms')
axes[1].set_title(f'fig2, remove edge bins and normalize', fontsize=10)

diff = effcounts_norm-1
axes[2].bar(effbins, diff, width=1, align='edge', edgecolor='k')
axes[2].set_xlim(-1,9)
axes[2].set_ylim(None, None)
axes[2].set_xlabel(f'bins')
axes[2].set_ylabel(f'ratio difference')
axes[2].set_title(f'fig3, diff', fontsize=10)

cal = n.copy()
cal[1:-1] /= effcounts_norm
axes[3].bar(bins[:-1], cal, width=1, align='edge', edgecolor='k')
axes[3].set_xlim(-1,9)
axes[3].set_ylim(None, None)
axes[3].set_xlabel(f'bins')
axes[3].set_ylabel(f'ratio difference')
axes[3].set_title(f'fig4, after TDC linearization', fontsize=10)

fig.savefig('./TDC_linearization_example.png', dpi=300)