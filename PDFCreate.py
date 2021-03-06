import asyncio

# Async Function to run Commands in Shell
async def run(cmd):
    """ 
    Async Function to run Commands in Shell
  
    Parameters: 
        cmd (String): Command to run  
    """
    # Making A Subprocess to run command
    proc = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    # Run command
    await proc.communicate()


# Class for Creating Pdf
class CreatePDF:
    def __init__(self, dictOfInformation):
        """ 
        Create PDf Constructor 
  
        Parameters: 
            dictOfInformation (Dict): User information stored in a Dict
        """
        self.dictOfInformation = dictOfInformation

    def update_template_context(self):
        """ 
        Updates Contebts in Template.tex file  
        """
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
        # Converting Level of Professinalty for each Template
        for skills_set in self.dictOfInformation["Skills"]:
            if skills_set[1] > 66:
                self.dictOfInformation["Advanced"].append(skills_set[0])
            elif skills_set[1] > 33:
                self.dictOfInformation["Intermediate"].append(skills_set[0])
            else:
                self.dictOfInformation["Basic"].append(skills_set[0])
        # Replacing Keywords in TEX file with User Info
        temptext = temptext.replace("rname", self.dictOfInformation["Name"])
        temptext = temptext.replace("raddress", self.dictOfInformation["Address"])
        temptext = temptext.replace("rrphone", self.dictOfInformation["Phone"])
        temptext = temptext.replace("rgit", self.dictOfInformation["Git"])
        temptext = temptext.replace("rlinkedin", self.dictOfInformation["Linkedin"])
        temptext = temptext.replace("rsite", self.dictOfInformation["Site"])
        temptext = temptext.replace("rmail", self.dictOfInformation["Mail"])
        temptext = temptext.replace("raboutme", self.dictOfInformation["Aboutme"])
        temptext = temptext.replace("rotherinfo", self.dictOfInformation["Info"])
        temptext = temptext.replace("rtitle", self.dictOfInformation["Title"])
        # Replacing Keywords in TEX file with User Info (Keywords with specific Style)
        if self.dictOfInformation["Template"] == "AliceCV":
            # Picture Path
            temptext = temptext.replace("rpic", self.dictOfInformation["Picture"])
            # Replacing Skills with it's specific style
            txt = ""
            for skills_set in self.dictOfInformation["Skills"]:
                txt += "{" + skills_set[0] + "/" + str(skills_set[1]) + "},"
            temptext = temptext.replace("rskills", txt[: len(txt) - 1])
            # Replacing Interests with it's specific style
            temptext = temptext.replace(
                "rinterests", self.dictOfInformation["Interests"]
            )
            # Replacing Education with it's specific style
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
            # Replacing Awards with it's specific style
            txt = ""
            for award_set in self.dictOfInformation["Awards"]:
                txt += (
                    "\\twentyitemshort{" + award_set[0] + "}{" + award_set[1] + "}\n\t"
                )
            temptext = temptext.replace("rawards", txt[: len(txt) - 2])
            # Replacing Experience with it's specific style
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
            # Replacing Gitrepos with it's specific style
            txt = ""
            txt_readme = ""
            for git_set in self.dictOfInformation["Gitrepos"]:
                # In case Readme file not added to CV
                if git_set[3] == False:
                    txt += (
                        "\\twentyitem{"
                        + git_set[0]
                        + "}{\href{https://github.com/"
                        + self.dictOfInformation["Git"]
                        + "/"
                        + git_set[1]
                        + "}{"
                        + git_set[1]
                        + "}}{\href{"
                        + git_set[2]
                        + "}{ReadMe File}}{}\n\t"
                    )
                else:  # In case Readme file added to CV
                    txt_readme += (
                        "\\newpage\n\\makeprofile\n\\section{Github Repos}\n\n\\begin{twenty}\n\t\\twentyitem{"
                        + git_set[0]
                        + "}{\href{https://github.com/"
                        + self.dictOfInformation["Git"]
                        + "/"
                        + git_set[1]
                        + "}{"
                        + git_set[1]
                        + "}}{\href{"
                        + git_set[2]
                        + "}{ReadMe File}}{}\n\\end{twenty}"
                        + "\\newenvironment{markdown}%\n\t\t"
                        + "{\\VerbatimEnvironment\\begin{VerbatimOut}{https://raw.githubusercontent.com/"
                        + self.dictOfInformation["Git"]
                        + "/"
                        + git_set[1]
                        + "/master/readme.md}}%\n\t\t{\\end{VerbatimOut}%\n\t\t\t"
                        + "\\immediate\\write18{pandoc "
                        + "https://raw.githubusercontent.com/"
                        + self.dictOfInformation["Git"]
                        + "/"
                        + git_set[1]
                        + "/master/readme.md -t latex -o tmp.tex}%\n\t\t\t\\input{tmp.tex}}\n\t\t\t\t"
                        + "\\begin{markdown}\n\t\t\t\\input{tmp.tex}\n\t\t\t\t\\end{markdown}\n"
                    )
            temptext = temptext.replace("rrepos", txt[: len(txt) - 2])
            temptext = temptext.replace("rreadmmemdgit", txt_readme)

        elif self.dictOfInformation["Template"] == "DeveloperCV":
            temptext = temptext.replace("rlastname", self.dictOfInformation["LastName"])
            # Replacing Skills with it's specific style
            txt = ""
            for skills_set in self.dictOfInformation["Skills"]:
                txt += (
                    "\t\t\\baritem{" + skills_set[0] + "}{" + str(skills_set[1]) + "}\n"
                )
            temptext = temptext.replace("rskills", txt[: len(txt) - 1])
            # Replacing Interests with it's specific style
            temptext = temptext.replace(
                "rinterests", self.dictOfInformation["Interests"]
            )
            # Replacing Education with it's specific style
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
            # Replacing Awards with it's specific style
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
            # Replacing Experience with it's specific style
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
            # Replacing Gitrepos with it's specific style
            txt = ""
            txt_readme = ""
            for git_set in self.dictOfInformation["Gitrepos"]:
                # In case Readme file not added to CV
                if git_set[3] == False:
                    txt += (
                        "\t \\entry\n\t\t   {"
                        + git_set[0]
                        + "}\n\t\t   {\href{https://github.com/"
                        + self.dictOfInformation["Git"]
                        + "/"
                        + git_set[1]
                        + "}{"
                        + git_set[1]
                        + "}}\n\t\t   {\href{"
                        + git_set[2]
                        + "}\n\t\t   {ReadMe File}}\n\t\t {}\n"
                    )
                else:  # In case Readme file added to CV
                    txt_readme += (
                        "\\newpage\n\\cvsect{Github Repos}\n\n\\begin{entrylist}\t \\entry\n\t\t   {"
                        + git_set[0]
                        + "}\n\t\t   {\href{https://github.com/"
                        + self.dictOfInformation["Git"]
                        + "/"
                        + git_set[1]
                        + "}{"
                        + git_set[1]
                        + "}}\n\t\t   {\href{"
                        + git_set[2]
                        + "}\n\t\t   {ReadMe File}}\n\t\t {}\n\end{entrylist}\n"
                        + "\\newenvironment{markdown}%\n\t\t"
                        + "{\\VerbatimEnvironment\\begin{VerbatimOut}{https://raw.githubusercontent.com/"
                        + self.dictOfInformation["Git"]
                        + "/"
                        + git_set[1]
                        + "/master/readme.md}}%\n\t\t{\\end{VerbatimOut}%\n\t\t\t"
                        + "\\immediate\\write18{pandoc "
                        + "https://raw.githubusercontent.com/"
                        + self.dictOfInformation["Git"]
                        + "/"
                        + git_set[1]
                        + "/master/readme.md -t latex -o tmp.tex}%\n\t\t\t\\input{tmp.tex}}\n\t\t\t\t"
                        + "\\begin{markdown}\n\t\t\t\\input{tmp.tex}\n\t\t\t\t\\end{markdown}\n"
                    )

            temptext = temptext.replace("rrepos", txt[: len(txt) - 1])
            temptext = temptext.replace("rreadmmemdgit", txt_readme)

        elif self.dictOfInformation["Template"] == "ModernCV":
            temptext = temptext.replace("rpic", self.dictOfInformation["Picture"])
            temptext = temptext.replace("rlastname", self.dictOfInformation["LastName"])
            # Replacing Skills with it's specific style
            txt = ""
            if len(self.dictOfInformation["Basic"]) > 0:
                txt = "\\cvitem{Basic}{" + self.dictOfInformation["Basic"][0]
                for sk in self.dictOfInformation["Basic"][1:]:
                    txt += ", " + sk
                txt += "}\n"
            if len(self.dictOfInformation["Intermediate"]) > 0:
                txt += (
                    "\\cvitem{Intermediate}{"
                    + self.dictOfInformation["Intermediate"][0]
                )
                for sk in self.dictOfInformation["Intermediate"][1:]:
                    txt += ", " + sk
                txt += "}\n"
            if len(self.dictOfInformation["Advanced"]) > 0:
                txt += "\\cvitem{Advanced}{" + self.dictOfInformation["Advanced"][0]
                for sk in self.dictOfInformation["Advanced"][1:]:
                    txt += ", " + sk
                txt += "}\n"
            temptext = temptext.replace("rskills", txt)
            # Replacing Interests with it's specific style
            txt = ""
            for inter in self.dictOfInformation["Interests"]:
                txt += "\\cvlistitem{" + inter + "}\n"
            temptext = temptext.replace("rinterests", txt[: len(txt) - 1])
            # Replacing Education with it's specific style
            txt = ""
            for ed_set in self.dictOfInformation["Education"]:
                txt += (
                    "\\cventry{"
                    + ed_set[0]
                    + "--"
                    + ed_set[1]
                    + "}{"
                    + ed_set[2]
                    + "}{"
                    + ed_set[3]
                    + "}{"
                    + ed_set[4]
                    + "}{}{}\n"
                )
            temptext = temptext.replace("reducation", txt[: len(txt) - 1])
            # Replacing Awards with it's specific style
            txt = ""
            for award_set in self.dictOfInformation["Awards"]:
                txt += "\\cvitem{" + award_set[0] + "}{" + award_set[1] + "}\n"
            temptext = temptext.replace("rawards", txt[: len(txt) - 1])
            # Replacing Experience with it's specific style
            txt = ""
            for ex_set in self.dictOfInformation["Experience"]:
                txt += (
                    "\\cventry{"
                    + ex_set[0]
                    + "}{"
                    + ex_set[1]
                    + "}{"
                    + ex_set[2]
                    + "}{"
                    + ex_set[3]
                    + "}{}{}\n"
                )
            temptext = temptext.replace("rexperience", txt[: len(txt) - 1])
            # Replacing Gitrepos with it's specific style
            txt = ""
            txt_readme = ""
            for git_set in self.dictOfInformation["Gitrepos"]:
                # In case Readme file not added to CV
                if git_set[3] == False:
                    txt += (
                        "\\cventry{"
                        + git_set[0]
                        + "}{\href{https://github.com/"
                        + self.dictOfInformation["Git"]
                        + "/"
                        + git_set[1]
                        + "}{"
                        + git_set[1]
                        + "}}{\href{"
                        + git_set[2]
                        + "}{ReadMe File}}{}{}{}\n"
                    )
                else:  # In case Readme file added to CV
                    txt_readme += (
                        "\\newpage\n\\makecvtitle\n\\section{Github Repo}\n\n\\cventry{"
                        + git_set[0]
                        + "}{\href{https://github.com/"
                        + self.dictOfInformation["Git"]
                        + "/"
                        + git_set[1]
                        + "}{"
                        + git_set[1]
                        + "}}{\href{"
                        + git_set[2]
                        + "}{ReadMe File}}{}{}{}\n"
                        + "\\newenvironment{markdown}%\n\t\t"
                        + "{\\VerbatimEnvironment\\begin{VerbatimOut}{https://raw.githubusercontent.com/"
                        + self.dictOfInformation["Git"]
                        + "/"
                        + git_set[1]
                        + "/master/readme.md}}%\n\t\t{\\end{VerbatimOut}%\n\t\t\t"
                        + "\\immediate\\write18{pandoc "
                        + "https://raw.githubusercontent.com/"
                        + self.dictOfInformation["Git"]
                        + "/"
                        + git_set[1]
                        + "/master/readme.md -t latex -o tmp.tex}%\n\t\t\t\\input{tmp.tex}}\n\t\t\t\t"
                        + "\\begin{markdown}\n\t\t\t\\input{tmp.tex}\n\t\t\t\t\\end{markdown}\n"
                    )
            temptext = temptext.replace("rrepos", txt[: len(txt) - 1])
            temptext = temptext.replace("rreadmmemdgit", txt_readme)

        fout.write(temptext)
        # close input and output files
        fout.close()

    def makeCV(self):
        """ 
        Creates PDF Resume 
        """
        # Making Font Map for LATEX
        asyncio.run(run("initexmf --enable-installer --mkmaps"))
        asyncio.run(run("initexmf --enable-installer --update-fndb"))
        # Running pdflatex to create pdf
        asyncio.run(
            run(
                f"pdflatex --enable-installer --shell-escape -enable-write18 -interaction=nonstopmode -aux-directory=./templates/Tempfiles -include-directory=./templates/{self.dictOfInformation['Template']} -job-name={self.dictOfInformation['nameOfFile']} -output-directory=./Output ./templates/{self.dictOfInformation['Template']}/template_new.tex"
            )
        )
        # Openning PDF RESUME
        asyncio.run(run("start ./Output/Resume.pdf"))
