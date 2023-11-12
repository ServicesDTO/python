import os


def print_data():
    with open("phonebook.txt","r",encoding="utf-8") as file:
        phonebook_str = file.read()
    print(phonebook_str)
    print()

def input_name():
    return input("Введите имя контакта: ")

def input_surname():
    return input("Введите фамилию контакта: ")

def input_patronic():
    return input("Введите отчество контакта: ")

def input_phone():
    return input("Введите номер телефона контакта: ")

def input_address():
    return input("Введите адрес контакта: ")

def input_data():
    name = input_name()
    surname = input_surname()
    patronic = input_patronic()
    phone = input_phone()
    address = input_address()
    my_rep = " "
    return f"{surname}{my_rep}{name}{my_rep}{patronic}{my_rep}{phone}\n{my_rep}{address}\n\n"


def add_contact():
    new_contact_str = input_data()
    with open("phonebook.txt","a",encoding="utf-8") as file:
        file.write(new_contact_str)

def search_contact():
    print("Вариант поиска:\n"
          "1. По Фамилии \n"
          "2. По имени\n"
          "3. По отчеству\n"
          "4. По телефону\n"
          "5. по адресу \n")
    command = input("Выберите вариант поиска: ")

    while command not in ("1","2","3","4","5"):
        print("Некорректный ввод, повторите запрос")
        command =  input("Выберите вариант поиска: ")
    
    i_search = int(command)-1
    search = input("Введите данные для поиска: ").lower()
    print()

    with open("phonebook.txt","r",encoding="utf-8") as file:
      contacts_list =  file.read().rstrip().split("\n\n")

    check_cont = False
    for contact_str in contacts_list:
        lst_contact = contact_str.lower().replace("\n", " ").split()
        if  search in lst_contact[i_search]:
            print(contact_str)
            print()
            check_cont = True
    if not check_cont:
        print("Такого контакта нет!")

def copy_string():
    command = input("Выберите номер строки справочника, которую нужно скопировать : ")
    
    i_copy = int(command)-1
    with open("phonebook.txt","r",encoding="utf-8") as file:
      contacts_list =  file.read().rstrip().split("\n\n")
    
    contacts_list = list(map(lambda x: x.replace("\n","") , contacts_list))
    
    if len(contacts_list) < i_copy:
        print("Ошибка, такой строки нет в справочнике")
        interface()
    else:
        with open("phonebook_copy.txt","a",encoding="utf-8") as file:
            file.write(contacts_list[i_copy] + "\n")




def interface():
    with open("phonebook.txt","a",encoding="utf-8"):
        pass
    command = ""
    os.system("cls")
    while command != "5":
        print("Меню пользователя: \n"
              "1. вывод данных на экран: \n"
              "2. добавить контакт:\n"
              "3. поиск контакта: \n"
              "4. скопировать данные.\n"
              "5. Выход \n")
        command =  input("Выберите пункт меню: ")

        while command not in ("1","2","3","4","5"):
            print("Некорректный ввод, повторите запрос")
            command =  input("Выберите пункт меню: ")

        match command:
            case "1":
                print_data()
            case "2":
                add_contact()
            case "3":
                search_contact()
            case "4":
                copy_string()    
            case "5":
                print("Завершение программы.")
        print()

if __name__ == "__main__":
    interface()
                
            
