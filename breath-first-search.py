from depth_first_search import SearchAlgorithms

class BFS:
    possibleDirectories:{} = {}
    moves = []
    flag:bool = False
    boundry:bool = False
    
    def __init__(self, possibleDirectories):
        self.possibleDirectories = possibleDirectories

    def breathFirstSearch(self, flag:bool=False, dstNode="ManOfWar.mp3", rootNode="Home", boundry:bool=False):
            mvflag = False
            if rootNode not in self.moves:
                self.moves.append(rootNode)

            for directory in self.possibleDirectories.get(rootNode):
                
                if dstNode in self.moves:
                    flag = True
                    
                else: 
                    self.flag = False
                    if self.possibleDirectories.get(directory) is not None:
                        if directory not in self.moves and not mvflag:
                            self.moves.append(directory)

                        if self.possibleDirectories.get(rootNode)[-1] is directory:
                            mvflag = True
                            self.breathFirstSearch(rootNode=directory, flag=self.flag,  boundry=True, dstNode=dstNode)

                    elif boundry is True:
                        SearchAlgorithms.depthFirstSearch(dstNode=dstNode)

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

    search = BFS(possibleDirectories=possibleDirectories)
    moves = search.breathFirstSearch(dstNode="gamersTheorem.pdf")
    print(moves)