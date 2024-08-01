from fpdf import FPDF


def main():
    all_pdf(input("username here: "))


def all_pdf(s):
    pdf = FPDF()
    pdf.add_page()

    pdf.image("shirtificate.png", 5, 70, 190)

    pdf.set_font("Helvetica", "B", 40)
    pdf.set_xy(0, 20)
    pdf.cell(0, 10, "CS50 Shirtificate", 0, 1, 'C')

    pdf.set_text_color(255, 255, 255)

    pdf.set_font("Helvetica", "B", 24)
    pdf.set_xy(0, 130)
    pdf.cell(0, 10, f"{s} took CS50", 0, 1, 'C')

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
