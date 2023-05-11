def majority_vote(votes):
    if(len(votes)==1):
        return votes[0]
    left_subarray_majority = majority_vote(votes[:len(votes)//2])
    right_subarray_majority = majority_vote(votes[len(votes)//2:])
    if left_subarray_majority == right_subarray_majority:
        return left_subarray_majority
    elif votes[:len(votes)//2].count(left_subarray_majority)>=votes[len(votes)//2:].count(right_subarray_majority):
        return left_subarray_majority
    else:
        return right_subarray_majority
