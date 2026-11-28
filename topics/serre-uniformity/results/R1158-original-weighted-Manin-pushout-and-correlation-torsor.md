# R1158：原最高矩的实际 S/U pushout 与完整相关 torsor

日期：2026-11-28（Asia/Taipei）  
会话：Astra-serre-24b8836b-20261126  
状态：完整纸证；无新数学执行。一般 $p$ 主目标仍为 OPEN。

## 1. 结论和实际目标群

固定 $p>37$ 及辅助素数 $3<n<p$，可始终取 $n=5$。
后继 R1157 §10 已付同一 trace-fixed 来源的 $n=2$；本篇全部构造同样适用该辅助数。
在 $\mathcal M=\mathcal M_{1,1,\mathbb Q}$ 上记
$\mathcal H=\mathcal E[p]$、$L_r=\mu_p^{\otimes r}$。
$\mathcal C_n\to\mathcal M$ 是真正的阶 $n$ 循环子群 cover，
其 tautological subgroup 仍记为 $C$。令
$$
\mathcal V_n=
 \bigl(\operatorname{Sym}^4\mathcal H(1)
       \oplus\operatorname{Sym}^8\mathcal H(1)\bigr)
 \oplus
 \operatorname{Res}_{\mathcal C_n/\mathcal M}
 \bigl(\operatorname{Sym}^4\mathcal H(1)
       \oplus\operatorname{Sym}^8\mathcal H(1)\bigr),
\qquad
\mathcal Z_0=\operatorname{Sym}^{12}\mathcal H(2).
\tag{1158.1}
$$
写 $\mathcal V_n$ 的坐标为 $(x,y;(x_C,y_C)_C)$。定义
$$
b_n(v,v')
 =\Pi_0(x,y')-\operatorname{Tr}_{C}\Pi_0(x_C,y_C'),
\qquad
\Pi_0(v^4,w^8)=v^4w^8.
\tag{1158.2}
$$
这里 $\operatorname{Tr}_C$ 是同一 cyclic subgroup 中两槽相乘
后的 trace，不能换成两个独立 trace 的乘积。群
$$
\mathcal G_n^{\rm corr}=\mathcal V_n\oplus\mathcal Z_0,\qquad
(v,z)(v',z')=(v+v',z+z'+b_n(v,v'))
\tag{1158.3}
$$
是实际 finite étale class-two group sheaf。

本文构造其实际 torsor。交换商是原全部有序非零 $p$-点的
theta 矩：
$$
\begin{aligned}
X_{n,d}&=\sum_{P\ne0}P^d\otimes\kappa(\theta_n(P)),\\
X'_{n,C,d}&=\sum_{P\ne0}P^d\otimes
                         \kappa(\theta'_{n,C}(P)),
\qquad d=4,8.
\end{aligned}
\tag{1158.4}
$$
求和是相应 finite étale sheaf 上的真实 transfer。
特别没有除以 $p$、$p-1$ 或 $m=(p-1)/2$。

新输入是将
[R1157](R1157-original-integral-SV-Manin-triangle-filling.md)
的原三项整上链，经明确的共同交换商拉回和 polynomial
pushout，接到 (1158.2) 的**完整双线性形式**。
独立点对、rank-one 点对、全部 cyclic-$n$ correlation 和
算术 level descent 都被保留。

这是原最高 $\operatorname{Sym}^{12}$ 的 smoothed correlation
torsor；它不是先把 $V_n$ 在 $H^2$ 中的单位性当成上链除法。
本文最后明确保留到原未平滑 $\mathcal G_0$ 的实际 Hecke
链同伦。尚不称已经读出原 $z_{12}$。

## 2. 真正的共同 even 单位槽

原 trace-fixed theta 满足
$\theta_n(-P)=\theta_n(P)$，
$\theta'_{n,C}(-P)=\theta'_{n,C}(P)$ 于
$K_1\otimes\mathbb Z_{(p)}$，见 R1157 (1157.6)。

这可以先在实际单位对象上完成，而不只是于符号末尾改下标。
对非零点的二重 cover $P\mapsto\bar P=\{P,-P\}$，取
$$
u_{\bar P}=\frac12
 \operatorname{Nm}_{P/\bar P}\theta_n(P),\qquad
u_{C,\bar P}=\frac12
 \operatorname{Nm}_{P/\bar P}\theta'_{n,C}(P).
\tag{1158.5}
$$
这里采用乘法群的加法记号。pullback 恰为原 theta 类；
唯一反除的 $2$ 是 $p$ 单位。清除 theta 类原有的有限
$p$ 单位分母后，这就是实际单位的 norm 与单位指数。
其 Kummer 根塔通过相应 $p$ 单位幂的逆映射定义。
如果与预先选取的原根比较，仍使用 R1156 (1156.6) 的
明确零次相位，不将该相位猜为零。

令 $\mathcal W_\infty$ 为以全部 $\bar P$ 和
$(C,\bar P)$ 编号的 permutation–Tate 格：
每个槽是一份 $\mathbb Z_p(1)$。
这些实际单位的兼容 Kummer 根给一个固定的
$\mathcal W_\infty$-torsor $\mathcal A_\infty$。
所有 $\bmod p^r$ 层都同时固定；写
$\mathcal W=\mathcal W_\infty/p$、$\mathcal A=\mathcal A_\infty/p$。

在几何纤维上，$\mathcal W$ 的坐标记为
$w_{\bar v},w_{C,\bar v}$。定义 ordered 双线性形式
$$
B_{v,w}(a,a')
 =a_{\bar v}a'_{\bar w}
   -\sum_Ca_{C,\bar v}a'_{C,\bar w}
\quad(v,w\ne0).
\tag{1158.6}
$$
其值为 $L_2$；未分裂 $C$ 时仍使用逐陪集乘积后求和。
因为已在 (1158.5) 中真取 even 单位槽，(1158.6) 在
$v\mapsto-v$、$w\mapsto-w$ 下分别不变。这是在同一
formal unit-slot module 上的等式，不把两个尚未比较的
Kummer representatives 当成相同向量。

## 3. 原 degree-12 filling 的完整显式式

在两个形式向量 $X,Y$ 的 symmetric algebra 中置
$$
\begin{aligned}
P(X,Y)&=X^4Y^8,\\
s(X,Y)&=XY(X-Y),\\
R(X,Y)&=2X^3-3X^2Y-3XY^2+2Y^3,\\
Q(X,Y)&=R(X,Y)s(X,Y)^3,\\
A(X,Y)&=\frac12P(X,Y)-\frac1{36}Q(X,Y),\\
B(X,Y)&=\frac1{54}Q(X,Y).
\end{aligned}
\tag{1158.7}
$$
全部次数为 $12$ 的系数只反除 $2,3$。
作用固定为
$$
S(X,Y)=(-Y,X),\qquad
U(X,Y)=(-Y,X-Y).
\tag{1158.8}
$$
直接代入给 $Us=s$、$UR=R$，所以 $UQ=Q$。
此外
$$
\begin{aligned}
&R(X,Y)(X-Y)^3-R(-Y,X)(X+Y)^3\\
&\hspace{22mm}=18XY(Y^4-X^4),
\end{aligned}
$$
乘 $X^3Y^3$ 后得到
$(1-S)Q=18(P-SP)$。因此完整 filling 为
$$
\boxed{\quad
P=(1+S)A+(1+U+U^2)B.
\quad}
\tag{1158.9}
$$
确切地，右边等于
$(P+SP)/2+(Q-SQ)/36=P$。
这是整多项式恒等式，随后才在
$\operatorname{Sym}^{12}\mathcal H$ 中约模 $p$。

两个使用边界同样明确：
$$
B(v,w)=0\quad\text{若 }v=0,\ w=0,\text{ 或 }v=w.
\tag{1158.10}
$$
所以本次三项 filling 不会要求读取
$\theta_n(0)$；不是将所有 rank-one 配置删去。
$A,B$ 的实际值只在约模 $p$ 后用作
$\mathcal Z_0$ 的系数。没有将有限 $v^d$ 任选提升为
$\operatorname{Sym}^dT_pE$，也没有遗漏加法 carry。

## 4. 两种 raw relation 和同一个交换商

### 4.1 S 关系

对非零 $v,w$，R1157 (1157.20) 给的 primitive
$H^S_{v,w}$ 的 ordered 双线性形式是
$$
B^S_{v,w}=B_{v,w}+B_{S(v,w)}.
\tag{1158.11}
$$
例如其中央一次上链是
$a_{\bar v}a_{\bar w}
-\sum_C\operatorname{Cor}(a_{C,\bar v}a_{C,\bar w})$。
微分准确是 (1158.11) 的负值。由于 theta even，
$B_{S(v,w)}=B_{w,v}$；这里保留对称 cup 的完整二次 primitive。

### 4.2 U 关系

若 $v,w\ne0$ 且 $v\ne w$，将 R1157 的原三角形取成
$$
(P_v,-P_w,P_w-P_v).
$$
三个点都非零。原 theta even 和同根修正给实际 primitive
$H^U_{v,w}$，其形式准确是
$$
B^U_{v,w}
 =B_{v,w}+B_{U(v,w)}+B_{U^2(v,w)}.
\tag{1158.12}
$$
因为
$U(v,w)=(-w,v-w)$、
$U^2(v,w)=(w-v,-v)$，
三槽的顺序正好是 R1157 的
$B_n(P_v,-P_w)+B_n(-P_w,P_w-P_v)+B_n(P_w-P_v,P_v)$。
没有另改中央号。

这些 $H^U$ 来自 R1157 的明确四线表达式与同一兼容根塔。
其辅助分裂域只含 $n$-division 和实际二、三次辅助域，
相对当前标记函数域为 prime-to-$p$。
特别对于依赖点对 $w=av$，可直接在
$(E,P_v\ne0,a)$ 的标记曲线上构造；
没有从完整基的 cover 除回含 $p$ 的稳定子。

### 4.3 共同商拉回，而非独立因子的错误 norm

每个 raw torsor 的交换商只使用
(1158.5) 中相应的有限槽，故有一个真实坐标投影
$\ell_j:\mathcal W_\infty\to\mathcal V_j^{\rm raw}$，
且其 quotient torsor 是
$\ell_{j*}\mathcal A_\infty$。
如果原构造用了不同的同函数根，先按 R1156 的
$d\rho$ 作实际 gauge，将此标识固定。

将 raw central extensions 沿这些 $\ell_j$ 拉回，
并在**同一个** $\mathcal A_\infty$ 上取纤维积。
所得群的交换商是一个 $\mathcal W_\infty$，
中心为各原 $\mathbb Z_p(2)$ 的直和，bracket 是
$$
\bigl(B_j(\ell_jw,\ell_jw')\bigr)_j.
\tag{1158.13}
$$
这不是把多个互不相关交换商的群直接映成两个总 norm；
因此不需要假设不同因子间的交换子本来为零。
原 cross terms 将由下一节在同一个 $\mathcal W$ 上的
完整双线性恒等式支付。

## 5. 无群阶反除的实际全算术下降

令
$$
\mathcal I=(\mathcal E[p]\setminus0)^2,\qquad
\mathcal J=\{(P,Q)\in\mathcal I:P\ne Q\}.
\tag{1158.14}
$$
这是 $\mathcal M$ 上实际 finite étale 标记 covers，
在模叠上保留全部 Weil components 和原 descent data。
S raw 对象在 $\mathcal I$ 上定义；U raw 对象在
$\mathcal J$ 各个连通分支的实际泛域上按 §4 构造。

R1157 §8.1 使这些固定函数整塔在相应标记曲线的全
noncusp 部分延伸。对每一有限层作 Weil restriction，
得到 $\mathcal M$ 上的 group/torsor。
其 quotient 是相应 restriction 的 quotient；
将它沿
$$
\mathcal A_\infty\longrightarrow
 \operatorname{Res}_{\mathcal I/\mathcal M}
      (\mathcal A_\infty|_{\mathcal I}),
\qquad
\mathcal A_\infty\longrightarrow
 \operatorname{Res}_{\mathcal J/\mathcal M}
      (\mathcal A_\infty|_{\mathcal J})
\tag{1158.15}
$$
的实际对角及坐标投影拉回，即是 §4.3 的共同商 construction。
所有 finite-level 层间态射同时保留。

几何纤维上，Weil restriction 就是按全部实际标记作乘积；
decomposition-group 作用只重排这些因子。
这正好给 (1158.13) 的全算术 descent，不需要让任意两份
四线分解逐项一致，也不需要对一个有 $p$-稳定子的点
先作群阶平均。

尤其独立标记分支可以有含 $p$ 的 degree，而 rank-one
分支的源直接带一个实际非零点及 scalar $a$。
整个证明从未反除这两个 cover 的 degree。
所有真正用过的反除只有 R1157 已付的
$n$、$2,3$ 以及其 auxiliary field 的 prime-to-$p$ degree。

## 6. 同一 formal slot module 上的完整 ordered 恒等式

将上节已延伸的 raw 塔约模 $p$。对其中心定义
$$
\mu((z^S_{v,w}),(z^U_{v,w}))
 =\sum_{v,w\ne0}A(v,w)z^S_{v,w}
  +\sum_{\substack{v,w\ne0\\v\ne w}}B(v,w)z^U_{v,w}.
\tag{1158.16}
$$
各 summand 的 $\mathbb F_p(2)$ 连同 degree-12 tensor
值确实落入 $\mathcal Z_0$。
这些 maps 是实际 finite-étale trace 加 tautological weight，
因此全算术等变。

逐槽重指标给
$$
\begin{aligned}
&\sum_{v,w\ne0}A(v,w)B^S_{v,w}
 +\sum_{\substack{v,w\ne0\\v\ne w}}B(v,w)B^U_{v,w}\\
&\hspace{16mm}=
 \sum_{v,w\ne0}v^4w^8 B_{v,w}
 \quad\text{于 }
 \operatorname{Hom}(\mathcal W\otimes\mathcal W,\mathcal Z_0).
\end{aligned}
\tag{1158.17}
$$
第一和重指标使用 $S^{-1}=-S$，而 $A$ 总次数为偶数 $12$，
所以系数恰是 $(1+S)A$。
第二和可先在所有点对中延拓为零：
(1158.10) 使所有含零标签或 $v=w$ 的项都为零。
其余 index 集在 $U$ 下稳定，重指标给
$(1+U+U^2)B$。式 (1158.9) 遂证明 (1158.17)。

这是 ordered 双线性形式的等式；不仅是外积等式或
cohomology 等式。没有额外的对称差需要事后忽略。
如果从未先做 (1158.5) 的另一套根出发，则先使用 §4.3 的
实际 gauge；不能将那套代表直接代入本式。

定义全有序 moment map
$$
\begin{aligned}
\lambda:\mathcal W&\longrightarrow\mathcal V_n,\\
x&=\sum_{v\ne0}v^4w_{\bar v},&
y&=\sum_{v\ne0}v^8w_{\bar v},\\
x_C&=\sum_{v\ne0}v^4w_{C,\bar v},&
y_C&=\sum_{v\ne0}v^8w_{C,\bar v}.
\end{aligned}
\tag{1158.18}
$$
所有向量仍按 $v$ 和 $-v$ 分别求和：
$\mathcal W$ 的 even 槽并没有删掉原 all-vector 的因子 $2$。
由定义直接得到
$$
\sum_{v,w\ne0}v^4w^8 B_{v,w}(a,a')
 =b_n(\lambda a,\lambda a').
\tag{1158.19}
$$
(1158.17)–(1158.19) 因而使
$$
(w,z)\longmapsto(\lambda w,\mu z)
\tag{1158.20}
$$
成为从共同商 raw 群到 (1158.3) 的实际群同态。
将已构造 torsor 沿它作 extension of structure group，
便得到主结论的 $\mathcal G_n^{\rm corr}$-torsor。

该结论不要求 (1158.20) 满射；torsor 的 extension of
structure group 对这一实际群同态本来就定义。
全部二次 cross-bracket 已由 (1158.17) 逐槽支付，
不再仅将其列为一个待证条件。

## 7. 与原未平滑矩的 quotient 比较和实际根修正

为准确定位交换商，另选 R1147 的合法辅助素数 $c$，
使 $k_d(c)=c^2-c^{-d}$ 对 $d=4,8$ 都为单位。
记 $\psi_C:E\to E/C$，并将目标曲线的 $p$-torsion
用 $\operatorname{Sym}^d(\psi_C^{-1})$ 运输回原 $\mathcal H$。
所得原矩记为
$$
\mathsf M_d^{\,C}
 =\operatorname{Sym}^d(\psi_C^{-1})q_C^*\mathsf M_d.
$$
Tate factor 保持原常数 sheaf 的规范；$\psi_C^{-1}$
在 $E[p]$ 上存在，因为 $(n,p)=1$。

R1138 的同一 theta divisor/trace-fixed 比较在两种平滑数间给
$$
\begin{aligned}
\frac{\theta_n(T)^{c^2}}{\theta_n(cT)}
 &=\frac{\theta_c(T)^{n^2}}{\theta_c(nT)},\\
\frac{\theta'_{n,C}(T)^{c^2}}{\theta'_{n,C}(cT)}
 &=\frac{\theta_{c,E/C}(\psi_CT)^n}{\theta_{c,E}(nT)}.
\end{aligned}
\tag{1158.21}
$$
等式于实际 $K_1\otimes\mathbb Z_{(p)}$；
所有共同常数按原 trace-fixed 规范处理。
对第一式两个 divisor 直接展开相同；
第二式是 R1138 的原 cyclic-$n$ 比较，未换 quotient 方向。

按 $P^d$ 加权重指标后得到整个 quotient 的真实 H¹ 等式
$$
\boxed{\quad
X_{n,d}=k_d(n)\mathsf M_d,\qquad
X'_{n,C,d}=n\mathsf M_d^{\,C}-n^{-d}\mathsf M_d,
\quad k_d(n)=n^2-n^{-d}.
\quad}
\tag{1158.22}
$$
它们在 $k_d(n)=0$ 时仍成立；本文没有反除 $k_d(n)$。

还可给实际 cocycle 间的有限修正，而非只停在 H¹。
对 (1158.21) 各个 $P$ 的乘法等式使用同一兼容根。
把“左边除右边”这个等于 $1$ 的乘积的根相位记为
$\rho(P)$；依 R1156 (1156.6)，相应 cocycles 的差是
$d\rho(P)$。令
$$
\rho_d=k_d(c)^{-1}\sum_{P\ne0}P^d\rho(P)\pmod p.
\tag{1158.23}
$$
第一式准确给
$a_{X_{n,d}}=k_d(n)a_{\mathsf M_d}+d\rho_d$；
第二式给
$a_{X'_{n,C,d}}
 =n a_{\mathsf M_d^C}-n^{-d}a_{\mathsf M_d}+d\rho_{C,d}$。
所以全部 quotient 可通过一份明确的零次向量 $\rho$
运输到 (1158.22) 的原 moment representatives。

必须同时运输中央坐标。对群律 (1158.3)，
若一个 cocycle 为 $(v_\sigma,h_\sigma)$，用
$q=(-\rho,0)$ 作 gauge $q^{-1}c_\sigma\,\sigma(q)$，则
$$
\begin{aligned}
v'_\sigma&=v_\sigma-d\rho(\sigma),\\
h'_\sigma&=h_\sigma+b_n(\rho,v_\sigma)
 -b_n(v_\sigma,\sigma\rho)-b_n(\rho,d\rho(\sigma)).
\end{aligned}
\tag{1158.24}
$$
这由该明确群律直接相乘得到。即使 quotient 在 H¹ 中相同，
(1158.24) 的中央项也不能省略。
所有 $\rho$ 均来自 (1158.21) 的原有限单位关系，
不是事后任选一个未知 gauge。

## 8. 固定 quotient 后的规范性与当前边界

R1147 (1147.2)、(1147.10) 的泛纤维部分给
$$
H^0(\mathcal M,\mathcal Z_0)=
H^1(\mathcal M,\mathcal Z_0)=0.
\tag{1158.25}
$$
这里 $\mathcal M$ 是本文的 $\mathbb Q$-泛纤维；
几何 $H^1$ 的算术角色为 $L_1$，确无全局不变量。

因此，在固定 (1158.4) 的实际 quotient torsor 及其标识后，
所构 $\mathcal G_n^{\rm corr}$-lift 唯一至唯一同构。
不同合法四线分解、辅助点和兼容根 choice，在完成上述真实
下降与 quotient gauge 后，给同一个 correlation torsor。
此处才使用原 universal 的 H¹ 消失；没有在一个较小开集
或单个 fixed-Weil cover 上提前使用它。

这仍不是原未平滑 $\mathcal G_0$ 的等同。
(1158.22) 的交换商含所有实际 $n$-isogeny pullbacks，
其中央 obstruction 是完整的
$\Pi_0(X_{n,4}\cup X_{n,8})
-\operatorname{Tr}_C\Pi_0(X'_{n,C,4}\cup X'_{n,C,8})$。
与原 $\Pi_0(\mathsf M_4,\mathsf M_8)$ 比较时，
必须保这些同子群 norm 和 (1158.24) 的实际中央修正。

尤其不能仅因某个 Hecke combination 在 $H^2$ 上是单位，
就将已经构造的一次 primitive 除以那个 scalar。
下一条准确接口是构造同一来源上该 Hecke operator 与其
目标 scalar 的实际链同伦，或给出等价的原 torsor 比较。
本文未声称完成该接口、未声称整 $S_0$ 上的 $n$-subgroup
系数也处处 étale，也没有宣布新的 supersingular 中央单位。

## 来源与核验

- R1157：原 SV 三项的 $-n^{-8}$ 三函数式、同 theta Norm、
  所有根和 Cor 修正、固定函数整塔及 noncusp 延伸。
- R1156：共同实际根、有限乘法关系见证、ordered/BCH 转换、
  实际 transfer 链同伦。
- R1140、R1144：原 degree-12 源、$\Pi_0$ 的 symmetric-power
  规范及 all-vector 两次 factor $2$。本篇 (1158.7)–(1158.9)
  另外给出完整显式 filling，不从仅有理维数论证约模。
- R1138：两个辅助数的原 theta 比较和实际 quotient 方向。
- R1147：原 universal $\mathcal Z_0$ 的 H⁰/H¹ 消失及 moment
  根规范。仅在整个 $\mathcal M$ 的真实 descent 完成后消费。
- o2_high_coefficient 已纸核 (1158.9)、S/U 的 ordered 槽、
  零标签的系数消去、完整 common-quotient bracket 及
  all-vector 尺度。无新数学程序执行。


### 后继实际未平滑接口

R1159 已给全部 crossed transfer / 根相位的一次修正 J_n；[R1160](R1160-original-explicit-arithmetic-descent-and-unsmoothing.md) 进一步由原算术群构造 dB_n=(V_n−v_n)Ω。因此最高原未平滑 primitive 现为 (hV+B_n)/v_n，n2/n5 覆盖所有 p>37。一般 Frobenius 的实际 conjugating-path 读取及原 F0 数值仍须继续，不能将该已成的上链程序当作数值已知。
