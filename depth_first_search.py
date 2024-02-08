# Processes
#  iterating through a list of possibilities, to get the best possible
#  Solution out of those possibilities.
#  at then i want to chose that final possibility
#  search through a list of files and find a particular file

class SearchAlgorithms:
    possibleDirectories:{} = {}
    moves = []
    flag:bool = False
    boundry:bool = False
    
    def __init__(self, possibleDirectories):
        self.possibleDirectories = possibleDirectories

    def depthFirstSearch(self, dstNode:str="ManOfWar.mp3", rootNode:str="Home", flag:bool=False): 
        
        if rootNode not in self.moves:
           self.moves.append(rootNode)

        for directory in self.possibleDirectories[rootNode]:     
            if flag is not self.flag:
                return self.moves
            
            if self.possibleDirectories.get(directory) != None:
                self.depthFirstSearch(dstNode=dstNode,rootNode=directory, flag=self.flag)
            else: 
                self.moves.append(directory) 
                if dstNode is directory :
                    self.flag = True
                    print("found document at:", rootNode) 
            
        return self.moves
    
    


if __name__ == "__main__":
    possibleDirectories = {
        "Home": ["Music", "Video", "Downloads", "Documents", "Desktop"],
        "Music": ["BattleAxe.mp3", "ManOfWar.mp3"],
        "Downloads" : ["AdobePhotoShop.exe", "Arduino.appImage"],
        "Documents" : ["Introduction to Artificial Intelligence.pdf", "Game Theory.pdf"],
        "Video": [],
        "Desktop": ["Flutter_apps", "Minecraft.exe", "Krita.png"],
        "Flutter_apps": ["RUNACES_mobile_app", "NewFolder"],
        "NewFolder": ["gamersTheorem.pdf"]
    }

    search = SearchAlgorithms(possibleDirectories=possibleDirectories)
    moves = search.depthFirstSearch(dstNode="gamersTheorem.pdf")
    print(moves)