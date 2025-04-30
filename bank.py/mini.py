from bank import Account

def main():
    acc1 = Account("Vikas Raswate", 1000, 1234)

    acc1.debit(500)
    acc1.credit(2000)
    acc1.credit(15000)
    acc1.debit(18000)

    acc1.mini_statement()

if __name__ == "__main__":
    main()
