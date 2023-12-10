def query(cursor, sql, params=None, is_execute=False):
    "pymysql 查询"
    # 执行查询
    if params is not None:
        execute = cursor.execute(sql, params)
    else:
        execute = cursor.execute(sql)
    # 获取查询结果
    results = None
    if is_execute is False:
        results = cursor.fetchall()
        if results:
            # 获取字段名
            column_names = [desc[0] for desc in cursor.description]
            # 构建字典列表，每个字典表示一行数据
            results = [dict(zip(column_names, row)) for row in results]

    return execute, results
