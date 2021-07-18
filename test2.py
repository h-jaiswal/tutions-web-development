
    # Assuming the data is given in following format

    # data = 
    # [
    #     {
    #         year: 1995,

    #         managers: 
    #             {
    #                 new: 750,
    #                 left: null
    #             },
    #         technicians:
    #             {
    #                 new: 1200,
    #                 left: null
    #             }
    #         operators:
    #             {
    #                 new: 880,
    #                 left: null
    #             }
    #         accoutants:
    #             {
    #                 new: 1160,
    #                 left: null
    #             }
    #         peons:
    #             {
    #                 new: 820,
    #                 left: null
    #             }
    #     },

    #     {
    #         and so on....
    #     }
    # ]

def main():

    data   # data array to process

    turnoverYearWise = []

    for row in data:
        maxTurnover = -inf
        maxTurnoverDepartment = null
        for key, value in row.values():
            if key == "year":
                year = value
            else:
                total = value["new"] + value["left"])

                turnover = value["left"] / total

                if turnover > maxTurnover:
                    maxTurnover = turnover
                    maxTurnoverDepartment = key
        turnoverYearWise.append( tuple( year, maxTurnoverDepartment, maxTurnover) )

    overallMaxTurnover = -inf
    overallMaxTurnoverDepartment = null
    for yearData in turnoverYearWise:
        department = yearData[1]
        turnover =  yearData[2]
        if turnover >  overallMaxTurnover :
            overallMaxTurnover = turnover
            overallMaxTurnoverDepartment = department

    print("Maximum overall turnover data: ")
    print( "Department " department + "Turnover "  + overallMaxTurnover)

            

