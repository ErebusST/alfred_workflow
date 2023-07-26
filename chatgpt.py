import openai

# 设置 API Key，申请地址：https://platform.openai.com/account/api-keys
openai.api_key = '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'
# 设置组织，查看地址：https://platform.openai.com/account/org-settings
openai.organization = "org-WKKNogcuucdPs52TKIl7xBxP"
# 请求模型
model_engine = "text-davinci-002"
# 输入内容
prompt = "如何写一篇论文"
# 调用接口
completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)
# 输出结果
message = completions.choices[0].text
print(message)
