# R448 — 49 个完整 self 方向在固定真实镜对上的准确 19 维像、十九行实际支付及三十维余核

## 0. 新结论与来源范围

[R443](R443-complete-self-image-of-the-paid-joint-kernel-and-forty-nine-formal-directions.md) 的唯一实际已给出完整 self-current 的 49 维形式像：K 链 11 列加原 53 联合核关系中的 38 个 pivot lifts。本稿**只读取该次原 249 记录的已付系数**，结合旧镜对 16 维定理作纸面证明；没有新运行、profile 评价、符号消元或 rank 任务。

对同一个真实偶母的固定镜点，保物理宽度并设

$$
r_*\ne0,\qquad s=p_*/r_*\ne0,\qquad h=u_*/r_*.
\tag{1}
$$

把实际第五幅除回后，完整 49 维 self 模块的两侧像准确为

$$
\boxed{\quad
(P,\ \mathsf T_{s,h}P+Q),\qquad
P\in\operatorname{Pol}_{10},\quad Q\in\operatorname{Pol}_7.
\quad}
\tag{2}
$$

因此镜对像恰为 **19 维**，相应 49 维 current 空间的镜对核恰为 **30 维**。不需要另加 generic $h$、例外多项式非零或新母假设。

同一原库中选 11 个左对应点和 8 个不同右对应点，在原非零幅条件下得到一个准确可逆的 19 行矩阵。本文给出全部 19 个原成本的确定构造、完整投影到 30 维 blind 核的公式，以及对其余全部真实根的准确像判据。原其它 C 的实际联合前提、完整基准与合法窗口仍须保持。

## 1. current 像与完整成本必须分开

沿 R443，记原 53 个准确响应组合为 $V_i$，它们的退化 self-current 为 $F_i$。选该文第 4 节的 38 个 pivot indices

$$
\begin{aligned}
\mathcal I=\{&
8,9,10,11,12,13,15,16,17,18,20,22,23,25,26,27,28,29,30,31,\\
&33,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52\}.
\end{aligned}
\tag{3}
$$

取一个具体原成本子空间

$$
\mathscr M=
\operatorname{span}\{K_0,\ldots,K_{10},V_i:i\in\mathcal I\}.
\tag{4}
$$

这些 49 个成本的 current 已独立，故 (4) 本身也是 49 维；其 current 映射为单射。它是原完整响应空间的明确子空间，并不是全部 $\mathcal R\cap\ker E$ 的分类。

R443 对旧参考只证明其 **current MEMBER**。若一个旧成本与新 53 列组合有相同 current，不能据此说二者的完整成本函数相等。为使以下每一个构造都确切落在 (4)，先用原 MEMBER 证书选新 source lifts：

$$
\begin{aligned}
D_0={}&-128V_9,\\
D_1={}&-\frac3{10}V_8-128V_{10}-128V_{11},\\
D_2={}&
\frac{484608}{2627}V_{12}
+\frac{318208}{2627}V_{13}
+\frac{84736}{2627}V_{15}
+\frac{892928}{2627}V_{16}
+\frac{169472}{2627}V_{20},\\
D_3={}&-128V_{26},\qquad D_4=256V_{18},\\
D_5={}&V_{31},\qquad D_6=V_{44},\qquad D_7=V_{51}.
\end{aligned}
\tag{5}
$$

前五个 current 分别准确等于旧 $J_1,J_2,J_3,W_3,\Xi_2$；其证书为 R443 原记录 240、241、242、245、248。后三个是原 pivot 成本本身。没有对每个查询点另选一个成本。

R443 的 full-Q / 全三尾 Af-current 证书及原响应 natural 恒等给

$$
J^+(C)=0,\qquad C_{i,\alpha}(C)=0
\quad(C\in\mathscr M)
\tag{6}
$$

在当前整圆全部包、全部真实 Af 根上成立。其完整两通道沿 R397/R435 为

$$
H_{d,i,\alpha}(C)=a_i^3R_i F_C(x_{i,\alpha};u_i,p_i,r_i),
\quad
H_{e,i,\alpha}(C)=-a_i^3T_iF_C(x_{i,\alpha};u_i,p_i,r_i).
\tag{7}
$$

这里 whole-Q 杀真实平台的二次部分，三尾 current 核杀内部 ordered 项；没有以 whole self 总量零直接代替 cap 值。

## 2. 固定物理镜对和原 K 左逆

采用 [R438](R438-constant-tail-S-responses-and-fifteen-joint-actual-mirror-fluxes.md)、[R440](R440-complete-zero-order-compatible-self-module-and-sixteen-actual-fluxes.md) 已固定的镜点和对应副本。把共同物理宽度收入参考偶 profile $u$，有

$$
u(-b)=u(b)=u_*,\quad
u'(-b)=p_*,\quad u'(b)=-p_*,
\quad u''(\pm b)=r_*,
\tag{8}
$$

且这两个是原实际简单 Af 根。其它根可以仍存在。

不同对应副本为 $\rho_j u(x-\xi_j)$，实际位置为

$$
x_j^-=\xi_j-b,\qquad x_j^+=\xi_j+b,
\qquad \rho_j\ne0.
\tag{9}
$$

原幅、中心和宽度不移动。若从无宽度的母 $U$ 写成 $U((x-\xi)/w_0)$，则 (8) 中的
$p_*,r_*,b$ 必须使用 $U'/w_0,U''/w_0^2,w_0b_{\rm ref}$。
不同实际宽度不能无证明合为同一 (1)。

对 $C\in\mathscr M$，定义其两个物理 $x$ 多项式

$$
f_C^-(x)=r_*^{-5}F_C(x,h r_*,s r_*,r_*),
\qquad
f_C^+(x)=r_*^{-5}F_C(x,h r_*,-s r_*,r_*).
\tag{10}
$$

第五次齐次性使 (10) 与选择的非零 $r_*$ 数值无关。真正副本的值再乘 $\rho_j^5r_*^5$。

令 $\kappa_n^\pm=f_{K_n}^\pm$。为使 (12) 的输入完全确定，原 R435 的完整 Af-current 生成式可直接写成

$$
w=1-zx,\qquad A_z=w^2r+2zwp+2z^2u,
$$

$$
F_{K_n}
=n![z^n]\frac{A_z^3}{15}
 \left(4A_z^2-10z^2uA_z-\frac{20}{3}w^4r^2\right).
\tag{10a}
$$

式 (10a) 是先恢复同右锚完整 current、再在外 Af 点代入后的原式；不是在积分内部代 Af 或改动左常数。代 (10) 给每个完整 $\kappa_n^\pm$，并得到

$$
\deg\kappa_n^\pm=n,\qquad
[x^n]\kappa_n^-=[x^n]\kappa_n^+=\ell_n,
$$

$$
\ell_n=-\frac8{45}(-1)^n n!\binom{10}{n}\ne0,
\qquad0\le n\le10.
\tag{11}
$$

这不是只保 leading 的替代式：下面全部逆映射使用完整 $\kappa_n^\pm$，它们由 R435/R443 的原生成式确定。

对任意 $P\in\operatorname{Pol}_{10}$，从最高次到常数准确递推

$$
a_n(P)=
\frac{[x^n]\{P-\sum_{m>n}a_m(P)\kappa_m^-\}}{\ell_n},
\quad n=10,\ldots,0.
\tag{12}
$$

定义原成本和右输运

$$
\mathscr K[P]=\sum_{n=0}^{10}a_n(P)K_n,
\qquad
\mathsf T P=\sum_{n=0}^{10}a_n(P)\kappa_n^+.
\tag{13}
$$

则 $\mathscr K[P]$ 的完整镜对值为 $(P,\mathsf TP)$。
$\mathsf T$ 保每个 $\operatorname{Pol}_d$，保持最高项系数；没有把它改成只由几何反射猜得的算子。

对任一 $C$，其准确镜差为

$$
\Delta_C=f_C^+-\mathsf T f_C^-.
\tag{14}
$$

## 3. 原记录给出的三个新 leading 项

R443 的全部 53 current 都是普通五次局部多项式，显式 $x$ 次数至多 7。这是原 complete_self_column 序号 57—109 的完整结果；其中没有待定非局部或高阶 jet 项。

本稿只需其中三条准确最高项：

| 原成本 | 原 source / complete-current 序号 | 唯一最高 $x$ 项 |
|---|---|---|
| $V_{31}$ | 35 / 88 | $-29x^5pr^4/256$ |
| $V_{44}$ | 48 / 101 | $313x^6pr^4/1404$ |
| $V_{51}$ | 55 / 108 | $-67x^7pr^4/1104$ |

这三条 complete-current payload 的 SHA256 分别为

- 100961b63dcf632537a4e7feb436d848ade2a40860b6a71ea3a4c2d7dc99f919；
- e7ba9586f402e06a79336baeffa6575a134141f7d77278f8d208681c583bc296；
- 2555840e1e7d5dab56751e026984ec5d5ae54dc33db4f6ac542e356f6286bbcd。

它们来自同一 [run 43801705436](https://github.com/Rogerhu12/math-research-public/actions/runs/43801705436)，source 9c796878a2f7f1b910ebcebadd0b2d05dc0d42ac。本稿没有重新生成其源场或再次计算 current。

在 (10) 的两侧，最高项是相反号的 $\pm s x^d$。由 (11)—(14)，得到

$$
[x^5]\Delta_{D_5}=\frac{29}{128}s,\qquad
[x^6]\Delta_{D_6}=-\frac{313}{702}s,\qquad
[x^7]\Delta_{D_7}=\frac{67}{552}s.
\tag{15}
$$

这些都是非零实数，且与 $h$ 无关。

## 4. 完整镜对像恰好 19 维

### 4.1 严格上界

全部新 53 列都在 $\operatorname{Pol}_7^2$；$K_0,\ldots,K_7$ 也在其中。其余 $K_8,K_9,K_{10}$ 只再添三个列。因此

$$
\dim\operatorname{im}\mathrm{ev}_{s,h}
 \le 2(7+1)+3=19.
\tag{16}
$$

这是比直接放入 $\operatorname{Pol}_{10}^2$ 的 22 维上界更强的完整原式上界。

### 4.2 三个新维数的全参数证明

旧 R440/R441 的镜对像准确为

$$
\{(P,\mathsf TP+Q):P\in\operatorname{Pol}_{10},
\ Q\in\operatorname{Pol}_4\},
\tag{17}
$$

维数为 16。其非 K current 的显式 $x$ 次数至多 4。

如果三新列模旧像有一个关系，先比较 $x^{10},x^9,x^8$，原 K 最高项 (11) 依次迫对应 K 系数为零。再比较 $x^7$ 的左右两系数：$K_7$ 的最高向量是同号 $(\ell_7,\ell_7)$，$D_7$ 是反号非零向量。二者线性独立，故 $D_7$ 与 $K_7$ 系数都为零。对 $x^6,x^5$ 同样处理 $D_6,D_5$。

因此三新列模旧 16 维严格独立。等价地，(15) 在镜差中逐次补出五、六、七次项。结合 (16)，

$$
\boxed{\operatorname{rank}\mathrm{ev}_{s,h}=19
 \quad\text{对所有实际 }s\ne0,\ r_*\ne0.}
\tag{18}
$$

没有 generic 参数例外。$h$ 不需要满足任何额外多项式条件。

## 5. 十九个真实原成本的完整确定式

为了同时给一个可消费右逆，先列 (5) 的八个镜差最高系数：

| $j$ | $\deg\Delta_{D_j}$ | $d_j=[x^j]\Delta_{D_j}$ |
|---:|---:|---|
| 0 | 0 | $-8s/3$ |
| 1 | 1 | $-16s/3$ |
| 2 | 2 | $-8s$ |
| 3 | 3 | $-8s$ |
| 4 | 4 | $-8s/3$ |
| 5 | 5 | $29s/128$ |
| 6 | 6 | $-313s/702$ |
| 7 | 7 | $67s/552$ |

前五条由 R443 的完整 MEMBER current 及 R440 原式给出，后三条是 (15)。所有低次、$u$ 项和真常数均通过 (12)—(14) 保留。

先置

$$
Z_j=D_j-\mathscr K[f_{D_j}^-],
$$

再从 $j=0$ 到 7 递推

$$
\boxed{\displaystyle
L_j=\frac1{d_j}
 \left(Z_j-\sum_{m<j}[x^m]\Delta_{D_j}\,L_m\right).
}
\tag{19}
$$

于是这些都是同一个 (4) 中的准确原成本，并且

$$
(f_{L_j}^-,f_{L_j}^+)=(0,x^j).
\tag{20}
$$

所需 19 个成本为

$$
\boxed{K_0,\ldots,K_{10},L_0,\ldots,L_7.}
\tag{21}
$$

(5)、(12)、(19) 是逐项可执行的精确有理定义。它们只使用已固定实际 $s,h$，不为不同点另换参数。分母仅为原非零 $\ell_n,d_j$；没有未核的 determinant 条件。

(13)、(20) 立即证明全文完整像 (2)，而不只给 rank 的下界。

## 6. 同一真实库的十九行矩阵与 actual 截面

在原完整 R/T 编码的对应 cell 中选 11 个不同左点和 8 个不同右点。沿 R435/R440，完整 cell 包含整个最细编码及二次矩闭合；不是把八个孤立同轴副本的三次差分当作二次闭合。

设相应实际系数满足

$$
d_j^\pm=\rho_j^5a_j^3R_jr_*^5\ne0.
\tag{22}
$$

它保原真实第五幅及 $R_j\ne0$。选中的右点可来自已有对应副本，不移动任何真实中心；原十二 cell 有足够数量。

按 11 左、8 右排列，(21) 的 raw $H_d$ 矩阵为

$$
\begin{pmatrix}
\operatorname{diag}(d_j^-)
 [\kappa_n^-(x_j^-)] & 0\\
* & \operatorname{diag}(d_j^+)[(x_j^+)^m]_{m=0}^7
\end{pmatrix}.
\tag{23}
$$

星号是原 K 的全部右值，没有丢掉。其 determinant 准确为

$$
\left(\prod_jd_j^-\right)\left(\prod_jd_j^+\right)
\left(\prod_{n=0}^{10}\ell_n\right)
\prod_{i<j}(x_j^--x_i^-)
\prod_{i<j}(x_j^+-x_i^+)\ne0.
\tag{24}
$$

因此可以实际联合支付这 **11+8 个 raw 内部通量**。这仍只是选中的同形镜对组，未扩成任意 19 个不同根。

其实际实现沿 R435/R440 的同一增强响应商：

$$
(J^+,\mathbf H_{19})(U)=J^+(U)\times\mathbb R^{19},
\qquad
(J^+,\mathbf H_{19})(\mathcal R)
 =J^+(\mathcal R)\times\mathbb R^{19}.
\tag{25}
$$

原 J⁺ 基与 (21) 给真正可逆的块三角响应矩阵。所有新 $V_i$ 仍由 R261 原 E8/Z 原型生成，不能只将一个显示 monomial 当成自由成本。

实际实施明确需要原 R433/R435 的共同合法窗口：从起点把有限 profiles、原型、保护芽、桥、共享真倒行和两次商校正放在同一窗口与目标紧包络中。原型非零成本基准、两次校正的 H/C 值都进入完整方程

$$
n(a+Mt)+F(t,y)=y_{\rm resp}.
\tag{26}
$$

内部整数先固定，最终一个足够大的有限 $n$ 在整紧目标集上给统一 $C^1$ 根；Klein 仍先减完整基准再除 4。没有将 signed 列直接拼到一条冻结的实际几何，亦不授任意预冻结窄窗口自动容纳全部控制字。

若全部其它 C 已按同一个 actual 联合接口支付，或已具备 R435 的共同响应等像前提，(6) 使这些列可在同一构造中追加并保持 C。若没有该前提，(25) 只授 J⁺ 与这十九行，不能把两个独立实际截面相加。

对于原完整 cell 首/末包中由 E 因子化的 C 行，最终 E 零与选中的 H 零一起支付这十九点的两条内部通道。它不因此清其它点的 C。

## 7. 49 列到三十维镜对核的准确原-source 投影

对任意 $C\in\mathscr M$，令 $P=f_C^-$、$Q=\Delta_C$。由 (2)，$\deg P\le10,\deg Q\le7$。定义

$$
\boxed{\displaystyle
\Pi_0 C
 =C-\mathscr K[f_C^-]
   -\sum_{j=0}^7[x^j]\Delta_C\,L_j.
}
\tag{27}
$$

则

$$
f_{\Pi_0C}^-=f_{\Pi_0C}^+=0,\qquad \Pi_0^2=\Pi_0.
$$

其核是 (21) 的 19 维成本空间，像是 (4) 内准确的 30 维镜对 blind 空间：

$$
\boxed{\dim\operatorname{im}\Pi_0=30.}
\tag{28}
$$

这给一个无需再选三十个数字 pivot 的完整、可消费生成集：

$$
\mathfrak b_C=\Pi_0C,\qquad
C\in\{K_0,\ldots,K_{10},V_i:i\in\mathcal I\}.
\tag{29}
$$

其中 $\Pi_0K_n=0$；其余列会有准确线性关系，但它们共同张成整个 30 维核。每一条都有 (27) 的原成本 source，不能把不同点的 blind 值按行分别改系数。

这里的 30 是 R443 的 **49 维 current / 所选独立 lift 子空间**中的核。原 64 个输入列的镜对系数核则为 $64-19=45$；其中 15 条已在 R443 对全部 Af jets 都盲。那 15 个完整成本仍可能改变其它 period 或规范槽，不应宣成完整成本零。

旧六个 blind 只生成旧 22 维子模块的镜对核，现在是 (28) 的一个子空间；不再是完整判据。

## 8. 全部其它真实根的目标与准确 iff

令 $V$ 为同一实际库、原 J⁺ 零成本，并假设其所需 C 已通过同一联合接口清零。对每个真实 Af 根保完整 raw 两通道，定义

$$
\eta_{i,\alpha}(V)=
\frac{R_iH_{d,i,\alpha}(V)-T_iH_{e,i,\alpha}(V)}
 {a_i^3(R_i^2+T_i^2)}.
\tag{30}
$$

$R_i$ 可为零，故不在全根公式中擅除 $R_i$。在 C 零时，清 $\eta$ 等价于同时清两通道；原非局部目标没有被改成一个猜测的局部多项式。

首先用 (23) 的准确十九行右逆清核心值。等价的明确做法是：

1. 对 11 个左 normalized 值作原 $x_j^-$ 的唯一十次插值，得到 $P$；
2. 在 8 个右点扣去完整 $\mathsf TP$，对余值作唯一七次插值，得到 $Q$；
3. 取
   $W_{\rm core}=\mathscr K[P]+\sum_{j=0}^7[x^j]Q\,L_j$，
   并置 $V^\flat=V-W_{\rm core}$。

具体地，上述 normalized 数据是 $\eta_{j,\pm}(V)/(\rho_j^5r_*^5)$。在所选 $R_j\ne0$ 且 C 零的核心点，它准确等于 $H_{d,j,\pm}(V)/d_j^\pm$，所以与 (23) 的 raw 右逆完全一致。所有原低次、中心、宽度和 cap 常数保持。

对剩余全部实际根建立完整矩阵

$$
\mathsf B_{(i,\alpha),C}
 =F_{\Pi_0C}(x_{i,\alpha};u_i,p_i,r_i),
\qquad C\text{ 遍历 (29) 的原 49 列}.
\tag{31}
$$

(31) 使用每个根真正的物理 jets，不在别的根重新选择 (1)。它是具体原成本的值表，不只一个维数上界。

因为 (23) 的十九行在 (2) 上已经单射，任何保持核心零的本模块修正都恰落 (28)。所以

$$
\boxed{\displaystyle
\mathscr M\text{ 在 signed 成本层清全部实际根}
\iff
\eta_{\rm rest}(V^\flat)\in\operatorname{im}\mathsf B.}
\tag{32}
$$

这是增广 49 模块对同一原目标的完整 iff。没有在本稿计算 (31) 的实际 rank，也不把其至多 30 维当作任意三十点可控。

具体边界：

- 对其它同镜对副本，(29) 全盲；其目标须由 (2) 的同一个 $P,Q$ 正确预测。
- 对不同物理宽度或不同 $(u/r,p/r)$ 的根，仍用 (31) 的原值，不改 (27) 的参考参数。
- 对 $r=0$ 的其它简单 Af 根，R443 多项式仍可准确评价；本稿不沿用旧六列在那里全盲的结论。新的 $u,p$ 项可能改变这个读出。
- 若实际目标不满足 (32)，只说明所选 (4) 不足；原更大响应空间，尤其尚未并入的 $\Theta_{71}(\ker\Pi_{71})$ 来源，仍不能被排除。
- 把全部剩余根的 signed 修正升级为 actual 联合截面，还须在同一个增强观察下保响应等像/正字符、原型基准和合法窗口。本文无条件的新 actual 组是 (23) 的十九行，未宣完整 period 或 13 行同规范已经解决。

## 9. 三条新原组合的完整成本来源

为使 (5)、(19)、(27) 无需重新重建旧 144 算子，以下直接列原 paid relation 展开的系数；所有未列项为零。记 $[E,\tau]=B_E\tau$。

$$
\begin{aligned}
V_{31}={}&-\frac{13}{10240}[Y,H_2]
-\frac7{30720}[V,H_3]-\frac{13}{61440}[T,H_3]
+\frac7{15360}[L,H_4]-\frac1{15360}[U,H_4]\\
&+\frac1{61440}[R,H_5]-\frac1{1228800}[S,H_5]
-\frac1{73728}[P,H_6]
-\frac{19}{2560}[Y,J_0]-\frac7{2560}[V,J_1]\\
&+\frac{19}{10240}[T,J_1]-\frac1{5120}[L,J_2]
-\frac7{10240}[U,J_2]
-21[Y,\chi_{32}]+\frac{31}{2}[Y,\chi_{34}]\\
&+2[V,\chi_{37}]+\frac52[T,\chi_{37}]
+\frac{43}{2}[L,\chi_{40}]+[U,\chi_{40}].
\end{aligned}
\tag{33}
$$

$$
\begin{aligned}
V_{44}={}&-\frac7{9360}[Y,H_3]
-\frac{997}{898560}[V,H_4]-\frac7{37440}[T,H_4]
+\frac1{8640}[L,H_5]-\frac1{17280}[U,H_5]\\
&+\frac1{103680}[R,H_6]+\frac{29}{1347840}[S,H_6]
-\frac{11}{4680}[Y,J_1]+\frac{19}{2080}[V,J_2]
-\frac{11}{18720}[T,J_2]\\
&+\frac{1504}{117}[Y,\chi_{37}]
-\frac{344}{13}[V,\chi_{40}]+\frac{368}{117}[T,\chi_{40}]
+\frac{64}{39}[Y,\chi_{100}]+[V,\chi_{104}].
\end{aligned}
\tag{34}
$$

$$
\begin{aligned}
V_{51}={}&-\frac1{44160}[Y,H_4]
-\frac1{4416}[V,H_5]-\frac1{35328}[T,H_5]
+\frac1{52992}[L,H_6]-\frac1{52992}[U,H_6]\\
&-\frac7{920}[Y,J_2]
+\frac{224}{23}[Y,\chi_{40}]
-\frac{16}{23}[Y,\chi_{104}]+[V,\chi_{109}].
\end{aligned}
\tag{35}
$$

它们分别来自 R434 已付 dependent 序号 795、811、819，经 R443 source 序号 35、48、55 精确展开。没有把 85 核索引误当 144 原标签。完整 current 分别在 R443 序号 88、101、108，所有非局部、高阶 jet 与分母分类已在那次实际中完整输出。

本稿的新信息是其固定真实镜对上的纸面评价结构、十九行控制与全根三十列投影接口；没有附加任何新的科学执行费用。
