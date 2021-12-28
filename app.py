import json
import hashlib
import streamlit as st


def json2Md5(jsData):
    hashMd5 = hashlib.md5(jsData.encode('utf-8'))
    strMd5 = hashMd5.hexdigest()
    return strMd5


def isDict(strData):
    try:
        eval(strData)
    except SyntaxError:
        return False
    return True


def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


def main():
    with st.form("json2md5"):
        txData = st.text_area("json格式的交易数据:", height=200)
        submitted = st.form_submit_button("提交")
        if submitted:
            if len(str(txData)) < 2:
                st.error("交易数据格式错误，或数据不能为空!")
                return

            if isNumber(str(txData)):
                st.error("交易数据格式错误，不能为纯数字!")
                return

            if not isDict(str(txData)):
                st.error("交易数据格式错误，应为json格式，比如:[{},{}]")
                return

            jsData = json.loads(str(txData))
            md5 = json2Md5(str(jsData))
            st.write('json md5 =', md5)


if __name__ == '__main__':
    main()
