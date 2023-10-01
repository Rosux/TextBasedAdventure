class Option:
    def __init__(self, text, nextNode=None, callback=None, resetNode=None):
        self.text = text
        self.nextNode = nextNode
        self.resetNode = resetNode
        self.callback = callback

class Dialogue:
    @classmethod
    def SetGame(cls, game):
        cls.game = game
        
    def __init__(self):
        self.nodes = {}
        self.currentNode = None
        self.game = None

    def AddNode(self, nodeId, text="", options=[], callback=None):
        self.nodes[nodeId] = {
            "text": text,
            "options": options,
            "callback": callback,
        }
        if self.currentNode == None:
            self.currentNode = self.nodes[nodeId]

    def RemoveNode(self, nodeId):
        if nodeId in self.nodes:
            del self.nodes[nodeId]

    def AddOption(self, nodeId, option, newIndex=-1):
        if nodeId in self.nodes:
            self.nodes[nodeId]["options"].insert(newIndex, option)

    def RemoveOption(self, nodeId, optionIndex):
        if nodeId in self.nodes and optionIndex >= 0 and optionIndex < len(self.nodes[nodeId]["options"]):
            del self.nodes[nodeId]["options"][optionIndex]

    def GetChoice(self, choice):
        choice -= 1
        if choice >= 0 and choice < len(self.currentNode["options"]):
            return self.currentNode["options"][choice]
        return None
    
    def GetNode(self, nodeId):
        if nodeId in self.nodes:
            return self.nodes[nodeId]
        return None

    def SetCurrentNode(self, node):
        self.currentNode = self.nodes[node]
        if self.currentNode["callback"] is not None:
            self.currentNode["callback"]()

    def Step(self, choice):
        choice -= 1
        if choice >= 0 and choice < len(self.currentNode["options"]):
            if self.currentNode["options"][choice].callback is not None:
                self.currentNode["options"][choice].callback()
            
            if self.currentNode["options"][choice].nextNode is None:
                if self.currentNode["callback"] is not None:
                    self.currentNode["callback"]()
                if self.currentNode["options"][choice].resetNode is not None:
                    self.currentNode = self.nodes[self.currentNode["options"][choice].resetNode]
                return
            nextNodeId = self.currentNode["options"][choice].nextNode
            if nextNodeId is not None and nextNodeId in self.nodes:
                if self.currentNode["callback"] is not None:
                    self.currentNode["callback"]()
                self.currentNode = self.nodes[nextNodeId]



# tutorial = Dialogue()
# tutorial.AddNode("normalGreeting", "Welcome, traveler. I am the ghost that runs this place. What do you need?", [
#     Option("I need travel directions.", "travelDirections"),
#     Option("I don't know the controls.", "controls"),
#     Option("Leave (and come back later)", "repeatedGreeting"),
# ])
# tutorial.AddNode("repeatedGreeting", "You again? What do you want? Hurry up I got more stuff to do!", [
#     Option("I still need travel directions.", "repeatedTravelDirections"),
#     Option("I still don't know the controls.", "repeatedControls"),
#     Option("Leave (and come back later)", None, None),
# ])
# tutorial.AddNode("travelDirections", "To continue your journey, head east from here. You'll come across a set of stairs. Choose whether to go up or down those stairs, and your adventure shall progress.", [
#     Option("...", "normalGreeting"),
# ])
# tutorial.AddNode("controls", "Use the arrow keys to move your character. To interact with objects or characters, walk onto the object. To pause the game or quit press 'ESC'. To access your inventory, press 'I' or access it in the pause menu. Enjoy your exploration!", [
#     Option("...", "normalGreeting"),
# ])
# tutorial.AddNode("repeatedTravelDirections", "Head east from here. 2 stairs. Up or down just like before. Didn't you listen before?", [
#     Option("...", "repeatedGreeting"),
# ])
# tutorial.AddNode("repeatedControls", "Arrow keys to move. Walk onto objects to interact. Inventory? Press 'I' or access it or go to the pause menu, click 'ESC' ok? Got it? Now get out!", [
#     Option("...", "repeatedGreeting"),
# ])
# tutorial.SetCurrentNode("normalGreeting")

# while True:
#     print("\n\n", tutorial.currentNode["text"])
#     for idx, option in enumerate(tutorial.currentNode["options"]):
#         print(f"{idx+1}: {option.text}")
#     if len(tutorial.currentNode["options"]) == 0:
#         break
#     option = int(input())
#     tutorial.Step(option)
#     if tutorial.GetChoice(option) is not None and tutorial.GetChoice(option).nextNode is None:
#         break


