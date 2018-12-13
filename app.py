import requests, json
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/study_image', methods = ['POST'])
def study_image():
    
	image_url = request.form['url-input']
    # At this point you have the image_url value from the front end
    # Your job now is to send this information to the Clarifai API
    # and read the result, make sure that you read and understand the
    # example we covered in the slides! 

    # YOUR CODE HERE!

	# you can use the headers to pass in hidden info, here we are sending a secret Key (think of it as a password)
	headers = {'Authorization': 'Key f2f339a3cc374420a221fa27e58a3202'}

	# this is the url of where your request will go
	api_url = "https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs"

	# this is content of the message(data) you are sending to clarifai
	data ={"inputs": [{"data": {"image": {"url": image_url}}}]}

	# putting everything together; sending the request!
	response = requests.post(api_url, headers=headers, data=json.dumps(data))
	response_dict = json.loads(response.content)
	works = response_dict["outputs"][0]["data"]["concepts"]
	for i in works:
		if "man" in i.values() or "woman" in i.values() or "people" in i.values():
			return render_template('human.html')
	#trying = json.loads(trying)
	return render_template('display_response.html', answers=works, link = image_url)

if __name__ == '__main__':
	app.run(debug=True)