from flask import Flask, render_template
import plotly.express as px
import pandas as pd


app = Flask(__name__)

#HOME PAGE
@app.route('/')
def home():
    data = {
        "tittle": "Data Visualization Website,  T1",
        "header": "Welcome to My Data Visualization Website, H1",
        "message": "Explore dynamic insights and Visualization here, P1",
        "Visualizations": ["Bar Chart", "Line Chart", "Scatter Plot", "Pie Chart", "List"]
        }
    return render_template('home.html', **data)

#Visualization Page.
@app.route('/Visualization')
def Visualization():
    #sample Data
    df = pd.DataFrame({
        "Catergory": ["A", "B", "C", "D"],
        "Values": [10,20,30,40]
        })

    #create a bar chart using Plotly.
    figure = px.bar(df, x="Catergory", y="Values", title="sample Bar Chart")
    garph_html = figure.to_html(full_html=False)

    return render_template('Visualization.html', title="Visualization", graph=garph_html)


@app.route('/about')
def about():
    return render_template('about.html', title="About - Data Visualization")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact - Data Visualization Website")


if __name__ == "main":
    app.run(debug=True)

