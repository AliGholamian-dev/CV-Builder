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

    def makeCV(self):
        asyncio.run(run("initexmf --mkmaps"))
        asyncio.run(run("initexmf --update-fndb"))
        asyncio.run(
            run(
                f"pdflatex -interaction=nonstopmode -aux-directory=./templates/Tempfiles -include-directory=./templates/{self.dictOfInformation['Template']} -job-name=Resume.pdf -output-directory=./Output ./templates/{self.dictOfInformation['Template']}/template.tex"
            )
        )


a = CreatePDF({"Template": "AliceCV"})

a.makeCV()
