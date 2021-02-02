from fpdf import FPDF


def createAliceCV(dictOfInformation):
    pdf = FPDF(format="A3")
    pdf.add_page()
    pdf.set_font("Arial", "B", 30)
    pdf.set_margins(left=5, top=10, right=1)
    pdf.set_fill_color(r=200, g=200, b=200)
    pdf.set_draw_color(r=200, g=200, b=200)
    pdf.rect(x=0, y=0, w=100, h=2000, style="DF")
    pdf.image(
        "./templates/AliceCV/pictures/picture.jpeg",
        x=0,
        y=0,
        w=70,
        h=80,
        type="JPEG",
        link="",
    )
    pdf.set_xy(x=5, y=80)
    pdf.set_text_color(r=70, g=100, b=200)
    pdf.multi_cell(w=60, h=10, txt="\nAli\nGholamian\ngholamian", border=0, align="L")
    # ----------------------------------------------
    pdf.ln()
    pdf.image(
        "./templates/icons/birth-date.png",
        x=pdf.get_x(),
        y=pdf.get_y(),
        w=10,
        h=10,
        type="PNG",
        link="",
    )
    pdf.set_text_color(r=0, g=0, b=0)
    pdf.set_font_size(size=17)
    pdf.set_xy(x=17, y=pdf.get_y() + 1)
    pdf.cell(w=60, h=10, txt="26 November 1996", border=0, align="L")
    # -------------------------------------------------
    pdf.ln()
    pdf.image(
        "./templates/icons/email.png",
        x=pdf.get_x(),
        y=pdf.get_y(),
        w=10,
        h=10,
        type="PNG",
        link="https://mail.google.com/mail/?view=cm&fs=1&to=alisepehr88@gmail.com&su=&body=",
    )
    pdf.set_text_color(r=0, g=0, b=0)
    pdf.set_font_size(size=17)
    pdf.set_xy(x=17, y=pdf.get_y())
    pdf.cell(
        w=60,
        h=10,
        txt="alisepehr88@gmail.com",
        border=0,
        align="L",
        link="https://mail.google.com/mail/?view=cm&fs=1&to=alisepehr88@gmail.com&su=&body=",
    )
    # -------------------------------------------------
    # -------------------------------------------------
    pdf.ln()
    pdf.image(
        "./templates/icons/phone.png",
        x=pdf.get_x(),
        y=pdf.get_y(),
        w=10,
        h=10,
        type="PNG",
        link="",
    )
    pdf.set_text_color(r=0, g=0, b=0)
    pdf.set_font_size(size=17)
    pdf.set_xy(x=17, y=pdf.get_y())
    pdf.cell(
        w=60, h=10, txt="09352117722", border=0, align="L", link="",
    )
    # -------------------------------------------------
    # -------------------------------------------------
    pdf.ln()
    pdf.image(
        "./templates/icons/github.png",
        x=pdf.get_x(),
        y=pdf.get_y(),
        w=10,
        h=10,
        type="PNG",
        link="https://github.com/AliGholamian-dev",
    )
    pdf.set_text_color(r=0, g=0, b=0)
    pdf.set_font_size(size=17)
    pdf.set_xy(x=17, y=pdf.get_y())
    pdf.cell(
        w=60,
        h=10,
        txt="AliGholamian-Dev",
        border=0,
        align="L",
        link="https://github.com/AliGholamian-dev",
    )
    # -------------------------------------------------
    pdf.ln()
    pdf.ln()
    pdf.set_draw_color(r=70, g=100, b=200)
    pdf.set_line_width(width=1)
    pdf.line(50, pdf.get_y() + 5, 95, pdf.get_y() + 5)
    pdf.set_text_color(r=200, g=100, b=70)
    pdf.set_font_size(size=25)
    pdf.cell(w=60, h=10, txt="About Me", border=0, align="L")
    pdf.ln()
    pdf.set_text_color(r=0, g=0, b=0)
    pdf.set_font_size(size=15)
    pdf.multi_cell(
        w=90,
        h=10,
        txt="jdnjksafskjfklfjkdijdlflekfrklfjdkljfkjfdkljfljfdlkfljlfjfldjf\nakfjalfhlhf\nakhfkdjf\nskjfhdkshf",
        border=0,
        align="L",
    )
    pdf.ln()
    pdf.set_line_width(width=1)
    pdf.line(35, pdf.get_y() + 5, 95, pdf.get_y() + 5)
    pdf.set_text_color(r=200, g=100, b=70)
    pdf.set_font_size(size=25)
    pdf.cell(w=60, h=10, txt="Skills", border=0, align="L")
    pdf.set_text_color(r=0, g=0, b=0)
    # for in skills
    pdf.ln()
    pdf.set_font_size(size=15)
    pdf.cell(w=60, h=10, txt="Java", border=0, align="L")
    pdf.ln()
    pdf.set_draw_color(r=150, g=150, b=150)
    pdf.set_fill_color(r=150, g=150, b=150)
    pdf.rect(x=pdf.get_x(), y=pdf.get_y(), w=90, h=10, style="DF")
    pdf.set_draw_color(r=10, g=100, b=200)
    pdf.set_fill_color(r=10, g=100, b=200)
    pdf.rect(x=pdf.get_x(), y=pdf.get_y(), w=0.6 * 90, h=10, style="DF")

    pdf.set_xy(x=110, y=10)
    pdf.set_fill_color(r=175, g=175, b=175)
    pdf.set_draw_color(r=175, g=175, b=175)
    pdf.rect(x=110, y=10, w=55, h=15, style="DF")
    pdf.set_text_color(r=255, g=255, b=255)
    pdf.set_xy(x=110, y=13)
    pdf.set_font_size(size=35)
    pdf.cell(w=60, h=10, txt="Interests", border=0, align="L")
    pdf.ln()
    pdf.ln()
    pdf.set_text_color(r=0, g=0, b=0)
    pdf.set_x(110)
    pdf.set_font_size(size=18)
    pdf.multi_cell(
        w=175,
        h=10,
        txt="jdnjksafskjffksjklfjksjfksjfkdljflkfjslfjsdfksldfjskdljflksjfsldkfsfkl\nakfjalfhlhf\nakhfkdjf\nskjfhdkshf",
        border=0,
        align="L",
    )

    pdf.ln()
    pdf.set_fill_color(r=10, g=100, b=200)
    pdf.set_draw_color(r=10, g=100, b=200)
    pdf.rect(x=110, y=pdf.get_y(), w=65, h=15, style="DF")
    pdf.set_text_color(r=255, g=255, b=255)
    pdf.set_xy(x=110, y=pdf.get_y() + 3)
    pdf.set_font_size(size=35)
    pdf.cell(w=60, h=10, txt="Education", border=0, align="L")
    pdf.ln()

    pdf.set_x(110)
    pdf.set_font_size(size=18)
    # for in education
    pdf.ln()
    pdf.set_x(110)
    pdf.set_text_color(r=100, g=200, b=100)
    pdf.cell(
        w=5, h=10, txt="1998-2015", border=0, align="L",
    )
    pdf.set_x(150)
    pdf.set_text_color(r=100, g=100, b=100)
    pdf.multi_cell(
        w=135,
        h=10,
        txt="phd from Ajknkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkmirkabir",
        border=0,
        align="L",
    )
    # ----------------------------------------------------

    pdf.ln()
    pdf.set_fill_color(r=175, g=175, b=175)
    pdf.set_draw_color(r=175, g=175, b=175)
    pdf.rect(x=110, y=pdf.get_y(), w=50, h=15, style="DF")
    pdf.set_text_color(r=255, g=255, b=255)
    pdf.set_xy(x=110, y=pdf.get_y() + 3)
    pdf.set_font_size(size=35)
    pdf.cell(w=60, h=10, txt="Awards", border=0, align="L")
    pdf.ln()

    pdf.set_x(110)
    pdf.set_font_size(size=18)
    # for in Awards
    pdf.ln()
    pdf.set_x(110)
    pdf.set_text_color(r=100, g=200, b=100)
    pdf.cell(
        w=5, h=10, txt="1998-2015", border=0, align="L",
    )
    pdf.set_x(150)
    pdf.set_text_color(r=100, g=100, b=100)
    pdf.multi_cell(
        w=135, h=10, txt="Winner", border=0, align="L",
    )
    # ----------------------------------------------------------
    pdf.ln()
    pdf.set_fill_color(r=10, g=100, b=200)
    pdf.set_draw_color(r=10, g=100, b=200)
    pdf.rect(x=110, y=pdf.get_y(), w=70, h=15, style="DF")
    pdf.set_text_color(r=255, g=255, b=255)
    pdf.set_xy(x=110, y=pdf.get_y() + 3)
    pdf.set_font_size(size=35)
    pdf.cell(w=60, h=10, txt="Experience", border=0, align="L")
    pdf.ln()

    pdf.set_x(110)
    pdf.set_font_size(size=18)
    # for in Awards
    pdf.ln()
    pdf.set_x(110)
    pdf.set_text_color(r=100, g=200, b=100)
    pdf.cell(
        w=5, h=10, txt="1998-2015", border=0, align="L",
    )
    pdf.set_x(150)
    pdf.set_text_color(r=100, g=100, b=100)
    pdf.multi_cell(
        w=135, h=10, txt="Teaching Robotics", border=0, align="L",
    )

    pdf.add_page()
    pdf.set_fill_color(r=200, g=200, b=200)
    pdf.set_draw_color(r=200, g=200, b=200)
    pdf.rect(x=0, y=0, w=10000, h=40, style="DF")
    pdf.set_text_color(r=255, g=255, b=255)
    pdf.set_xy(x=10, y=15)
    pdf.set_font_size(size=45)
    pdf.cell(w=0, h=10, txt="Github Repositories", border=0, align="C")
    pdf.image(
        "./templates/icons/github-big.png",
        x=0,
        y=0,
        w=40,
        h=40,
        type="PNG",
        link="https://github.com/AliGholamian-dev",
    )
    pdf.ln()
    pdf.ln()
    pdf.ln()
    pdf.ln()

    # ------------------------------------------------------------------
    # for in Repos
    pdf.set_font_size(size=30)
    pdf.set_text_color(r=10, g=100, b=200)
    pdf.set_x(x=10)
    pdf.cell(
        w=285,
        h=10,
        txt=f"{1} - first repo",
        border=0,
        align="L",
        link="https://github.com/AliGholamian-dev/AP_Midterm_Project",
    )
    pdf.ln()
    pdf.set_font_size(size=15)
    pdf.set_text_color(r=0, g=0, b=0)
    pdf.set_x(x=20)
    pdf.multi_cell(
        w=275,
        h=10,
        txt="gjhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg",
        border=0,
        align="L",
    )

    pdf.ln()
    pdf.set_font_size(size=25)
    pdf.set_text_color(r=150, g=0, b=100)
    pdf.set_x(x=20)
    pdf.cell(
        w=50, h=10, txt="Language: ", border=0, align="L",
    )
    pdf.set_text_color(r=0, g=200, b=10)
    pdf.cell(
        w=275, h=10, txt="C++", border=0, align="L",
    )
    # pdf.image(
    #     "https://github.com/AliGholamian-dev/AP_Midterm_Project/blob/master/readme.md",
    #     x=0,
    #     y=0,
    #     w=40,
    #     h=40,
    #     type="PNG",
    #     link="https://github.com/AliGholamian-dev/AP_Midterm_Project/blob/master/readme.md",
    # )

    pdf.output("Resume.pdf")

