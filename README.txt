This is a code which can be used for analysis of data which was collected from the patients while being admited to the hospital with a heart attack. Data was collected by
UCI and combined from four different institutions from their data from 1986. This code looks into linear models and linear regression present between data set and creates
two different models which can help in assessment of general health before heart attack and patient's lifestyle.

        1. Download the script of your choice (.py or .ipynb) and the data set ("heart.csv") into single directory.
        
        2. Change the location of the .csv file in the code acordingly to where it is placed on your computer.
        
        3. Run the program. The script should provide:
        
            a) table including mean, median, standard deviation, minimum and maximum value for each column
            b) correlation values as: correlation coefficent, heat map and scatter matrix
            c) correlation between age and resting blood pressure as a scatter plot with distinction between type of chest pain felt by the patient during arrival at the 
            hospital (shape) and number of blockeed blood vesels on the fluoroscopy (colour); two graphs for each of the sexes
            d) linear models of correlation between age and resting blood pressure in different types of chest pains (numbers 0 to 3); 4 graphs for each of the sexes registered
            e) linear models between age and resting blod pressure divided into different types of chest pain, number of blocked arteries and sex (20 graphs)
            f) histograms of cholesterol and resting blood pressure levels based on the sex (2 histograms)
            g) linear regression model of the dependency of resting blood pressure based on age, with training and test data
            h) linear regression model of the dependency between cholesterol levels in plasma and resting heart rate, with training and test data
                    In regression models there is a possibility to change the number of values, which would be randomly chosen to train and test the model. It was set up for value 
                    '46' which is 15% of the data set.
                    
         4. If different data set used, make sure they maintain the same names or adjust them accordingly. Additionally, change the number of values used for training the data set for the regression model.           

Legend of the values used in the code:
    - age*: in years
    - sex*: 0 - female, 1 - male
    - cp*: type of chest pain when admited to hospital:
            -- Value 1: typical angina
            -- Value 2: atypical angina
            -- Value 3: non-anginal pain
            -- Value 4: asymptomatic
    - trestbps*: esting blood pressure (in mm Hg on admission to the hospital)
    - chol*: serum cholestoral in mg/dl
    - fbs: if fasting blood sugar > 120 mg/dl (1 = true; 0 = false)
    - restecg: resting electrocardiographic results
            -- Value 0: normal
            -- Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
            -- Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria
    - thalach: maximum heart rate achieved
    - exang: exercise induced angina (1 = yes; 0 = no)
    - oldpeak: ST depression induced by exercise relative to rest
    - slope: the slope of the peak exercise ST segment
            -- Value 1: upsloping
            -- Value 2: flat
            -- Value 3: downsloping
    - ca*: number of major vessels (0-4) colored by flourosopy
    - thal: 3 = normal; 6 = fixed defect; 7 = reversable defec
    - target: the predicted attribute
    
    *values used in the analysis