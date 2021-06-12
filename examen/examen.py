"""
A factory needs an iterable object to keep track of employee working hours for each day.
Each employee has a string name and a tuple containing start work and end work time (use format you like).
Iterating the object will return tuple with name and hours worked that day for each employee
1) 40p: Definition
    a) 10p: Class with constructor that receives the date in the format you desire (representing the day)
    b) 10p: Create method to add worker start time
         - if start time has already been added a custom exception inheriting ValueError (exception: WorkStartError)
         exception will be raised with message indicating employee name and existing start time
    c) 10p: Create method to add worker end time
         - if end time has already been added a custom exception inheriting ValueError (exception: WorkEndError)
         exception will be raised with message indicating employee name and existing end time
    c) 10p: Iterating the object will return tuple with name and time worked that day for each employee
2) 40p: Execution:
    a) 10p: Create instance of class with date format you selected.
    b) 10p: Add start of work for the following employees:
        - Joe: 09:01:20 - start time
        - Ana: 09:03:15 - start time
        - Tim: 09:04:25 - start time
        - Tim: 09:04:30 - start time - treat this exception
    c) 10p: Add end of work for the following employees:
        - Joe: 16:01:20 - end time
        - Ana: 18:04:15 - end time
        - Tim: 18:05:25 - end time
        - Tim: 18:05:30 - end time - treat this exception
    d) 10p: Iterate the created object and save each value on a new line in a file
3) 20p: Documenting:
   a) 5p: type hints for all arguments (optional for returned values)
   a) 5p: module documentation
   b) 5p: class documentation for all classes
   c) 5p: method documentation for all methods
"""

import datetime

class WorkStartError(ValueError):
    """doc for class"""
    pass

class WorkEndError(ValueError):
    """doc for class"""
    pass

class Factory:
    """doc for class"""
    def __init__(self, date: int):
        """doc for method"""
        self.date = date
        self.worker_dict = {}
        self.worker_dict2 = {}

    def add_worker_start_time(self, worker_name: str, start_time: str):
        """doc for method"""
        self.worker_dict = {}
        self.worker_dict[worker_name] = start_time
        try:
            worker_name in self.worker_dict.keys()
        except WorkStartError:
             print(f"Conflict: worker {worker_name} start time {start_time}")
        print(self.worker_dict)


    def add_worker_end_time(self, worker_name: str, end_time: str):
        """doc for method"""
        self.worker_dict2 = {}
        self.worker_dict2[worker_name] = end_time
        try:
            worker_name in self.worker_dict2.keys()
        except WorkStartError:
            print(f"Conflict: worker {worker_name} end time {end_time}")
        print(self.worker_dict2)

    def __iter__(self):
        """doc for method"""
        # empty_tuple = tuple()
        # for key in self.worker_dict.keys():
        #     for key2 in self.worker_dict2.keys():
        #         if key == key2:
        #             worked_hours = int(self.worker_dict2.get(key)) - int(self.worker_dict.get(key2))
        # empty_tuple.insert(key, worked_hours)
        # return FactoryIter(empty_tuple)

class FactoryIter:
    """doc for class"""
    def __init__(self, data: tuple):
        """doc for method"""
        self.data = data

    def __iter__(self):
        """doc for method"""
        return self

    def __next__(self):
        """doc for method"""
        if not self.data:
            raise StopIteration
        return self.data.pop(0)

worker = Factory('2021, 06, 12, 17, 00, 21')
worker.add_worker_start_time('Joe', '09:01:20')
worker.add_worker_start_time('Ana', '09:03:15')
worker.add_worker_start_time('Tim', '09:04:25')
worker.add_worker_start_time('Tim', '09:04:30')

worker.add_worker_end_time('Joe', '16:01:20')
worker.add_worker_end_time('Ana', '18:04:15')
worker.add_worker_end_time('Tim', '18:05:25')
worker.add_worker_end_time('Tim', '18:05:30')


# with open('examen.txt', 'w') as file:
#     for x in worker:
#         file.write(str(x) + '\n')
