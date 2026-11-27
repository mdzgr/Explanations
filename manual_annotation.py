
def random_x_problems_dis_agreement_exc_ids(
    data_with_split, excluded_ids=(), sample_size=250
    '''selects x amounts of high and low agreeement examples'''
):
    def check_low_agreement(counter_annotations):
      return sorted(counter_annotations.values()) == [2, 3]

    excluded_ids = set(excluded_ids)
    if excluded_ids:
        data_with_split = {
            k: v for k, v in data_with_split.items() if k not in excluded_ids
        }

    high_ids = [k for k, v in data_with_split.items() if 5 in v["lcnt"].values()]
    low_ids = [k for k, v in data_with_split.items() if check_low_agreement(v["lcnt"])]

    return (
        {k: data_with_split[k] for k in random.sample(high_ids, sample_size)},
        {k: data_with_split[k] for k in random.sample(low_ids, sample_size)},
    )
