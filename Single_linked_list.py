class Node:
    def __init__(self,data:int=None):
        self.data = data
        self.ref = None


class SLL:
    def __init__(self):
        self.head:Node = None
        self.counter = 0

    def insert_at_end(self,data) -> None:

        newNode:Node = Node(data)

        if self.head == None:
            self.head = newNode
            self.counter+=1
        else:
            temp:Node = self.head

            while temp.ref != None:
                temp=temp.ref

            temp.ref = newNode
            self.counter+=1

        print("Data inserted succesfully!!!")

    
    def insert_at_first(self,data) -> None:

        newNode:Node = Node(data)

        if self.head == None:
            self.head = newNode
            self.counter+=1
        else:
            newNode.ref = self.head
            self.head = newNode
            self.counter+=1

        print('Data inserted at the first position succesfully.')


    def insert_at_any_pos(self,data,pos) -> None:

        newNode:Node = Node(data)

        if self.head == None:
            self.head = newNode
            self.counter+=1

        elif pos == 1:

            self.insert_at_first(data)

        else:

            temp = self.head

            count:int =1

            while temp.ref!=None:

                if count == pos-1:
                    break

                count+=1

                temp=temp.ref

            newNode.ref = temp.ref
            temp.ref = newNode
            self.counter+=1


        print('Inserted data succesfully..')


    def delete_at_first(self) ->None:

        if self.head == None:
            print('Empty list..')

        else:

            self.head = self.head.ref
            self.counter-=1


    def delete_at_last(self) -> None:


        if self.head == None:
            print('Empty SLL..')


        elif self.counter == 1:
            self.delete_at_first()

        else:
            temp = self.head

            while temp.ref.ref != None:

                temp = temp.ref

            temp.ref = None
            self.counter-=1

        print("Deleted succesfully..")


    def delete_at_any_pos(self,pos) -> None:

        if pos == 1:
            self.delete_at_first()

        elif pos == self.counter:
            self.delete_at_last()

        else:
            temp = self.head
            count=1
            while temp.ref!=None:
               if count == pos -1:
                break
               temp=temp.ref
            
            tempo = temp.ref
            temp.ref = temp.ref.ref 
            temp = None
            self.counter -=1
            print('Succesfully deleted..')


    def display(self):
        if self.head == None:
            print("Empty SLL!!")

        else:
            temp:Node = self.head

            while temp != None:

                print(temp.data,end="-->")

                temp=temp.ref

            print('NULL')

            print()
            print(self.counter)

            


def main():

    obj:SLL = SLL()

    while True:
       x:int=int((input('''
       1.Create a Node.
       2.Display the data.
       3.Insert at first position.
       4.Insert at any position.
       5.Delete at first element.
       6.Delete at last element.
       7.Delete at any position.
       8.Exit
       Enter your choice:''')))
   
       
       if x == 1:
           obj.insert_at_end(int(input("Enter the data:")))
       elif x == 2:
           obj.display()

       elif x == 3:
            obj.insert_at_first((int(input("Enter the data:"))))
   
       elif x == 4:
          obj.insert_at_any_pos((int(input("Enter the data:"))),(int(input("Enter the position:"))))

       elif x == 5:
            obj.delete_at_first()

       elif x == 6:
          obj.delete_at_last()

       elif x == 7:
        obj.delete_at_any_pos(int(input("Enter the position:")))

       elif x ==8:
            exit()
   
       else:
           print('Invalid choice!!!')



if __name__ == '__main__':

    main()


