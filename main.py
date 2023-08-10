from fpdf import FPDF
import pandas
pdf = FPDF(orientation="P", unit="mm", format="A4")
dataframe = pandas.read_csv("topics.csv", sep=",")
pdf.set_font(family="Times", style="B", size=16)
pdf.set_text_color(100, 100, 100)
for index, row in dataframe.iterrows():
    for i in range(row["Pages"]):
        pdf.add_page()
        pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
        pdf.line(10, 22, 200, 22)
pdf.output("output.pdf")