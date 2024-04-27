import components

calculators = {
    'COMPOUND_INTEREST': components.compound_interest,
    'CREDIT_CALCULATOR': components.credit_calculator,
}


def main():
    components.title()
    calculator_type = components.sidebar()
    calculators[calculator_type]()


if __name__ =='__main__':
    main()