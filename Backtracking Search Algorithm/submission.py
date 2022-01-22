import plotly.express as px

countries = ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Falkland Islands", "Guyana", "Paraguay",
             "Peru", "Suriname", "Uruguay", "Venezuela"]

colors = ["blue", "red", "green", "yellow"]

c_list = [
    [0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0]
]


initialColors = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
vertices = 13

countries_dict = {}


def checkColor(vrtx, matrix, listC, colorindex) -> bool:
    for i in range(vertices):
        if (matrix[vrtx][i] == 1 and colorindex == listC[i]):
            return False
    return True

def graphColoring_(matrix, c_length, listC, vrtx)-> bool:

    if vrtx == vertices:
        return True

    for i in range(1, c_length + 1):
        if checkColor(vrtx, matrix, listC, i):
            listC[vrtx] = i
            if graphColoring_(matrix, c_length, listC, vrtx + 1):
                return True
            listC[vrtx] = 0
    return False

a=1
def coloringOperation(listC):
    for i in range(vertices):
        countries_dict[countries[i]] = colors[listC[i] - a]



def graphColor(matrix, listC):

    if not graphColoring_(matrix, listC, initialColors, 0):
        print("Color schema not possible")
        return False
    coloringOperation(initialColors)
    return True




def plot_choropleth(colormap):
    fig = px.choropleth(locationmode="country names",
                        locations=countries,
                        color=countries,
                        color_discrete_sequence=[colormap[c] for c in countries],
                        scope="south america")
    fig.show()


# Implement main to call necessary functions
if __name__ == "__main__":
    color_lenght = len(colors)
    graphColor(c_list, color_lenght)
    plot_choropleth(countries_dict)
