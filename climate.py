import streamlit as st
import pandas as pd
from pathlib import Path
from PIL import Image

app_formal_name = "Unsplash+CLIP image similarity"

st.set_page_config(
    layout="wide",
    page_title=app_formal_name,
)

head_image = Image.open(Path("./images/head_image.jpeg"))

st.title("Let's Say Goodbye to Global Warming")
st.image(head_image, width=1100)

# The Letter for Polar Bear

st.subheader("A Letter for Polar Bear")
st.write(
    """
Dear Polar bear,

You guys are the planet’s biggest land-based carnivores. Although most of you are born on land, you spend most of their time on the sea ice. Since your habitats are around water and ice, sorry that you are particularly at risk due to global warming, which is melting the Arctic Sea ice you depend on. Because of the dependence of the sea ice, you guys are now classified as marine mammals.

Due to the loss of the habitats caused by climate change, you are classified as vulnerable species as well.

You are such strong predator which can generally live and hunt alone, and I believe you are born to be strong. You learn strategies to hunt seals when you are little: you can use your sensible smell to locate a seal in the water beneath compacted snow from almost a mile away.

You can swim for hours to get from one piece of ice to another, and you are capable of fasting for up to several months in late summer and early fall because you can’t hunt for seal when the sea is unfrozen.

Since the first industrial revolution, we have contributed negatively to the global environment. The fact of humanism in that period have damaged so many species and lands. The deforestation and pollution have brought the greenhouse effect which cause the temperature to increase. I can’t believe that you, lovely and powerful creature, is vulnerable due to man-made climate change. 

Your life is on our hand. Let us help You! 

Sincerely,

Lovely human

"""
)

polar_image = Image.open(Path("./images/polar1.jpeg"))
st.image(polar_image)


st.header("What are the signs of climate change?")
st.write(
    """
1.	Temperatures are rising world-wide each year.
2.	The duration of drought becomes longer and more damaging around the world.
3.	Tropical storms are more frequent and more severe.
4.	Glaciers are melting at a faster rate.
5.	Sea level rises due to melting ice sheets.

"""
)
st.header("What are the effects of climate change?")
st.write(
    """
1.	Hotter temperature in all land increases the possibility of heat-related illness.
2.	Melting glaciers threaten the life of coastal community. More carbon dioxide makes the ocean acidic.
3.	Climate change endangers the survival of species on land and near the ocean.
4.	Extreme weather stagnates the production of food. Fisheries and crops may be destroyed and less productive.
5.	Changing weather patterns expand some diseases such as malaria.

    """
)

df_climate = pd.read_csv(Path("./data/GlobalTemperatures.csv"))
df_climate["dt"] = pd.to_datetime(df_climate["dt"])
df_climate.set_index("dt", inplace=True)
st.subheader("Average Land Temperature from the First Industrail Revoluzation")
st.text(
    "Note that the uncertainty of the average temperature is much larger in 1800s than the uncertainty currently"
)
st.line_chart(
    df_climate["LandAverageTemperature"].groupby(by=[df_climate.index.year]).mean()
)

st.subheader("Average Uncertainty of the Average Temperature")
st.text(
    "The decreasing uncertainty of the average temperature provides suffient proof that the average temperature has an increasing trend."
)
st.text(
    "We are more confident based on historical data that our planet is experiencing harmly temperature increase!"
)
st.line_chart(
    df_climate["LandAverageTemperatureUncertainty"]
    .groupby(by=[df_climate.index.year])
    .mean()
)

st.header("Why is temperature increasing?")
st.write(
    """
    One of the main reasons that the temperature increases is the greenhouse effect. A greenhouse gas is any gaseous compound in the atmosphere that can absorb infrared radiation, trapping and holding heat in the atmosphere. The most significant greenhouse gases, according to the Environmental Protection Agency (EPA), are: water vapor (H2O), carbon dioxide (CO2), methane (CH4) and nitrous oxide (N2O). 
    """
)

df_greenhouse = pd.read_csv(Path("./data/greenhouse_gas.csv"), index_col="Year")
df_total = df_greenhouse.loc[(df_greenhouse["VAR"] == "TOTAL")]
df_ghg = df_total.loc[(df_total["POL"] == "GHG")]
country = list(df_ghg["Country"].unique())

st.subheader("The Total Greenhouse Gases Emission from a Country(1990-2015)")
option1 = st.selectbox(
    "Choose a country to see if they are helping the planet.", (country)
)
st.line_chart(df_ghg[(df_ghg["Country"] == option1)]["Value"])

st.subheader("Compare the Greenhouse Gases Emission between two countries")
option2 = st.selectbox("Choose the first country you want to compare.", (country))
option3 = st.selectbox("Choose the second country you want to compare.", (country))
df_combine = pd.DataFrame(
    {
        option2: df_ghg[(df_ghg["Country"] == option2)]["Value"],
        option3: df_ghg[(df_ghg["Country"] == option3)]["Value"],
    }
)
st.line_chart(df_combine)

st.header("What can we do to prevent greenhouse effect?")
pie = Image.open(Path("./images/pie.jpeg"))
st.image(pie, width=400)

st.subheader("Use less energy")
st.write(
    """
    You can try to use less electricity when it comes to burn coal or gas when electricity is responsible for the quarter of greenhouse gases emissions.

1.	Use LED light to require less electricity.
2.	Set thermostat lower in winter and higher in summer.
3.	Turn off the lights when no one is home.

    """
)
energy = Image.open(Path("./images/energy.jpeg"))
st.image(energy, width=600)

st.subheader("Use electricity without emissions")
st.write(
    """
    Nowadays, there are so many renewable resources for people to use. Since it does not burn fuels, these renewable resources don’t burn greenhouse gases.

1.	Solar energy.
2.	Geothermal.
3.	Wind turbines.
4.	Hydropower.

    """
)
solar = Image.open(Path("./images/solar.jpeg"))
st.image(solar, width=600)

st.subheader("Travel without emissions")
st.write(
    """
    Most of the transportations require greenhouse gases to travel. Cars need gasoline and airplanes need jet fuel. While the transportation is responsible to three tenth of the greenhouse gases, people can shift to alternative way for traveling to limit greenhouse effect.

1.	Use public transportation.
2.	Drive hybrid car.
3.	Biking.
4.	Walking

City can also add more paths for buses, more routes for biking, and more walkway for walking to encourage people to avoid using transportations that require gasoline.

    """
)

bike = Image.open(Path("./images/bike.jpeg"))
st.image(bike, width=600)

st.subheader("Reduce carbon dioxide in the air")
st.write(
    """
    One of the greenhouse gases is carbon dioxide, and if we reduce carbon dioxide, or take carbon dioxide out of air, the greenhouse effect will be limited.
    
1.	Conserve forest, and grass land.
2.	Throw trashes into trash bin.
3.	Plant trees.
4.	Start recycling.

    """
)
tree = Image.open(Path("./images/tree.jpeg"))
st.image(tree, width=600)

st.subheader(
    "If you can find something to do as listed above, such as changing the way of transportation, we encourage you please to do so to try to reduce greenhouse gases emission. "
)
st.subheader("As you start recycling, polar bear may be saved from the danger. ")
st.write(":heart:" * 53)
st.text("'That's one small step for man, one giant leap for mankind.-Neil Armstrong'")

n = 0
st.text("Are you going to take action right now to save the polar bear?")
result = st.button("YES!!")
if result:
    n = n + 1
st.text(f"You are the {n} person who is helping save the polar bear")
