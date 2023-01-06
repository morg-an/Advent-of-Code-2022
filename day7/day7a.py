def readfile():
    with open("day7input.txt", 'r') as terminalOutput:
        terminalOutput = terminalOutput.readlines()
    return terminalOutput

class Folder():
    _registry = []

    def __init__(self, name, path, parent=None):
        self.name = name
        self.path = path
        self.parent = parent
        self.files = []
        self.children = []
        self._registry.append(self)
        print(f"Directory Added: {self.name}")
    
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

    def print_info(self):
        print("Directories: ", len(self.get_children()), 
        "    Files: ", len(self.get_files()), 
        "    Total Size:", self.get_directory_size())

    def get_directory_size(self):
        value = 0
        for doc in self.files:
            value += doc.get_size()
        return value

class Document():
    def __init__(self, name, path, size):
        self.name = name
        self.path = path
        self.size = int(size)
        print(f"File Added: {self.name} ({str(self.size)})    Path: {self.path}")

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

def getFolderString(currentFolderList):
    folderString = "/"
    nonRootFolders = currentFolderList[1:]
    for folder in nonRootFolders:
        folderString += folder
        folderString += '/'
    if len(folderString) > 1:
        folderString = folderString[:-1]
    return folderString

def buildFileStructure(parcedOutput):
    currentFolder = ['/']
    folderString = '/'
    root = Folder(folderString, currentFolder[0])
    folder = root

    i = 0
    while i < len(parcedOutput):
        line = parcedOutput[i]
        if line[0] == "Change Directory":
            if line[1] == '/':
                j = 1
                while j < len(currentFolder):
                    currentFolder.pop(-1)
                    j += 1
                folder = root
            elif line[1] == '..':
                currentFolder.pop(-1)
                if folder != root:
                    folder = folder.get_parent()
            else:
                currentFolder.append(line[1])
                fileName = currentFolder[-1]
                folderChildren = folder.get_children()
                for child in folderChildren:
                    if line[1] == child.get_name():
                        folder = child
            folderString = getFolderString(currentFolder)
            #print(f"Directory Changed To: {folder.get_name()}    path: {folder.get_path()}")

        elif line[0] == "Contains Directory":
            fileName = folderString
            fileName = Folder(line[1], currentFolder, folder)
            folder.add_child(fileName)
            #folder.print_info()
            
        elif line[0] == "Contains File":
            document = Document(line[1][1], currentFolder, line[1][0])
            folder.add_file(document)
            #folder.print_info()

        i += 1

def findChildDirectorySize(directory):
    children = directory.get_children()
    childFileSize = 0
    for child in children:
        childFileSize += child.get_directory_size()
        if len(child.get_children()) > 0:
            childFileSize += findChildDirectorySize(child)
    return childFileSize

def getAnswer():
    answer = 0
    minDirectorySize = 0
    maxDirectorySize = 100000
    for folder in Folder._registry:
        size = folder.get_directory_size()
        children = folder.get_children()
        if len(children) == 0:
            if size >= minDirectorySize and size <= maxDirectorySize:
                answer += size
        else:
            childFileSize = findChildDirectorySize(folder)
            totalSize = size + childFileSize
            if totalSize >= minDirectorySize and totalSize <= maxDirectorySize:
                answer += totalSize
    return answer

input = readfile()
parcedOutput = parceTerminalOutput(input)
buildFileStructure(parcedOutput)
answer = getAnswer()
print(answer)