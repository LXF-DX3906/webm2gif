一个将webm转为gif文件的小脚本

依赖：`moviepy`

```shell
pip3 install moviepy
```

使用方法:

```shell
# 单文件
./webm2gif.py -i <file_name.webm> -o <output_filname.gif>

# 批量
./webm2gif.py -i <in_directory> -o <output_directory>
```

