def search(pattern,text):
	M = len(pattern)
	N = len(text)
	i=0
	while i<N-M:
		j = 0
		while(j < M):
			if (txt[i + j] != pat[j]):
				break
			j += 1
		if (j == M):
			print("Pattern found at index ", i)
		i=i+1	


txt = "aaaabbbaaababac"
pat = "baba"
search(pat, txt)
