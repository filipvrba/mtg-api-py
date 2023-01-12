import sqlite3


def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}


def get_content(execute):
    content = None
    connection = sqlite3.connect("all_printings.sqlite")
    connection.row_factory = dict_factory

    try:
        cursor = connection.cursor()
        result = cursor.execute(execute)
        content = result.fetchall()
    except Exception as e:
        content = {
            "code": "Error",
            "message": e.__str__()
        }

    connection.close()
    return content
