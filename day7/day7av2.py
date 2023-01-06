def readfile():
    with open("day7input.txt", 'r') as terminalOutput:
        terminalOutput = terminalOutput.readlines()
    return terminalOutput

class Folder():
    numFolders = 0

    def __init__(self, name, path, parent=None):
        self.name = name
        self.path = path
        self.parent = parent
        self.files = []
        self.children = []
        print(f"Folder Added: {self.name} in {self.path}")
    
    def get_name(self):
        return self.name

    def get_path(self):
        return self.path
    
    def get_parent(self):
        return self.parent
    
    def get_files(self):
        return self.files

    def get_children(self):
        return self.children

    def add_file(self, document):
        self.files.append(document)
    
    def add_child(self, folder):
        self.children.append(folder)
        Folder.numFolders += 1

    def print_info(self):
        print("Folder Children", len(self.get_children()), 
        "Folder Docs: ", len(self.get_files()), 
        "Folder Size:", self.get_folder_size())

    def get_folder_size(self):
        value = 0
        for doc in self.files:
            value += doc.get_size()
        return value

class Document():
    def __init__(self, name, path, size):
        self.name = name
        self.size = int(size)
        self.path = path
        print(f"Document Added: {self.name} ({str(self.size)}) in {self.path}")

    def get_size(self):
        return self.size
    
    def get_path(self):
        return self.path

def parceTerminalOutput(terminalOutput):
    parcedOutput = []
    lineFunction = ""
    for line in terminalOutput:
        line = line.strip('\n')
        if line[2] == 'c' and line[3] == 'd':
            lineFunction = ["Change Directory", line[5:]]
        elif line [2] == 'l' and line[3] == 's':
            lineFunction = ["Command: List Files"]
        elif line[0] == 'd' and line[1] == 'i' and line [2] == 'r':
            lineFunction = ["Contains Directory", line[4:]]
        else:
            lineFunction = ["Contains File", line.split(" ")] 
        parcedOutput.append(lineFunction)
    return parcedOutput

def buildFileStructure(parcedOutput):
    i = 0
    folderString = '/'
    root = Folder('/', folderString)
    Folder.numFolders += 1
    folder = root
    while i < len(parcedOutput):
        line = parcedOutput[i]
        if line[0] == "Change Directory":
            if line[1] == '/':
                folderString = '/'
                folder = root
            elif line[1] == '..':
                folderString = folderString[:-1]
                if folder != root:
                    folder = folder.get_parent()
            else:
                folderString = folderString + line[1]
                fileName = folderString
                folderChildren = folder.get_children()
                for child in folderChildren:
                    if line[1] == child.get_name():
                        folder = child
            print(f"Directory Changed To: {folderString} ({folder.get_name()})")

        elif line[0] == "Contains Directory":
            fileName = folderString
            fileName = Folder(line[1], folderString, folder)
            folder.add_child(fileName)
            folder.print_info()
            
        elif line[0] == "Contains File":
            document = Document(line[1][1], folderString, line[1][0])
            folder.add_file(document)
            folder.print_info()

        i += 1

input = readfile()
parcedOutput = parceTerminalOutput(input)
buildFileStructure(parcedOutput)