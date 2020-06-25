from flask import Flask, render_template, request
from diet import vijay
import json
app = Flask(__name__)

@app.route('/')
def login():
   return render_template('login.html')

@app.route('/success')
def success():
	return render_template('success.html')

@app.route('/datatable')
def datatable():
	return render_template('datatable.html')

@app.route('/search',methods = ['GET','POST'])
def search():
	if(request.method =="GET"):
		print("as")
		return render_template('search.html')
	elif(request.method == 'POST'):
		form = request.form.to_dict()
		data = list(form.values())
		food_entry = data[0]
		quantity = data[1]
		data = vijay(food_entry)
		carb = int(quantity) * int(data[2])
		fat = int(quantity) * int(data[3])
		proteins = int(quantity)*int(data[4])
		print(food_entry,quantity,carb,fat,proteins)
		print(data)
		result = {"FoodName":food_entry.capitalize(),"CarbPerUnit":str(carb),"FatPerUnit":str(fat),"ProteinsPerUnit":str(proteins)}
		print(result)
		print(type(result))
		return render_template("success.html",result = result)

@app.route('/user',methods=['GET','POST'])
def user():
	return render_template('user.html')

@app.route('/charts',methods=['GET','POST'])
def charts():
	return render_template('charts.html')

@app.route('/result',methods = ['GET','POST'])
def result():
   if(request.method == 'POST'):
   	form = request.form.to_dict()
   	data = list(form.values())

   	food_entry = data[0]
   	quantity = data[1]
   	data = vijay(food_entry)
   	carb = int(quantity) * int(data[2])
   	fat = int(quantity) * int(data[3])
   	proteins = int(quantity)*int(data[4])
   	print(food_entry,quantity,carb,fat,proteins)
   	print(data)
   	result = {"FoodName":food_entry.capitalize(),"CarbPerUnit":str(carb),"FatPerUnit":str(fat),"ProteinsPerUnit":str(proteins)}
   	print(result)
   	print(type(result))
   	return render_template("success.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)