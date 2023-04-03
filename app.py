import streamlit as st
import numpy as np
import pickle

# Load the pickled model
loaded_model = open("pipe.pkl", "rb")
model = pickle.load(loaded_model)

# Define the Streamlit app
def get_user_inputs():

    age = st.slider('Age',min_value=18,max_value=100)
    job = st.selectbox('Job', ['admin.', 'blue-collar', 'entrepreneur', 'housemaid', 'management',
                               'retired', 'self-employed', 'services', 'student', 'technician', 'unemployed'])
    marital = st.selectbox('Marital Status', [ 'single','divorced', 'married'])
    education = st.selectbox('Education', ['basic.4y', 'basic.6y', 'basic.9y', 'high.school', 'illiterate',
                                           'professional.course', 'university.degree'])
    default = st.selectbox('Has Credit in Default', ['no', 'yes'])
    housing = st.selectbox('Has Housing Loan', ['no', 'yes'])
    loan = st.selectbox('Has Personal Loan', ['no', 'yes'])
    contact = st.selectbox('Contact Type', ['cellular', 'telephone'])
    month = st.selectbox('Last Contact Month', ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 
                                                'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])
    day_of_week = st.selectbox('Last Contact Day of Week', ['mon', 'tue', 'wed', 'thu', 'fri'])
    campaign = st.slider('Number of Contacts Performed During this Campaign', 0, 50, 5,)
    pdays = st.slider('Days Since Previous Contact', 0, 1000, 50)
    previous = st.slider('Number of Contacts Performed Before this Campaign', 0, 50, 5)
    poutcome = st.selectbox('Outcome of the Previous Marketing Campaign', ['failure', 'nonexistent', 'success'])
    emp_var_rate = st.slider('Employment Variation Rate', -4.0, 4.0, -0.5, step=0.1)
    cons_price_idx = st.slider('Consumer Price Index', 92.0, 95.0, 93.0, step=0.1)
    cons_conf_idx = st.slider('Consumer Confidence Index', -52.0, -26.0, -38.0, step=0.1)
    euribor3m = st.slider('3 Month Euribor Rate', 0.0, 5.0, 2.0, step=0.1)
    nr_employed = st.slider('Number of Employees', 4800, 5400, 5000, step=20)
    
    # Return a dictionary of inputs
    return np.array([age, job,marital, education, default, housing, loan, contact, month, day_of_week,
            campaign, pdays, previous, poutcome, emp_var_rate, cons_price_idx, cons_conf_idx, euribor3m, nr_employed],dtype=object).reshape(1,19)



# Define a function to make predictions
def predict_output(inputs):

    # Make a prediction using the pre-trained model
    prediction = model.predict(inputs)
    
    # Return the prediction as a string
    return 'will' if prediction == 1 else 'will not'

# Create a Streamlit app
def main():
    # Set the app title and description
    st.set_page_config(page_title='Bank Marketing Prediction', page_icon=':money_with_wings:',
                       layout='wide', initial_sidebar_state='auto')
    st.title('Bank Marketing Prediction')
    st.write('Please enter the following information to predict whether the customer will subscribe to a term deposit.')
    
    # Get the user inputs
    inputs = get_user_inputs()
    
    # Make a prediction and display the result
    if st.button('Predict'):
        prediction = predict_output(inputs)
        st.write('The customer', prediction, 'subscribe to a term deposit.')


# Run the Streamlit app
if __name__ == '__main__':
    main()




