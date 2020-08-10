from dbBase import dbBase
import numpy as np

class accessSchedule(dbBase):
    def __init__(self):
        dbBase.__init__(self, "DSN=DEMODATA-LOCAL;")

        self.TABLE_NAME = "AccessSchedule"

        self.prepare_table()

    def prepare_table(self):
        if(self.check_if_table_exists(self.TABLE_NAME)):
            return
        else:
            # Creating table
            create_table_statement = "CREATE TABLE " \
                + self.TABLE_NAME + " (EmployeeId varchar(2))"
            
            self.cursor.execute(create_table_statement)
    
            # Adding data
            self.add_data(15)

    def add_data(self, max_count):
        insert_item_statement = "INSERT INTO " \
                + self.TABLE_NAME + " VALUES(?)"

        for i in np.arange(1, max_count, 2):
            # Format employee id
            item = '{:02}'.format(i)
            
            # Insert item
            self.cursor.execute(insert_item_statement, item)
            self.cursor.commit()

    def can_access_today(self, employee_id):
        select_item_statement = "SELECT COUNT(EmployeeId) FROM " \
            + self.TABLE_NAME \
            + " WHERE EmployeeId=" \
            + employee_id

        employee_count = self.cursor.execute(select_item_statement)
        employee_count = employee_count.fetchone()[0]

        return employee_count == 1