import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title('Most Crowded Countries In The World')  #title
st.write("This Project is an anaylis for the top 100 most countries with population")

st.sidebar.title("Navigation")

file = st.sidebar.file_uploader("Upload File or use MostCrowded100inWorld.csv File")
action = st.sidebar.radio("Select What To Display", ('Home', 'Top 10','Dictionary' , 'Statistics', 'Chart',))

if file == None:
    df = pd.read_csv("MostCrowded100inWorld.csv")
else:
    df = pd.read_csv(file)

def add_bg_from_url():
    st.markdown(
        f""" 
        <style> 
        .stApp {{ 
            background-image: 
url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSvFp4-Yn1ijum8k6a2GN_dmSmembUldppb_Q&usqp=CAU"); 
                    background-attachment: 
fixed; 
                    background-size: cover 
                }} 
        </style> 
        """,
        unsafe_allow_html=True
    )
add_bg_from_url()

def dic():
    # Dictionaries allow us to work with key value pairs. We decided to make a dictionary of countries and their population,
    # since dictionaries have keys that can store all kinds of arguments like integers, strings and even functions-

    dictionary = {'India': 'Delhi',
                  'China': 'Shanghai',
                  'Egypt': 'Cairo',
                  'Japan': 'Tokyo'
                  }

    # we will now use another dictionary to show the integer of the population
    # of each of the most crowded cities related to those countries

    population_number = {'Delhi': 18000000,
                         'Shanghai': 29000000,
                         'Cairo': 22000000,
                         'Tokyo': 38000000
                         }

    st.write(dictionary)
    st.write(population_number)

    # we can also print the keys in the dictionary only by using the for loop, illustrated below:

    for countries in dictionary.items():
        st.write(countries)

    # and if we want to go into more details we can use the item method and print the keys and values
    # by showing the countries and their most crowded cities:
    st.write("\n")

    for cities in population_number.items():
        st.write(cities)



def Home():
    st.header("Most Crowded countries in the World Top 100")
    st.write(df)


def Top10():
    st.header("Most Crowded countries in the World Top 10")
    st.write(df.head(11))


def statistics():
    st.header("Data Summary Statistics")
    stats = df.describe()
    st.write(stats)

def Figure1():
    st.header("Chart")
    Fig = plt.figure("Bar Graph Of Population")
    cc = ["China", "India", "United States", "Indonesia", "Pakistan"]
    pp = [1412600000, 1375586000, 334200979, 275773800, 235825000]
    plt.bar(cc, pp)
    plt.title('Population Density')
    plt.xlabel('Countries')
    plt.ylabel('Population')
    st.pyplot(Fig)

def Figure2():
    st.header("The Following Graph Show the Percentage of The Top 5 Countries Population")
    Fig2 = plt.figure("Pie Chat of Population")
    per = [17.70,17.20,4.18,3.45,2.95]
    name = ['China','India','United States','Indonesia','Pakistan']
    plt.pie(per)
    plt.title('Population Density')
    plt.xlabel('O:China   B:India  G:USA  R:Indonesia   P:Pakistan  ')
    plt.ylabel('Population')
    st.pyplot(Fig2)



if action == "Home":
    Home()
elif action == "Top 10":
    Top10()
elif action == "Dictionary":
    dic()
elif action == "Statistics":
    statistics()
elif action == "Chart" and file == None:
    Figure1()
    Figure2()
else:
    ll=st.button("Most Crowded Countries In The World")
    if ll==True:
        Figure1()
        Figure2()
