import csv

male_path = "unemployment_male.csv"
female_path = "unemployment_female.csv"

#module of reading .csv files
def read_csv(path): 
    f = open(path, "r")
    content = []
    reader = csv.reader(f)
    for row in reader:
        content.append(row)
    f.close()
    return content

unemploy_male = read_csv(male_path)
unemploy_female = read_csv(female_path)

print unemploy_male[:2]
print unemploy_female[:2]
#[['Country Name', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014'], ['Afghanistan', '15.80000019', '15.80000019', '16', '15.69999981', '15.69999981', '15.60000038', '15.69999981', '15.80000019', '15.60000038', '15.69999981', '16.20000076', '15.89999962', '15.19999981', '16.5', '19', '20.10000038', '18.79999924', '20.29999924', '17.70000076', '19.60000038', '19.89999962', '18.70000076', '19.79999924', '19.29999924']]
#[['Country Name', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014'], ['Afghanistan', '30.89999962', '30.89999962', '31.20000076', '30.70000076', '30.79999924', '30.60000038', '30.79999924', '30.89999962', '30.60000038', '30.79999924', '31.39999962', '31', '30.10000038', '31.79999924', '24.79999924', '26.20000076', '24.5', '26.60000038', '23', '25.60000038', '26', '24.39999962', '27.5', '28.10000038']]


from matplotlib import pyplot as plt
from matplotlib import cm
import numpy as np

#class to operate unemployment of youth dataset
class Youth:
    
    def __init__(self, dataset):
        self.dataset = dataset
    
    def gen_by_country(self, country):
        
        for row in self.dataset:
            if row[0] == country:
                return row
        
        print "no such country"
        return 

     def gen_by_time(self, time):
        
        for i in range(len(self.dataset[0])):
            if self.dataset[0][i] == str(time):
                posi_of_time = i
        
        content = []
        
        try: 
            for row in self.dataset[1:]:
                content.append(row[posi_of_time])
        except:
            print "no such time"
            return
        
        return content
    
    def plot_by_country(self, country, gender):
        
        content = self.gen_by_country(country)  #find data of given country 
        if content == None:
            pass
        else:
            time = map(lambda x:int(x), self.dataset[0][1:])    #get all years 
            content = map(lambda x:float(x), content[1:])   #get the unemployment data
            plt.plot(time, content)
            plt.title(gender)
            plt.show()
    
    def plot_by_time(self, time, countries):

        content = self.gen_by_time(time)    #find data of given time

        if content == None:
            pass
        else:
            countries_ = [row[0] for row in self.dataset[1:]]   #get all countries
            posi_of_country = []
            for i in range(len(countries_)):    #find given countries
                if countries_[i] in countries:
                    posi_of_country.append(i)

            content_ = [content[i] for i in posi_of_country]    #get data of given countries 
            content = map(lambda x:float(x), content_)


            ind = np.arange(1, len(content)+1)  #array([1, 2, 3])
            width = 0.35

            N = len(content)    #number of countries
            for i in range(N):
                    plt.bar(ind[i],content[i],width, color=cm.jet(1.*i/N))

            plt.title(str(time))
            plt.xticks(ind + width/2., countries)
            plt.show()

#find data by country   
un_male_youth = Youth(unemploy_male)
china_un_male = un_male_youth.gen_by_country("China")
print china_un_male
#['China', '10.60000038', '9.600000381', '9.600000381', '9.800000191', '10.39999962', '10.60000038', '10.80000019', '11.19999981', '11.19999981', '10.89999962', '11', '10.69999981', '10.39999962', '10.39999962', '10.10000038', '9.699999809', '9.199999809', '10.60000038', '10.80000019', '10.39999962', '10.80000019', '11.30000019', '11.69999981', '12.10000038']

#find data by time(year)
un_male_2014 = un_male_youth.gen_by_time(2014)
print un_male_2014
#['19.29999924', '9.899999619', '32', '24.26637287', '8', '18.79999924', '31.29999924', '14', '9.100000381', '13.10000038', '9.699999809', '24.10000038', '1.5', '6', '8.899999619', '25.89999962', '8.5', '26.29999924', '56.90000153', '11.39999962', '13.39999962', '4.300000191', '12.30000019', '24.29999924', '10.39999962', '9.399999619', '28.5', '11.5', '14.69999981', '23.6948604', '9.100000381', '14.5', '12.10000038', '6.400000095', '5.599999905', '10', '14.60000038', '10.10000038', '14.39999962', '16.29999924', '19.62784699', '6.699999809', '35.79999924', '15.5', '8.100000381', '13.39999962', '21.79999924', '17.60000038', '12.56559795', '13.12669506', '12.35917536', '16.68935534', '20.73830914', '8.199999809', '32.70000076', '27.65154727', '10.19999981', '57.79999924', '20.10000038', '4.599999905', '25.35607193', '14.17014602', '20.70000076', '15.10000038', '25.10000038', '30.89999962', '18.60000038', '33.20000076', '3.200000048', '2.400000095', '9.899999619', '10.5', '11.89999962', '49.29999924', '5.300000191', '20.10000038', '18.07536944', '10.10000038', '5.400000095', '9.917640225', '45.5', '14.5', '20.29999924', '14.00767488', '12.89323975', '10.18000273', '10.07112519', '21.29999924', '10.24000064', '10.19999981', '27.29999924', '26.10000038', '30.79999924', '13.60000038', '10.5', '43', '23.89999962', '24', '7.400000095', '3.099999905', '16.89999962', '13.10000038', '0.800000012', '11.80000019', '22.5', '11.68278637', '4.300000191', '18.70000076', '3.5', '38.70000076', '11.87434955', '10.18703118', '9.317642746', '15.69999981', '12.53171101', '12.84228685', '27.5', '12.4098049', '22.39999962', '18.10000038', '19', '2.700000048', '20.60000038', '9.100000381', '4.599999905', '19.10000038', '25.18894297', '9.300000191', '13.28849054', '51', '7.900000095', '14.5', '8.300000191', '26.52734542', '39.59999847', '8.899999619', '41.59999847', '48.90000153', '16', '12.60000038', '6.099999905', '15.06229885', '34.79999924', '7.800000191', '14', '6.5', '10.30000019', '9.399999619', '4.800000191', '13.60000038', '16.74783126', '16.39999962', '19.94326725', '7.599999905', '9.100000381', '8.899999619', '15.19999981', '4.699999809', '23', '13.21220179', '30.20000076', '12.5', '37', '7.599999905', '17.9327869', '0.5', '25', '12.30000019', '0.899999976', '9.927237969', '22.20000076', '17.79999924', '9.300000191', '7.5', '8.5', '7', '11.69999981', '10.10000038', '45', '13.20948355', '13.20948355', '19.57816481', '14.5', '29.70000076', '20.20000076', '24.39999962', '40.09999847', '23.29999924', '10', '12.56643387', '17.38332447', '10', '3.299999952', '17.20000076', '19.29999924', '11.84118759', '26.35148964', '10.60000038', '9.927237969', '13.20948355', '8.800000191', '32.70000076', '16.60000038', '4.400000095', '6.199999809', '17.89999962', '14.31872389', '16', '15.10000038', '19.29999924', '14.80000019', '5.699999809', '38.5', '13.46571406', '20.29999924', '48.79999924', '10.30000019', '27', '9.5']

#plot bar graph of given time and countries
un_male_youth.plot_by_time(2014, ["China", "Australia", 'Euro area'])

#plot chinese female unemployment
un_female_youth = Youth(unemploy_female)
un_female_youth.plot_by_country("China", "female")