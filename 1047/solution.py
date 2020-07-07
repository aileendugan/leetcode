def removeDuplicates(S):
	S = list(S)
	for i,x in enumerate(S):
		if S[i] and S[i+1]:
			if S[i] == S[i+1]:
				S.remove(S[i])
				S.remove(S[i+1])
		if S[i] and S[i-1]:
			if S[i] == S[i-1]:
				S.remove(S[i])
				S.remove(S[i-1])
	return ''.join(S)
