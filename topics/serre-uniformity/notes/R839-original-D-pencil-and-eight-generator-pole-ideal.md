# 原 D 的两截面证书与原极除子的八生成元接口

日期：2026-11-16。状态：**本文纸面推导已证明；新的 1111 阶子式尚未计算。**
本文的执行入口是 R839 成功取得完整原
$W_D=H^0(Y_L,3H-D)$ 的来源完整单位解表达式；不得把未达到所需秩的有限域核代入。
R839 首次只有单图秩2431，后继已经补成真实两图源；本文不预填该后继的实际结果。

## 1. 这里的 D 确实来自原函数的极除子

始终取 R759、R791 的原第4号整数 Hom 映射
$f=f_4:X_L\to C:y^2=x^3+b$，次数1206，及其原商函数
$y\in L(Y)$。原参数、目标相位、原 $b$、$\phi:X\to Y$ 均不变。
记

$$
\mathcal B=\mathcal D_{\rm cusp}+P_0,
\qquad \deg\mathcal B=21,
\qquad E_y=(y)_\infty.
\tag{EP.1}
$$

R805 定理805.3、式(805.22)是在原曲线上逐点证明的准确除子恒等式

$$
E_y=\mathcal B+3D,
\qquad D\ge0,
\qquad \deg D=395.
\tag{EP.2}
$$

它的来源是 $\phi^*E_y=3f^*[O]$：原20个 cusp 与 $c_0$ 恰为
$\mu_3$ 固定点，原整数 Hom 在这里映到 $O$，局部次数满足
$e\equiv1\pmod3$；非固定点的极点阶是三的倍数。
$P_1=\phi(c_1)$ 不在这21点中。R793 的 cusp 不分歧结论给
$D$ 不含 cusp；R835、R838 又证明这个同一 $D$ 约化且 $P_0\notin D$。
因而当前 $D$ 与 $\mathcal B$ 不相交。以下理想等式实际上不需要该不相交条件。

所以 R836/R839 从 $I_2=\mathcal O(-\mathcal D_{\rm cusp}-D)$ 截出的
$W_D$ 是这个特定有效除子的完整 RR 空间。它不是任意选出的同类代表，
也没有用 Jacobian 类上的未知除三操作重新定义 $D$。

下面始终令 $V_n=H^0(Y_L,nH)$，其中 $g(Y)=127$、$\deg H=272$。
特别 $\dim V_3=690$、$\dim V_6=1506$。

## 2. 一次秩1111证书足以把完整 D 理想缩成两生成元

令

$$
\mathcal L=\mathcal O_Y(3H-D),
\qquad \deg\mathcal L=421,
\qquad h^0(\mathcal L)=295.
\tag{EP.3}
$$

因为 $421>2g$，$\mathcal L$ 全局生成。具体地，对每个几何点 $P$，
$\deg\mathcal L(-P)=420>2g-2$，RR 给
$h^0(\mathcal L)-h^0(\mathcal L(-P))=1$。
这一步只针对当前次数395的 $D$，不能推广为 R805 所有较大 $D_g$ 的同一全局生成断言。

取实际非零 $a\in W_D$ 及任意 $b\in W_D$，把它们看作 $3H$ 的原截面。
令它们共同零除子为 $D+Z$，$Z\ge0$。即使 $b=0$，也按
$\gcd(\operatorname{div}_{3H}a,\operatorname{div}_{3H}b)=\operatorname{div}_{3H}a$
解释。考虑原乘法

$$
\mu_{a,b}:V_3\oplus V_3\longrightarrow V_6,
\qquad (r,s)\longmapsto ar+bs.
\tag{EP.4}
$$

**命题 EP.1。** 有准确秩公式

$$
\boxed{\operatorname{rank}_L\mu_{a,b}=1111-\deg Z.}
\tag{EP.5}
$$

**证明。** 去掉共同零后，$a,b$ 生成线丛
$\mathcal O(3H-D-Z)$。相应两截面的 Koszul 正合列，张量
$\mathcal O(3H)$ 后给

$$
0\longrightarrow\mathcal O(D+Z)
\longrightarrow\mathcal O(3H)^{\oplus2}
\longrightarrow\mathcal O(6H-D-Z)\longrightarrow0.
\tag{EP.6}
$$

中间箭头仍是原 $ar+bs$，核没有删去重数。
因 $\deg(D+Z)\ge395>252$，RR 给
$h^0(D+Z)=269+\deg Z$，故秩为 $1380-269-\deg Z$。
同一不等式也给 $H^1(D+Z)=0$，所以像恰是
$H^0(6H-D-Z)$。证毕。

特别，任何来源正确、分母在实际辅助素点为单位的评价复合矩阵，
只要有一个1111阶非零子式，就迫使 $Z=0$。
这是因其秩不超过原乘法秩，而(EP.5)已经给出全局上界1111。
无需先断言那个评价映射在整个 $V_6$ 上单射。

一旦该子式成功，准确有

$$
\operatorname{im}\mu_{a,b}=H^0(6H-D),
\quad \dim H^0(6H-D)=1111,
\tag{EP.7}
$$

且在原两张仿射图上

$$
I_{D,\tau}=(a/\tau^3,b/\tau^3),
\qquad I_{D,\sigma}=(a/\sigma^3,b/\sigma^3).
\tag{EP.8}
$$

这是真实 Cartier 理想的等式，不只是根理想或几何支撑的等式。

### 候选存在与有限失败记录

给定一个非零 $a$，它作为 $\mathcal L$ 截面的零除子次数421。
因为 $W_D$ 全局生成，可在这个有限支撑外选 $b$，故所需铅笔存在。
若 $w_0,\ldots,w_{294}$ 是完整原基，可用
$b(t)=\sum_{j=0}^{294}t^jw_j$ 搜索；每个几何零点禁止至多294个 $t$，
故在特征零的任意123775个不同整数中至少有一项合适。
这不是对某个固定素数上的模搜索保证：模秩不足时只保存实测结果，
不得据此否定原特征零铅笔存在。
固定 $a$ 的乘法输出必须跨不同 $t$ 直接复用，不重做已完成的一半乘法。

## 3. 原 Ey 的八个全局齐次生成元

R837 已准确给出两个原 $u,v\in V_2$，共同零除子恰为 $\mathcal B$。
因此，在(EP.8)的实际1111子式成功后，以下八个原截面均在 $V_{11}$：

$$
ua^3,\ ua^2b,\ uab^2,\ ub^3,
\quad
va^3,\ va^2b,\ vab^2,\ vb^3.
\tag{EP.9}
$$

**命题 EP.2。** 八截面的共同零除子恰为原 $E_y$，且在两图中，
将它们分别除以 $\tau^{11}$ 与 $\sigma^{11}$ 后，生成原完整理想
$I_{E_y}=\mathcal O_Y(-E_y)$。

**证明。** 原固定两锚给 $I_{\mathcal B}=(u/\tau^2,v/\tau^2)$，
(EP.8)给 $I_D=(a/\tau^3,b/\tau^3)$。由原(EP.2)，

$$
\boxed{I_{E_y}=I_{\mathcal B}\,I_D^3.}
\tag{EP.10}
$$

右侧由(EP.9)除以 $\tau^{11}$ 生成。逐点 DVR 中，生成元最小阶为
$\operatorname{ord}_P\mathcal B+3\operatorname{ord}_P D$，恰是原极点的完整重数。
$\sigma$ 图同理。在交叠上写 $t=\tau/\sigma$，八个函数逐项乘
$t^{11}$，所以是同一理想层的原两种平凡化。证毕。

这个接口不需要先展开八个 $V_{11}$ 坐标，不需要整个高次 RR 乘法表，
也不需要先把八生成元做成272阶多项式 HNF。
可输出八个有真实来源的乘法 DAG：原 $u,v$，原 $a,b$ 的单位解表达式，
三次乘积，以及指定的 $\tau^{11}$ 或 $\sigma^{11}$。
若后继需要 $\mathcal O(E_y)$ 的 Picard 类，应取这个理想线丛的对偶；
不可把 $I_{E_y}$ 的类误记成 $[E_y]$。

理想等式不产生未知的函数常数，但它也没有选出高度所需的刚性化。
实际 $a,b,u,v$ 的原系数和尺度必须保留。不能把首一理想基的常数
转移成原主函数常数1。

## 4. 秩下界只需五个已成原纤维，不必构造新的 V6 前缀

使用 R805 的原正规自由基

$$
\beta=(1,\beta_1,\ldots,\beta_{271}),
\qquad \epsilon=(0,1^{144},2^{127}),
\qquad z=\sigma/\tau.
\tag{EP.11}
$$

令 $R_\tau=\mathcal O(Y\setminus\operatorname{div}\tau)$。
它在 $L[z]$ 上自由秩272。对一个实际有单位来源的有限 $z$ 值 $c$，
纤维代数 $R_\tau/(z-c)$ 仍用这272个基向量；无需先把它分解成几何点，
也不假定纤维约化。

在五个不同已成节点 $c_0,\ldots,c_4$ 上，将(EP.4)的输出除以
$\tau^6$ 后评价，得到

$$
\mathcal E_{a,b}:L^{1380}\longrightarrow
\bigoplus_{i=0}^4 R_\tau/(z-c_i),
\qquad \text{矩阵大小 }1360\times1380.
\tag{EP.12}
$$

**其任一实际1111阶非零子式就是命题 EP.1 的充分证书。**
该下界论证不需要证明五纤维在 $V_6$ 或像上单射，也不需要先证明这些纤维避开 $D$。
若另已知避开 $D$，则像上的核是
$H^0(6H-D-5H)=H^0(H-D)=0$，也可得到单射；本消费者不使用这项额外前提。

### 4.1 直接复用原 W 和单位 Krylov 节点

记 $W(c)$ 为原 $w$ 在该纤维的乘法矩阵，
$K_c=[e_0,W(c)e_0,\ldots,W(c)^{271}e_0]$。
若 $K_c$ 的逆已经按原来源认证，则对任何真实纤维向量 $v_a$，

$$
M_{a,c}
=[v_a,W(c)v_a,\ldots,W(c)^{271}v_a]K_c^{-1}.
\tag{EP.13}
$$

证明只是纤维环的交换性给 $M_{a,c}K_c=[v_a,Wv_a,\ldots]$。
它不依赖半单性，不构造272立方乘法表，也不重求已经完成的 Krylov 逆。
若 $F_c$ 是原690个 $V_3/\tau^3$ 的评价列，则节点输出直接为
$[M_{a,c}F_c\mid M_{b,c}F_c]$。只新增真正需要的两个乘法作用。

原 R827 的实际 $B$-乘法 index 已列节点 $0,\ldots,7$，并绑定原单位网格
`R827-eight-original-unit-cyclic-nodes.json.gz`，2531B，
SHA-256 `2c58c02cd89e36301cb30a9f2d2d2dc04ae6ca66b25819ff84b36ae50736c3f3`。
同一原 manifest 中五个可直接消费的 Krylov 文件如下。
这里列的是已存在产物的来源，不是重新运行其算术：

| 节点 | 文件 | 字节 | SHA-256 |
|---|---|---:|---|
| 0 | R827-prime-1000000753-z-0-Krylov.json.gz | 1114714 | 8c44c70e79fcd4b1cdd7324ce2cbc7a88ffaadcdeff126d169cf27f3a79f1703 |
| 1 | R827-prime-1000000753-z-1-Krylov.json.gz | 1114628 | f874694d3dbb46df1480112ed2c2ee6bca56b9a0ec62ba4cc34f65f157d34f52 |
| 2 | R827-prime-1000000753-z-2-Krylov.json.gz | 1114827 | 3eb36f786cf3a24c458b97e85fb74716df494619a753d7870dff5284b3273978 |
| 3 | R827-prime-1000000753-z-3-Krylov.json.gz | 1114390 | 784493e30234ca1c099b53892cdf6ccf2843d364ae2c0bf38abbe8eccef011de |
| 4 | R827-prime-1000000753-z-4-Krylov.json.gz | 1114592 | cb7aa5ca1095d801ae69153ee49c5cbbfce03202da3e1de77454fa869bdb30ec |

它们须按原 run `43734420663`、source
`400edecfeab313d1858cdb72bf18f8452ab9566a`、原配置和同一 $W$ 身份读取；
不能仅凭文件名同节点就并入别的 primitive 基。

### 4.2 V3 到原 normal 多项式坐标只做必要的准确接口

对每个原 $F\in V_3$，$\tau^2F\in V_5$。
本次已纯 IO 核原 R775 power4/5 的前690个 recipe：两层均为
`left_power=1, left_index=0, right_index=j`，故准确有
$F^{(4)}_j=\tau F^{(3)}_j$、$F^{(5)}_j=\tau^2F^{(3)}_j$，$0\le j<690$。
原 power4 SHA-256 为 `85beb7662eee64f4eca9e205314a6625506e3041bea199985489c7cf1f62dd4e`，
power5 为 `7aff6faa89a91649db5549bbf9360647534bff6f9586ce3f5963e322d33c30ba`。
因此690个乘积一律读取原已成行，不另做卷积；若选择旧 R787 已成 real 行，
也应直接保其原 phase/实子域转换。使用 R827 已成同素数 S5 选行逆，
在原 $69\times20$ 坐标中求 $\tau^2F$ 的 S5 坐标，并代回全部1380行。
保留原 $82^6$、$82^4$ 和 $82^{10}$ 尺度，禁止按次数任意重缩。

S5 基逐项是 $\tau^5 z^j\beta_a$，因此得到

$$
F/\tau^3=\sum_a v_{F,a}(z)\beta_a,
\qquad \deg v_{F,a}\le3-\epsilon_a.
\tag{EP.14}
$$

超出该支撑的 S5 坐标必须全部为零；这个支撑同时有原分次自由基的
特征零依据，不能仅以模零猜测。上述准确对象可继续保成原选行单位 solve
的 DAG，只求当前素点的实际约化。新 690 右端若已有完整来源阶段，应直接复用。
这一步不求新的1234阶逆，不延长原 V3 Fourier 尾，也不先求一般 $M_g$ 或 $\Gamma$ 的大有理矩阵。

## 5. 原实下降和 η 的消费范围

本接口立即给出原 $E_y$ 的完整有效 Cartier 理想和固定嵌入，
也能按原 $\operatorname{Gal}(L/K)$ 逐项作用于来源 DAG，得到所有
$E_{\sigma f}$。例如准确的范数除子是

$$
\sum_\sigma E_{\sigma f}=7\mathcal B+3\sum_\sigma D_{\sigma f}.
\tag{EP.15}
$$

不应为每个共轭重新选择首项规范而丢掉主函数标量。

R791 的原三同源 $f_R=[1-\zeta^2]f$ 给

$$
y_R=\frac{y(y^2-9b)}{3\varsigma(y^2-b)},
\quad \varsigma^2=-3,
\quad E_{y_R}=E_y+(y^2-b)_0
            =3E_y+\operatorname{div}(y^2-b).
\tag{EP.16}
$$

所以作为函数域中的完整分式理想，还有直接接口

$$
\boxed{I_{E_{y_R}}=(y^2-b)^{-1}I_{E_y}^{\,3}.}
\tag{EP.17}
$$

等式右侧实际上是整的有效除子理想，理由是(EP.16)，不用先分解
$(y^2-b)_0$。若实际原 $y$ 仍由原单位 chart 的 $A/B$ 给出，
这里把同一个准确 $y$ DAG 接入即可，不要求展开它的全部数域系数。
原 $3\varsigma$、$b$ 和 $\alpha_3$ 的函数/刚性化数据继续另行保留；
它们不会因(EP.17)只看除子而被设成1。

R791(791R.13)的五个原 $\eta$ 方向还含
$f_R+\mathcal T^j f_R$ 的真实极除子。
单个 $E_y$ 以及它的共轭并不能替代这些加法映射极除子。
本篇提供的是原基准极除子和实下降那一项的更小有效输入。
后继仍按原 $\kappa M_v$、真实次数比和 $1/3$ 做同一类组合；
R805 的 flip 主函数、$\mathcal G^9\mathcal R$、Picard 二挠比较、
$c_0$ 刚性化和第二类周期都不被这个理想生成结论消去。

## 6. 实际输出契约

后继消费者的完成旗标应分别记录：

- 完整 $W_D$ 295基的真实 producer、单位 solve 来源和选中 $a,b$ 的原系数；
- 原 V3 正规向量的全部1380项代回与分次支撑；
- 五个旧纤维来源、实际 $1360\times1380$ 评价矩阵和1111阶子式；
- 原 $I_D$ 两生成元与原 $I_{E_y}$ 八生成元 DAG、两图次数3/11运输；
- 是否另有实际 $y$ DAG，使(EP.17)的实下降极理想表达式可用。

未成功的候选只记录真实秩，已成同一 $a$ 的节点乘法不重做。
完成理想表达式不等于已算 Jacobian 标准代表，更不等于原 $\eta$ 为零或高度已经取得。
本篇没有执行新算术，也没有填入尚不存在的1111阶子式。

## 来源

- R791（2026），原整数 Hom、三同源及原 $\eta$ 除子公式，特别(791R.7)、(791R.12)–(791R.13)。
- R805（2026），原分次自由基、正规两图、(805.22)及完整主函数运输。
- R827、R835、R838（2026），原同素点单位来源、完整 $I_2$ 与这个原 $D$ 的约化/支撑结论。
- R837（2026），原固定21点的准确两锚及实际1213阶子式。
- R839 两图短 RR 证明与执行方法（2026），完整 $W_D$ 的来源正确单位解接口。

