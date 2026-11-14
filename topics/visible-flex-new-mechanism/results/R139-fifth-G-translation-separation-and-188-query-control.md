# R139：第五次 G 平移严格分离与一百八十八个真实联合查询

日期：2026-11-14。**已证明；只消费一个新权块的公开实际。**

记完整响应空间为 $R=\mathcal R_8$，真实第四成本空间为 $U=\mathcal U_4$，
$A_G=R+\operatorname{span}\operatorname{Orb}(G)$。本次得到

$$
\boxed{\dim R_{-4}=40,\quad N^5G\notin R,\quad6\le s\le10,}
\tag{1}
$$

其中 $s=\dim(A_G/R)$。结合已经支付的同一纯尾映射的核，

$$
\boxed{\dim R\ge182,\quad\dim A_G\ge188.}
\tag{2}
$$

R120 使 $A_G$ 包含于真实闭成本锥的 lineality；R122 的实际有限构造因而支付
至少 188 个共同独立实查询。R136 另已给 $U/A_G\ne0$，所以本稿还严格推出
**$\dim U\ge189$**。这个额外 1 不计入 lineality 或有符号查询数。

## 1. 新实际及其完整来源

[公开 run 43654534244](https://github.com/Rogerhu12/math-research-public/actions/runs/43654534244)，
source `1177f251dc3d9455adf88b585e4c0e4bd6f7e69b`，lane `g_translation_successor`，
实际显式参数 `--order 5`。驱动
[literature_G_translation_successor.py](../scripts/literature_G_translation_successor.py)
仍为 39670 B，SHA256
`a4583ea776facd4ec4d92a121fed2e79af8de20d57bffc5fa22e47a8026ef406`。

紧前 R135 的 run 43653875461、source 481bb84991ff27a177f9524a38f8a4324dadefae、
25739 B 主报告、34427 B 发布回执、原生产器和两模式 N⁴G 哈希均显式绑定。
本次没有把默认 N²G 证据用于任意后继。相同字节驱动的 19 项开发检查复用
run 43653293263 已发通过证据；没有机械重跑旧开发或旧数学结论。

实际正常 complete，耗时 **25.043468767999997 秒**，峰值 RSS
**125.33984375 MiB**。没有重编旧 forcing、原局部生成元、第三模板或以前各权响应块。

## 2. 同右锚真平移与完整原列上界

使用 R126/R131 的真正 profile 平移生成元

$$
N(\xi)=1,\qquad N(q^{(j)})=N(\bar q^{(j)})=0,
\qquad N(IF)=I(NF).
$$

输入与右锚共同运输；这不是固定输入的完整空间导数。G 的真权为 1，故 N⁵G
的真权为 −4。原目标为：

| 模式 | 原式 SHA256 | 原项数 |
|---|---|---:|
| −4 | `738a4accaf1fcd03482336d25cda192571c6e613faabdd0f1d4d43a612d384a1` | 174 |
| −2 | `2cd42bf47f4109bbab5e0947c53a835a5ff5745bb8efb07aaed6a4fbabb18290` | 772 |

完整 E8×W36 表的真权 −4 原列恰为 **50** 列，每个实系数同时作用于两模式。
有声正规形式仅提出候选依赖；最终保留原列

~~~text
0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,
21,22,23,24,26,27,28,29,30,32,34,35,36,37,41,42,43,44,45,49
~~~

其余 **10** 条有理依赖逐一回到完整两模式原式核零。全部原式依赖的规范 SHA256 为

`866e724012d102537c7ff1da010c5deb5d94d1ab19cffb601552248043f8f0ab`。

所以真实函数空间中 $\dim R_{-4}\le40$。此上界没有把非零 word 代表当作线性独立证据。

## 3. 原有理 40/41 子式给出严格非成员

用同一个实测试对

$$
f=t^8(1-t)^8,\quad g=f(1+2t+3t^2+5t^3),\quad q=f+ig,
\qquad t=\xi-2\in[0,1],
$$

共同右锚为 3，外侧零延拓。该输入是 C⁷；本块实际最高输入 jet 为 4，足以
定义全部原式并使用光滑逼近连续性。它未被冒称为已配平三矩的合法圆。

在 $t=j/25$，$j=1,\ldots,24$ 上依次取 −4 实/虚、−2 实/虚，共 96 个原有理查询。
令 A 为 40 个保留原列，b 为 N⁵G 的原评价列。选行

~~~text
J=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,
   22,23,26,27,30,31,34,35,38,39,42,43,46,47,50,51,54,55,58,59,62),
e=63.
~~~

在已检查素数 $p=2147483647$ 下，实际

$$
\det A_J\equiv1532152211\ne0,\qquad
\det\begin{pmatrix}A_J&b_J\\A_e&b_e\end{pmatrix}
\equiv1412276136\ne0\pmod p.
\tag{3}
$$

全部遇到的 77 个有理分母均可逆；最大原多项式次数 74。
完整 41×41 增广模矩阵在完整报告中，规范 SHA256
`4846f99370541159cd40369f6d51a3600be31685e3992df0981641e1cce67881`。

以原有理矩阵定义

$$
\Lambda_0(V)=\operatorname{ev}_e(V)-A_eA_J^{-1}\operatorname{ev}_J(V).
\tag{4}
$$

它按定义准确杀全部 40 个保留原列，再由十条原式关系杀全部 50 列。
而 $\Lambda_0(N^5G)\equiv1903604729\ne0\pmod p$。
这是原有理泛函的合法非零约化；模系数不是其有理系数，也不提供实数符号。

原 40 阶子式与真上界合并得 $\dim R_{-4}=40$；增广子式给 $N^5G\notin R_{-4}$。
真实缩放的直和分解再提升为 $N^5G\notin R$。没有声称固定测试对上的 (4)
还杀掉其他权的评价列。

## 4. 六个权的核与真实可调子空间

R118、R126、R128、R131、R135 与本稿的非成员分别处于
$1,0,-1,-2,-3,-4$，所以它们的商类独立。原显式坐标次数至多 9 仍给
$N^{10}G=0$，得到 $6\le s\le10$。

R116 的同一真实映射 $\Pi_8:R\to T$ 满射，$\dim T=31$。已证明各权的数据为

| 真权 | 完整响应维数 | 同一纯尾像维数 | 核维数 |
|---:|---:|---:|---:|
| 1 | 7 | 1 | 6 |
| 0 | 16 | 3 | 13 |
| −1 | 29 | 6 | 23 |
| −2 | 40 | 6 | 34 |
| −3 | 44 | 5 | 39 |
| −4 | 40 | 4 | 36 |

不同真权的核直接相加，因此

$$
\dim\ker\Pi_8\ge6+13+23+34+39+36=151,
\quad\dim R\ge31+151=182.
\tag{5}
$$

加上六个 G 商方向给 $\dim A_G\ge188$。这是同一真实函数空间和同一映射上的
秩—零化度计算，不是相加多个不同输入的采样秩。

R120 给 $A_G\subseteq C\cap(-C)$，所以 lineality 至少 188 维。
R122 的构造保全部真实 prototype、桥、N²/N³ 基准成本，先有限缩放，再中央复制，
最后响应复制，支付至少 188 个实际共同查询。合法圆由 R96 的同一忠实表示
选择；并非上面的未经配平测试对。没有授予任意预先指定的窄区间或有界总长。

R136 的完整加速度 J 已证明不在整个 $A_G$ 中，因而 **$\dim U\ge189$**。
这不能自动把查询数也改成 189：J 目前只有真实 span 成员性，双向实际可调尚未支付。

## 5. 完整原式和下一门

目录为 `notes/actions-43654534244-1-g_translation_successor`。

| 文件 | bytes | SHA256 |
|---|---:|---|
| [主报告](../notes/actions-43654534244-1-g_translation_successor/G-fifth-translation.json) | 24966 | `faf6c2a0019ce614bb8d6f28b049f0a38a6c2f6e2e00930a1beab17e6c86f93e` |
| [发布回执](../notes/actions-43654534244-1-g_translation_successor/receipt.json) | 34625 | `e8f37f37ba85f822e6eacc17167fb6941017dc05ec7670b8fafa7b450dc4d24d` |
| [完整数学证书](../notes/actions-43654534244-1-g_translation_successor/G-fifth-translation-complete-report.json.gz) | 34287 | `98b404bcaf175d4d22784dc4e2a833171e6283ab0c7e973bd3432219ee5ef4f4` |
| [全部新原式](../notes/actions-43654534244-1-g_translation_successor/G-fifth-translation-original-expressions.json.gz) | 76352 | `b266eebf27d001ef90fcc94f8b49b9f9984ed5d3f7a047d9b5cef5ddffd2423b` |

完整数学原文 146781 B，SHA256
`579c6a5053cab6f80a85611a17d36ea396a1e848eaace1ba7feaf81c3f383b37`。
可携原式原文 427950 B，SHA256
`6e19e56d879eed7f7d741957526679521f65f06b92c42b4cb29f39fb2c2276e4`；
含全部 50 列及目标的 102 个根、933 atoms、19122 个根单项，没有只存基列或哈希。

下一链问题仅为 N⁶G 的新权 −5；首次得到真实成员或零目标时按 R122 停止并确定 s。
R136 已排除 $U=A_G$，故完成这条链只确定已知可调部分，不再作为完整成本已经解决的前提。
新 J 的正性/lineality 接 R137/R140。完整函数、ruling、全部高阶、有限等距族、闭嵌入、
reach 和主课题宏观运动仍未完成。
