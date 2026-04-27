class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        n = len(accounts)
        emails = [] # emails 
        email_id = {} # map email -> id
        email_acc = {} # map email -> account
        
        m = 0
        for accId, acc in enumerate(accounts): 
            for i in range(1, len(acc)):
                email = acc[i]
                if email in email_id:
                    continue
                emails.append(email)
                email_id[email] = m
                email_acc[m] = accId 
                m += 1
        
        adj = [[] for _ in range(m)]
        for a in accounts: 
            for i in range(2, len(a)):
              id1 = email_id[a[i]]
              id2 = email_id[a[i-1]]
              adj[id1].append(id2)
              adj[id2].append(id1)  


        emailGroup = defaultdict(list)
        visited = [False] * m 
        def dfs(node, accId):
            visited[node] = True
            emailGroup[accId].append(emails[node])
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei, accId)

        for i in range(m):
            if not visited[i]:
                dfs(i, email_acc[i])

        res = []
        for accId in emailGroup: 
            name = accounts[accId][0]
            res.append([name] + sorted(emailGroup[accId]))
                

        return res
