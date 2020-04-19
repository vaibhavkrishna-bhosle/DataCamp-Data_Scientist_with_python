'''In the previous exercise, you computed the mean birth weight for full-term babies; you
filtered out preterm babies because their distribution of weight is different.

The distribution of weight is also different for multiple births, like twins and triplets.
In this exercise, you'll filter them out, too, and see what effect it has on the mean.'''

# Filter full-term babies
full_term = nsfg['prglngth'] >= 37

# Filter single births
single = nsfg['nbrnaliv'] == 1

# Compute birth weight for single full-term babies
single_full_term_weight = birth_weight[single & full_term]
print('Single full-term mean:', single_full_term_weight.mean())

# Compute birth weight for multiple full-term babies
mult_full_term_weight = birth_weight[~single & full_term]
print('Multiple full-term mean:', mult_full_term_weight.mean())