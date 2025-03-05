class StrategyAgent:
    def __init__(self):
        pass

    def plan(self, insights):
        if not insights:
            return "No insights to generate a strategy"
        
        strategy = (
            "Based on the analyzed insights, we recommend the following research strategy: \n"
            "1. Deep dive into emerging trends related to the topic.\n"
            "2. Identify key players and competitors.\n"
            "3. Formulate actionable investment or business strategies.\n"
            "4. Monitor industry developments and iterate research regularly."
        )
        return strategy
