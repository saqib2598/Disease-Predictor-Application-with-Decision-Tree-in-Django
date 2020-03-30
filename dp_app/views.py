from django.shortcuts import render,redirect
from django.contrib import messages
import pandas as pd
import joblib

# Create your views here.


def index(request):
    return render(request,'dp_app/index.html')

def acutecholecystitis(request):

    if request.method == 'POST':
        fever = request.POST['fever']
        nausea = request.POST['nausea']
        sweat = request.POST['sweat']
        appetite = request.POST['appetite']
        yellowskin = request.POST['yellowskin']
        abdomin = request.POST['abdomin']

        inputList = [fever,nausea,sweat,appetite,yellowskin,abdomin]
        for i in range(len(inputList)):
            if inputList[i] == 'Yes':
                inputList[i] = 1
            else:
                inputList[i] = 0
        
        dtree = joblib.load('D:\MyProjects\Disease-Predictor-Application\Disease-Classifier-WebApp\dp_project\dp_app\AcuteCholecystitis.pk1')
        result = dtree.predict([inputList])
        
        if result == [0]:
            result = 'Fifty'
            messages.info(request,'There is Fifty Percent Chance That You Maybe Suffering From Acute Cholecystitis.')
            return redirect('dp_app-acute')
        elif result == [1]:
            result = 'Yes'
            messages.info(request,'Yes, You Are Suffering From Acute Cholecystitis')
            return redirect('dp_app-acute')
        elif result == [2]:
            result = 'Seventy-Five'
            messages.info(request,'There is Fifty Percent Chance That You Maybe Suffering From Acute Cholecystitis.')
            return redirect('dp_app-acute')
        elif result == [3]:
            result = 'Thirty'
            messages.info(request,'There is Thirty Percent Chance That You Maybe Suffering From Acute Cholecystitis.')
            return redirect('dp_app-acute')
        elif result == [4]:
            result = 'No'
            messages.info(request,'No, You Are Not Suffering From Acute Cholecystitis.')
            return redirect('dp_app-acute')

    else:
        return render(request,'dp_app/acutecholecystitis.html')

def bronchitis(request):
    if request.method == 'POST':
        sorethroat = request.POST['sorethroat']
        headache = request.POST['headache']
        runnynose = request.POST['runnynose']
        pains = request.POST['pains']
        tired = request.POST['tired']
        

        inputList = [sorethroat,headache,runnynose,pains,tired]
        for i in range(len(inputList)):
            if inputList[i] == 'Yes':
                inputList[i] = 1
            else:
                inputList[i] = 0
        
        dtree = joblib.load('D:\MyProjects\Disease-Predictor-Application\Disease-Classifier-WebApp\dp_project\dp_app\dronchitis.pk1')
        result = dtree.predict([inputList])
        
        if result == [1]:
            result = 'No'
            messages.info(request,'No, You Are Not Suffering From Bronchitis')
            return redirect('dp_app-bronchitis')
        elif result == [2]:
            result = 'Yes'
            messages.info(request,'Yes, You Are Suffering From Bronchitis')
            return redirect('dp_app-bronchitis')
        elif result == [0]:
            result = 'Maybe'
            messages.info(request,'You Maybe Suffering From Bronchitis. Kindly Consult A Doctor.')
            return redirect('dp_app-bronchitis')
        

    else:
        return render(request,'dp_app/bronchitis.html')

def diabetes(request):
    if request.method == 'POST':
        vision = request.POST['vision']
        thirsty = request.POST['thirsty']
        weightloss = request.POST['weightloss']
        wounds = request.POST['wounds']
        tired = request.POST['tired']
        urine = request.POST['urine']

        inputList = [vision,thirsty,weightloss,wounds,tired,urine]
        for i in range(len(inputList)):
            if inputList[i] == 'Yes':
                inputList[i] = 1
            else:
                inputList[i] = 0
        
        dtree = joblib.load('D:\MyProjects\Disease-Predictor-Application\Disease-Classifier-WebApp\dp_project\dp_app\diabetes.pk1')
        result = dtree.predict([inputList])
        
        if result == [0]:
            result = 'Fifty'
            messages.info(request,'There is Fifty Percent Chance That You Maybe Suffering From Diabetes.')
            return redirect('dp_app-diabetes')
        elif result == [1]:
            result = 'Yes'
            messages.info(request,'Yes, You Are Suffering From Acute Cholecystitis')
            return redirect('dp_app-diabetes')
        elif result == [2]:
            result = 'Seventy-Five'
            messages.info(request,'There is Fifty Percent Chance That You Maybe Suffering From Diabetes.')
            return redirect('dp_app-diabetes')
        elif result == [3]:
            result = 'Thirty'
            messages.info(request,'There is Thirty Percent Chance That You Maybe Suffering From Diabetes.')
            return redirect('dp_app-diabetes')
        elif result == [4]:
            result = 'No'
            messages.info(request,'No, You Are Not Suffering From Diabetes.')
            return redirect('dp_app-diabetes')
        
        

    else:
        return render(request,'dp_app/diabetes.html')

def hepatitisC(request):
    if request.method == 'POST':
        flu = request.POST['flu']
        nausea = request.POST['nausea']
        abdomin = request.POST['abdomin']
        appetite = request.POST['appetite']
        sick = request.POST['sick']
       

        inputList = [flu,nausea,abdomin,appetite,sick]
        for i in range(len(inputList)):
            if inputList[i] == 'Yes':
                inputList[i] = 1
            else:
                inputList[i] = 0
        
        dtree = joblib.load('D:\MyProjects\Disease-Predictor-Application\Disease-Classifier-WebApp\dp_project\dp_app\hepatitisC.pk1')
        result = dtree.predict([inputList])
        
        if result == [1]:
            result = 'No'
            messages.info(request,'No, You Are Not Suffering From Hepatits C')
            return redirect('dp_app-hepatitisC')
        elif result == [2]:
            result = 'Yes'
            messages.info(request,'Yes, You Are Suffering From Hepatits C')
            return redirect('dp_app-hepatitisC')
        elif result == [0]:
            result = 'Maybe'
            messages.info(request,'There is a slight Chance You Might Be Suffering From Hepatitis C, Kindly Consult A Doctor.')
            return redirect('dp_app-hepatitisC')
        
        

    else:
        return render(request,'dp_app/hepatitisC.html')