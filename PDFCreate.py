import asyncio


async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )

    stdout, stderr = await proc.communicate()

    print(f"[{cmd!r} exited with {proc.returncode}]")
    if stdout:
        print(f"[stdout]\n{stdout.decode()}")
    if stderr:
        print(f"[stderr]\n{stderr.decode()}")


class CreatePDF:
    def __init__(self, dictOfInformation):
        self.dictOfInformation = dictOfInformation

    def update_template_context(self):
        # input file
        fin = open(
            f"./templates/{self.dictOfInformation['Template']}/template.tex", "rt"
        )
        # output file to write the result to
        fout = open(
            f"./templates/{self.dictOfInformation['Template']}/template_new.tex", "wt",
        )
        # for each line in the input file
        temptext = str(fin.read())
        fin.close()
        # read replace the string and write to output file
        temptext = temptext.replace("rname", self.dictOfInformation["Name"])
        temptext = temptext.replace("raddress", self.dictOfInformation["Address"])
        temptext = temptext.replace("rrphone", self.dictOfInformation["Phone"])
        temptext = temptext.replace("rgit", self.dictOfInformation["Git"])
        temptext = temptext.replace("rlinkedin", self.dictOfInformation["Linkedin"])
        temptext = temptext.replace("rsite", self.dictOfInformation["Site"])
        temptext = temptext.replace("rmail", self.dictOfInformation["Mail"])
        temptext = temptext.replace("raboutme", self.dictOfInformation["Aboutme"])
        temptext = temptext.replace("rotherinfo", self.dictOfInformation["Info"])

        if self.dictOfInformation["Template"] == "AliceCV":
            temptext = temptext.replace("rpic", self.dictOfInformation["Picture"])
            temptext = temptext.replace("rtitle", self.dictOfInformation["Title"])
            txt = ""
            for skills_set in self.dictOfInformation["Skills"]:
                txt += "{" + skills_set[0] + "/" + str(skills_set[1]) + "},"
            temptext = temptext.replace("rskills", txt[: len(txt) - 1])
            temptext = temptext.replace(
                "rinterests", self.dictOfInformation["Interests"]
            )
            txt = ""
            for ed_set in self.dictOfInformation["Education"]:
                txt += (
                    "\\twentyitem{"
                    + ed_set[0]
                    + "-"
                    + ed_set[1]
                    + "}{"
                    + ed_set[2]
                    + "}{"
                    + ed_set[3]
                    + "}{"
                    + ed_set[4]
                    + "}\n\t"
                )
            temptext = temptext.replace("reducation", txt[: len(txt) - 2])
            txt = ""
            for award_set in self.dictOfInformation["Awards"]:
                txt += (
                    "\\twentyitemshort{" + award_set[0] + "}{" + award_set[1] + "}\n\t"
                )
            temptext = temptext.replace("rawards", txt[: len(txt) - 2])

            txt = ""
            for ex_set in self.dictOfInformation["Experience"]:
                txt += (
                    "\\twentyitem{"
                    + ex_set[0]
                    + "}{"
                    + ex_set[1]
                    + "}{"
                    + ex_set[2]
                    + "}{"
                    + ex_set[3]
                    + "}\n\t"
                )
            temptext = temptext.replace("rexperience", txt[: len(txt) - 2])

        elif self.dictOfInformation["Template"] == "DeveloperCV":
            temptext = temptext.replace("rlastname", self.dictOfInformation["LastName"])
            txt = ""
            for skills_set in self.dictOfInformation["Skills"]:
                txt += (
                    "\t\t\\baritem{" + skills_set[0] + "}{" + str(skills_set[1]) + "}\n"
                )
            temptext = temptext.replace("rskills", txt[: len(txt) - 1])
            temptext = temptext.replace(
                "rinterests", self.dictOfInformation["Interests"]
            )
            txt = ""
            for ed_set in self.dictOfInformation["Education"]:
                txt += (
                    "\t \\entry\n\t\t   {"
                    + ed_set[0]
                    + "}\n\t\t   {"
                    + ed_set[1]
                    + "}\n\t\t   {"
                    + ed_set[2]
                    + "}\n\t\t   {"
                    + ed_set[3]
                    + "}\n"
                )
            temptext = temptext.replace("reducation", txt[: len(txt) - 1])
            txt = ""
            for award_set in self.dictOfInformation["Awards"]:
                txt += (
                    "\t \\entry\n\t\t   {"
                    + award_set[0]
                    + "}\n\t\t   {"
                    + award_set[1]
                    + "}\n\t\t{ }\n\t\t{ }\n"
                )
            temptext = temptext.replace("rawards", txt[: len(txt) - 1])

            txt = ""
            for ex_set in self.dictOfInformation["Experience"]:
                txt += (
                    "\t \\entry\n\t\t   {"
                    + ex_set[0]
                    + "}\n\t\t   {"
                    + ex_set[1]
                    + "}\n\t\t   {"
                    + ex_set[2]
                    + "}\n\t\t   {"
                    + ex_set[3]
                    + "}\n"
                )
            temptext = temptext.replace("rexperience", txt[: len(txt) - 1])

        fout.write(temptext)
        # close input and output files

        fout.close()

    def makeCV(self):
        asyncio.run(run("initexmf --enable-installer --mkmaps"))
        asyncio.run(run("initexmf --enable-installer --update-fndb"))
        asyncio.run(
            run(
                f"pdflatex --enable-installer -interaction=nonstopmode -aux-directory=./templates/Tempfiles -include-directory=./templates/{self.dictOfInformation['Template']} -job-name={self.dictOfInformation['nameOfFile']} -output-directory=./Output ./templates/{self.dictOfInformation['Template']}/template_new.tex"
            )
        )


_dict = {
    "Template": "DeveloperCV",
    "nameOfFile": "Ali",
    "Picture": "ali.jpeg",
    "Name": "Ali",
    "LastName": "Gholamian",
    "Title": "Developer",
    "Address": "ksjdfdkj",
    "Phone": "sdjhfdj",
    "Git": "sdjfhdjkf",
    "Linkedin": "sdjkfkjdf",
    "Site": "sdjkfhdjkhf",
    "Mail": "dsklfjldf",
    "Aboutme": "sdjkfhnsjfhdshfkdjfhfhjsfjks",
    "Skills": [["JAVA", 60], ["C++", 100]],
    "Interests": "sdfjdfjslfjs\n\n\nsjkdhdjkshf\n\n\n\ndshgfdhsfg",
    "Education": [
        ["1865", "2020", "asd", "University", "Degree"],
        ["1865", "2020", "adsad", "University", "Degree"],
    ],
    "Awards": [["1865", "a"], ["1865", "b"],],
    "Experience": [
        [
            "1865",
            "Alice in Wonderland-The Circra (1900's) Silent Film.",
            "Film",
            "The first Alice on film was over a hundred years ago.",
        ],
        [
            "1865",
            "Alice in Wonderland-The Circra (1900's) Silent Film.",
            "Film",
            "The first Alice on film was over a hundred years ago.",
        ],
    ],
    "Info": "Nothin yet",
}
a = CreatePDF(_dict)

a.update_template_context()
a.makeCV()
