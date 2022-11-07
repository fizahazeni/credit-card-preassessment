#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, jsonify, render_template
import joblib


# In[2]:


app = Flask(__name__)


# In[3]:


#Values

#Variable 6: Gender
female = 0
male = 0

#Variable 7: FlagOwnCar
flagowncar_Y = 0
flagowncar_N = 0

#Variable 8:
realty_N=0
realty_Y=1

#Variable 9: Income
commercialassociate = 0
pensioner = 0
stateservant = 0
working = 0

#Variable 10: Education
academicdegree = 0
highereducation = 0
incompletehigher = 0
lowersecondary = 0
secondaryspecial = 0

#Variable 11:
married = 0
single = 0
separated = 0
widow = 0

#Variable 12: HousingType
coopapartment = 0
houseapartment = 0
municipalapartment = 0
officeapartment = 0
rentedapartment = 0
withparents = 0

#Variable 13:
accountants = 0
cleaningstaff = 0
cookingstaff = 0
corestaff = 0
drivers = 0
hrstaff = 0
highskilltechstaff = 0
itstaff = 0
laborers = 0
lowskilllaborers = 0
managers = 0
medicinestaff = 0
nooccupation = 0
privateservicestaff = 0
realtyagents = 0
salesstaff = 0
secretaries = 0
securitystaff = 0
waitersbarmanstaff = 0

#Final Predict
newvalue = 0

variables_int=[]


# In[4]:


@app.route('/')
def abc():
    return render_template("index.html")

@app.route('/', methods=['POST'])

def index():
    #Variable 1: Number of Children
    children = int(request.form.get("cnt_children"))

    #Variable 2: Annual Income Amount
    amtincometotal = int(request.form.get('amtincometotal'))
  
    #Variable 3: Age
    age = int(request.form.get('age'))
  
    #Variable 4: Years Employed
    yearsemployed = int(request.form.get('yearsemployed'))

    #Variable 5: Family Members
    family = int(request.form.get('family'))

    #Variable 6: Gender
    gender = request.form.get('gender')
    global female, male
    if gender == "Female":
        female = 1
    elif gender == "Male":
        male = 1
    
    #Variable 7: FlagOwnCar
    flagowncar = request.form.get("flagowncar")
    global flagowncar_Y,flagowncar_N  
    if flagowncar == "Yes":
        flagowncar_Y = 1
    elif flagowncar == "No":
        flagowncar_N = 1
    
    #Variable 8: Realty
    realty = request.form.get('realty')
    global realty_N, realty_Y
    if realty == "No":
        realty_N = 1
    elif realty == "Yes":
        realty_Y = 1
      
    #Variable 9: Income
    income = request.form.get('income')
    global commercialassociate, pensioner, stateservant, working
    if income == "Commercial associate":
        commercialassociate = 1
    if income == "Pensioner":
        pensioner = 1
    if income == "State servant":
        stateservant = 1
    if income == "Working":
        working = 1

    #Variable 10: Education
    education = request.form.get('education')
    global academicdegree, highereducation, incompletehigher, lowersecondary, secondaryspecial
    if education == "Academic Degree":
        academicdegree = 1
    if education == "Higher education":
        highereducation = 1
    if education == "Incomplete higher":
        incompletehigher = 1
    if education == "Lower secondary":
        lowersecondary = 1
    if education == "Secondary / secondary special":
        secondaryspecial = 1
    
    #Variable 11: Family Status
    family = request.form.get('family')
    global married, single, separated, widow
    if family == "Married":
        married = 1
    if family == "Single / not married":
        single = 1
    if family == "Separated":
        separated = 1
    if family == "Widow":
        widow = 1

    #Variable 12: Housing Type
    housing = request.form.get('housingtype')
    global coopapartment, houseapartment, municipalapartment,officeapartment,rentedapartment, withparents

    if housing == "Co-op Apartment":
        coopapartment = 1
    if housing == "House/Apartment":
        houseapartment = 1
    if housing == "Municipal Apartment":
        municipalapartment = 1
    if housing == "Office Apartment":
        officeapartment = 1
    if housing == "Rented Apartment":
        rentedapartment = 1
    if housing == "With Parents":
        withparents = 1
    
    #Variable 13: Occupancy Type
    occupancy = request.form.get('occupancy')
    global accountants, cleaningstaff, cookingstaff, corestaff, drivers, hrstaff, highskilltechstaff, itstaff, laborers, lowskilllaborers, managers, medicinestaff, nooccupation, privateservicestaff, realtyagents, salesstaff, secretaries, securitystaff, waitersbarmanstaff
    if occupancy == "Accountants":
        accountants = 1
    if occupancy == "Cleaning Staff":
        cleaningstaff = 1
    if occupancy == "Cooking Staff":
        cookingstaff = 1
    if occupancy == "Core Staff":
        corestaff = 1
    if occupancy == "Drivers":
        drivers = 1
    if occupancy == "HR Staff":
        hrstaff = 1
    if occupancy == "High Skill Tech Staff":
        highskilltechstaff = 1
    if occupancy == "IT Staff":
        itstaff = 1
    if occupancy == "Laborers":
        laborers = 1
    if occupancy == "Low Skill Laborers":
        lowskilllaborers = 1
    if occupancy == "Managers":
        managers = 1
    if occupancy == "Medicine Staff":
        medicinestaff = 1
    if occupancy == "No Occupation":
        nooccupation = 1
    if occupancy == "Private Service Staff":
        privateservicestaff = 1
    if occupancy == "Realty Agents":
        realtyagents = 1
    if occupancy == "Sales Staff":
        salesstaff = 1
    if occupancy == "Secretaries":
        secretaries = 1    
    if occupancy == "Security Staff":
        securitystaff = 1
    if occupancy == "Waiters/Barman Staff":
        waitersbarmanstaff = 1
        
    #Final Model Run
    model1 = joblib.load("creditcard_model")
    #Array of variables
    
    variables=[children,amtincometotal,age,yearsemployed,family,female,male,flagowncar_N,flagowncar_Y, realty_N, realty_Y,commercialassociate, pensioner, stateservant, working,academicdegree, highereducation, incompletehigher, lowersecondary, secondaryspecial,married,separated,single,widow,coopapartment,houseapartment, municipalapartment,officeapartment,rentedapartment, withparents, accountants, cleaningstaff, cookingstaff, corestaff, drivers, hrstaff, highskilltechstaff, itstaff, laborers,lowskilllaborers, managers, medicinestaff, nooccupation, privateservicestaff, realtyagents, salesstaff,secretaries, securitystaff, waitersbarmanstaff]
    
    for i in variables:
        variables_int.append(int(i))
        
    r1 = model1.predict([variables_int])
    
    #Indicator
    if r1 == 0:
        newvalue = "Rejected. Please contact the bank for more enquiries."
    elif r1 ==1:
        newvalue = "Approved. Congratulations."
    return(render_template("index.html",result1=newvalue))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:


#@app.route("/")
#def Home():
#  return render_template("index.html")


# In[ ]:


#@app.route("/predict",methods =["POST"])
#def predict():
#    float_features = [float(x) for x in request.form.values()]
#    features = [np.array(float_features)]
#    prediction = model.predict(features)

#    return render_template("index.html", prediction_text = "The customer is".format(prediction))

#if __name__ == "__main__":
#  app.run(debug = True)


# how to input the categorical variables 

