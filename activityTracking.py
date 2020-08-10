from dbBase import dbBase
import time
import datetime

class activityTracking(dbBase):
    def __init__(self):
        dbBase.__init__(self, "DSN=DEMODATA-REMOTE;")        

        self.TABLE_NAME = "ActivityTracking"
        self.prepare_table()

        self.actions = []

    def prepare_table(self):
        if(self.check_if_table_exists(self.TABLE_NAME)):
            return
        else:
            # Creating table
            create_table_statement = "CREATE TABLE " \
                + self.TABLE_NAME + " (TimeStamp datetime, EmployeeId varchar(2), Action varchar(256))"
            
            self.cursor.execute(create_table_statement)

    def add_action(self, employee_id, action): 
        # Add 1 sec delay
        time.sleep(1)

        # Get time stamp
        time_stamp = datetime.datetime.utcnow()        

        # Append action to a local list 
        self.actions.append((time_stamp, employee_id, action))

        # Display action
        print(employee_id + ": " + action)

    def transfer_actions_to_remote_database(self):
        insert_action_statement = "INSERT INTO " \
                + self.TABLE_NAME + " VALUES(?,?,?)"

        for action in self.actions:
            # Insert action
            self.cursor.execute(insert_action_statement, action)
            self.cursor.commit()

    def display_employee_actions(self, employee_id):
        select_actions_statement = "SELECT * FROM " + self.TABLE_NAME

        # Invoke statement
        row = self.cursor.execute(select_actions_statement)

        # Display header
        print("\n---=== A list of actions of employee " \
                + employee_id + ": ===---")

        # Get and display the resulting rows
        row = self.cursor.fetchone() 

        while row: 
            print(str(row[0]) + ": " + row[2])
            row = self.cursor.fetchone()
