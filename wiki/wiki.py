from wikiFunction import *

# версаль https://ru.wikipedia.org/wiki/%D0%92%D0%B5%D1%80%D1%81%D0%B0%D0%BB%D1%8C
flink_array = []

while True:
    first_page = input("first page wiki: ")
    find_links(first_page, flink_array)
    print(f"len array: {len(flink_array)}")
    
    
    while True:
        for link in flink_array:
            
            print("собираю ссылки с сайта: " + link)
            
            temp_flink_array = []
            find_links(link, temp_flink_array)
            flink_array.extend(temp_flink_array)
            print(f"len array: {len(flink_array)}")
            temp_flink_array = []
            
            if "https://ru.wikipedia.org/wiki/%D0%A4%D0%B8%D0%BB%D0%BE%D1%81%D0%BE%D1%84%D0%B8%D1%8F" in flink_array:            
                print("ФИЛОСОФИЯ НАЙДЕНА!")
                break

