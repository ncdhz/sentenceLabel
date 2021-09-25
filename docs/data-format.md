# 数据格式

显然任何软件都不可能支持所有格式的数据，这个软件也一样，他只支持特定格式的数据（不过此软件可以通过配置文件来修改对应的名称）。

1. 还是对着刚开始我们列举的例子来讲解对应的格式

```json
{
    "data": [
        {
            "answer": "B",
            "options": [
                "Went to the amusement park",
                "Went to the park",
                "Go home and sleep"
            ],
            "question": "Where did Xiao Ming go this noon?",
            "article": "Xiao Ming got up early today. He went to the park at noon. He went to the amusement park in the afternoon. He goes home to bed at night."
        }
    ]
}
```

+ 首先映入眼帘的是，这是一个典型的 `Json` 格式（也就是说我们的软件只支持 Json 格式）。
+ 第一层级分解，他首先有一个 `data` 字段（是一个数组），用来存放我们需要打标的文章

```json
{
    "data": []
}
```

+ 接下来我们分析一下，文章的格式。他有四个字段 `article`、`question`、`options` 和 `answer`，分别对应的是文章问题选项和答案，其中文章和问题是一个字符串，选项是一个数组，数组中按顺序存放着答案（答案也是字符串），答案是用 `A、B、C、D... or a、b、c、d... or 0、1、2、3...` 这种形式存放的（如果用数字存放答案，必须从 0 开始）

```json
{
    "answer": "B",
    "options": [
        "Went to the amusement park",
        "Went to the park",
        "Go home and sleep"
    ],
    "question": "Where did Xiao Ming go this noon?",
    "article": "Xiao Ming got up early today. He went to the park at noon. He went to the amusement park in the afternoon. He goes home to bed at night."
}
```

+ 经过上面的讲解，在使用本软件之前，我们应该把数据处理成以下格式，然后再用本软件打开数据

```json
{
    "data": [
        {
            "answer": "str or int",
            "options": [
                "str",
                "..."
            ],
            "question": "str",
            "article": "str"
        }
    ]
}
```