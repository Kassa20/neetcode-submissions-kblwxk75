class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.forward_stack = []
        self.cur = 0  # not strictly needed with this approach, see note below

    def visit(self, url: str) -> None:
        self.history.append(url)
        self.forward_stack = []

    def back(self, steps: int) -> str:
        while steps and len(self.history) > 1:
            self.forward_stack.append(self.history.pop())
            steps -= 1
        return self.history[-1]

    def forward(self, steps: int) -> str:
        while steps and self.forward_stack:
            self.history.append(self.forward_stack.pop())
            steps -= 1
        return self.history[-1]