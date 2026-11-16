# R860 原半线性余子式源 DAG：实际首次激活

日期：2026-11-16。状态：**全部原源已明确，首次公开请求已写；实际运行与输出尚待该推送的真实 Actions 回执。**

证明 [R860](R860-original-adjugate-semilinear-descent-and-rational-differential.md) 的 SHA256 为 `7a200b7dd74e1fd51b43e2bac12d277f7b5a3e4fa4161f463bf8c20d51eadf3f`。这是已发布8c9ea5ae稿仅将错误交叉引用FM.23改为实际FM.27后的同一证明；数学未改。执行方法见 [完整契约](R860-original-semilinear-resolvent-DAG-method.md)。

| 文件 | bytes | SHA256 |
|---|---:|---|
| 方法 | 8537 | 20fa1948b7d13990cca9c157ed5f349058f75422e4d13dda9e3f445223f6395a |
| R860_original_semilinear_resolvent_DAG.py | 34469 | 4b70a64d3158ff7d0c5272562fab16722bc38af1fde466e93f7b6086d43724d5 |
| R860_public_original_semilinear_resolvent_DAG.py | 43434 | d9b7a23c8d09a633d8ec5ed720b247383b19c531af3bb833bb147129bbe43ca4 |
| R860-semilinear-resolvent-DAG-public-request.json | 27116 | d4becaf4c025ca21ecc15ac77b1118021ea7b56dc1c45da6ec8e942238f6a7c8 |
| serre-R860-original-semilinear-resolvent-DAG.yml | 6882 | f57cc45b9e0c65916171cd0fdc056d883c4a4d6d4b8c6347d59e4ee0fb2b6f05 |

## 实际空 runner 来源

本次61件原文件共有112979829字节：R805七件、R806四十五件、R853九件，全部原bytes/SHA/metadata与交叉基身份已有本地纯IO读取。它们仍保持旧数学producer/configuration，不改成新计算。

R806由实际已结束R815 run43777837244/source7cddfd0d5896f0d1ea7d49143dd1a91a68eb11d7的artifact14198893567取得。其真实原输入carrier为109958828B/`051571e117cdaafe31f9851c664c72583f55181444dbe112bbcbb7f2d2fbf1b3`，完整53成员核SHA后选R806的45件；R815此轮退出124且无core receipt，只承担原输入字节续存。原retained receipt为16388B/`7de014be25e8d963d651662a7670ba32c7fef4a1a571eb9854edb8a6868c28a0`，实际producer身份含certificate_name/certificate_sha256，封装按BASE身份及这两项分别核对。

R805由真实成功R856 run43805659598/sourceebdb4e512bb3cb8f8fadbb3bf2b9e69f11127051的artifact14198217155取得。其569原件carrier为13406926B/`fd6329bd17f2d729a3c3834e78fe7b4b626be84b692e77d0e51bbdf205f01e41`，全成员核后选七件。R853九件直接来自成功run43801910753/artifact14197275258。

新artifact只保61必要原输入、运输metadata及新完成stage；不将两个运输producer的所有大输出带入。原R805/R806已到期artifact不再是首次执行的必需下载路径。冻结纯IO helper为R837 eec99c9e、R824 c5907739，无数学核心导入或旧值重算。

## 实际 scope 与续算

预算60分钟。原34组W分子/逐列分母及完整S行映射构成有类型的系数索引，再构造D、N两个未展开determinant节点；N删行72/列0，D删行0/列0。由原primitive/次数与单项式结构给源绑定的非零分母证明。输出根是原β72=N/D、cYz=z−2β72、cYw=w、cYs=−s、δ与ν的准确下降接口。

不重原690基、272列820行乘回、旧cyclic见证或三个旧共轭。DAG构造成功不称二元多项式已展开、完整Krylov/normal半线性矩阵已得或RR/period已完成；分母不保证每个点为单位。

每个新stage原子保存；同tag直接恢复完成组/索引/表达式和最新current，旧false FINAL不锁住新阶段。完整source/manifest/真实结束回执在一日artifact中续存，raw不入Git/Release。局部仅AST、源码与真实源IO，没有新数学计算。

本推送触发后才登记真实run/job/source；主目标、原RR、η、Hecke/nonp校准和完整height仍开放。
