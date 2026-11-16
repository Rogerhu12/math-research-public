# 原六次对称矩阵曲面恰有35个几何普通双点

作者：Astra-ISP-789f / normal_annihilator；与 /root 联合推导、独立核验。AI-assisted: GPT-6 Astra Pro。  
日期：2026-11-16（UTC）。  
**状态：已证明；同原系数重建、完整35维迹配对及全来源七次门均已实际完成。**

## 1. 同原曲面及结论

沿用[原完整六次矩阵族](R150-appendix-original-rank-three-mean-incidence-and-complete-sextic-pencil.md)的固定数域
$$
E=\mathbb Q[d]/(3725d^3-43931504d^2+6080833024d+52565262336)
$$
和四个原规范对称矩阵
$$
A(\mu)=\sum_{i=0}^3\mu_iT'_i\in\operatorname{Sym}_6(E[\mu_0,\ldots,\mu_3]).
$$
记
$$
\Delta(\mu)=\det A(\mu),\qquad
Y=V(\Delta)\subset\mathbb P^3_E,\qquad
Z=V(I_5(A))\subset\mathbb P^3_E.
$$
此前已付
$$
I_4(A)=(\mu_0,\mu_1,\mu_2,\mu_3)^4
\tag{1.1}
$$
及 $Z\subset\{\mu_0\ne0\}$。[原自由35证明](R150-appendix-original-corank-two-pencil-exception-algebra-has-free-rank-thirty-five.md)还给
$$
E[\mu_1,\mu_2,\mu_3]/I_5(A(1,\mu_1,\mu_2,\mu_3))
\quad\text{的维数恰为 }35.
\tag{1.2}
$$
本次在同一个原矩阵族上补全：

1. $Z$ 为 $E$ 上的有限 étale 概形，次数恰35；在代数闭包上是35个互异的 rank4 参数点。
2. $Y$ 的几何奇点恰为这35点，每个都是普通双点，即几何 $A_1$ 奇点；不存在 rank5 的其他奇点。
3. $Y$ 几何整且正规。
4. 原完整关联曲面
   $$
   X=\{([\mu],[y])\in\mathbb P^3_E\times\mathbb P^5_E:A(\mu)y=0\}
   $$
   光滑且几何整，投影 $X\to Y$ 是极小解消。全部35条例外纤维都是原完整核线，几何上为两两不交的 $(-2)$ 曲线。

“35个互异点”是几何结论，不是声称35点均在 $E$ 上有理。上述关联和解消完整保留 rank4 处的二维核。

这些结论仍没有消去 Bell=1 的全部剩余临界关系。原十七梯度、全部 moment 参数和原9×56表示的其余关系保持原范围；普通不变子空间问题不由本稿宣告完成。

## 2. 新计算重建的是逐项相同的原 $E$ 张量

本次没有恢复已经失效的旧大型系数数组。它只从两件已锁小源码重建完整原 $K,J_3,R_3$、全部17个原梯度和匹配 Bell 多项式，实际重新通过原 $N/\Gamma$ 身份、两侧 $J_3$ 逆及加权 Euler 等式。

原 Bell 系数写为
$$
B_r(y,H)=\beta(y)+y^{\mathsf T}MH.
$$
原固定 Hankel 坐标次序仍为
$$
P=(2,1,0,3,4,5),\qquad U=(6,7,8,9,10).
$$
[已付全局原坐标运输](R150-appendix-global-matched-bell-hyperbolic-coordinates-and-normalized-critical-ideal.md)为
$$
H=Lw+Nu-\tfrac13L\nabla_y\beta,\qquad
L_U=0,\quad L_P=M_P^{-1},\quad
N_U=I_5,\quad N_P=-M_P^{-1}M_U.
\tag{2.1}
$$
$[L,N]$ 是完整可逆的11×11常数矩阵。

令 $Q_m(u)$ 为原 $\partial_{H_m}R_3$ 在 $H=Nu$ 后的完整 $u^2$ 部分。新六个 $w$ 梯度和五个 $u$ 梯度的二次首项是
$$
\begin{pmatrix}L^{\mathsf T}\\N^{\mathsf T}\end{pmatrix}Q,
\tag{2.2}
$$
故它们和全部11个原 $Q_m$ 张成同一二次空间。

再令 $Y_{ij}(u)$ 为原 $\partial_{y_i}R_3$ 在 $H=Nu$ 后的 $y_ju^2$ 系数。由完整链式法则，新 mean 梯度的二次部分与
$$
\sum_jy_jY_{ij}(u)
$$
相差线性 $y$ 倍的 $Q_m$。$w$ 与纯 $y$ 平移不会改变这些最高二次系数。因此这里只需要原势函数的 $H^3$ 与 $y^2H^2$ 部分，但其定义和全部原来源仍来自完整原多项式。

在固定保留单项式
$$
v=(u_1u_4,u_2u_3,u_2u_4,u_3u_4)
$$
之外的11个二次位置上，实际原方块 $U_{11}$ 为单位。程序计算
$$
\widehat Y=Y-Y_{\rm elim}U_{11}^{-1}Q,
\tag{2.3}
$$
并核全部396个被消坐标和540个完整二次来源坐标。

旧算法先消5个平方、再消6个混合项；(2.3)一次消同一空间。两者均在同四个 $v$ 上取余项，而单位方块使该余项唯一。所以每个固定 mean 行、$y_j$ 及 $v_l$ 上的 $E$ 系数都相同，得到的就是[原四个 $T_l$](R150-appendix-complete-six-mean-relations-and-nine-bell-normalized-generators.md)，不是另一个仅模127相似的张量。

规范化仍用原四个上三角位置
$$
(0,0),(0,1),(0,2),(0,3).
$$
因此其固定常数逆给同一 $T'_l$ 和同一 $\mu_0=1$ 图。程序另核四个旧行列式剩余 $(106,93,100,92)$、原144个坐标返回和既有六次直线七系数。这些只是额外审计；同原性的证明是(2.1)–(2.3)及唯一余项。

所有 $E$ 运算均可按上述有限表达式重建，只除固定系数域常数，不除任何 $y,w,u,\mu$ 参数。没有用一组有限域行列式数值替代 $E$ 上的同原关系。

## 3. 原系数环上真自由35基

令
$$
\mathcal D=
\left(\mathbb Z_{(127)}[d]/(\operatorname{mon}f)\right)_{(127,d-100)},
\quad
f=3725d^3-43931504d^2+6080833024d+52565262336.
$$
$f$ 的原首项模127为42，且 $f'(100)$ 的模127剩余为49。因此这是同一 $E$ 的合法离散赋值环，剩余域为 $\mathbb F_{127}$。本次实际使用的原常数逆均有非零剩余，故(2.1)–(2.3)及原规范化都定义在 $\mathcal D$ 上。

设 $c_i$ 是 $A(1,\mu_1,\mu_2,\mu_3)$ 的21个原上三角余因子。写
$$
c_i=\sum_{|\alpha|=5}C_{\alpha i}\mu^\alpha+\ell_i,
\qquad\deg\ell_i\le4.
$$
本次从原矩阵重新建立全部21个余因子及整个21×21最高次系数方块，实际
$$
\det\bar C=103\in\mathbb F_{127}^{\times},
$$
其左右逆全部核验。于是每个五次单项式有真原来源
$$
\mu^\alpha-\rho_\alpha
 =\sum_i(C^{-1})_{i\alpha}c_i,\qquad
\deg\rho_\alpha\le4.
\tag{3.1}
$$
反复乘单项式并降低总次数，给满射
$$
\mathcal D^{35}\longrightarrow
\mathcal A_{\mathcal D}:=
\mathcal D[\mu_1,\mu_2,\mu_3]/(c_i).
\tag{3.2}
$$
35个生成元正是全部次数至多4的原普通单项式。

(1.2)说明(3.2)张量 $E=\operatorname{Frac}(\mathcal D)$ 后为35维空间之间的满射。其原核是 $\mathcal D^{35}$ 的子模，故无扭；核张量 $E$ 为零就迫其本身为零。因此
$$
\boxed{\mathcal A_{\mathcal D}\cong\mathcal D^{35}
\text{，以同35个原单项式为基。}}
\tag{3.3}
$$
这是从原单位降次和已付 $E$ 维数推出的真正平坦运输，不是先假模127保持长度。

## 4. 完整迹配对给35个几何互异参数

在(3.3)上，(3.1)给三张35×35原参数乘法矩阵。实际剩余域计算完整核验：

- 全21条原余因子 border 来源身份；
- 三对乘法的3675个交换坐标；
- 35个原基单项式作用于单位的1225个坐标；
- 全21个原余因子在该乘法表示上的25725个算子坐标。

这些算子是原 $\mathcal A_{\mathcal D}$ 乘法的约化。不是仅由三个可交换数值矩阵猜测原坐标环。

对同35个原基 $m_a$，计算
$$
\mathcal T_{ab}=
\operatorname{Tr}_{\mathcal A_{\mathcal D}/\mathcal D}(m_am_b).
$$
实际完整剩余迹矩阵满足
$$
\operatorname{rank}_{\mathbb F_{127}}\bar{\mathcal T}=35,\qquad
\boxed{\det\bar{\mathcal T}=95\ne0.}
\tag{4.1}
$$
其完整左右逆也核验通过。

故 $\det\mathcal T$ 为 $\mathcal D$ 的单位。有限局部自由代数的迹判别式可逆等价于 étale，参见 [Stacks Lemma 49.3.1, Tag 0BJF](https://stacks.math.columbia.edu/tag/0BJF) 及其[迹配对定义](https://stacks.math.columbia.edu/tag/0BVH)。于是
$$
\mathcal A_{\mathcal D}\text{ 有限 étale、秩35，}
\qquad
\mathcal A_E\otimes_E\overline E\cong\overline E^{35}.
\tag{4.2}
$$
配(1.1)，这些点的矩阵秩恰4；没有更小秩的几何参数。

## 5. 全原七次来源排除全部 rank5 奇点

定义原四个二次式和原六行四列矩阵
$$
q_i(y)=y^{\mathsf T}T'_iy,\qquad
M(y)=[T'_0y,T'_1y,T'_2y,T'_3y].
$$
程序保留四个 $q_i$ 和 $M$ 的全部15个原4阶子式。每级完整列分别是 $q_i$ 乘全部次数 $D-2$ 单项式，以及每个原子式乘全部次数 $D-4$ 单项式；输出是全部六变量次数 $D$ 单项式。

实际完整秩为：

| 次数 | 完整矩阵 | 实际模127秩 |
|---|---:|---:|
| 5 | 252×314 | 234 |
| 6 | 462×819 | 458 |
| 7 | 792×1848 | 792 |

前两级不足只作为该级完整记录，不作特征零负判定。第七级选出同一个原792列方块 $U_7$，计算其非零行列式和完整双逆；源码两边各792²个坐标全部通过，即总计1254528个实际原系数门。

日志没有列出 $U_7$ 行列式模127的具体数值，本稿不为它指定数值。结论使用真实非零门、两边完整逆和对应临时 phase 的完整 SHA。

每个原七次单项式的 $E$ 来源由
$$
U_7^{-1}=\frac{\operatorname{adj}U_7}{\det U_7}
$$
对同样的原列标签回填。其系数只除一个非零固定 $E$ 常数。全部行、全部原生成元及单项式乘子都由完整字典规定，所以得到
$$
\boxed{
(y_0,\ldots,y_5)^7
 \subset (q_0,q_1,q_2,q_3,I_4(M))
 \quad\text{于 }E[y_0,\ldots,y_5].
}
\tag{5.1}
$$
这是原多项式的全来源身份，并非参数点秩测试。

若 $[\mu]\in Y_{\overline E}$ 且 $A(\mu)$ 的秩为5，取其非零核向量 $y$。对称性给
$$
\operatorname{adj}A(\mu)=c\,yy^{\mathsf T},\qquad c\ne0.
$$
因此
$$
\partial_{\mu_i}\Delta(\mu)
 =\operatorname{tr}(\operatorname{adj}A(\mu)T'_i)
 =c\,q_i(y).
\tag{5.2}
$$
又 $A(\mu)y=M(y)\mu=0$，故 $I_4(M)(y)=0$。如果这个 rank5 点奇异，(5.2)会给全部 $q_i(y)=0$，与(5.1)及 $y\ne0$ 矛盾。于是
$$
\operatorname{Sing}(Y_{\overline E})\text{ 的支撑完全是 }Z_{\overline E}.
\tag{5.3}
$$
这里已同时保留全部均值方向和所有原核方向。

## 6. 每个 rank4 点都是原普通双点

在任一几何 rank4 点，选择一个可逆的4×4主对称块。对称消元给局部同余
$$
A\sim
\begin{pmatrix}U&0\\0&S\end{pmatrix},
\qquad
S=\begin{pmatrix}a&b\\b&c\end{pmatrix},
\quad \det U\text{ 为单位}.
\tag{6.1}
$$
由于 $U$ 可逆，局部5阶子式理想严格等于
$$
I_5(A)=(a,b,c).
\tag{6.2}
$$
(4.2)使该 rank4 点为原 $Z$ 的约化点。故在光滑三维参数空间 $\mathbb P^3_{\overline E}$ 的局部环内，(6.2)就是极大理想。因此 $a,b,c$ 是完整局部参数，其微分独立。这个局部坐标判准也可用 [Stacks Tag 00TE](https://stacks.math.columbia.edu/tag/00TE) 的 Jacobian 平滑性判准表述。

由(6.1)
$$
\Delta=\det U\,(ac-b^2).
\tag{6.3}
$$
所以在形式或 étale 局部坐标中，原曲面为
$$
ac-b^2=0.
$$
该二次型在特征零秩3，故正是普通双点、几何 $A_1$ 奇点。其局部 Jacobian 理想由 $a,b,c$ 生成，因而原奇点概形也在此处约化。

结合(5.3)，原六次曲面的全部几何奇点恰为这35个 $A_1$ 点。

## 7. 几何整性与原关联的光滑极小解消

若原 $\Delta$ 在代数闭包上有重复曲面分量，则其整个重复分量都奇异，与有限奇点矛盾。若有两个不同的正次数曲面分量，它们在 $\mathbb P^3$ 中至少交成曲线，交线上乘积的全部偏导为零，同样矛盾。因此
$$
\boxed{Y\text{ 几何整。}}
\tag{7.1}
$$
它是具有孤立奇点的超曲面，故满足 $S_2$ 且余维一处正则，由 Serre 判准正规。

原关联
$$
X=\{A(\mu)y=0\}\subset\mathbb P^3_E\times\mathbb P^5_E
$$
在 rank5 开集上是唯一核点的图，因而到光滑开集 $Y\setminus Z$ 为同构。

在(6.1)的 rank4 局部，原四个单位方向完全解出，剩余关联恰为
$$
\begin{pmatrix}a&b\\b&c\end{pmatrix}
\begin{pmatrix}v_1\\v_2\end{pmatrix}=0,\qquad
[v_1:v_2]\in\mathbb P^1.
\tag{7.2}
$$
在 $v_1\ne0$ 图，令 $t=v_2/v_1$，两式给
$$
b=-ct,\qquad a=ct^2.
$$
因此该图有光滑坐标 $(c,t)$。在 $v_2\ne0$ 图，令 $s=v_1/v_2$，相同地得到光滑坐标 $(a,s)$。交叠上
$$
s=t^{-1},\qquad a=t^2c.
$$
例外纤维是 $c=0$ 或 $a=0$ 的完整 $\mathbb P^1$，其法丛为 $\mathcal O_{\mathbb P^1}(-2)$。这是原节点的标准解消，没有删去伴随矩阵在 rank4 处读不到的任何核方向。

于是 $X$ 到处光滑；rank5 稠密开集几何整，全部核线都在其闭包中，所以 $X$ 也几何整。投影为适当双有理态射，例外曲线仅为35条 $(-2)$ 核线。它们两两不交，且没有可在解消中再收缩的例外 $(-1)$ 曲线。因此
$$
\boxed{X\longrightarrow Y\text{ 是原曲面的光滑极小解消。}}
\tag{7.3}
$$
此前通过 $I_3(M)=(y)^3$ 建立的原 rank3 mean 退化概形与 $X$ 的同构继续有效。所有后续 Bell=1 剩余方程仍需在这个完整原空间及全部 moment 变量上处理。

## 8. 完整实际执行身份

独立 Actions：

- run：43836278134；
- job：133193599424；
- step：complete-original-pencil-trace-and-singularity-gates；
- 实际 source commit：733002b66fa2c7337b26ff8cf8e270f3ea16283b；
- 实际完成：2026-11-16 09:03 UTC，exit0；
- 数学程序时间：2.981291404秒；外墙：3.071673173秒；
- 峰值常驻：101456 KiB。

原小回执3926字节，SHA256：
~~~text
8e8ed8c4afcb0e177137cd7ab18fab82e99be7050c515c0af8d6460e97c3df3d
~~~
语义 binding：
~~~text
b2760f962db8cdca270eb353a64f421d02c6cd4e30de5b4203ac6fd26e65f8af
~~~

| 临时完整对象 | 压缩字节 | 压缩 SHA256 | 逻辑 SHA256 |
|---|---:|---|---|
| 同原小矩阵重建 | 3772 | 275b391662d4fcde39379fd1d649ad56c33db81584f855c7c26e1b0dfa9849a1 | 4275f49d86f9a16b669d6034c49dfeb72adaac817c005dd648d00002d661ef36 |
| 全35代数与迹配对 | 19964 | fade55217156bddc15f1734c4a34aebd01bc623659e23fc1f263b72c68091843 | 6b31072fee07c243503eb5453eb4b36dc685b25d2826ad4bd9b5fb3263630c9d |
| 完整次数5 | 14677 | 3719c69a1418a9bd3338891d4fea88056fa101485eea81edc247e93a22192d1e | a05d605dc2fd871335d7db617976a088c10eabdac541c5fe861b4c01f34b7bad |
| 完整次数6 | 18125 | 714c5d78872afac0102832ae5c249cf915b9f260a9c3a9faae43c98520cc1322 | 6adaf68c6593fd453475685a0c7d34c2a128ff1f25e55b3e373aeadc286c93e8 |
| 完整次数7及原792单位来源 | 879625 | 620f1ce8077cecbd550d13b67d10220e4f6fb742f2494bbeec9eb15366aa8e1a | 3d4058ce2ba1501075b17192a3715bfefb1d6aa831d210ddf3115aff0d2b2242 |

临时1955字节 manifest 的 SHA256：
~~~text
15825c7298f9900fdee28346ebd04d1c30f4844cd661bf49977370ee44d69c5e
~~~

[实际执行身份](../notes/r150-original-pencil-trace-execution-789f/43836278134-complete-original-pencil-trace-and-singularity-gates.json)只存源、参数、run与输出SHA；其 blob 为 ef952a4c337a7f7d8f4ae22b10011917564ee5b8，2469字节，SHA256为3dc6410f20b5eb21e5beea4636fac025a81ac70866b9aaf739219d1993502292。数学结果由完成job的原日志读取，未新增数学数组到仓库。

## 9. 可重现原来源

- [实际数学源码](../notes/2026-11-16-r150-original-pencil-trace-and-complete-singularity-gates-789f.py)：blob 9c0575db323f24cd278429d4cd787e48b642d062，26614字节，SHA256 4d0fd8ddaa51725b60705813555502036fed310979542aeb2cac8b320b57d326。
- [完整inputs](../notes/2026-11-16-r150-original-pencil-trace-and-complete-singularity-inputs-789f.json)：锁原物理 helper 与 Bell 原模型的全部source pins。
- [数学接口](../notes/2026-11-16-r150-original-pencil-trace-and-complete-singularity-interface-789f.md)：完整坐标、$E$ 唯一余项与整系数环的来源范围。
- [独立执行包](../notes/2026-11-16-r150-original-pencil-trace-session-interface-789f.md)：180/360/720秒whole-phase续接及manifest-only发布；本次首段已完成，后两段没有执行。

只有固定系数 place 被使用。全原理想的特征零来源、35基的平坦性和节点几何分别由以上原恒等式与实绩推出，不从一般参数点、计数或有限域负结果外推。
