# R144：第七次 G 平移严格分离与二百三十个真实共同查询

日期：2026-11-15。**已证明；只消费一个新的完整权块。**

沿用 [R142](R142-sixth-G-translation-and-215-query-control.md) 的真实函数空间
$R=\mathcal R_8$、$U=\mathcal U_4$、$A_G=R+\operatorname{span}\operatorname{Orb}(G)$。
本次结论为

$$
\boxed{\dim R_{-6}=16,\quad N^7G\notin R,\quad 8\le s\le10,}
$$

$$
\boxed{\dim R\ge222,\quad\dim A_G\ge230,\quad\dim U\ge231.}
$$

R120、R122支付其中至少230维闭成本锥 lineality 及相应真实共同查询。
R136 的额外方向 J 不在整个 $A_G$，但尚未获得双向控制，不能把查询数改成231。

## 1. 实际来源与新的平移目标

[公开 run 43655713308](https://github.com/Rogerhu12/math-research-public/actions/runs/43655713308)，
source `d21c87a4d9341369a3dee35598ed88fb666cb99d`，lane `g_translation_successor`，
显式 order7。生产器仍为39670 B的
[literature_G_translation_successor.py](../scripts/literature_G_translation_successor.py)，SHA256
`a4583ea776facd4ec4d92a121fed2e79af8de20d57bffc5fa22e47a8026ef406`。
紧前 G6 的 main、receipt、run/source、生产器及两模式目标原哈希均显式绑定；
复用相同字节驱动已经公开通过的19项人工开发结果，没有重跑旧权块或旧 forcing。

本次 complete，实际耗时 **12.777465388999985 秒**，峰值 RSS **125.23828125 MiB**。
同右锚的真平移满足 $N\xi=1$、$Nq^{(j)}=N\bar q^{(j)}=0$、$N(IF)=I(NF)$，
并非固定输入函数的完整空间导数。G真权1，故本目标真权为−6。

| 模式 | $N^7G$ 原式 SHA256 | 原项数 |
|---|---|---:|
| −4 | `63eb0cc8ba1c72cbb8880551817c8861bcae9e437ded06bd4dce6dba1e9bf2c2` | 34 |
| −2 | `67e55d68ca5498a698438f389ffb28346aaed3da329cd024a5332183846ed09c` | 147 |

## 2. 真上界与完整原式非成员证书

完整 $E_8\times W_{36}$ 的新权−6恰有20原列，全部保两模式。保留原列索引为

~~~text
0,1,2,3,4,5,6,7,8,9,11,12,13,15,16,17
~~~

其余4条有理依赖分别回到完整原式核零，全部依赖规范 SHA256 为
`e91fc2506262b7b9e5b0ddb19864a123e4a037acc3a8bf0f5bae6ea6d28d4b2e`。
因此真实函数空间有上界 $\dim R_{-6}\le16$；不是从非零正规形猜独立性。

原有理评价仍用同一个测试对

$$
q=f+ig,\qquad f=t^8(1-t)^8,\qquad
g=f(1+2t+3t^2+5t^3),\quad t=\xi-2\in[0,1],
$$

右锚3，区间外零延拓。C⁷输入与所需最高jet4相容，并允许原式评价的光滑逼近；
此测试对不被冒称为满足低阶矩的合法圆。在 $t=j/25$、$1\le j\le24$ 的
两模式实/虚查询中，选取

~~~text
J=(0,1,2,3,4,6,7,10,11,14,15,18,19,22,23,26), e=27.
~~~

令 A 为16保留列的原有理评价矩阵，b为目标列。素数 $p=2147483647$ 下，
实际74个有理分母均可逆，且

$$
\det A_J\equiv100394708\ne0,\qquad
\det\begin{pmatrix}A_J&b_J\\A_e&b_e\end{pmatrix}
\equiv1731522970\ne0\pmod p.
$$

最高原多项式次数72；主报告保存完整17×17增广模矩阵。
定义在原有理评价上的泛函

$$
\Lambda_0(V)=\operatorname{ev}_e(V)-A_eA_J^{-1}\operatorname{ev}_J(V).
$$

它准确杀16个保留原列，借4条原式关系杀全部20列，而
$\Lambda_0(N^7G)\equiv1601033508\ne0\pmod p$。
模数只用于证明有理量非零，不给实数符号，也不把模系数误写成有理泛函系数。

16阶子式配合真上界给恰16维；17阶子式给新权块的真实非成员。
完整响应的真缩放直和再给 $N^7G\notin R$。不声称上述固定测试泛函还杀其他权。

## 3. 同一纯尾映射的核与真实可调维数

R142已在同一映射 $\Pi_8:R\to T$ 下得到总核至少177维，$\dim T=31$。
R116已付权−6的同一纯尾像维数2，因此新增真核恰为 $16-2=14$ 维。
不同真权的核直和，得到

$$
\dim\ker\Pi_8\ge191,\qquad \dim R\ge31+191=222.
$$

G至 $N^7G$ 的八个非成员分处八个真权，商类独立。原显式坐标次数≤9仍给
$N^{10}G=0$，故 $8\le s\le10$，以及 $\dim A_G\ge222+8=230$。
这里相加的是同一真实映射的不同权核，不是不同输入上的数值秩。

R120将整个 $A_G$ 放入真实闭成本锥 lineality；R122保留合法圆、端口、全部
prototype/连接/中央与响应复制基准及 N²/N³ 历史，支付相应至少230共同实查询。
这一结论不授任意预指定窄区间、总长、物理盒或有限等距族。
R136再给 $\dim U\ge231$，其J仍不加入有符号查询数。
R138的一般pure身份也不抹去这些完整两模式非零商类。

## 4. 完整公开证据

目录 `notes/actions-43655713308-1-g_translation_successor`。

| 文件 | bytes | SHA256 |
|---|---:|---|
| [主报告](../notes/actions-43655713308-1-g_translation_successor/G-seventh-translation.json) | 26745 | `f5e514164cede76ba91786833d455b4638a45a3ee82cd2b7cadbcd76ee18ff15` |
| [完整数学报告](../notes/actions-43655713308-1-g_translation_successor/G-seventh-translation-complete-report.json.gz) | 19158 | `818bc9e48b7b5999aa1a7c63f6cfd8a48ccb2ca9ca9cd129798ad328272474eb` |
| [完整新原式](../notes/actions-43655713308-1-g_translation_successor/G-seventh-translation-original-expressions.json.gz) | 15427 | `936a19bd60b49b236343cdea9466f8a2bbbfbf108b3163ffe6b25e99eb66a664` |
| [发布回执](../notes/actions-43655713308-1-g_translation_successor/receipt.json) | 35234 | `d1a5b9d8aa03553dfcf45731cbbbbb7861fbcbb496e90fb960e723e1597c3389` |

完整数学原文79832 B，SHA256
`ab5a8da0f9363b0eb04222b323dc501149f6b14e3f2d551a084304e3d354cfdc`。

完整新原式原文80081 B，SHA256
`cffc0109bccd0a2aeb4e6e23e400c2de94e0bde68c57b41f08df724cd37a9dcb`；
包含20原列与目标的全部42根、256 atoms、2746根单项。

下一只处理 $N^8G$ 的新权−7；首次准确成员或零目标立即停止链并确定s。
该链只完成已有可调子空间的结构，不能完成R136已证明更大的U。
完整正性、一般pure其他方向、ruling、高阶收敛及README的闭嵌入/全时reach/宏观
连续等距族仍继续推进。
