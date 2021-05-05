import time
from time import sleep
from Bico_Python_Thread import *

# User output thread - begin ------------------------------------------------------------------------------------------------------------------------
class UserOutputThread(BicoThreadTemplate):
    def __init__(self, thread_name):
        BicoThreadTemplate.__init__(self, thread_name)

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
class UserInputThread(BicoThreadTemplate):
    def __init__(self, thread_name):
        BicoThreadTemplate.__init__(self, thread_name)

    def run(self):
        while(1):
            user_command = input()
            # ----------------------------------------------------------------------------------
            if user_command == "1":
                if BicoThreadGetThreadByName("pr_thread") != 0:
                    BicoThreadGetThreadByName("pr_thread").enqueue("data_from_user_input", 1, self.getName())
                if BicoThreadGetThreadByName("user_output_thread") != 0:
                    BicoThreadGetThreadByName("user_output_thread").enqueue("data_from_user_input", 1, self.getName())
                break
            elif user_command == "2":
                if BicoThreadGetThreadByName("pr_thread") != 0:
                    BicoThreadGetThreadByName("pr_thread").enqueue("data_from_user_input", 2, self.getName())
            elif user_command == "3":
                if BicoThreadGetThreadByName("pr_thread") != 0:
                    BicoThreadGetThreadByName("pr_thread").enqueue("data_from_user_input", 3, self.getName())
            elif user_command == "4":
                if BicoThreadGetThreadByName("pr_thread") != 0:
                    BicoThreadGetThreadByName("pr_thread").enqueue("data_from_user_input", 4, self.getName())
            else:
                pass
            # ----------------------------------------------------------------------------------
            sleep(0.001)
# User input thread - end ------------------------------------------------------------------------------------------------------------------------



# Producer thread - begin ------------------------------------------------------------------------------------------------------------------------
class PrThread(BicoThreadTemplate):
    def __init__(self, thread_name):
        BicoThreadTemplate.__init__(self, thread_name)

    def run(self):
        while(1):
            data_queue = self.dequeue()
            if data_queue != 0:
                # ----------------------------------------------------------------------------------
                if data_queue["data"] == 1:
                    if BicoThreadGetThreadByName("task_0") != 0:
                        BicoThreadGetThreadByName("task_0").enqueue("data_from_producer", 1, self.getName())
                    if BicoThreadGetThreadByName("task_1") != 0:
                        BicoThreadGetThreadByName("task_1").enqueue("data_from_producer", 1, self.getName())
                    break
                elif data_queue["data"] == 2:
                    if BicoThreadGetThreadByName("user_output_thread") != 0:
                        BicoThreadGetThreadByName("user_output_thread").enqueue("print", self.getName() + " receive from " + data_queue["sender"] + ": " + str(data_queue), self.getName())
                elif data_queue["data"] == 3:
                    if BicoThreadGetThreadByName("task_0") != 0:
                        BicoThreadGetThreadByName("task_0").enqueue("data_from_producer", 3, self.getName())
                elif data_queue["data"] == 4:
                    if BicoThreadGetThreadByName("task_1") != 0:
                        BicoThreadGetThreadByName("task_1").enqueue("data_from_producer", 4, self.getName())
                else:
                    pass
                # ----------------------------------------------------------------------------------
            sleep(0.001)
# Producer thread - end ------------------------------------------------------------------------------------------------------------------------



# Consumer A thread - begin ------------------------------------------------------------------------------------------------------------------------
class CsAThread(BicoThreadTemplate):
    def __init__(self, thread_name):
        BicoThreadTemplate.__init__(self, thread_name)

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
                    if BicoThreadGetThreadByName("user_output_thread") != 0:
                        BicoThreadGetThreadByName("user_output_thread").enqueue("print", self.getName() + " receive from " + data_queue["sender"] + ": " + str(data_queue), self.getName())
                elif data_queue["data"] == 4:
                    if BicoThreadGetThreadByName("user_output_thread") != 0:
                        BicoThreadGetThreadByName("user_output_thread").enqueue("print", self.getName() + " receive from " + data_queue["sender"] + ": " + str(data_queue), self.getName())
                else:
                    pass
                # ----------------------------------------------------------------------------------
            sleep(0.001)
# Consumer A thread - end ------------------------------------------------------------------------------------------------------------------------

# Consumer B thread - begin ------------------------------------------------------------------------------------------------------------------------
class CsBThread(BicoThreadTemplate):
    def __init__(self, thread_name):
        BicoThreadTemplate.__init__(self, thread_name)

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
                    if BicoThreadGetThreadByName("user_output_thread") != 0:
                        BicoThreadGetThreadByName("user_output_thread").enqueue("print", self.getName() + " receive from " + data_queue["sender"] + ": " + str(data_queue), self.getName())
                elif data_queue["data"] == 4:
                    if BicoThreadGetThreadByName("user_output_thread") != 0:
                        BicoThreadGetThreadByName("user_output_thread").enqueue("print", self.getName() + " receive from " + data_queue["sender"] + ": " + str(data_queue), self.getName())
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