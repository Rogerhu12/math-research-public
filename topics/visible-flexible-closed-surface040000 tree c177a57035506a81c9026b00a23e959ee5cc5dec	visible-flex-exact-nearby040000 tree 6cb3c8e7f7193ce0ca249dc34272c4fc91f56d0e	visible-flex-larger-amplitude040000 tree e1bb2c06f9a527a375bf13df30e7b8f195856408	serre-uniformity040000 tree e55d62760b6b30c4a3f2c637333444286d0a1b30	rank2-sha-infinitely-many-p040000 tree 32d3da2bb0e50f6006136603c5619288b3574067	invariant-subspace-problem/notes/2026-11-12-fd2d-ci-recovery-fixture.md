# CI恢复脚本的真实隔离执行

两个新源码不仅作了语法编译，也在/tmp的三个独立bare-git仓库真正执行。没有操作真实GitHub origin。

- 正常分支：run=0、publish=0，远端实际得到产物提交。accepted-0001未进入清单，最后accepted-0002大于1MB的实体实际以gzip纳入。
- 并发改动：另一个clone向ROOT LOG和HANDOFF追加人类文字；本批真正pull/rebase后只合并自己的LOG行和H CI块，publish=0，全部人类文字在远端保留。
- 真实失败与规则变更：第一个子命令exit7，第二命令未执行；另一个clone随后修改根README，publish紧随pull读到差异并exit78，远端HEAD仍是新规则提交，本批没有推改它。

最终源码身份、三次实际fixture工作路径和真实tool回执见同名receipt。首次fixture真实exit1定位了长python -c代码误当文件名的ENAMETOOLONG；已修正。另一静态定位的LOG UTC重试漂移已改为沿用marker所在完整原行，gzip归档也禁止覆盖已有文件。

这只是基础设施运行证据，不是数学解成功、连续metric或任何强几何验收。接下来主代理在恢复仓库使用同一数值主线；CI保留为可恢复的普通git后备。
