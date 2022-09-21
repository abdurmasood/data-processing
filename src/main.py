from inputoutput.DataReader import DataReader
from inputoutput.DataWriter import DataWriter
from services.DataFormattingService import DataFormattingService
from services.RuleService import RuleService


def main():
    # Initialise services.
    rule_service = RuleService('Carbon_B1262BW0377022_07.2022_Risk bdx.xlsx')
    rule_service.parse_configuration_rules()

















    # ------------------------------------------------------------------------------

    # input_directory = "../data/input"
    # known_files = []

    # while True:
    #     # Watch for new incoming files.
    #     actual_files = data_reader.get_all_files_in_directory(input_directory)
    #     new_files = [f for f in actual_files if f not in known_files]

    #     # If there are any new files to be processed.
    #     if new_files:
    #         # Process each new file.
    #         for new_file in new_files:
    #             pass


if __name__ == "__main__":
    main()
