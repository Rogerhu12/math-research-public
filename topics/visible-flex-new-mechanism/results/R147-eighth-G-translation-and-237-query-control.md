# R147：第八次 G 平移分离与二百三十七个真实共同查询

日期：2026-11-15。**已证明；仅新增真权−7的完整响应块。**

沿用 [R144](R144-seventh-G-translation-and-230-query-control.md) 的
$R=\mathcal R_8$、$U=\mathcal U_4$ 与 $A_G=R+\operatorname{span}\operatorname{Orb}(G)$。
本次严格得到

$$
\boxed{\dim R_{-7}=7,\quad N^8G\notin R,\quad9\le s\le10,}
$$

$$
\boxed{\dim R\ge228,\quad\dim A_G\ge237,\quad\dim U\ge238.}
$$

前237维属于 R120 的真实闭成本锥 lineality，R122支付相应真实共同查询。
R136 的 J 只增加真实 U 的下界，仍未加入可自由取正负的控制数。

## 1. 唯一新实际及来源

[公开 run 43656638584](https://github.com/Rogerhu12/math-research-public/actions/runs/43656638584)，
source `6d02617d127fc9c6d3fbbd7d3458281603f16b52`，lane `g_translation_successor`，
显式 order8。生产器仍为39670 B的
[literature_G_translation_successor.py](../scripts/literature_G_translation_successor.py)，SHA256
`a4583ea776facd4ec4d92a121fed2e79af8de20d57bffc5fa22e47a8026ef406`。
紧前 G7 的 run/source、main、receipt、生产器和两模式原目标全部绑定；
同源19项已公开人工开发结果复用，没有重新计算旧响应块或原 forcing。

实际 complete，耗时 **4.910097854 秒**，峰值 RSS **125.08203125 MiB**。
保持同右锚真平移 $N\xi=1,Nq^{(j)}=N\bar q^{(j)}=0,N(IF)=I(NF)$。
G的真权为1，故 $N^8G$ 真权−7；不用固定输入的完整空间导数代替这个作用。

| 模式 | 原目标 SHA256 | 原项数 |
|---|---|---:|
| −4 | `1e0bc8e1d5e16c5b8da865563c6fde3d60bb5702f8a693590b9d3c22a7e4b792` | 10 |
| −2 | `eeb1d70da81a2a498e8bb6cc6bccbc8f4143e16a290889660b1757a13ca47df6` | 39 |

## 2. 恰七维及原有理非成员

完整 $E_8\times W_{36}$ 新权−7有8原列，保留索引

~~~text
0,1,2,3,4,5,7
~~~

剩余1条有理依赖已经回到完整两模式原式核零，规范 SHA256 为
`dcd5f267aec72dc59b5ac1018f837581861f46f04d05128a582c59fa4f71e822`。
它给真实函数上界 $\dim R_{-7}\le7$，不是把非零正规形当独立性。

使用 R144 同一原实测试对 $q=f+ig$，
$f=t^8(1-t)^8$、$g=f(1+2t+3t^2+5t^3)$，$t=\xi-2\in[0,1]$，
右锚3、外部零延拓。最高输入jet4，C⁷延拓允许全部所需原式评价及光滑逼近。
此处没有声称这个诊断测试对是合法低阶矩圆。

在 $t=j/25$、$j=1,\ldots,24$ 的两模式实/虚原查询中取

~~~text
J=(0,2,3,6,7,10,11), e=14.
~~~

令 A 为7保留原列的有理评价矩阵，b为目标列。已检查素数 $p=2147483647$ 下，
全部72个实际有理分母可逆，且

$$
\det A_J\equiv700074793\ne0,\qquad
\det\begin{pmatrix}A_J&b_J\\A_e&b_e\end{pmatrix}
\equiv691937332\ne0\pmod p.
$$

最高原多项式次数71。完整8×8模增广矩阵保存在主报告。
原有理泛函

$$
\Lambda_0(V)=\operatorname{ev}_e(V)-A_eA_J^{-1}\operatorname{ev}_J(V)
$$

准确杀7保留原列，借原依赖杀全部8列；目标值约化为
$1126381027\ne0\pmod p$。
模值只证明原有理量非零，不提供实数正负，也不把模逆冒称实有理系数。

7阶原子式与真实上界合并得恰7维，8阶增广子式给该权块的真实非成员。
真缩放权直和再给 $N^8G\notin R$。不声称该固定查询泛函杀其他权的全部评价。

## 3. 同一纯尾核与237个真实查询

R144给同一 $\Pi_8:R\to T$ 的核至少191维及像维数31；
R116给本权−7的同一像恰1维。因此新增核 $7-1=6$ 维，不同真权直接相加，

$$
\dim\ker\Pi_8\ge197,\qquad\dim R\ge31+197=228.
$$

G至 $N^8G$ 的九个非成员分处不同真权，所以商类独立。
原显式坐标次数≤9仍给 $N^{10}G=0$，遂 $9\le s\le10$，
以及 $\dim A_G\ge228+9=237$。

R120、R122的已有真实有限构造继续保全部端口、同一合法三矩圆、prototype、桥、
中央及响应复制基准和 N²/N³ 历史，故得到至少237共同实查询；没有重新跑旧构造。
R136证明J在**整个** $A_G$ 外，故 $\dim U\ge238$，但J还不是第238个有符号控制。
这些结论不授任意预定窄区间、长度、物理盒、完整ruling或有限连续等距族。

## 4. 完整公开证据

目录 `notes/actions-43656638584-1-g_translation_successor`。

| 文件 | bytes | SHA256 |
|---|---:|---|
| [主报告](../notes/actions-43656638584-1-g_translation_successor/G-eighth-translation.json) | 19980 | `86e032bb35f19c429d9f46217623fc972ff7fc4cf8071b82624da219c2f4bf55` |
| [完整数学报告](../notes/actions-43656638584-1-g_translation_successor/G-eighth-translation-complete-report.json.gz) | 11851 | `e9953e2103f32897e30c06690e0df7a43bbc11850e060e7f3f9268920b43a2f9` |
| [完整原式](../notes/actions-43656638584-1-g_translation_successor/G-eighth-translation-original-expressions.json.gz) | 6361 | `56dd71eb5e5f9749cd5543bb8b5aed4827f372c9657f1d038d22a5ce556c91c7` |
| [发布回执](../notes/actions-43656638584-1-g_translation_successor/receipt.json) | 35431 | `3e383001b2a63fc462cae22980a28937244e953220dffc13802007c15c679e68` |

数学原文52480 B，SHA256
`4d4e81ef10870cb0550b29b24d94c427114de80d4bcb3e55d685421fd12861bb`。
新原式原文25395 B，SHA256
`665effbb4b6ac73383f4e5143cdc05319d0a545b3300a68ef2f022faae4bec1a`；
保存8原列和目标的全部18原根、112 atoms、558根单项。

下一仅处理 $N^9G$ 的新权−8。首次准确成员或零目标即结束这条平移链并确定s；
若继续非成员，则原 $N^{10}G=0$ 上界已经给精确商维数。
这条链从R136起已明确不能完成整个U，后续仍须解决新J、完整action、一般pure、
ruling、高阶收敛，以及课题README的全部几何完成标准。
