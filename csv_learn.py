import csv

with open('eggs.csv', newline='') as f:
    spamreader = csv.reader(f, delimiter=' ', quotechar='|')
    # delimiter 允许使用不同的定界符
    for row in spamreader:

        for e in row:            
            print(e)

    spamwriter = csv.writer(f, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    nms = []
    
    for row in nms:
        spamwriter.writerow(row)


    # 将读取的信息映射到字典中。 字典的键可以使用fieldnames参数传入，也可以从 CSV 文件的第一行推断出来
    # fieldnames 参数是一个 sequence。如果省略 fieldnames，则文件 f 第一行中的值将用作字段名。无论字段名是如何确定的，字典都将保留其原始顺序。
    reader = csv.DictReader(f)

    for row in reader:
        print(row['min'], row['avg'], row['max'])

    fnames = ['first_name', 'last_name']
    writer = csv.DictWriter(f, fieldnames=fnames)    

    writer.writeheader()
    writer.writerow({'first_name' : 'John', 'last_name': 'Smith'})

    # 指定方言
    csv.register_dialect("hashes", delimiter="#")
    writer = csv.writer(f, dialect="hashes")
    writer.writerow(("pens", 4)) 

    # csv.unregister_dialect(name)
    # 从变种注册表中删除 name 对应的变种。如果 name 不是已注册的变种名称，则抛出 Error 异常。

    # csv.get_dialect(name)
    # 返回 name 对应的变种。如果 name 不是已注册的变种名称，则抛出 Error 异常。该函数返回的是不可变的 Dialect 对象。

    # csv.list_dialects()
    # 返回所有已注册变种的名称。

    # csv.field_size_limit([new_limit])
    # 返回解析器当前允许的最大字段大小。如果指定了 new_limit，则它将成为新的最大字段大小。