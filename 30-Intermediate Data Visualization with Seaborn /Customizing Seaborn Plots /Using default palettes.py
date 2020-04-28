'''Seaborn includes several default palettes that can be easily applied to your plots. In this example, we will look at the impact of two different palettes on the same distplot.'''

# Loop through differences between bright and colorblind palettes
for p in ['bright', 'colorblind']:
    sns.set_palette(p)
    sns.distplot(df['fmr_3'])
    plt.show()

    # Clear the plots
    plt.clf()