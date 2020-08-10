from recognizer import recognizer
from accessSchedule import accessSchedule
from activityTracking import activityTracking

if __name__ == "__main__": 
    # Prepare face recognizer, access schedule, and activity tracking
    face_recognizer = recognizer()
    access_schedule = accessSchedule()
    activity_tracking = activityTracking()

    # Get random face image
    face_image_file_path = face_recognizer.get_random_face_image_file_path()

    # Perform face recognition
    employee_id = face_recognizer.recognize(face_image_file_path)    

    # Check if recognized employee can access the resource
    if(access_schedule.can_access_today(employee_id)):
        # If so, print an information and track activity
        print('Access granted for employee: ' + employee_id)
        print('\nTracking actions...')

        # Track actions
        activity_tracking.add_action(employee_id, "Performed X action")
        activity_tracking.add_action(employee_id, "Performed Y action")
        activity_tracking.add_action(employee_id, "Performed Z action")
        activity_tracking.add_action(employee_id, "Signing out")

        # Write activity to the remote database
        activity_tracking.transfer_actions_to_remote_database()

        # Display actions stored in the remote DB
        activity_tracking.display_employee_actions(employee_id)

    else :
        print('Access denied for employee: ' + employee_id)    