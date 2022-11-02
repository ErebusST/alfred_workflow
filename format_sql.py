# -*- coding: UTF-8 -*-
import re
import sys


def getParmeter(sql: str):
    parameters: list[str] = []
    regex = r":[a-zA-Z]+\w*"
    matches = re.finditer(regex, sql, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        group = match.group()
        field = group.removeprefix(":")
        # parameters.put("phone", phone);
        parameters.append(" parameters.put(\"" + field + "\", " + field + ");")
    return parameters


def isJavaCode(sql: str):
    return sql.find("sbSql.append(") >= 0


def fixSql(sql: str):
    # 清除 java 中的 注解以及空行
    lines: list[str] = sql.splitlines(True)

    def check(line: str):
        temp: str = line.strip()
        if len(temp) == 0:
            return False
        if temp.startswith("//"):
            return False
        if temp.startswith("if ("):
            return False
        if temp.startswith("} else"):
            return False
        if temp.startswith("StringBuilder sbSql"):
            return False
        if temp.startswith("Map<String, Object>"):
            return False
        if temp.startswith("parameters.put"):
            return False
        if temp == "}":
            return False
        return True

    return list(filter(check, lines))


def toJava(sql: str):
    data: list[str] = fixSql(sql)
    list: list[str] = ["StringBuilder sbSql = new StringBuilder();"]
    for line in data:
        # sbSql.append(" UPDATE event_give_the_phone ");
        list.append("sbSql.append(\" " + line.removesuffix("\n") + " \");")

    parameters = getParmeter(sql)
    if len(parameters) > 0:
        list.append("")
        list.append("")
        list.append("Map<String, Object> parameters = new HashMap();");
        for parameter in parameters:
            list.append(parameter)
    list.append("")
    return "\n".join(list)


def toSql(javaCode: str):
    lines: list[str] = fixSql(javaCode)
    list: list[str] = []
    for line in lines:
        temp = line.strip().removeprefix("sbSql.append(\"").removesuffix(" \");")
        list.append(temp)
    return "\n".join(list)


data = sys.argv[1]
# path = "/Users/situ/Desktop/sql.sql"
# file = open("/Users/situ/Desktop/sql.sql", "r", encoding="utf-8")
# data = file.read()
# print("输入的 sql:" + data)

javaCode = isJavaCode(data)

result = ""
if javaCode == True:
    result = toSql(data)
else:
    result = toJava(data)

print(result)
