import threading
import time
from time import sleep

class PeritecThreadQueue:
    def __init__(self):
        self.qin = []
        self.locker = threading.Lock()

    def enqueue(self, mess, data, sender = ""):
        self.locker.acquire()
        self.qin.append({"mess": mess, "data": data, "sender": sender})
        self.locker.release()

    def dequeue(self):
        if len(self.qin) > 0:
            self.locker.acquire()
            data_queue = self.qin.pop()                
            self.locker.release()
        else:
            data_queue = 0
        return data_queue
        

# Thread Template - begin ------------------------------------------------------------------------------------------------------------------------
class PeritecThreadTemplate(threading.Thread, PeritecThreadQueue):
    def __init__(self, thread_name):
        PeritecThreadQueue.__init__(self)
        threading.Thread.__init__(self)
        self.setName(thread_name)
# Template thread - end ------------------------------------------------------------------------------------------------------------------------


# Get thread by name -----------------------------------------------------------------
def PeritecThreadGetThreadByName(thread_name):
    for thread in threading.enumerate():
        if thread.getName() == thread_name:
            return thread
    return 0
# Get thread by name -----------------------------------------------------------------





# The MultiThreading template definition end here ---------------------------------------------------------------
# The code below is just for test purpose ---------------------------------------------------------------







# User output thread - begin ------------------------------------------------------------------------------------------------------------------------
class UserOutputThread(PeritecThreadTemplate):
    def __init__(self, thread_name):
        PeritecThreadTemplate.__init__(self, thread_name)

    def run(self):
        while(1):
            data_queue = self.dequeue()
            if data_queue != 0:
                # ----------------------------------------------------------------------------------
                if data_queue["data"] == 1:
                    break
                elif data_queue["mess"] == "print":
                    print(data_queue["data"])
                else:
                    pass
                # ----------------------------------------------------------------------------------
            sleep(0.001)
# User output thread - end ------------------------------------------------------------------------------------------------------------------------

# User input thread - begin ------------------------------------------------------------------------------------------------------------------------
class UserInputThread(PeritecThreadTemplate):
    def __init__(self, thread_name):
        PeritecThreadTemplate.__init__(self, thread_name)

    def run(self):
        while(1):
            user_command = input()
            # ----------------------------------------------------------------------------------
            if user_command == "1":
                if PeritecThreadGetThreadByName("pr_thread") != 0:
                    PeritecThreadGetThreadByName("pr_thread").enqueue("data_from_user_input", 1, self.getName())
                if PeritecThreadGetThreadByName("user_output_thread") != 0:
                    PeritecThreadGetThreadByName("user_output_thread").enqueue("data_from_user_input", 1, self.getName())
                break
            elif user_command == "2":
                if PeritecThreadGetThreadByName("pr_thread") != 0:
                    PeritecThreadGetThreadByName("pr_thread").enqueue("data_from_user_input", 2, self.getName())
            elif user_command == "3":
                if PeritecThreadGetThreadByName("pr_thread") != 0:
                    PeritecThreadGetThreadByName("pr_thread").enqueue("data_from_user_input", 3, self.getName())
            elif user_command == "4":
                if PeritecThreadGetThreadByName("pr_thread") != 0:
                    PeritecThreadGetThreadByName("pr_thread").enqueue("data_from_user_input", 4, self.getName())
            else:
                pass
            # ----------------------------------------------------------------------------------
            sleep(0.001)
# User input thread - end ------------------------------------------------------------------------------------------------------------------------



# Producer thread - begin ------------------------------------------------------------------------------------------------------------------------
class PrThread(PeritecThreadTemplate):
    def __init__(self, thread_name):
        PeritecThreadTemplate.__init__(self, thread_name)

    def run(self):
        while(1):
            data_queue = self.dequeue()
            if data_queue != 0:
                # ----------------------------------------------------------------------------------
                if data_queue["data"] == 1:
                    if PeritecThreadGetThreadByName("task_0") != 0:
                        PeritecThreadGetThreadByName("task_0").enqueue("data_from_producer", 1, self.getName())
                    if PeritecThreadGetThreadByName("task_1") != 0:
                        PeritecThreadGetThreadByName("task_1").enqueue("data_from_producer", 1, self.getName())
                    break
                elif data_queue["data"] == 2:
                    if PeritecThreadGetThreadByName("user_output_thread") != 0:
                        PeritecThreadGetThreadByName("user_output_thread").enqueue("print", self.getName() + " receive from " + data_queue["sender"] + ": " + str(data_queue), self.getName())
                elif data_queue["data"] == 3:
                    if PeritecThreadGetThreadByName("task_0") != 0:
                        PeritecThreadGetThreadByName("task_0").enqueue("data_from_producer", 3, self.getName())
                elif data_queue["data"] == 4:
                    if PeritecThreadGetThreadByName("task_1") != 0:
                        PeritecThreadGetThreadByName("task_1").enqueue("data_from_producer", 4, self.getName())
                else:
                    pass
                # ----------------------------------------------------------------------------------
            sleep(0.001)
# Producer thread - end ------------------------------------------------------------------------------------------------------------------------



# Consumer A thread - begin ------------------------------------------------------------------------------------------------------------------------
class CsAThread(PeritecThreadTemplate):
    def __init__(self, thread_name):
        PeritecThreadTemplate.__init__(self, thread_name)

    def run(self):
        while(1):
            data_queue = self.dequeue()
            if data_queue != 0:
                # ----------------------------------------------------------------------------------
                if data_queue["data"] == 1:
                    break
                elif data_queue["data"] == 2:
                    pass
                elif data_queue["data"] == 3:
                    if PeritecThreadGetThreadByName("user_output_thread") != 0:
                        PeritecThreadGetThreadByName("user_output_thread").enqueue("print", self.getName() + " receive from " + data_queue["sender"] + ": " + str(data_queue), self.getName())
                elif data_queue["data"] == 4:
                    if PeritecThreadGetThreadByName("user_output_thread") != 0:
                        PeritecThreadGetThreadByName("user_output_thread").enqueue("print", self.getName() + " receive from " + data_queue["sender"] + ": " + str(data_queue), self.getName())
                else:
                    pass
                # ----------------------------------------------------------------------------------
            sleep(0.001)
# Consumer A thread - end ------------------------------------------------------------------------------------------------------------------------

# Consumer B thread - begin ------------------------------------------------------------------------------------------------------------------------
class CsBThread(PeritecThreadTemplate):
    def __init__(self, thread_name):
        PeritecThreadTemplate.__init__(self, thread_name)

    def run(self):
        while(1):
            data_queue = self.dequeue()
            if data_queue != 0:
                # ----------------------------------------------------------------------------------
                if data_queue["data"] == 1:
                    break
                elif data_queue["data"] == 2:
                    pass
                elif data_queue["data"] == 3:
                    if PeritecThreadGetThreadByName("user_output_thread") != 0:
                        PeritecThreadGetThreadByName("user_output_thread").enqueue("print", self.getName() + " receive from " + data_queue["sender"] + ": " + str(data_queue), self.getName())
                elif data_queue["data"] == 4:
                    if PeritecThreadGetThreadByName("user_output_thread") != 0:
                        PeritecThreadGetThreadByName("user_output_thread").enqueue("print", self.getName() + " receive from " + data_queue["sender"] + ": " + str(data_queue), self.getName())
                else:
                    pass
                # ----------------------------------------------------------------------------------
            sleep(0.001)
# Consumer B thread - end ------------------------------------------------------------------------------------------------------------------------



def main():
    user_input_thread = UserInputThread("user_input_thread")
    user_input_thread.start()

    user_output_thread = UserOutputThread("user_output_thread")
    user_output_thread.start()

    thread_1 = PrThread("pr_thread")
    thread_1.start()

    thread_2 = CsAThread("task_0")
    thread_2.start()

    thread_2 = CsBThread("task_1")
    thread_2.start()


if __name__ == "__main__":
    main()