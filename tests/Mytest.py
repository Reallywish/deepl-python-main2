import deepl
import docx
import os

translator = deepl.Translator("6363fb24-c0a9-cf1c-4a9e-edcd43d6769c")


# translator = deepl.Translator("6ea368c8-9799-5676-d137-4c1c8417e107:fx")

#  传入内容，直接返回翻译内容
#  参数说明：
#  text-> 要翻译的内容
#  target_lang-> 文本应翻译成的语言
#  source_lang-> 要翻译文本的语言
# result = translator.translate_text(text="The table is green. The chair is black.", target_lang="ZH", source_lang="EN")
# print(result)


# 将多个文本翻译为英语,跟上面那个调的同一个api，参数text支持数组类型。
# result = translator.translate_text(text=["お元気ですか？", "¿Cómo estás?"], target_lang="EN-GB")
# print(result[0].text)  # "How are you?"
# print(result[0].detected_source_lang)  # "JA"
# print(result[1].text)  # "How are you?"
# print(result[1].detected_source_lang)  # "ES"


# 将文件翻译
def translateFile_docx(sourceFile, resFile, target_lang, source_lang=None):
    sour_file = docx.Document(sourceFile)
    with open(resFile, "w+") as res_file:
        for f in sour_file.paragraphs:
            try:
                if source_lang is None:
                    res = translator.translate_text(text=f.text, target_lang=target_lang)
                else:
                    res = translator.translate_text(text=f.text, target_lang=target_lang, source_lang=source_lang)
                res_file.write(str(res) + "\n")
            except:
                print("可能文件中有图片")


def get_files(path, target_lang):
    files = os.listdir(path)
    for file in files:
        source_file = path + file
        res_file = path + file.split(".")[0] + "_" + target_lang + ".docx"
        print(source_file)
        print(res_file)
        translateFile_docx(source_file, res_file, target_lang=target_lang)


if __name__ == '__main__':
    get_files("C:\\Users\\Administrator\\Desktop\\新建文件夹\\", "ZH")
