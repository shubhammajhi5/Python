class Employee:

    company = 'Youtube'

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def fullName(self):
        return f'{self.first} {self.last}'

    @property
    def eMail(self):
        return f'{self.first}.{self.last}@gmail.com'

    def __repr__(self):
        return f'({self.first}, {self.last}, {self.pay})'


def main():
    e = Employee('Bhuvan', 'Bam', 50000)
    print(e)
    print(e.fullName)
    print(e.company)
    print(e.eMail)


if __name__ == '__main__':
    main()
