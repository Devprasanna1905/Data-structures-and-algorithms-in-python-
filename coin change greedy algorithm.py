def find(V):
      
    deno = [1, 2, 5, 10, 20, 50,100, 500, 1000]
    n = len(deno)
    ans = []
    deno.sort(reverse=True)

    i=0
    while(i<len(deno)):
          
        
        while (V >= deno[i]):
            V -= deno[i]
            ans.append(deno[i])
  
        i += 1
  
    
    for i in range(len(ans)):
        print(ans[i], end = " ")
  
n = 45
print("Following is minimal number of change for", n, ": ", end = "")
find(n)
