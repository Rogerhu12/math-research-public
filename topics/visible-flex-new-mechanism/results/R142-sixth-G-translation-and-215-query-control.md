# R142：第六次 G 平移严格分离，真实可调查询下界二百一十五

日期：2026-11-14。**已证明；消费一个新的公开权块。**

沿用 [R139](R139-fifth-G-translation-separation-and-188-query-control.md) 的
$R=\mathcal R_8$、$U=\mathcal U_4$ 与 $A_G=R+\operatorname{span}\operatorname{Orb}(G)$。
本次新结论是

$$
\boxed{\dim R_{-5}=29,\quad N^6G\notin R,\quad7\le s\le10,}
\tag{1}
$$

$$
\boxed{\dim R\ge208,\quad\dim A_G\ge215,\quad\dim U\ge216.}
\tag{2}
$$

前215维属于 R120 已证明的真实闭成本锥 lineality，并由 R122 支付相应共同实查询；
U 的额外至少一维来自 R136 的 J，目前不计入有符号控制。完整成本更大这一事实
没有因继续 G 链而改变。

## 1. 实际来源和唯一新目标

[公开 run 43655163769](https://github.com/Rogerhu12/math-research-public/actions/runs/43655163769)，
source `2fba8713aff3421ff14fe8bc63fb95199755abb2`，lane `g_translation_successor`，
显式 `--order 6`。生产驱动仍为39670 B的
[literature_G_translation_successor.py](../scripts/literature_G_translation_successor.py)，SHA256
`a4583ea776facd4ec4d92a121fed2e79af8de20d57bffc5fa22e47a8026ef406`。

前驱 G5 的 run43654534244/source1177f251、24966 B main/faf6c2a0、34625 B receipt/e8f37f37、
生产器及两模式目标原哈希均显式绑定。复用相同字节驱动的公开19项开发通过记录。
没有重编 G 至 N⁵G 的已付响应块、旧 forcing、W36 或旧分离证书。

本次正常 complete，耗时 **12.730878902000029 秒**，峰值 RSS **125.4375 MiB**。
同右锚真平移仍是 $N(\xi)=1,N(q^{(j)})=N(\bar q^{(j)})=0,N(IF)=I(NF)$，
不是固定profile的完整空间导数。G真权1，故 N⁶G 真权−5。

| 模式 | N⁶G 原式 SHA256 | 原项数 |
|---|---|---:|
| −4 | `b372ec641158ec30e76efdd451e140352f46f8b1e81f9c2bb7c7b35013798c95` | 87 |
| −2 | `e054a08b99abeb46bdeb750d9f1eee630a0d1b1788e6dec660b854f9b8f45fe4` | 384 |

## 2. 完整真实上界与原有理分离

完整 E8×W36 中真权−5恰有36原列，全部同时保两模式。保留的原列为

~~~text
0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,20,21,23,25,26,27,28,29,31,33
~~~

其余7条有理依赖逐一回到完整原式核零；全部依赖规范 SHA256
`769c76bb9fa0c20b8c22d2c468f7180e26e180b49ae3cbe24f363fdc4e55df01`。
因此 $\dim R_{-5}\le29$ 是真实函数上界，而非不完备正规形的独立性猜测。

用 R139 同一个实测试对
$f=t^8(1-t)^8,g=f(1+2t+3t^2+5t^3),q=f+ig,t=\xi-2\in[0,1]$，
右锚3、外侧零延拓。C⁷输入与本块最高jet4相容，也允许所需原式评价的光滑逼近。
没有把此测试对冒称为合法三矩圆。

在 $t=j/25,j=1,\ldots,24$ 的两模式实/虚原式查询中，取29个控制行

~~~text
J=(0,1,2,3,4,5,6,7,8,9,10,11,14,15,18,19,22,23,26,27,30,31,34,35,38,39,42,43,46),
e=47.
~~~

令 A 为29保留原列的有理评价矩阵，b为目标原列。已检查素数 $p=2147483647$ 下

$$
\det A_J\equiv813703351\ne0,\qquad
\det\begin{pmatrix}A_J&b_J\\A_e&b_e\end{pmatrix}
\equiv1219186308\ne0\pmod p.
\tag{3}
$$

全部75个实际有理分母可逆，最高原多项式次数73。主报告内直接保完整30×30模矩阵。
原有理泛函

$$
\Lambda_0(V)=\operatorname{ev}_e(V)-A_eA_J^{-1}\operatorname{ev}_J(V)
\tag{4}
$$

准确杀29个保留原列，由7条原式关系杀完整36列，而
$\Lambda_0(N^6G)\equiv1665464827\ne0\pmod p$。
模值只证明合法约化非零，不给实数符号，不把打印模系数冒成有理系数。

29阶原子式与真上界合并给恰29维；30阶增广子式给该权块的真实非成员。
再由完整响应的真实缩放直和得到 $N^6G\notin R$。不声称固定测试对上的(4)
还能杀其他权的评价列。

## 3. 同一纯尾核与215个共同查询

R139已付真权1至−4的同一 $\Pi_8:R\to T$ 的核至少151维，$\dim T=31$。
R116已付新权−5的同一纯尾像维数3，因此本次新增核

$$
\dim\ker(\Pi_8|R_{-5})=29-3=26.
$$

不同真权的核直接相加，故

$$
\dim\ker\Pi_8\ge177,\qquad\dim R\ge31+177=208.
\tag{5}
$$

G至N⁶G七个非成员分别处于不同真权，其商类独立；原显式坐标次数≤9仍给N¹⁰G=0，
所以 $7\le s\le10$。这给 $\dim A_G\ge208+7=215$。

R120、R122因此支付至少215维lineality和相应实际共同查询。有限构造仍保真实端口、
同一合法圆、全部prototype/连接/中央与响应复制基准，包括N²/N³项；这里未重跑旧控制。
它不授任意预指定窄区间、总长、物理盒或有限等距族。

R136已给J不在**整个** $A_G$，因此 $\dim U\ge216$。
J只是目前已知真实span的新方向，不能把215个已付有符号查询改成216。
R138又说明G商轨道可选pure恒零代表；一般pure身份并未抹掉完整两模式的这些商类。

## 4. 已保存的完整证据

目录 `notes/actions-43655163769-1-g_translation_successor`。

| 文件 | bytes | SHA256 |
|---|---:|---|
| [主报告](../notes/actions-43655163769-1-g_translation_successor/G-sixth-translation.json) | 42526 | `2e197e46a3e79487925b08a9fb2f8c44264199b9dbb380248d0373fdc8c819e6` |
| [完整数学报告](../notes/actions-43655163769-1-g_translation_successor/G-sixth-translation-complete-report.json.gz) | 31946 | `d3f9b312920c9676988147dc05ff48ad4872f49e90c8ee3d4291305e9ed83466` |
| [完整新原式](../notes/actions-43655163769-1-g_translation_successor/G-sixth-translation-original-expressions.json.gz) | 36336 | `c88d56ac3333867d5dbb643b44241f3b8bdfe2a3d6329206fdfeb4d42b633720` |

完整数学原文129246 B，SHA256
`b6d860e9bd1db065a77949e149dbaaf7f435423b9a7668e5f8c099e2d06bce1b`。
新原式原文204043 B，SHA256
`6feb1ab243ea9b9130f7e2bddfa16105065168b80aabadb6dd722dcddb236338`；
保存全部36列和目标的74原根、527 atoms、8310根单项。
[终端发布回执](../notes/actions-43655163769-1-g_translation_successor/receipt.json)绑定全部源与输出。

下一只处理N⁷G的新权−6；首次准确成员/零目标即停止并确定s。
该链只确定已有可调子空间。新J及完整成本的真实正性、ruling、高阶收敛、
闭嵌入、全时reach和宏观连续等距族仍须继续。
