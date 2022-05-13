import re

with open("./potential-contacts.txt") as f:
    text_from_file = f.read()


def number_slicer(phone_number):
    actual_number = phone_number[:3] + '-' + phone_number[3:6] + '-' + phone_number[6:]
    return actual_number


def validate_nums(text):
    pattern = re.compile(r"\d{3}\D?\d{3}\D?\d{4}")

    extracted_nums = re.findall(pattern, text_from_file)

    cleaned_nums = []
    for num in extracted_nums:
        num = re.sub('[-.)(]', "", num)
        cleaned_nums.append(num)

        fixed_nums = []
        for number in cleaned_nums:
            final_num = number_slicer(number)
            fixed_nums.append(final_num)
            number_list = list(set(fixed_nums))

        print(number_list)

    with open("phone_numbers.txt", "w") as f:
        for x in number_list:
            f.write(x)
            f.write('\n')


# validate_nums(text_from_file)


def validate_email(text):
    pattern = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
    extracted_addys = re.findall(pattern, text_from_file)
    email_list = list(set(extracted_addys))

    with open("email.txt", "w") as f:
        for x in email_list:
            f.write(x)
            f.write('\n')


validate_email(text_from_file)
