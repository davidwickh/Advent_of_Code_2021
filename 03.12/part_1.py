import pandas as pd


def diagnositcs():
    df = pd.read_excel("/Users/David/Documents/GitHub/Advent_of_Code_2021/03.12/input.xls")

    gamma_bin_result = []
    epsilon_bin_result = []
    for column in df:
        bin = pd.DataFrame(df[column].value_counts())
        if bin.at[1, column] > bin.at[0, column]:
            gamma_bin_result.append("1")
        else:
            gamma_bin_result.append("0")

    for column in df:
        bin = pd.DataFrame(df[column].value_counts())
        if bin.at[1, column] > bin.at[0, column]:
            epsilon_bin_result.append("0")
        else:
            epsilon_bin_result.append("1")

    def bin_to_string(series_bin=None):
        result = 0
        for i in range(len(series_bin)):
            if i == 0:
                result = str(series_bin[i])
            if i > 0:
                result += str(series_bin[i])
        return result
    def bin_to_dec(bin_result=None):
        """
        @type bin_result: object
        """
        dec_result = 0
        for element in range(0, len(bin_result)):
            length = len(bin_result)
            index = length - element - 1
            dec_result += int(bin_result[element]) * 2 ** index
        return dec_result

    gamma_bin_result = bin_to_string(gamma_bin_result)
    epsilon_bin_result = bin_to_string(epsilon_bin_result)
    gamma_dec_result = 0
    epsilon_dec_result = 0
    gamma_dec_result = bin_to_dec(gamma_bin_result)
    epsilon_dec_result = bin_to_dec(epsilon_bin_result)


    print(gamma_dec_result*epsilon_dec_result)

if __name__ == "__main__":
    diagnositcs()
