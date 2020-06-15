import streamlit as st
from PIL import Image
import pickle

st.title('Titanic Survival Prediction')
img = Image.open('sinking_titanic.jpg')
st.image(img,width=450)

st.sidebar.title('Created by')
st.sidebar.markdown('[Adarsh Shetty](https://twitter.com/adarshetty11)')
st.sidebar.title('About')
st.sidebar.info('The sinking of the RMS Titanic is one of the most infamous shipwrecks in history. On April 15, 1912, during her maiden voyage, the Titanic sank after colliding with an iceberg, killing numerous passengers and crew.')
st.sidebar.info('One of the reasons that the shipwreck led to such loss of life was that there were not enough lifeboats for the passengers and crew. Although there was some element of luck involved in surviving the sinking, some groups of people were more likely to survive than others, such as women, children, and the upper-class.')
st.sidebar.info('This Application predicts the type of people who may have survived this epic disaster')


st.subheader('Enter details')

st.write('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

sex = st.radio('SEX',('Male','Female'))

age = st.number_input('AGE(In Years)',min_value=1,max_value=100)

pclass = st.radio('Passenger Class',('1','2','3'))

sibsp = st.selectbox("SibSp(Number of siblings / spouses aboard the Titanic)",['0','1','2','3','4','5','6'])

parch = st.selectbox("Parch(Number of parents / children aboard the Titanic)",['0','1','2','3','4','5','6'])

fare = st.number_input('Enter Fare(in $)',min_value=1,max_value=550)

embarked = st.selectbox('Embarkation',['Cherbourg','Queenstown','Southampton'])

submit = st.button('Submit')

if sex == 'Male':
        sex_1 = 0
        sex_2 = 1
else:
        sex_1 = 1
        sex_2 = 0

if embarked == 'Cherbourg':
        embarked_1 = 1
        embarked_2 = 0
        embarked_3 = 0
elif embarked == 'Queenstown':
        embarked_1 = 0
        embarked_2 = 1
        embarked_3 = 0
else:
        embarked_1 = 0
        embarked_2 = 0
        embarked_3 = 1

if submit:
    p1 = int(pclass)
    p2 = age
    p3 = int(sibsp)
    p4 = int(parch)
    p5 = int(fare)
    p6 = sex_1
    p7 = sex_2
    p8 = embarked_1
    p9 = embarked_2
    p10 = embarked_3

    with open('model_pickel','rb')as f:
        model = pickle.load(f)
    
    prediction = model.predict([[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]])

    survive = {0:'May Not Survive',1:'May Survive'}
    result = survive[prediction[0]]

    if result == 'May Survive':
        st.info(result)
        st.balloons()
    else:
        st.error(result)


    