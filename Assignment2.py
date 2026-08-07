def report_decorator(func):
    def wrapper(self):
        print("----- Report -----")
        func(self)
        print("------------------")
    return wrapper


class Report:
    template = "Simple"

    def __init__(self, title, content):
        self.title = title
        self.content = content

    @classmethod
    def set_template(cls, name):
        cls.template = name

    @report_decorator
    def display(self):
        print("Template :", Report.template)
        print("Title    :", self.title)
        print("Content  :", self.content)

    def __str__(self):
        return self.title + " (" + Report.template + " Template)"

    def __len__(self):
        return len(self.content)


Report.set_template("Professional")

r1 = Report("Student Report", "Python practical completed successfully.")

print(r1)
print("Content Length:", len(r1))
r1.display()