class BrowserHistory:

    def __init__(self, homepage: str):
        self.backward = [homepage]
        self.f = []

    def visit(self, url: str) -> None:
        self.backward.append(url)
        self.f = []

    def back(self, steps: int) -> str:
        while steps and len(self.backward) > 1: 
            self.f.append(self.backward.pop())
            steps -= 1
        
        return self.backward[-1]


    def forward(self, steps: int) -> str:
        while steps and self.f:
            self.backward.append(self.f.pop())
            steps -= 1

        return self.backward[-1]



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)