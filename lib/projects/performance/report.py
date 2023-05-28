import os

import aspose.words as aw

from lib.projects.project import Project
from lib.components.base_component import BaseComponent

class Report:
    def __init__(self, project: Project, output: str) -> None:
        self._project: Project = project
        self._output: str = output
        self._report: str = ""

    def header(self):
        return f"""# OCCULAR EXECUTION REPORT

_This report was generated automatically._

___

**Project :** {self._project.name}

**Date :** {self._project._date.strftime('%d/%m/%Y %H:%M:%S')}

**User :** {os.getenv("USER", "occular")}

___

## Project informations

| Begin time | End time | Duration |  Mean fps |
|:----------:|:--------:|:--------:|:---------:|
| {self._project._begin_time.strftime('%d/%m/%Y %H:%M:%S')} | {self._project._end_time.strftime('%d/%m/%Y %H:%M:%S')} | {(self._project._end_time - self._project._begin_time)} | null |
"""


    def component_report(self, component: BaseComponent):
        report = component._benchmarker.report()
        return f"""| {component.name} | {report['iterations']} | {report['fps']} | {report['performance']} |
"""

    def components_performances(self):
        table: str = f"""
## Components performances
        
> Null values are components whose benchmarker weren't enabled.

| Component | Iterations | FPS | Performances |
|:---------:|:----------:|:---:|:------------:|
"""
        for component in self._project._components.values():
            table += self.component_report(component)

        return table

    def export_markdown(self):
        with open(f"{self._output}/{self._project.name}_report_{self._project._date.strftime('%d-%m-%Y_%H-%M-%S')}.md", "w") as file:
            file.write(self._report)
            file.close()

    def export_pdf(self):
        self.export_markdown()
        report = aw.Document(f"{self._output}/{self._project.name}_report_{self._project._date.strftime('%d-%m-%Y_%H-%M-%S')}.md")
        saveOptions = aw.saving.PdfSaveOptions()
        # saveOptions.compliance = aw.saving.PdfCompliance.PDF17
        report.save(f"{self._output}/{self._project.name}_report_{self._project._date.strftime('%d-%m-%Y_%H-%M-%S')}.pdf")

    def build(self):
        self._report += self.header()
        self._report += self.components_performances()
        return self

    def export(self, format: str = "md"):
        {
            "md": self.export_markdown,
            "pdf": self.export_pdf
        }[format]()
