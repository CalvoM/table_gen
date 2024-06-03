from typing import Dict


class TableElement:
    indent_size = 1

    def __init__(self, _type: str = "", _content: str = ""):
        self.type = _type
        self.content = _content
        self.children = []
    
    def add_child_element(self, element):
        if isinstance(element, TableElement):
            self.children.append(element)
    
    def __str(self, indent):
        lines = []
        i = " " * (indent * self.indent_size)
        lines.append(f"{i}<{self.type}>")

        if self.content:
            i1 = " " * ((indent + 1) * self.indent_size)
            lines.append(f"{i1}{self.content}")
        for e in self.children:
            lines.append(e.__str(indent + 1))
        
        lines.append(f"{i}</{self.type}>")
        return "\n".join(lines)

    def __str__(self):
        return self.__str(0)

    @staticmethod
    def start_building():
        return TableBuilder()
    pass


class TableBuilder:
    def __init__(self):
        self.__table_root: TableElement = TableElement("table")
    
    def add_child(self, child_name:str, child_text:str):
        self.__table_root.children.append(TableElement(child_name,child_text))
    
    def add_child_element(self, element:TableElement):
        self.__table_root.children.append(element)
    
    def __str__(self):
        return str(self.__table_root)

class Table:
    def __init__(self, table_data: Dict):
        self._raw_data: Dict = table_data
        self.builder = TableElement.start_building()
        self._generate_table_attrs()
        self._generate_headers()
        self._generate_data()
    
    def _generate_table_attrs(self):
        caption = self._raw_data.get("caption", None)
        if caption:
            self.builder.add_child("caption", caption)
    
    def _generate_headers(self):
        headers = self._raw_data.get("headers", [])
        if len(headers):
            header_element = TableElement("thead")
            header_row = TableElement("tr")
            for h in headers:
                e = TableElement("th", h)
                header_row.add_child_element(e)
            header_element.add_child_element(header_row)
            self.builder.add_child_element(header_element)

    def _generate_data(self):
        data = self._raw_data.get("data", [])
        body_element = TableElement("tbody")
        if(len(data)):
            for row in data:
                body_row = TableElement("tr")
                for d in row:
                    e = TableElement("td", d)
                    body_row.add_child_element(e)
                body_element.add_child_element(body_row)
            self.builder.add_child_element(body_element)

    def __str__(self) -> str:
        return str(self.builder)
