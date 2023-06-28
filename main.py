import json
import config


def answer_questions(data):
    for key in data:
        if key == "student_name":
            data[key] = input("write your name: ")
        if key == "student_surname":
            data[key] = input("write your surname: ")
        if key == "exam_content":
            for key_question, question in data['exam_content'].items():
                print(key_question, ":")
                for answers, value in data['exam_content'][key_question].items():
                    print(answers, ":", value)
                data["exam_content"][key_question] = input("Your answer: ")


def main():
    with open(config.exam_file) as file:
        data = json.load(file)

    answer_questions(data)

    with open(config.answers_file, 'w') as file:
        json.dump(data, file, indent=4)

    print(config.answers_file)


if __name__ == '__main__':
    main()
