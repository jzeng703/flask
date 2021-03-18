from flask import Flask, request, jsonify
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)


# @app.route("/", methods=["GET"])
# def server_status():
#     return "The server is on."


# @app.route("/info", methods=["GET"])
# def information():
#     output = "The server will allow the user to request blood analyses."
#     return output


# @app.route("/HDL", methods=["POST"])
# def HDL_request():
#     """
#        input info: {"HDL": 60}
#     """
#     from blood_tests import analyze_HDL
#     in_data = request.get_json()
#     print(in_data)
#     HDL = in_data["HDL"]
#     result = analyze_HDL(HDL)
#     answer = {"HDL": HDL, "Analysis": result}
#     if answer != "Normal":
#         return "Bad HDL", 400
#     return jsonify(answer)

# @app.route("/say_hello/<name>")
# @app.route("/say_hello/<name>/<age>", methods=["GET"])
# def say_hello_function(name, age = 40):
#     next_year = int(age) + 1
#     output = "Hello there, {}! You will be {} old next year."\
#         .format(name, next_year)
#     return output


db = list()


def init_server():
    add_patient_to_db("Ann Ables", 101, "A+")
    add_patient_to_db("Bon Boyles", 102, "B-")


def add_patient_to_db(name, id, blood_type):
    new_patient = {"name": name,
                   "id": id,
                   "blood_type": blood_type,
                   "test": list()}
    db.append(new_patient)
    # print(db)
    logging.info(new_patient)
    return True


@app.route("/new_patient", methods=["POST"])
def post_new_patient():
    # get input data from requests
    in_data = request.get_json()

    # validate input & process patient
    answer, server_status = process_new_patient(in_data)

    return answer, server_status
    

def validate_blood_type(in_data):
    blood_types = ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]
    if in_data["blood_type"] not in blood_types:
        return "{} is not a valid blood type".format(in_data["blood_type"]), 400
    return True


def validate_new_patient_info(in_dict):
    expected_keys = ("name", "id", "blood_type")
    expected_types = (str, int, str)
    for key, ty in zip(expected_keys, expected_types):
        if key not in in_dict.keys():
            return "{} key not found".format(key), 400
        if type(in_dict[key]) != ty:
            return "{} key has the wrong value type".format(key), 400
    return True, 200


def process_new_patient(in_data):
    validate_input, server_status = validate_new_patient_info(in_data)
    if validate_input is not True:
        return validate_input, server_status

    valid_blood_type = validate_blood_type(in_data)

    add_patient_to_db(in_data['name'],
                      in_data['id'],
                      in_data['blood_type'])

    return "Patient successfully added", 200


if __name__ == "__main__":
    init_server()
    app.run()
