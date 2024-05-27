import objc
from Foundation import NSBundle
from Quartz import *

# Загрузка Carbon фреймворка
carbon_bundle = NSBundle.bundleWithPath_("/System/Library/Frameworks/Carbon.framework")
objc.loadBundleFunctions(carbon_bundle, globals(),
                         [("TISCreateInputSourceList", b"^{__CFArray=}@?@"),
                          ("TISSelectInputSource", b"i@"),
                          ("TISGetInputSourceProperty", b"@^v@")])

kTISPropertyInputSourceID = objc.selector(b'__cfstring')
kTISCategoryKeyboardInputSource = b'__cfstring'


def switch_to_input_source(source_id):
    # Получение списка всех источников ввода
    source_list = TISCreateInputSourceList(None, False)

    for source in source_list:
        # Получаем идентификатор текущего источника ввода
        source_id_value = TISGetInputSourceProperty(source, kTISPropertyInputSourceID)

        if source_id_value:
            source_id_value = str(source_id_value)

            # Если идентификатор совпадает с нужным, переключаем раскладку
            if source_id_value == source_id:
                status = TISSelectInputSource(source)
                return status == 0

    return False


# Пример использования:
# Замените "com.apple.keylayout.US" на идентификатор нужной вам раскладки
result = switch_to_input_source("com.apple.keylayout.US")
print(f"Раскладка изменена: {result}")
