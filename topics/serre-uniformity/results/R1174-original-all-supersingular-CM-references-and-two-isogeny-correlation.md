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


## 11. 一般辅助素数：保留垂直 PD 方向后的第一层结论

本节以下扩大 §5 的辅助素数范围，使用另一份完整证明，
而不把二同源切线表照搬到一般素数。

固定原合法的平滑辅助数 $c$，并令
$$
\mathcal A_p^{(6)}
 =\{\ell>3:\ \ell\ne p,\ \ell^6\not\equiv1\pmod p\}
   \setminus\{c\}.
\tag{1174.23}
$$
删去 $c$ 只是保持原同源分布中的互素条件。
R1171 §§10–13 已付这一族的原 SV 三角、两套 S/U filling、
prime-to-$p$ 分裂域以及余有限 Hecke 理想。
本节证明，对每个 $\ell\in\mathcal A_p^{(6)}$，
§§6–8 的最高及两次配对相关项读式都成立。

新输入是一条准确的第一层结论：

> 对同一原 raw 整塔，在 CM 参数盘的实际 scalar
> log-syntomic complex 中，其指定中央 primitive 的模 $p$
> gauge 类有唯一的零第一槽、ordinary 第二槽代表。

这里 ordinary 指第二槽属于 $k[[z]]$，
不含垂直 PD 变量，也没有负 $z$ 次数。
所说的是**完成实际比较和 gauge 之后**的代表；
没有假定原四线表达式的各个 Bloch 参数都为 good unit，
也没有声称全部 $\bmod p^r$ 层都能同时写成 ordinary。
实际全 $\mathbf Z_p$ 塔仍用于下节的水平延伸；
有限 FL 读取则只需要这份准确的第一层代表。

特别不能把带 $\log p$ 的底换成恒等嵌入。
下面始终保留独立的 base variable $u$ 和
$$
g_{\rm v}=u-p.
$$
最后的 $p$-挠点 specialization 才把 $u$ 送到 $z^e$，
从而把它变成原 $z^e-p$，所有 carry 都随同一个 PD map
运输。

## 12. 原 raw 整塔在 CM 参数曲线上的真实延伸

### 12.1. 同一三角形可以先在参数曲线上构造

在 §2 的实际 CM 曲线 $E/F$ 上固定原 CM 整数 $\alpha$。
对于非退化三角形，要求 $\alpha$、$1+\alpha$ 在
$\mathcal O_{K,p}$ 中为单位，三个端点始终是
$$
O,\qquad P,\qquad [1+\alpha]P.
\tag{1174.24}
$$
$p$-点对的每个允许剩余类都可如此处理。
实际 U 关系取 $(P,-Q,Q-P)$ 时相应把 $1+\alpha$
换成 $1-\alpha$；其为零的剩余标签已经由原 filling
的零系数处理。

R1157 (1157.4)–(1157.16) 的证明，对变量 $P$ 仍然成立。
其中使用的仅是 $E[\ell]$ 平移、三个零边际、trace-fixed
范数以及三个陪集的分离；并没有使用 $[p]P=0$ 来
principal 化除子。所需 principal 化的整数是 $\ell^2$，
不是 $p$。在参数曲线的 generic point，三个陪集分离；
从一个有限开集开始便得到完全相同的 $K_3$ 见证。

在 universal 点配置上作同一 R1156 四线、同根和 transfer
构造，再分别限制到原 full-level 点及 (1174.24)。
这固定的是同一个 actual raw object 和其 quotient 标识，
不是在每个 CM 盘重新挑一个任意 cup primitive。
若为一般位置而更换四线，仍先使用原五项、
乘法根和 ordered Cor 同伦比较。
最后原 R1158 或 R1169 的全模叠固定 quotient
唯一性仅用于识别整个已下降相关 torsor，
不用于猜单个盘上的中央常数。

由于
$$
p\nmid \ell(\ell-1)^2(\ell+1)
\qquad(\ell\in\mathcal A_p^{(6)}),
$$
原 $E[\ell]$ splitting 以及四线算法的二、三次辅助扩张
都只需 $p$ 单位 transfer。这里允许 $\ell>p$；
没有再次引入已经删去的 $\ell<p$ 限制。

### 12.2. 只有最终 theta 交换商需要在盘上为 log unit

先把 $E[\ell]$ 放在一个有限未分歧 $F'/F$ 中分裂。
这是 good reduction 下 prime-to-$p$ étale 群的实际分裂域。
原最终 raw quotient 只含
$$
\theta_\ell(P),\quad \theta_\ell(Q),\quad\theta_\ell(-P-Q),
\quad
\theta'_{\ell,C}(P),\quad\theta'_{\ell,C}(Q),
\quad\theta'_{\ell,C}(-P-Q),
\tag{1174.25}
$$
以及它们在原同一 permutation–Tate 格中的重复位置。
辅助 cross-ratios 只用来制造中央 primitive，
不被添成这个最终交换商的独立槽。

这些 theta 槽 near $O$ 的 leading 常数都是 $p$ 单位。
以下给出包含 trace-fixed 常数的证明。
记 $\psi_\ell$ 为实际 division polynomial，
$\Delta_E$ 为原 good 模型的 discriminant。类
$$
t_\ell^{\,0}
 =\frac1{12}\left[\frac{\Delta_E^{\,\ell^2-1}}
                         {\psi_\ell^{\,12}}\right]
\tag{1174.26}
$$
具有原除子 $\ell^2[O]-[E[\ell]]$，
没有 vertical divisor；其 $O$ 处首项的常数为单位，
因为 $\ell,\Delta_E$ 都是单位。
式 (1174.26) 的 $\Delta$ 幂准确消去 Hodge 权。

选择整数 $a$ 满足 $a\equiv2\pmod p$、
$a\equiv1\pmod\ell$。则 $a$、$a^2-1$ 都为 $p$ 单位，
$[a]$ 在 good 模型上 finite étale。
$[a]_*t_\ell^{\,0}-t_\ell^{\,0}$ 的 horizontal divisor 为零，
vertical valuation 也为零，因此是一个 base unit 类 $C_a$。
真正 trace-fixed 的 $\theta_\ell$ 与 (1174.26) 之差为
$$
-\frac{C_a}{a^2-1}.
\tag{1174.27}
$$
这是由原 $[a]_*\theta_\ell=\theta_\ell$ 直接解得，
保留了该实际常数；不是把两份同除子的函数猜成相等。
故 $\theta_\ell$ 本身仍有 unit leading。
原
$\sum_{T\in C}\theta_\ell(P+T)=\ell\theta'_{\ell,C}(P)$
同样包含全部常数，且 $\ell$ 可反除，
所以每个 primed 槽也有相同的整性性质。

清除有限个 $p$ 单位分母后，
$\alpha$、$1+\alpha$ 的 endomorphisms 在 $O$ 处 étale，
其余 $\ell$-division 支撑都与 $O$ 的特殊纤维分离。
因此 (1174.25) 在同一个实际参数中准确为
$$
f=t^m V,\qquad m\in\mathbb Z,\quad
V\in\mathcal O_{F'}[[t]]^\times.
\tag{1174.28}
$$
随后只按原单位指数反除。
这里是 divisor、étale 差因子和 unit leading 的结论，
不从一个 $L$-点上的赋值反推整函数形式。
所有端点仍用固定 $\alpha$ 和真正 $[1+\alpha]$。

### 12.3. 人工水平点必须先由整个整塔消去

把除 $O$ 外的实际 quotient 支撑从参数曲线删除。
在其余 generic 闭点 $x$ 上，(1174.25) 的 Kummer
交换商无惯性；整个 raw 塔的惯性因而落在
有限直和的无挠中心 $\mathbb Z_p(2)$ 中。
其 decomposition-group 等变性准确给
$$
\operatorname{Hom}_{G_{F_x}}
     (\mathbb Z_p(1),\mathbb Z_p(2))
 =H^0(F_x,\mathbb Z_p(1))=0,
\tag{1174.29}
$$
其中 $F_x/F'$ 是有限扩张，不可能含全部 $p$-power
单位根。故整个连续惯性同态为零。
逐层 normalization 和曲线 purity 给唯一有限 étale
延伸；层间 morphisms 也唯一延伸，保相容性。

因此原 actual raw tower 确在 $O$ 附近的
punctured generic curve 上定义。
(1174.29) 没有对单独有限层宣称
$H^0(F_x,\mathbb Z/p^r(1))=0$，
也没有只从 quotient 无分歧就断言中央无分歧。
人工四线交点即使有坏 reduction，仍由这一整塔论证处理。

## 13. 同一 henselian log chart 的精确 primitive 比较

取上述 algebraic curve 在 $(p,O)$ 的 henselization
$X_h$，以 $t$ 为实际 étale 参数，带 divisor $pt=0$
的 log structure。记
$$
j:U_h=X_h[1/(pt)]\hookrightarrow X_h,\qquad
i:(X_h)_k\hookrightarrow X_h.
\tag{1174.30}
$$
原塔由 §12 确已限制到 $U_h$。
这里的 $j$ 同时去掉 $p$ 和 $t$；不将它只写成
horizontal puncture。

Tsuji Theorem 4.2（亦为 Theorem 5.1 的特例）给
$r=1,2$ 的精确 small-weight 比较。
其应用于 henselization 是沿实际 étale neighbourhoods
取限制，并非另援一个未经证明的 formal comparison。
在严格 henselian neighbourhood 上，Stacks Project
Tag 03QO 给全局截面等于闭点 stalk，且无高 étale
cohomology。故
$$
R\Gamma((X_h)_k,i^*Rj_*\mathbb Z/p(r))
 \simeq R\Gamma(U_h,\mathbb Z/p(r)).
\tag{1174.31}
$$
一般有限 residue field 情形再对同一 $G_k$ 取 cohomology。
这保留全部算术 Frobenius，没有只取 geometric invariants。
本处不使用 proper base change 去偷换一个非 proper 开集。

在 $r=1$ 的 $H^0,H^1$ 与 $r=2$ 的 $H^0,H^1,H^2$
上，Tsuji period map 因而都是同构。
其 §2 (2.5)、(2.8)、Proposition 2.11 保原 ordered product
和 Kummer convention。于是 R1163 §5 的 obstruction、
difference、automorphism 论证原样给出：
固定 (1174.25) 的 quotient 和其同根标识后，
该实际 raw primitive 有唯一的 syntomic gauge 类原像。
先用中央 $H^2$ 得存在，再用 $H^1$ 选中原 object，
并用 $H^0$ 运输其 morphisms；三个步骤都不能省去。

这里可使用全局的实际 log-PD embedding：
引入独立 $u$，令 $X_h$ 由 $u=p$ 切出，
两个 log generators 是 $u,t$，
Frobenius 在 ambient 上为
$$
u\longmapsto u^p,\qquad t\longmapsto t^p,
\qquad a\longmapsto\sigma(a).
$$
Étale 参数 chart 的提升由 henselian 性唯一完成。
PD ideal 是 $(u-p)$ 的 divided powers，绝不是零。
各 PD/微分项在 affine special chart 上准凝聚，
故其 hypercohomology 可以在这个实际 complex 的
全局 sections 中表示；无限 PD 项用其准凝聚 filtered
colimit，完成后逐有限精度作同一操作。

然后完成到原 strict LT 参数 $z$。
先运输已经得到的这一个 object，
再使用 Tsuji §2 的实际双 embedding/refinement、
Frobenius-change maps 和 products。
形式参数变换 $t=z\,V_0(z)$ 的 $V_0$ 为整单位；
两个 log Frobenius lifts 的比属于 $1+p\mathcal O_{F'}[[z]]$。
这些 maps 是同一 PD 复形的真 map/同伦，
如 R1166 的同一 ambient comparison；不自行重选一份
与原根没有比较的 ordinary lift。

这一完成不需要对全部形式对象另宣一个 exact
comparison theorem。我们只拉回已由 (1174.31) 支付的
原 gauge 类，§2 的 embedding-independence 与
functorial product maps 保持其原 étale identification。
目标 formal ring 的 $u,z$ 仍是 log $p$-basis，
$u-p$ 是 regular immersion；Tsuji Lemmas 2.2–2.3
及 Corollary 1.11 的 PD 比较适用。
最终到 $\mathcal O_L$ 的合成仍是原 algebraic 点 $P_0$
的特化；syntomic functoriality 使经形式中间环的合成
等于这个直接 map，其两端的原 period 比较保持交换。
因此不需要为形式中间环额外假定 nearby-cycle 满射。
以下在此同一完成后的 complex 中做显式消元。

## 14. 保完整 vertical carry 的 weight-two 消元

置
$$
\mathscr R=\mathcal O_{F'}[[z]],\qquad
\mathscr S=\mathscr R\langle\gamma_n(g_{\rm v})\rangle^\wedge,
\quad g_{\rm v}=u-p,\quad
\psi(u)=u^p,\quad\psi(z)=z^p.
\tag{1174.32}
$$
完成同时按实际所需的 $p$、$z$ 精度理解。
本节只在模 $p$ complex 中计算，
$\overline{\mathscr R}=k[[z]]$；
$\psi$ 在它上面是注入的，通常不满射。
写 $N_u=u\partial_u$、$N_z=z\partial_z$。

按原 mapping-fibre convention，
weight-two 的前两次数为
$$
C^0=J^{[2]},\qquad
C^1=J^{[1]}(d\log u\oplus d\log z)\oplus\mathscr S,
\qquad
dX=(dX,(1-\phi_2)X).
\tag{1174.33}
$$
这里 $\phi_j=p^{-j}\psi$ 只在其合法 filtered 域上定义。
在 degree-one forms 上的 divided Frobenius 是
$\phi_1$ 作用于两个系数，因为 $\psi(d\log u)=p\,d\log u$、
$\psi(d\log z)=p\,d\log z$。

固定 quotient 的每个实际 symbol 为
$$
a_f=\left(d\log f,\ \frac1p\log\frac{f^p}{\psi f}\right),
\qquad f=z^mV.
\tag{1174.34}
$$
第二槽等于 $p^{-1}\log(V^p/\psi V)\in\mathscr R$，
first slot 只有 $d\log z$，无 $d\log u$。
因此任何原 ordered raw cup $\Omega$ 的 first component
为零，其 second component 是 ordinary
$\omega(z)d\log z$。多槽 bilinear 和同子群 Cor
仍具有这同一性质。

取 §13 已对齐原 quotient 的 primitive
$$
h=(a_u\,d\log u+a_z\,d\log z,\beta),\qquad
dh=-\Omega,\qquad a_u,a_z\in J^{[1]}.
\tag{1174.35}
$$
下面不把它的 first component 猜为零。
展开
$\beta=\sum_{n\ge0}\beta_n(z)\gamma_n(g_{\rm v})$，
并令
$$
\beta_{\ge2}=\sum_{n\ge2}\beta_n\gamma_n,\qquad
F=\phi_2(\beta_{\ge2}),\qquad F_0=F|_{\gamma_{>0}=0}.
$$
完整 Frobenius carry 为
$$
\frac{\psi(g_{\rm v})}{p}\equiv-1-\gamma_p(g_{\rm v})
 \pmod p.
$$
对 $n>2$，包括 $n\ge p$，
$n-2-v_p(n!)\ge1$。因此准确有
$$
F=\frac{(1+\gamma_p)^2}{2}\,\psi(\beta_2),
\qquad
F_0=\frac{\psi(\beta_2)}2.
\tag{1174.36}
$$

定义合法的 degree-zero gauge
$$
X=\beta_{\ge2}+(F-F_0)\in J^{[2]}.
\tag{1174.37}
$$
$F-F_0$ 的 normal indices 只有 $p,2p$，
所以模 $p$ 下
$N_u(F-F_0)=0$、$\phi_2(F-F_0)=0$。
这里只对 (1174.37) 的 filtered 元素施 $\phi_2$；
不能分拆成对 ordinary $F_0$ 单独施这个未定义的 map。
由此
$$
h'=h-dX,\qquad
\beta'=\beta_0+\frac{\psi(\beta_2)}2+\beta_1\gamma_1.
\tag{1174.38}
$$

vertical 方程是
$$
(1-\phi_1)a'_u=N_u\beta'.
$$
若 $c_1$ 为 $a'_u$ 的 $\gamma_1$ 系数，
左边的 normal-zero 项是 $\psi(c_1)$，
因为 $\phi_1(\gamma_1c_1)=-(1+\gamma_p)\psi(c_1)$。
右边无 normal-zero 项，故由 $\psi$ 注入得 $c_1=0$。
随后整式变成 $a'_u=\beta_1\gamma_1$，
比较一次项再得 $\beta_1=0$，所以 $a'_u=0$。

first component 的闭性再给 $N_u a'_z=0$。
模 $p$ 下 $N_u\gamma_n=n\gamma_n$，
而 $a'_z\in J^{[1]}$，故只可能留下
$\gamma_{hp}$、$h\ge1$ 的项。
它们全被 $\phi_1$ 杀掉。
horizontal 方程的右边与 $\beta'$ 都是 ordinary，
于是这些 positive normal 项也全为零。
最终
$$
\boxed{\qquad
h_{\rm ord}=(0,\beta_{\rm ord}),\qquad
\beta_{\rm ord}
 =\beta_0+\frac{\psi(\beta_2)}2\in k[[z]],
\qquad dh_{\rm ord}=-\Omega.
\qquad}
\tag{1174.39}
$$
这是实际 $h-dX$，完整 $dX$ 留在比较中。
没有删 $\gamma_p$，没有要求 $\psi$ 满射，
没有先反除 $p$ 后再约模。

这个 ordinary 代表在固定 gauge 类中唯一。
若 $dY=(0,\delta)$，$Y\in J^{[2]}$ 且
$\delta\in k[[z]]$，则 $N_uY=0$ 只留下 positive
$\gamma_{hp}$；$\phi_2Y=0$，所以
$\delta=(1-\phi_2)Y=Y$ 迫 $\delta=Y=0$。
这也支付相同 raw object 的 étale descent、
完成/refinement 和固定同根 morphism 之间的 glue：
先运输 actual gauge 类，再取其唯一 ordinary 代表。
不把这一结论扩大为任意不同 primitive 的值相同。

## 15. 送入原挠点 PD 模型及全部辅助素数的读式

### 15.1. 实际 specialization，而非舍弃法向误差

现在固定原 $p$-点 $P_0$，其 strict LT 坐标
$\varpi$ 满足 $\varpi^e=p$，$e=p^2-1$。
从 (1174.32) 到原 coefficient PD 模型的 map 是
$$
u\longmapsto z^e,\qquad z\longmapsto z,\qquad
g_{\rm v}\longmapsto g=z^e-p,\qquad
d\log u\longmapsto e\,d\log z.
\tag{1174.40}
$$
它与两端 $\psi$ 严格交换，且在实际 fibre 上就是
$t(P_0)$ 的原 specialization。$g^n=n!\gamma_n(g)$
使 $z$ 在这个目标 PD 环中拓扑幂零，所以普通整幂级数
的代入真实收敛。§14 的 $\psi$ 注入性只在特化前的
$k[[z]]$ 使用；特化后不再假设它注入。
特别 $\psi(g)$ 的旧非零 normal carry 保持不变；
没有声称 $\psi$ 保持未经 PD 化的 $E[p]$ ideal。

(1174.37) 的 gauge 随 (1174.40) 一并运输。
其 Hodge evaluation 为零，故保持原 filtered torsor
的唯一 Hodge 点；不是把原 étale 根相位设成零。
由此 (1174.39) 在原 ramified marked fibre 上仍代表
同一个 raw object。随后才作既定的群 pushout、实际
same-coset Cor 和完整 nonlinear contraction。

乘原 pointed Miller 的 actual $H^0_{\rm syn}$ 系数时，
primitive 的 first slot 为零，故 R1166 (1166.25)–(1166.27)
的这一次 external-product 修正确为零。
这是当前 scalar primitive 乘 degree-zero coefficient
的判断，不删除两个 moments 相乘时的 ordered 修正。

### 15.2. 原低 normal 支持与系数式不再限于二同源

式 (1174.39) 没有负 $z$ 次数。
§4 的原 degree-$d$ 系数第 $k$ 项包含
$$
z^{p(d-k)+k}(1+\gamma_p)^{d-k}g^k,
\qquad 0<p(d-k)+k<e.
$$
所以 actual tame trace 的第零 $e$-block 从 $u^1$
开始。模 $p$ 下，原最高 raw U 和仍满足
$J_{k,n}=0$ 对 $n<k+1$，特别 $J_0=0$。
每个 theta moment 的第一 log 槽由 (1174.34) 给出，
同样具有此支持；其 divided Frobenius 边界项为零，
闭性准确给 $a=N_u y$。

R1166 §19 的 S/Q 反对称消去、§20 的 ordered nonlinear
gauge 和本篇 §§6–7 的 factorial/Frobenius 尺度消去
因而全部适用。对每个 $\ell\in\mathcal A_p^{(6)}$，定义
$$
\begin{aligned}
A_{\ell,d}
 &=\bigl(\ell^2-\ell^{-d}\bigr)\mathsf A_d(E),\\
A'_{\ell,C,d}
 &=\ell\,\operatorname{Sym}^d(\psi_C^{-1})
                    \mathsf A_d(E/C)-\ell^{-d}\mathsf A_d(E),\\
B^{(\ell)}_{kl}
 &=(A_{\ell,4})_k(A_{\ell,8})_l
   -\sum_C(A'_{\ell,C,4})_k(A'_{\ell,C,8})_l.
\end{aligned}
\tag{1174.41}
$$
所有 quotient 值先按原 $\psi_C^{-1}$ 送回同一实际基。
若使用别的已选参考点，仍按 R1171 的右增量和完整
shear 运输。两个 primed 槽必须使用同一个 $C$。

于是原最高与两次配对 correlation 的准确读数是
$$
\boxed{\begin{aligned}
W_{\ell,r}^{\rm corr}
 &=\sum_{k=0}^{4}\sum_{l=0}^{8}
     \frac{k-l}{2(k+l+2)}\,B^{(\ell)}_{kl}\,
                  \Pi_r(U^{(4)}_k,U^{(8)}_l),\\
Z_{\ell,r}^{\rm corr}
 &=\sum_{k=0}^{4}\sum_{l=0}^{8}
     \frac{k+1}{k+l+2}\,B^{(\ell)}_{kl}\,
                  \Pi_r(U^{(4)}_k,U^{(8)}_l),
\qquad r=0,2 .
\end{aligned}}
\tag{1174.42}
$$
$W$ 为 BCH，$Z$ 为 ordered；原 $U_k^{(d)}=\omega^k\mu^{d-k}$。
全部分母小于 $p$。
(1174.42) 使用原完整 raw moments，不提前除
$\ell^2-\ell^{-d}$。该因子即使在某槽为零，
公式仍然成立。

对 $r=2$，目标指数仍是 $K=k+l-2$，其 target
filtration 为 $12$，读取 normal $K+4=k+l+2$。
真正 paired Tate factor、$\sigma$、阶乘、same-subgroup
和原 $n^{-2}$ 系数运输均与 §7/R1169 相同。
这里没有把它改成未配对的 degree-$8$ 普通乘积。

### 15.3. 原 affine Hecke 系统现在有完整的余有限右端

R1173 已唯一重建所有参考点的两条
$\mathsf A_4,\mathsf A_8$；实际 quotient 的值由其原
abelian 右增量取得。因此 (1174.41)–(1174.42) 给出
R1171 affine 系统在整个 (1174.23) 上的真实已知右端。

相应功能方程仍是 R1159/R1169 的跨曲线式：
最高槽使用
$(\ell^4+\ell^{-11})-\ell^2T_\ell^{(12)}$，
两次配对槽使用
$(\ell^4+\ell^{-11})-T_\ell^{(8)}$。
返回参考点时须加原中央 affine correction；
它由已知 abelian 值和同一个 reference-to-quotient
increment 决定，不含待求的中央参考值。

R1170/R1171 已证明这两个余有限辅助族的算子理想为一。
故以有限次实际算子和 (1174.42) 解线性系统，
即可恢复全参考点的原最高、两次配对中央第一层值。
无需逐字数值化 R1160 的 Galois conjugating word。
这里增加的是完整相关项的显式二次右端；
没有把单点 eigenvalue $v_\ell$ 当成真正 Hecke 算子。

这与 R1175 的全连接有限算法是两个独立入口。
本节没有执行任一算法，也没有宣称所得中央值、
原 global-subtracted 顶系数或任何 whole-disc 排除非零。
最低槽的正 $\lambda_\infty X T'$ 仍按 R1172
保留，其自己的 raw endpoint 读取不由 (1174.42) 冒得。

## 16. 新增 primary 及第一层范围

新增并亲读：

- T. Tsuji, *On p-adic nearby cycles of log smooth families*，
  BSMF 128 (2000), 529–575，
  [正式 PDF](https://www.numdam.org/article/BSMF_2000__128_4_529_0.pdf)。
  §2（印刷页539–546）的 PD embedding、不同 embedding/
  Frobenius 的 canonical comparison、product (2.5)、
  period map (2.8) 及 Proposition 2.11；
  Theorem 4.2（印刷页550）和 Theorem 5.1（印刷页555）。
  本文只在实际 henselian smooth log chart 消费其 exact
  比较；完成后是已给 object 的 functorial PD 运输。

- Stacks Project，
  [Lemma 59.55.1，Tag 03QO](https://stacks.math.columbia.edu/tag/03QO)：
  严格 henselian local scheme 上全局截面等于闭点 stalk。
  其在 (1174.31) 中的算术 descent 及 primitive groupoid
  用法已在 §13 说明。

§14 的完整 $\gamma_p$ 消元、ordinary 代表唯一性、
(1174.40) 的 actual specialization 和一般辅助族的
读式均由本文证明。
没有使用恒等 embedding 的 $J=0$ 假设，
没有把一次上链的 rational 比较直接约模，
也没有在各层分别选 primitive 后假定存在兼容整塔。
全塔先由原 R1156–1158 存在并支付水平延伸；
新 ordinary 结论精确限于其模 $p$ 层。
