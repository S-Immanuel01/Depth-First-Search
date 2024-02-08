class Node :
    g_score = 0
    f_score = 0
    left_node = None
    right_node = None
    center_node = None

    def __init__(this, h_score, parentNodeDis = 0):
        this.g_score += parentNodeDis
        this.f_score = this.g_score + h_score

class Algorithms:
    f_values = {}
    min_value = 0

    def A_star(this, parentNode:Node, goalNode:Node, shouldPop=False):
        # print("iteration")
        
        
        if len(this.f_values) == 0 and shouldPop == True:
            return

        if parentNode == goalNode:
            print("reach goal")
            return

        this.f_values[parentNode.f_score]  = parentNode


        if parentNode and parentNode.center_node and parentNode.left_node:
            min_f_score = min(parentNode.right_node.f_score, parentNode.center_node.f_score, parentNode.left_node.f_score)
            print(min_f_score)
            this.f_values[parentNode.center_node.f_score] = parentNode.center_node
            this.f_values[parentNode.left_node.f_score] = parentNode.center_node
            this.f_values[parentNode.right_node.f_score] = parentNode.center_node
            if parentNode.center_node.f_score == min_f_score:
                print("center node")
                this.A_star(parentNode=parentNode.center_node, goalNode=goalNode, shouldPop=shouldPop)
            elif parentNode.left_node.f_score == min_f_score:
                print("left node")
                this.A_star(parentNode=parentNode.left_node, goalNode=goalNode, shouldPop=shouldPop)
            elif parentNode.right_node.f_score == min_f_score:
                print("right node")
                this.A_star(parentNode=parentNode.right_node, goalNode=goalNode, shouldPop=shouldPop)
        elif parentNode.center_node is not None or parentNode.left_node is not None or parentNode.right_node is not None:
            if parentNode.center_node is not None:
                print("center node")
                this.A_star(parentNode=parentNode.center_node, goalNode=goalNode, shouldPop=shouldPop)
            elif parentNode.right_node is not None:
                print("right node")
                this.A_star(parentNode=parentNode.right_node, goalNode=goalNode, shouldPop=shouldPop)
            elif parentNode.left_node is not None :
                print("left node")
                this.A_star(parentNode=parentNode.left_node, goalNode=goalNode, shouldPop=shouldPop)
        else:
            if shouldPop:
                this.f_values.pop(this.min_value)
            temp_list = []
            min_value = 0
            for values in this.f_values:
                temp_list.append(values)
                min_value = min(temp_list)
            if min_value == 0:
                return
            this.min_value = min_value | 0
            print("Unable to find result in this node")
            print("BackTracking")
            this.A_star(parentNode=this.f_values[min_value], goalNode=goalNode, shouldPop=True)
            

            

if __name__ == '__main__':
    parentNode  = Node(10, parentNodeDis=0)
    parentNode.center_node = Node(5, parentNodeDis=5)
    parentNode.left_node  = Node(2, parentNodeDis=5)
    parentNode.right_node = Node(8, parentNodeDis=5)
    parentNode.right_node.left_node = parentNode.center_node
    parentNode.left_node.center_node = Node(3, parentNodeDis=5)
    parentNode.left_node.center_node.left_node = Node(4, parentNodeDis=6)
    goalNode = parentNode.center_node
    Algorithms().A_star(parentNode=parentNode, goalNode=goalNode)
    # calculate A*
