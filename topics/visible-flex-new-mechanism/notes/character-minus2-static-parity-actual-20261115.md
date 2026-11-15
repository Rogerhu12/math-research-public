# 静态负方向与完整二阶奇偶联合续算：实际回执

日期：2026-11-15。公开 run **43668125602**，研究 source **c8a89721ee361074096b202af6aa0841ac1bc445**。

## 1. 本轮准确结论

联合续算完整结束，并保存一个满足更新必要系统的非零有理外部点。因此这份有限系统仍未排除全部非零权 −2 正字符。

程序确实加入了 R166 的静态必要行和 R168 的完整三族二阶反射奇偶。它没有重建旧等式、旧 RREF、旧半空间或六条路径积分。实际耗时 **0.42743059900000446 秒**，峰值 RSS **89.68359375 MiB**，不是预算退出。

这个非零点仍只是外部必要系统中的点，不是真实正字符或真实泛函存在证明。未表达的原函数依赖和未测试的全路径条件仍有可能排除它。

## 2. 新增行的精确作用

输入是原 run 43665971895 的完整有理证书：107 个 normal 坐标、124 条已存准确等式、其 RREF、23 个旧自由坐标，以及 63 条旧约化半空间。旧等式秩 84 与自由编号全部原样继承。

本轮新增计数：

| 对象 | 实际值 |
|---|---:|
| 继承的约化半空间 | 63 |
| 新静态行 | 1 |
| 扫描出的错误奇偶系数 | 4 |
| 两个符号去同后新增奇偶半空间 | 4 |
| 更新后约化半空间总数 | 68 |

“4 个系数”和“4 条新增半空间”不被解释为四个新独立真实关系。原 RREF 没有重算，程序也没有宣称更新后外部等式空间仍有 23 个独立自由方向；23 仅是继续使用的原坐标接口。

静态行先在原 normal 坐标中由已存 F0 系数组成，沿原 $x=B y$ 代入后，准确为

$$
-\frac3{16}y_0-\frac{15}{64}y_1-\frac14y_2-\frac34y_{12}\ge0.
\tag{1}
$$

正整数归一化后的行编号 63 是

$$
-12y_0-15y_1-16y_2-48y_{12}\ge0.
\tag{2}
$$

原已发表候选在归一化前的值为 $-11/64$，因此确被切除。新输出不是把旧点原样重新报告。

完整奇偶扫描覆盖：

| 族 | 已存全部次数 | 被要求为零的错误次数 |
|---|---|---|
| Q2_0 | 0, 1, 2 | 1 |
| Q2_1 | 1, 2, 3 | 2 |
| Q2_2 | 0, 1, 2, 3, 4 | 1, 3 |

每条错误系数在同一旧自由坐标中以正负两个半空间表达。相同行只引用已有索引，不改旧 record 的来源计数；经旧等式已为零的情况也保留扫描元数据。这里依据的是 R168 真实 corrected action 的反射等式，不是对原候选拟合奇偶。

## 3. 双证状态与外部点的含义

准确 Farkas 检验仍要求全部自由坐标的两个符号都有有理非负组合证书，才可宣称整个外锥为零。本轮在第 0 个旧自由坐标的正号目标处未取得该证书，随后保存了经过准确有理行验证的非零外部候选。

报告中 exact_dual_certificates=0 表示此次在首个未证目标停止前没有保存双证；它不表示各坐标都未受约束，也不表示新增成对等式没有效果。算法没有为了已经获得的非零外部点而继续重证其他坐标的显然零化。

浮点求解器的 status=2 不作为非成员或不可行证明。实际数学状态由已保存的准确外部点以及全部已列有理行来解释，仍明确为：

~~~text
positive_character_excluded = false
true_character_existence_claimed = false
complete_action_positivity_proved = false
complete_period_or_ruling_paid = false
~~~

下一步应读取这个新点的完整十四族系数，针对它检查一个具体真实门。现有 R165/R169/R170 等纸面条件可提供定向的有理行；本轮没有擅自扩大状态网或路径表，也没有预先宣称其中某条必定切掉新点。

## 4. 来源与输出

目录：
[actions-43668125602-1-character_minus2_static_parity](actions-43668125602-1-character_minus2_static_parity)。

| 文件 | 字节 | SHA256 |
|---|---:|---|
| character-minus2-static-parity.json | 6971 | bb2e66e4ddd6e0e826c8aa78cef96462e23290852f512b84ab0d3fceb800f968 |
| receipt.json | 40112 | 947bbcd35c08476233568a67c8f6b4c322bf8991284b8c9382fc65fea2ccd6d2 |
| character-minus2-static-parity-development.json | 2353 | 0ae6d3719d109e7f86d8cb9da5e18d713536596709419fed821507d6cbeb8edb |
| character-minus2-static-parity-certificate.json.gz | 9222 | 2431172cb890ad9d6bc7fa227793fabd9a33e5f254531ff2411b6fbc6870e3af |

完整证书 raw 为 34807 字节，SHA256：

~~~text
f15004c94a2400bf9fed2e9705227ba2cd1ca2dacc38080a25bf703e9f27ef23
~~~

源码链：

| 源文件 | 字节 | SHA256 |
|---|---:|---|
| literature_character_minus2_static_and_parity_cuts.py | 18508 | 9e7f7d2b9b70b78a3eec17f8c4c2e4cd64caf8d6304247355aaff55c962f41e1 |
| literature_character_minus2_static_cut.py | 26313 | d5a65482df040627b1a9a13fb8fce3e813f90e8ec196714cb9cf1bd78e97da5d |
| literature_character_minus2_finite_necessary.py | 45116 | d4c3751cf58f1ef08c534e61a16d7a40cd368980c0cca0ef48a0bce505ce3545 |

新公开 development 的八项专用人工全部通过，用时 0.0009907019999957356 秒。它没有读取真实 head，也没有重跑旧十三项或单 static-cut 的八项人工。实际继承的旧主/receipt/gzip 来源链全部由冻结输入身份绑定。

