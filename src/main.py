from services.RuleService import RuleService


def main():
    rule_service = RuleService('Carbon_B1262BW0377022_07.2022_Risk bdx.xlsx')
    rule_service.parse_configuration_rules()


if __name__ == "__main__":
    main()
