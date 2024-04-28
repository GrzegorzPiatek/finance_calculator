import components

calculators = {
    'COMPOUND_INTEREST': components.compound_interest,
    'REGULAR_INVESTMENT': components.regular_investment,
}


def main():
    components.title()
    calculator_type = components.sidebar()
    calculators[calculator_type]()
    
    components.footer()

if __name__ =='__main__':
    main()