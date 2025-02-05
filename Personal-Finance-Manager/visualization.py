import matplotlib.pyplot as plt

class Visualization:
    @staticmethod
    def plot_spending(transactions):
        """Plot spending by category."""
        category_totals = {}
        for _, transaction_type, category, amount, _ in transactions:
            if transaction_type == "expense":
                category_totals[category] = category_totals.get(category, 0) + amount

        categories = list(category_totals.keys())
        amounts = list(category_totals.values())

        plt.figure(figsize=(10, 5))
        plt.bar(categories, amounts, color='skyblue')
        plt.title("Spending by Category")
        plt.xlabel("Category")
        plt.ylabel("Amount ($)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_goal_progress(goals):
        """Plot progress toward financial goals."""
        names = [goal[0] for goal in goals]
        targets = [goal[1] for goal in goals]
        currents = [goal[2] for goal in goals]

        plt.figure(figsize=(10, 5))
        plt.bar(names, targets, color='lightgray', label="Target")
        plt.bar(names, currents, color='skyblue', label="Current")
        plt.title("Progress Toward Financial Goals")
        plt.xlabel("Goal")
        plt.ylabel("Amount ($)")
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()