from app.core.collections import student_collection

# inserting data in database

async def add_student(student):

    result = await student_collection.insert_one(student)

    return result.inserted_id
