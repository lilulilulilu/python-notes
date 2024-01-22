class TestClass:
    value = 2
    
    def test_one(self):
        assert self.value == 2

    def test_two(self):
        self.value += 1
        assert self.value == 3
        
    def test_three(self):
        self.value += 1
        assert self.value == 3
