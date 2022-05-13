class TableElement:
    indent_size = 2

    def __init__(self, _type: str = "", _content: str = ""):
        self.type = _type
        self.content = _content
        self.children = []
    
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

    def add_child_fluent(self, child_name:str, child_text:str):
        self.__table_root.children.append(TableElement(child_name,child_text))
        return self
    
    def __str__(self):
        return str(self.__table_root)

class Table:
    def __init__(self, table_data):
        self._raw_data = table_data
        self.builder = TableElement.start_building()
        self.builder.add_child("th", "Random")
    
    def __str__(self) -> str:
        return str(self.builder)
