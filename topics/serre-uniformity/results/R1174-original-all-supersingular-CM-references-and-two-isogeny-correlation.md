# R1174 — 全部原超奇异 CM 参考点的整标架与二同源相关读取

日期：2026-11-28  
会话：Astra-serre-24b8836b-20261126  
状态：已证明；只作纸面证明，没有数学程序执行。

## 1. 结论和这次实际扩大的范围

固定 $p>37$。R1171 的有限仿射重建允许逐个超奇异同构类选择一个自同构相容的参考提升。本篇证明可以全部选为未分歧底上的、在 $p$ 处极大的二次 CM 提升，并把 R1168、R1169 的原二同源相关读式延伸到这整套参考点。

记原未平滑 abelian Frobenius 向量为
$\mathsf A_d(E)$，$d=4,8$。它们由
[R1173](R1173-original-abelian-moment-reconstruction-from-Brandt-affine-equations.md)
的实际 Norm 仿射方程唯一重建。对原 $n=2$ correlation，定义
$$
\begin{aligned}
\mathcal A_d&=(4-2^{-d})\mathsf A_d(E),\\
\mathcal A'_{C,d}
 &=2\operatorname{Sym}^d(\psi_C^{-1})\mathsf A_d(E/C)
       -2^{-d}\mathsf A_d(E),
\qquad \psi_C^{-1}=\tfrac12\phi_C^* .
\end{aligned}
\tag{1174.1}
$$
这里 $\phi_C:E\to E/C$ 是实际商同源，三个 $C\subset E[2]$ 各取一次。商曲线的值须先按 R1171 的实际 quotient 位置和完整右增量读取，再运输；不能把它设为相同约化参考点的值。

在下文原整 CM 基 $(\omega,\mu)$ 中，写
$$
U_k^{(d)}=\omega^k\mu^{d-k},\qquad
\mathcal A_d=\sum_{k=0}^d A_{d,k}U_k^{(d)},\qquad
\mathcal A'_{C,d}=\sum_{k=0}^d A'_{C,d,k}U_k^{(d)}
$$
及
$$
B_{k,l}=A_{4,k}A_{8,l}
             -\sum_C A'_{C,4,k}A'_{C,8,l}.
\tag{1174.2}
$$
同一个 $C$ 的两个槽先相乘再求和。

**定理。** 对全部这些参考点，原两个已构造的二同源 correlation torsors 的完整第一层中央读数为
$$
\boxed{
\begin{aligned}
Z_{r,\mathrm{corr}}^{\mathrm{BCH}}
 &=\sum_{k=0}^4\sum_{l=0}^8
       \frac{k-l}{2(k+l+2)} B_{k,l}\,
                \Pi_r(U_k^{(4)},U_l^{(8)}),\\
Z_{r,\mathrm{corr}}^{\mathrm{ord}}
 &=\sum_{k=0}^4\sum_{l=0}^8
       \frac{k+1}{k+l+2} B_{k,l}\,
                \Pi_r(U_k^{(4)},U_l^{(8)}),
\qquad r=0,2 .
\end{aligned}}
\tag{1174.3}
$$
$\Pi_0$ 是乘法，$\Pi_2$ 是 R1163/R1169 的原 normalized contraction。所有分母对 $p>37$ 都可逆。

这不要求重新证明一般 CM 点的 Miller 定标
$\kappa=-b_E$，也不把 $\mu$ 认成 $x\omega$。实际整标架的 Frobenius 单位以及未定的 $\kappa$ 在 (1174.3) 中严格消去。两个 abelian 向量已经由 R1173 的独立方程给出，所以本式的右端没有尚未读取的原 $U$-primitive 加权和。

本篇只扩大原 **二同源** 的实际 ordinary source 和读数。余有限辅助素数族的四线代表仍须另付；不能由本式和 R1170 的共同核定理宣称一个 $T_2$ 方程已经足够。最低 $\Pi_4+\lambda_\infty X T'$ 槽也不在 (1174.3) 中。

## 2. 全部超奇异类都有所需的未分歧 CM 参考提升

### 2.1. 固定 $\mathbb F_{p^2}$ 模型及在 $p$ 处极大的二次整序

每个几何超奇异同构类可以取一个 $\mathbb F_{p^2}$ 模型，使其 $p^2$-Frobenius 是 $[-p]$。可直接说明这项规范：$[p]$ 是纯不可分的二次 Frobenius；两者相差一个几何自同构。对 $p>3$，$\mathbb F_{p^2}$ 已定义全部可能的 $\mu_2,\mu_4,\mu_6$ 自同构，作相应有限 twist 即得 $[-p]$。此时 Frobenius 是标量，全部几何 endomorphisms 都定义在这个域上。

由 Deuring 的极大整序定理，
$$
\mathcal O=\operatorname{End}(\bar E)
$$
是判别式 $p$ 的定四元数代数的极大整序。其 $p$-进完成是局部除代数的 valuation ring，剩余域是 $\mathbb F_{p^2}$。[来源 1]

利用 $\mathcal O$ 在其 $p$-进完成中的稠密性，取
$\vartheta\in\mathcal O$，其剩余值属于
$\mathbb F_{p^2}\setminus\mathbb F_p$。
它的二次最小多项式模 $p$ 可分且不可约。因此
$$
K=\mathbb Q(\vartheta)
\quad\text{是虚二次域},\qquad
\mathbb Z_p[\vartheta]=\mathcal O_{K,p}\simeq\mathbb Z_{p^2}.
\tag{1174.4}
$$
虚二次性来自原定四元数代数；没有另加一个正则素数条件。

在 $j=0,1728$ 的超奇异类，分别选原
$\mathbb Z[\zeta_3]$、$\mathbb Z[i]$。在这些类出现时 $p$
对相应域惰性，故仍满足 (1174.4)，并且全部原自同构包含在所选整序中。其它类只有 $\{\pm1\}$，自动相容。

### 2.2. 真正提升到有限未分歧底，而不是仅在特征零给一个 CM 点

$\bar E[p^\infty]$ 连通，附上 (1174.4) 的作用后，是高度一的
$\mathbb Z_{p^2}$-formal module。Lubin–Tate deformation theorem
的维数为高度减一，所以这个带作用的对象有唯一的 lift 到
$W(\mathbb F_{p^2})$；这里没有变形参数，也不引入 ramified
底扩张。[来源 2，§2 及 §14]

使用一般 Serre–Tate 等价，而不是 ordinary 情形的
Serre–Tate 参数理论，把此 $p$-divisible lift 与
$\bar E$ 合成各个 $W/p^n$ 上的椭圆曲线。该等价的 full
faithfulness 同时提升原 $\vartheta$ 和原可交换自同构。[来源 3，
定理 1.2.1]

这些有限层相容并实际代数化。具体地，可暂添 prime-to-$p$
的 fine level $3$；在原特殊点的一个 affine étale 模空间邻域内，
相容的 $W/p^n$ 点给一个 $W$ 点，再拉回 universal elliptic
curve。忘记 level 后，唯一性给回原 $W(\mathbb F_{p^2})$
下降。因而所得是一个真正的 good elliptic scheme
$\mathcal E/W(\mathbb F_{p^2})$，不是只在
$W(\overline{\mathbb F}_p)$ 上命名的形式对象。
其特征零 endomorphism ring 含 $\mathbb Z[\vartheta]$，
故它是 CM 提升。

此构造对有限个超奇异类逐个进行，得到 R1171 所需的
自同构相容参考集合。所有后续有限未分歧底变换仍保留
实际 $\sigma$；不会因基域变成 $\mathbb Q_{p^2}$ 而把
$\sigma$ 设为恒等。

### 2.3. 实际 prime-to-$p$ 商曲线仍在此局部 CM 范畴

若 $(n,p)=1$ 且 $C\subset\mathcal E[n]$ 是实际循环子群，
$\mathcal E/C$ 仍是 good CM 曲线。保持 $C$ 的 CM 子整序
至少包含 $\mathbb Z+n\mathbb Z[\vartheta]$，其在 $p$ 处的
完成仍是 $\mathbb Z_{p^2}$。所以商曲线也有同样的整 CM
特征线和高度一 formal module。

在特殊纤维，$[-p]$ 保持每个 $C$，因此原 subgroup 和
quotient 已在 $\mathbb F_{p^2}$ 下降；分裂其各个点只需
未分歧扩张。商提升所带的是**运输得到的** CM embedding，
未必等于该约化类预先选择的参考 embedding。
两者的差仍由 R1171 的实际有限仿射增量处理。

## 3. 整 CM 基、strict LT 坐标和不能省的剪切

取原短模型的
$$
\omega=\frac{dx}{2y},\qquad \eta=x\omega,\qquad
\langle\omega,\eta\rangle=1 .
$$
必要时先作一个已给定的整单位坐标缩放，使 $\omega$
与下文 LT 坐标的一阶微分相同；这只是明确的 coefficient
基变换，R1173 的原方程随之运输。

$\vartheta^*$ 的两个 CM 特征值之差为单位。
因此其 idempotents 在原整 de Rham 格上定义。
Hodge 线是 $\mathcal O\omega$；另一条特征线有唯一
与 $\eta$ 相同 quotient 系数的生成元
$$
\boxed{\qquad \mu=\eta+s\omega,\qquad s\in\mathcal O.\qquad}
\tag{1174.5}
$$
例如若
$\vartheta^*\omega=c\omega$、
$\vartheta^*\eta=d\omega+\bar c\,\eta$，
则 $s=d/(\bar c-c)$。所以它是实际的整 adapted 基，
不是只在分式域中对 Frobenius 作对角化。

CM 特征和半线性 Frobenius 给精确的两列
$$
\Phi_M\omega=p a\,\mu,\qquad
\Phi_M\mu=b\,\omega,\qquad a,b\in\mathcal O^\times .
\tag{1174.6}
$$
$\Phi_M^2=[-p]$ 给
$b\sigma(a)=a\sigma(b)=-1$。
在上述 cup 归一中还可读出 $ab=-1$；以下最高读式
直接保留 $a,b$，无需先以此将它们替换成任何特定数。

带 $\mathbb Z_{p^2}$ 作用的 formal module 可取
Lubin–Tate 的原模型
$$
[-p]z=-pz+z^{p^2},\qquad [\xi]z=\xi z
\quad(\xi\in\mu_e),\qquad e=p^2-1 .
\tag{1174.7}
$$
这里使用高度一 canonical lift 的同一性。
在特殊纤维，原 $[-p]$ 与标准模型都等于 $p^2$ 次
Frobenius。任一匹配 CM embedding 的 formal isomorphism
满足 $f(z^{p^2})=f(z)^{p^2}$，故其系数已在
$\mathbb F_{p^2}$；唯一 deformation 将它提升到同一
未分歧底。因此无需加入一个无限的未分歧常数域。
令 $z/t$ 的首项为一，对应前述明确的 differential
缩放。

取
$$
\varpi^e=p,\qquad g=z^e-p,\qquad
S=\mathcal O[z,\gamma_n(g)]^\wedge_p,\qquad
\psi z=z^p,\quad\psi|_{\mathcal O}=\sigma.
\tag{1174.8}
$$
所有运算都先在这个原 PD 底上进行，不能先令 $g=0$。
式 (1174.7) 只在当前 CM 参考点或实际 CM quotient
使用，不把局部 CM endomorphism 升为全模曲线的 Cartan 作用。

## 4. 不用一般 Miller 定标也能得到完整低 normal 支持

由 R1163–1166 的实际 pointed Miller 比较，原非零
$p$-点 $P_0$ 给 coefficient degree-zero cycle
$x_{P_0}\in\operatorname{Fil}^1(S\otimes H^1)/p$，
满足 $Nx=0,\Phi_1x=x$。
原 Weil adjoint 和 CM 自然性给
$$
A(\xi z)=\xi^p A(z),\qquad B(\xi z)=\xi B(z)
\quad\text{当 }x_{P_0}=A\omega+B\mu .
$$
这里可用原全局 CM 整数模 $p^2$ 逼近局部 $\xi$，
不把一个任意有限标签提升为 $T_pE$ 元素。

完整固定方程与 R1167 §3 相同，只保留实际两列 (1174.6)：
$$
\boxed{
x_{P_0}=
 \kappa z^p(1+\gamma_p(g))\omega
     +a\sigma(\kappa)zg\,\mu ,
\qquad \kappa\in\mathbb F_{p^2}^{\times}.
}
\tag{1174.9}
$$
为自足核准，$\psi(g)/p=-1-\gamma_p(g)\pmod p$；
$\Phi_1$ 只读取 $A$ 的 normal $0$ 和 $B$ 的 normal $1$，
却输出整个 $\gamma_p$ 项。第二列先给
$B_1=a\sigma(\kappa)$，第一列再用
$b\sigma(a)=-1$ 给回 $\kappa=\sigma^2(\kappa)$。
若 $\kappa=0$，整个 cycle 为零，与原非零点的
pointed Kummer identification 矛盾。
因此只证明它是单位，没有从特殊两模型搬入
$\kappa=-b_E$。

第 $d$ 次 pure power 中，输入基
$e_k^{(d)}=\omega^{d-k}\mu^k$ 的每项都有因子
$$
z^{j_{d,k}}g^k(1+\gamma_p)^{d-k},
\qquad j_{d,k}=p(d-k)+k,\qquad 0<j_{d,k}<e
\quad(0<d\le12).
\tag{1174.10}
$$
所有额外常数、二项系数以及 $\kappa$ 都保留在该项的
系数内。高 $\gamma_p$ 次数不能先删；本式只付精确的
低 normal 支持。

## 5. 原二同源 four-line source 在这些参考点上仍是 ordinary

这一节负责 actual source，不由 (1174.9) 的形式形状
直接宣布中央 primitive 存在。

### 5.1. 三次辅助点及原整差因子

R1157 §12 的几何证明只需要
$\bar E/\mathbb F_{p^2}$ 的 Frobenius 为 $[-p]$，
不需要 $j=0,1728$ 或特定的特征零方程。
令 $M=p^2-p+1$，取精确阶 $M$ 的特殊点 $\bar T_0$。
它的三个 $p^2$-Frobenius 共轭和为零，且
$$
x(3\bar T_0)\notin\mathbb F_{p^2}.
\tag{1174.11}
$$
若该坐标在底域，则 $3\bar T_0$ 的阶会整除
$p-1$ 或 $p+1$，而其阶是 $M/\gcd(M,3)>p+1$。
提升三个共轭所成的横截直线，取得原实际三次
finite étale 辅助点；不加入整个 $E[M]$。

选固定的 CM 整数 $\alpha$，其剩余值不为 $0,-1$，
并使用同一个形式端点
$$
B_0=0,\qquad B_1=P(z),\qquad B_2=[1+\alpha]P(z).
\tag{1174.12}
$$
各差分别是原 $P,[\alpha]P,[1+\alpha]P$。
三者差参数都准确为 $z$ 乘整单位；
首比在 $\mathbb F_{p^2}$ 且互异。
**不能**把 $[1+\alpha]z$ 替换为
$\operatorname{Teich}(1+\bar\alpha)z$。

原两切线 identity 仍是
$$
\begin{aligned}
\operatorname{div}L_a(B)&=2[B+a]+[3T_0-2B],\\
R_i(T-B)&=R_i(T_0-B)
          \left(\frac{L_{A_i}(B)(T)}{L_0(B)(T)}\right)^2 .
\end{aligned}
\tag{1174.13}
$$
此处第二行的 $L_0(B)$ 是零二扭标签的切线，不是额外参考线。
所有原 leading 常数保留。参考线按 R1157 的有限避点
条件整选，交点为 transverse cubic étale algebra。

原 determinant 的精确因子和 leading 检查逐项适用：
两同标签先除端点差；三个不同标签的首项是
$\sum\mu_j l_{a_j}(x(3\bar T_0))b_j$，
(1174.11) 将它分成两个独立方程，其共同核只含
$b_1=b_2=b_3$；全同标签用非二、三扭切点的 dual
Wronskian，除三份差后为单位。
因此 R1157 (1157.47)、(1157.50)–(1157.53)
的完整表在当前形式环中原样成立。

这里先有 exact 差因子，再有非零首项。
所以每个真正 line value、determinant、归一常数以及
四线参数与其补数都是
$$
z^mV,\qquad V\in\mathcal O_{F'}[[z]]^\times .
\tag{1174.14}
$$
不是由在 $z=\varpi$ 处一个 valuation 反推该式。
$F'/F$ 只需分裂二扭点和上述横截三次代数，仍为有限
未分歧扩张；原函数的所有重数和 closed-point Cor 保留。

### 5.2. 同一个 ordinary primitive，而不是事后选 lift

在 (1174.14) 的共同环上，用
$\psi(\sum a_jz^j)=\sum\sigma(a_j)z^{pj}$。
原 Kummer second 槽满足
$$
p^{-1}\log\frac{(z^mV)^p}{\psi(z^mV)}
=p^{-1}\log\frac{V^p}{\psi V}\in\mathcal O_{F'}[[z]] .
$$
原 R1155/R1166 的四种 corner 公式因而给每个指定
$D$ primitive 的整 ordinary 代表，含全部常数、
ordered 乘法项及 Frobenius carry。

再逐项执行 R1156–1158 的同根比较、实际群 pushout、
共同 quotient 的纤维积和同陪集 Cor。
这些是 whole filtered torsor morphisms，保持唯一的
Hodge 点；其 Hodge-frame 操作只是已给定的整线性、
二次及实际有限共轭求和。
所以 R1166 §21 的论证在此原样给
$$
h^U_{P,Q}=(0,\beta^U_{P,Q}),\qquad
\beta^U_{P,Q}\in\mathcal O_{F'}[[z]] .
\tag{1174.15}
$$
第一槽为零是该 Hodge frame 的中央连接结论。
没有把原 étale $\rho$ 设为零，也没有用局部中心
$H^1$ 的消失替换实际 root/五项比较。

若用新的三次辅助点替换已固定的另一份全局分解，
仍消费 R1157 §12.6 所列有限乘法关系、同根
$d\rho$、五项及 Cor/res homotopy。随后才得到同一
原 correlation 对象；不能仅因它们具有同一个 divisor
便认定局部中央值相等。

## 6. 最高槽：所有未知 CM 尺度严格消去

记 raw original 和三个 primed moments 的 coefficient
cone 代表为 $(a_d\,d\log u,y_d)$，$u=z^e$。
式 (1174.10) 乘 ordinary second 槽后作原 tame trace：
因为 $0<j_{d,k}<e$，零 $e$-block 从 $u^1$ 开始。
因此模 $p$，
$$
(y_d)_{k,n}=0\ (n<k+1),\qquad
(a_d)_{k,n}=0\ (n<k+1),\qquad
\phi_d a_d=0,\quad a_d=N_u y_d .
\tag{1174.16}
$$
第一 log 槽中裸 $d\log z$ 的项由
$\sum_{\xi\in\mu_e}\xi^{j_{d,k}}=0$ 准确消去。
原 $N_z=eN_u$ 和 log-trace 因子沿 R1166 §9，
不另乘一份 $e$。

同样，最高 $J_U$ 的 normal 常数为零。
R1166 原 $S/U$ 拼接及完整 nonlinear gauge 因而给
$$
\begin{aligned}
N_uJ_U&=\tfrac12
     \{b_2(y,N_uy)-b_2(N_uy,y)\},\\
Z_{0,\mathrm{corr}}^{\mathrm{BCH}}&=-\mathcal R_{12,2}(J_U).
\end{aligned}
\tag{1174.17}
$$
这里 $\mathcal R$ 不是乘法映射；第二式已经包含原有序
gauge 的全部项。

R1168 的整 log-PD 收缩只使用 adapted filtration、
两列 Frobenius 为单位反对角和原 $\gamma_p$ carry。
在当前基中，令
$$
F_k^{(d)}
=p^{-(d-k)}\Phi_M(e_k^{(d)})
 =a^{d-k}b^k U_k^{(d)} .
$$
它给原 abelian constant coefficients
$$
A_{d,k}
 =\frac{(-1)^{k+1}}{(k+1)!}\,
        a^{d-k}b^k\,\sigma((y_d)_{k,k+1}),
\tag{1174.18}
$$
primed 槽同式。目标 $(d,t)=(12,2)$ 的 normal
$q=K+2$ reader 是
$$
\frac{(-1)^{K+2}}{(K+2)!}\,
        a^{12-K}b^K\,\sigma((J_U)_{K,K+2}) .
\tag{1174.19}
$$
所有 positive $\gamma_{hp}$ 输出先保留；它们的次数
至少为 $p$，超过本次 $q\le14$，故在真正的收缩时不贡献。

由 (1174.16)，(1174.17) 的第 $K+2$ 项只来自
$(k+1,l+1)$，其中 $k+l=K$。它准确为
$$
(J_U)_{K,K+2}
=\sum_{k+l=K}\frac{l-k}{2(K+2)}
 \binom{K+2}{k+1}
 \left(y_{4,k,k+1}y_{8,l,l+1}
       -\sum_C y'_{C,4,k,k+1}y'_{C,8,l,l+1}\right).
\tag{1174.20}
$$
$K+2<p$，所以这份系数由实际微分唯一决定；
normal 常数则已经由 actual ordinary source 单独支付。

把 (1174.20) 代入 (1174.19)。两份 (1174.18) 的共同
Frobenius 因子恰是
$$
(-1)^{k+l+2}a^{12-k-l}b^{k+l},
$$
与中心相同；$\sigma$ 保乘法，不再对 $a,b$ 额外施一次
$\sigma$。二项式及阶乘消成
$1/((k+1)!(l+1)!)$。
因此得到 (1174.3) 的 $r=0$ 式。
$\kappa$ 从未被求值，也从未反除一个可能为零的
abelian 坐标。

## 7. 两次配对槽使用同一 actual source

R1169 的原 filling 是
$\langle P,Q\rangle^2Q_8(P,Q)/42$，
其 scalar primitive 仍是 (1174.15)。
原 paired projector 是 R1163 已校准的
integral Frobenius-compatible map，不新定标度。

输入 $\omega^{4-k}\mu^k$ 与
$\omega^{8-l}\mu^l$ 经两次配对后，目标的 $\mu$
下标为 $K=k+l-2$。每次配对先消掉一个 $\omega$
和一个 $\mu$，但其 coefficient 仍保原
$z^{p+1}g(1+\gamma_p)$。
故与 R1169 (1169.6) 一样，
$$
(J_2)_{K,n}=0\ (n<K+3),\qquad
(J_2)_{K,0}=0 .
\tag{1174.21}
$$
目标是 $(d,t)=(8,4)$，所读
$q=K+4=k+l+2$ 仍小于 $p$。
原 nonlinear gauge 和微分给 (1174.17) 的
$\Pi_2$ 版本，边界 normal 系数仍是
$(l-k)\binom q{k+1}/(2q)$。

最后的尺度消去直接用
$$
\Phi\,\Pi_2(v,w)=\Pi_2(\Phi v,\Phi w)
$$
在 R1163 原 Tate/paired 模型中的准确形式。
两个被配对的 $H^2$ Frobenius 因子已经包含其中；
不得把它换成没有 Tate 修正的裸 $\operatorname{Sym}^8$。
交换两条 CM 特征线使一次 alternating pairing 变号，
但两次配对的总号为正。
因此同一 factorial 和 Frobenius 因子消去给
(1174.3) 的 $r=2$ 式。

$\langle\omega,\mu\rangle
=\langle\omega,\eta\rangle=1$，
所以 R1169 (1169.12) 的 normalized monomial 公式
也原样适用，只把 $\eta$ 写成 $\mu$。
它不依赖 $s=0$，不反除任何 Bernoulli 数。

## 8. 把实际 abelian 重建值送入公式，保全部 quotient shear

(1174.1) 是 R1159 (1159.23) 的实际群 map 在唯一
Hodge 点上的读数，不是只从 $H^1$ 类推出的线性等式。
因此可直接以 R1173 的
$\mathsf A_d(E_i)$ 和实际 quotient 增量填入。

对一个二同源核 $C_i=\{O,(e_i,0)\}$，原 meromorphic
form 恒等式仍为
$$
\phi_i^*\eta_i
 =2\eta-e_i\omega
       -d\!\left(\frac{y}{x-e_i}\right),
\qquad \phi_i^*\omega_i=\omega .
$$
令 quotient 的运输 CM 基为
$\mu_i=\eta_i+s_i\omega_i$。在完成原 Čech/PD
exact 比较之后，
$$
\boxed{\quad
\psi_i^{-1}\omega_i=\tfrac12\omega,\qquad
\psi_i^{-1}\mu_i
 =\mu+\tfrac{s_i-e_i-2s}{2}\omega .
\quad}
\tag{1174.22}
$$
这是完整剪切式。若特意使用通过 $\phi_i$ 运输的同一
CM embedding，两条特征线必须相互对应，
cup–trace 又给 $\phi_i^*\mu_i=2\mu$，
所以此时 $s_i=e_i+2s$。
于是 (1174.22) 在这两个**相互对应**的 CM 基中成为
$\operatorname{diag}(1/2,1)$。
这不是对原 $\eta$ 的 exact 项或剪切作删除。

对于一般 prime-to-$p$ 的实际 quotient，完全相同的
paired argument 给运输 CM 基中的
$\operatorname{diag}(1/n,1)$。
若将它识别回预选的另一个参考基，必须再乘完整的
coefficient 基变换以及 R1171 的实际有限增量。
这里没有把 quotient 提升默认成那个参考提升。

在每一个输入上按这个顺序做，(1174.2) 的全部
$A,A'$ 均由原有限几何资料和 R1173 的有限线性
重建给出。所需辅助素数集合由单位理想保证存在，
但本篇没有执行重建，也不给一个小素数或时间界。

## 9. 后续接口的准确边界

本篇已经把原最高及第二中央 **二同源相关项** 的读取
从原两特殊 CM 模型扩展到全部所选 SS 参考点。
其右端是实际 abelian 系数的双线性式；没有剩余的
$\kappa$、$\beta^U$ 加权值或未定的 CM-period 比例。

仍须保留三个不同问题。

第一，R1170/R1171 的共同核使用一个足够丰富的辅助素数族。
本篇没有把 n=2 的两切线精确阶表外推到任意 $\ell$。
一般原 $\theta_\ell$ 的 Miller/chord 分解必须另给
共同 ordinary source、同根比较和零 first slot，
才能把相同 normal 论证用于相应相关项。

第二，R1159 的功能方程是跨实际 $E$ 和所有 $E/C$
的方程。不能将它替换为单点 scalar $v_n Z(E)$。
一个已知 $n=2$ 右端也不自动求出所有原未平滑中心。

第三，最低槽含 R1172 的正
$\lambda_\infty X T'$ 修正，尚需其自己的实际 endpoint
读取。这里没有把裸 $\Pi_4$ 当成那一完整对象。

所有结论保原 first-layer finite FL 语义；
不由这次模 $p$ 读数宣称 whole $p$-disc 已关闭，
也不预判一般 $p$ 主目标。

## 10. 本篇亲读的 primary 与来源范围

1. John Voight, *Quaternion Algebras*, GTM 288 (2021)，第42章，
   Proposition 42.1.7、Theorem 42.1.9及其局部极大性证明。
   [出版社开放正文](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_42)。
   本篇已读这些段落，用于原 SS endomorphism order；二次
   embedding 的选取和有限 twist 的规范在 §2 自证。

2. Jiu-Kang Yu, *On the moduli of quasi-canonical liftings*,
   Compositio Mathematica 96 (1995), 293–321。
   [正式原文 PDF](https://www.numdam.org/article/CM_1995__96_3_293_0.pdf)。
   已读 §2 的 formal-module deformation theorem
   （印刷页294–295，PDF第3–4页），§4 的 Lubin–Tate
   canonical model，以及 §14 的固定 embedding、高度一
   唯一 lift（印刷页318–319，PDF第27–28页）。
   只使用这些明示输入，不把全文其它 quasicanonical
   估值结论搬入本篇。

3. Nicholas Katz, *Serre–Tate local moduli*,
   [作者完整 PDF](https://web.math.princeton.edu/~nmk/old/serretatelocmod.pdf)，
   Theorem 1.2.1及 full-faithfulness 的证明
   （印刷页143–146，PDF第6–9页）。
   这里实际使用一般 nilpotent-base 等价；
   没有把该文后面的 ordinary 参数理论套在 SS 曲线上。

原整比较、same-root、ordered products、actual coefficient
运输分别沿 R1163–1168、R1159 和 R1169 已发表版本。
本篇新增的是全参考点的合法 CM 选择、一般整特征标架
上的实际 source 延伸，以及不需求出 $\kappa$ 的尺度消去。
