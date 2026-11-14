# 纯 bulk 第四漂移与28个第三响应：首次完整代数实算

状态：**完整程序输出的准确代数证据；尚无 whole-function 抵消关系，也没有非成员定理。**

公开 Actions [43628716304](https://github.com/Rogerhu12/math-research-public/actions/runs/43628716304)，源 `e42c78ff34087089b8ce6ee74cb25a9a74bef7bd`，`p1_bulk_exact`成功完成。主文件为 `notes/actions-43628716304-1-p1_bulk_exact/p1-bulk-exact-membership.json`，16529字节，SHA256 `abb3d2afdb3622cc0314eeffb5769d250c4808cd4e301e1a359fb1fb8ab627ce`。公开producer `f7f3e3c6c8732ad9da047fb6005d314dc8568c189fe3cc0c9edef8843051eb70` 与开发版相同，R56依赖Git blob `01c7424af3a96f2c2a0f0cb0c782b2037ff3ec74`。publisher实际pull到 `b0c231e5ad6fb988c3f9e95a18844df794fdafab`，双README无差。

## 实际问题

同一个任意复光滑profile $q$，在共同右collar为零，物理区间紧含于 $(1,\infty)$。保普通复乘法，不换成正模平方。真实R56先编译全部history导数，再将进入段的history值设零，得到互反常态的纯第四目标 $P[q]/16$。

将R71的八矩两两交换子 $\tau_{ij}$ 送入真实响应

$$
H_A(\tau)(q)=\frac{D\tau(q)[A(q,q)]-2A(q,\tau(q))}{8}.
$$

所有控制系数是profile无关的常数；任意有限值可用固定有限数目的小loop实现。本次只检查纯bulk目标，未加入不同scalar基准桥第三成本。

## 实际输出

| 项 | 输出 |
|---|---:|
| 研究编译与消元用时 | 2.121130564秒 |
| 峰RSS | 36.703125MiB |
| 系数DAG节点 | 23131 |
| history状态 | 248 |
| profile atoms | 619 |
| 原始target项数 | 473 |
| 经过已实现合法改写的target项数 | 59 |
| 28个响应代表的准确有理数秩 | 18 |
| 消元后代表余项数 | 76 |
| 找到代表关系 | 否 |
| 产生并重核whole-function身份 | 否 |

余项SHA为 `f37a17713aeebf0b0c6a6268d4fde1edc62bf04c0f31be800ad5ae338b1fff21`。target原始SHA `a4d4c092f3ff4582b9bfe386a9f176eb36c47f8a25dd03abace8c19fb1b35685`，改写后SHA `09bad57d356dfb8683cf5999c66a0b31fafa3834a643e79e6132b86f4fcd6235`。已实现右IBP共375次primitive调用、234次唯一高jet改写、28次一级shuffle、4次幂shuffle，循环fallback为0。此处“秩18”只属于实现所用的形式代表；不能无证明称为真实函数空间维数。

## 能说明什么，不能说明什么

这次确实完成预定完整符号目标，既不是超时，也不是内存或项数上限导致的partial。没有理由仅增加原预算或重跑同一流程。

改写器只采用已证明正确的一部分右端分部积分及shuffle恒等式，**没有证明正规形式的唯一性或函数独立性**。因此代表余项非零不能推出纯bulk目标不在真实28响应跨度中；甚至代表秩18也可能继续下降。若后来得到零关系，该关系可以从原始表达式逐项重核成为证书；本次没有这样的正证书。

R73已把真实M0桥的第三history准确缩成可达交换子，但仍有局部三次密度积分。后续首先分析具体代数余项与该局部成本、以及还缺的合法改写或真实控制方向，不将这次代表消元包装成普遍不可能性。即使纯bulk关系解决，也还须同一真实桥/同一profile支付全部phase $P_1$、$P_0$和每个ruling，继而有限等距族、嵌入与宏观reach/幅度。

本次没有数值profile或几何积分，没有生成任何新曲面候选，主课题未完成。
