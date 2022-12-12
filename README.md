test_create_pet_simple_with_long_name_in_data не проходит, т.к. поле ошибочно принимаем строку свыше 256 символов
test_create_pet_simple_with_long_anymal_type_in_data не проходит, т.к. поле ошибочно принимаем строку свыше 256 символов
test_create_pet_simple_with_invalid_data не проходит, т.к. сервер принимает пустую строку в обязательном поле
test_unsuccessful_update_self_pet_info не проходит, т.к. сервер в поле принимает строку длинной более 256 символов