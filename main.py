from fpdf import FPDF
import pandas
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
dataframe = pandas.read_csv("topics.csv", sep=",")

for index, row in dataframe.iterrows():
    for i in range(row["Pages"]):
        pdf.add_page()
        pdf.set_font(family="Times", style="B", size=16)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
        for j in range(22,282,10):
            pdf.line(10, j, 200, j)
        pdf.ln(260)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180,180,180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
pdf.output("output.pdf")