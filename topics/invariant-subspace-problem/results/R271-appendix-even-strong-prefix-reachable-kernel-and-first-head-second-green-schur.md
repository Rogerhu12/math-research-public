# R271 附录：原偶段的可达核与首头第二逆能量的一位完整正 Schur

日期：2026-11-16（UTC）。

作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 对原 N/Y 真实头与有限连续强位段，本稿先证明一个物理支撑结论：偶数强位段时，完整 $\ker C$ 与 $\ker C^*$ 正交，因此每个核向量确实可由 $C$ 提升。随后对同一个原首头来源给出新增一位后的完整第二逆能量公式。所有核外返回与最小范数自由均保留；该公式不提供第二逆能量的统一上界，也不证明 $N=M$。

内积对第一变量线性。依据为：

- [原真实头与真实链权](R239-appendix-true-head-jordan-cost-and-pure-graded-formal-range.md)，§§1、3。
- [首物理头的准确恢复](../notes/2026-11-15-first-physical-head-exact-gauge-recovery-and-same-gap-scaling-789f-next.md)，§1。
- [匹配完整 Schur 的首远孔读数](R271-appendix-matched-full-resolvent-first-far-hole-and-native-mean-feedback.md)。
- [移动第一远孔整行](R271-appendix-moving-first-far-coherent-row-bessel-and-matched-source-cost.md)。

## 1. 原有限对象与准确分级

取 $m\ge1$、$d=2^m$，原真实头为
$$
A_m=F_m(B_m),\qquad
B_me_i=\frac{W_i}{W_{i-1}}e_{i-1}\quad(i\ge1),\qquad B_me_0=0,
$$
其中 $W_0=1$，且 $W_i=\prod_{j:\,\mathrm{bit}_j(i)=1}d_j$；原系数函数为
$
F_{N,m}(z)=\sum_{i<m}b_i\frac{z^{2^i}}{d_i},\qquad
F_{Y,m}(z)=\sum_{i<m}b_i\frac{z^{2^i}}{d_i+z^{2^i}},
\qquad b_i=(i+1)^{-2}.
$$
Y 型在幂零矩阵上按其有限 Taylor 截断取值。两型均有
$$
F_m'(0)=d_0^{-1},\qquad A_m^d=0,\qquad A_me_1=e_0,\qquad A_me_0=0.
\tag{1.1}
$$

令 $R\ge0$ 为整数，$x=m+R$，并取**全部**前缀强位：
$$
E=D_{[m,x)}=\sum_{m\le i<x}b_iE_i,\qquad
C=A_m\otimes I+I\otimes E,\qquad h=d+R.
\tag{1.2}
$$
这里 $E_i$ 是原 Boolean 删除，有限头空间为
$\mathcal H_{<m}\otimes\mathcal H_{[m,x)}$。
没有选择强位的对称子块，也没有删除任何 primitive 来源。

只在本稿中，把头的**整数标签** $i$ 加上强位孔数 $q$ 记作级
$$
\mathcal G=i+q.
$$
这不声称 $A_m$ 齐次降一级。实际 $F_m(B_m)$ 含多种降级，
这一点在下面的支撑证明中完整保留；也不声称任何 Gram 逆保持这个级。

## 2. 两个真核的物理半区支撑

**命题 2.1。** 令
$$
\ell=\left\lfloor\frac{R+d-1}{2}\right\rfloor .
$$
则
$$
\boxed{
\ker C\subset\{\mathcal G\le\ell\},\qquad
\ker C^*\subset\{\mathcal G\ge R+d-1-\ell\}.
}
\tag{2.1}
$$
特别，当 $R$ 为偶数时，$d$ 为偶数，故
$$
\boxed{
\ker C\perp\ker C^*,\qquad
\ker C\subset\operatorname{Ran}C.
}
\tag{2.2}
$$
$R$ 为奇数时，本稿仅断言两个支撑半区最多在一个中央级相遇。

### 2.1 有限 Boolean 删除的所需单射范围

先取无权删除 $D_0$ 与创建 $D_0^*$。逐位计算给
$$
[D_0,D_0^*]=R-2N.
$$
若 $u\in\ker D_0\cap\mathcal H_s$，则归纳得到
$$
D_0(D_0^*)^k u
=k(R-2s-k+1)(D_0^*)^{k-1}u.
\tag{2.3}
$$
相应的 primitive 塔正交分解第 $q$ 层，塔的出生满足
$0\le s\le\min(q,R-q)$。这个分解可直接逐层归纳：
在下半层，$D_0D_0^*=D_0^*D_0+(R-2q)I$ 给创建单射；
取其像的正交补就是下一 primitive 核，再由 (2.3) 继续每条塔。
补集反射给上半层，故全部层均被这些塔覆盖。

若 $2q\ge R+d$，则每条出现的塔都有
$q-s\ge2q-R\ge d$，所以 (2.3) 连续 $d$ 次的系数均非零。因此
$$
D_0^d:\mathcal H_q\longrightarrow\mathcal H_{q-d}
\quad\text{在 }2q\ge R+d\text{ 时单射}.
\tag{2.4}
$$
对于所有正权 $b_i$，对角映射
$T e_I=(\prod_{i\in I}b_i)e_I$ 给 $E=T^{-1}D_0T$。
它只用于有限维代数单射性，不支付任何条件数。因此
$$
y\in\ker E^d\quad\Longrightarrow\quad
y_q=0\quad(q>\ell).
\tag{2.5}
$$
若所写范围超出实际层数，结论按空层理解；也覆盖 $R<d$。

### 2.2 原真实首头列

令 $\psi_m$ 为 $F_m$ 在零点的逆芽，只取模 $z^d$ 的有限多项式。
其最低项为 $d_0z$。对 $v=(v_0,\ldots,v_{d-1})\in\ker C$，
$A_mv=-Ev$、$A_m^dv=0$ 给
$$
E^dv_i=0,\qquad B_mv=\psi_m(-E)v.
$$
沿原 $B_m$ 的行递推，
$$
v_i=W_i^{-1}\psi_m(-E)^iy,\qquad y=v_0\in\ker E^d.
\tag{2.6}
$$
反过来，这个式子对每个 $y\in\ker E^d$ 构成真核向量：
$B_m v=\psi_m(-E)v$，再代回 $F_m$ 即得
$(A_m+E)v=0$。因而 (2.6) 没有少取核来源。

在 $\psi_m(-E)^i$ 中每个非零单项式都是 $E^k$、$k\ge i$。
若它来自 $y_q$，其输出级为 $i+q-k\le q$。
由 (2.5)，这证明 (2.1) 的第一个包含。

### 2.3 原补集反射

在头上取 $J_me_i=e_{d-1-i}$，在强位上取全补集反射，
其张量积记作 $\mathcal J$。
原链权满足
$\alpha_{v_2(d-i)}=\alpha_{v_2(i)}$，所以
$J_mB_mJ_m=B_m^*$。
两个 $F_m$ 的有限 Taylor 系数均为实数，且
$\mathcal J E\mathcal J=E^*$。于是
$$
C^*=\mathcal J C\mathcal J.
\tag{2.7}
$$
$\mathcal J$ 将级 $\mathcal G$ 送到 $R+d-1-\mathcal G$，
故第二个包含随即成立。偶 $R$ 时 $R+d-1$ 为奇数，两个支撑区正交。
有限维中 $\operatorname{Ran}C=(\ker C^*)^\perp$，得到 (2.2)。

作为纯代数核对，原 $A_m$ 的 Jordan 型是一条偶长 $d$ 链；
偶数 Boolean 段的 Jordan 长度全为奇数。
Kronecker 和的长度因而全为偶数，亦说明没有长度一的块，
从而 $\ker C\subset\operatorname{Ran}C$。
上述代数包含也能直接推出原 Hilbert 度量中的核正交。(2.1) 额外给出具体的原物理半级支撑范围；这一更强支撑信息不是该非单位相似核对本身的结论。

## 3. 新增一位的完整核与指定来源增益

以下 $R$ 为偶数，记
$$
K=\ker C,\quad Z=\ker C^*,\quad P=P_K,\quad
G=(CC^*)^\dagger,\quad
\Gamma=P G|_K.
\tag{3.1}
$$
因为 $K\subset\operatorname{Ran}C$，$\Gamma$ 在 $K$ 上严格正。
全部 MP 均为当前原有限头的真实 MP；没有环境换序。

新增一个权 $b>0$ 的真 Boolean 位，按真空／占据写
$$
C_b=\begin{pmatrix}C&bI\\0&C\end{pmatrix}.
\tag{3.2}
$$
由 (2.2)，其完整核准确为正交和
$$
\ker C_b=(K\oplus0)\ \oplus^\perp\ J_bK,\qquad
J_bv=\binom{-bC^\dagger v}{v}.
\tag{3.3}
$$
证明：核方程给 $Cv_1=0$、$Cv_0=-bv_1$；每个
$v_1\in K$ 都可提升，全部 $v_0$ 是
$-bC^\dagger v_1+k$、$k\in K$。而 $C^\dagger v_1\perp K$。
特别
$$
J_b^*J_b=I+b^2\Gamma.
\tag{3.4}
$$

对任意同一头 forcing $f$，令
$$
t=(C^*)^\dagger f,\qquad \theta=P t.
$$
由 (3.3)--(3.4)，新增完整核投影的增益是
$$
\boxed{
\|P_{\ker C_b}(f,0)\|^2-\|P_Kf\|^2
=b^2\left\langle\theta,(I+b^2\Gamma)^{-1}\theta\right\rangle.
}
\tag{3.5}
$$
它使用全部新核，不是一个候选核向量的费用上界。

## 4. 首头的第一逆与第二逆必须分开

令 $e_0,e_1$ 都含原强位真空。原 (1.1) 给 $Ce_1=e_0$，
且 $e_0\in K$。因此
$$
\boxed{
(C^*)^\dagger e_1=G e_0,\qquad
\langle e_0,G e_0\rangle=\|C^\dagger e_0\|^2\le1.
}
\tag{4.1}
$$
第一式是一般 MP 恒等式
$(C^*)^\dagger=(CC^*)^\dagger C$ 的当前指定列。
第二式只用了合法前像 $e_1$。

设
$$
v=(I+b^2\Gamma)^{-1}e_0.
\tag{4.2}
$$
最小化 $C_by=(e_0,0)$ 的全部前像，得到
$$
\boxed{
C_b^\dagger(e_0,0)=\binom{C^\dagger v}{b\Gamma v}.
}
\tag{4.3}
$$
具体地，$y_1\in K$，而
$y_0=C^\dagger(e_0-by_1)+k$；先极小化得 $k=0$，
再在 $y_1\in K$ 上极小化
$\langle\Gamma(e_0-by_1),e_0-by_1\rangle+\|y_1\|^2$，
即得 (4.3)。

故第一逆能量准确为
$$
\boxed{
\left\langle(e_0,0),(C_bC_b^*)^\dagger(e_0,0)\right\rangle
=\left\langle e_0,\Gamma(I+b^2\Gamma)^{-1}e_0\right\rangle.
}
\tag{4.4}
$$
等价地，其下降量为
$b^2\langle\Gamma e_0,(I+b^2\Gamma)^{-1}\Gamma e_0\rangle$。
(3.5) 用 $f=e_1$ 也给同一式，因为
$\|P_K e_1\|^2=1-\|C^\dagger e_0\|^2$。

实际移动第一远孔门需要的却是
$S_x\|Ge_0\|^2$，即第二逆能量。
(4.4) 本身只控制压到 $K$ 的 $\Gamma$，不能替换这个量。

## 5. 首头第二逆的完整正 Schur

置
$$
r=(I-P)Gv,\qquad
\mathcal A=(C^*)^\dagger|_Z:Z\longrightarrow\mathcal H_{<x},
\qquad
q=(C^*)^\dagger r.
\tag{5.1}
$$
这里的 $q$ 是明确核外返回列；不是尾孔数。

**定理 5.1。** 原完整第二逆满足
$$
\boxed{
\begin{aligned}
\|(C_bC_b^*)^\dagger(e_0,0)\|^2
&=\|Gv\|^2+
 \min_{z\in Z}\{\|z\|^2+
        b^2\|(C^*)^\dagger(r+z)\|^2\}\\
&=\|Gv\|^2+
 b^2\left\langle q,(I+b^2\mathcal A\mathcal A^*)^{-1}q\right\rangle.
\end{aligned}
}
\tag{5.2}
$$
两项均非负；最后的逆为整个实际目标空间上的正逆。

证明：第二逆向量是对 (4.3) 再取 $C_b^*$ 的最小原像。
先解第一行
$$
C^*t_0=C^\dagger v.
$$
其全部解为 $t_0=Gv+z$、$z\in Z$，因为
$C^*Gv=C^\dagger v$。
第二行成为
$$
C^*t_1=-b[(I-P)Gv+z].
$$
$K\perp Z$ 保证右侧确在
$K^\perp=\operatorname{Ran}C^*$。
其全部解为
$$
t_1=-b(C^*)^\dagger(r+z)+z_1,\qquad z_1\in Z.
$$
$Gv\in\operatorname{Ran}C=Z^\perp$，且
$(C^*)^\dagger(r+z)\in\operatorname{Ran}C=Z^\perp$。
所以先极小化得 $z_1=0$，剩余恰为 (5.2) 第一行。
这已保留 $\ker C_b^*$ 的全部自由。

最后，最小化
$\|z\|^2+b^2\|q+\mathcal A z\|^2$
给
$z=-b^2(I+b^2\mathcal A^*\mathcal A)^{-1}\mathcal A^*q$；
代回并用正 Woodbury 身份得第二行。没有把 $P$、
$G$、$C$ 或任何 MP 逆相互交换。

## 6. 对当前原来源的准确用途

在标准 $R=d$ 的实际强尾联块中，(2.2) 无附加条件成立。
若原强位按其原权依次增加，上述公式适用于每个偶数 $R$ 到
$R+1$ 的一步；不能把下一奇数段的核正交仍当作自动成立。

(5.2) 显示当前未付费用的具体位置：除了
$G(I+b^2\Gamma)^{-1}e_0$，还有同一原来源的
$(C^*)^\dagger(I-P_K)G(I+b^2\Gamma)^{-1}e_0$，
并且它只在真正 $\ker C^*$ 自由上作共同正 Schur。
不能由 (4.4) 的单调性、短池核截面，或第一逆标量不超过一，
推出第二逆有界。

本稿不改变匹配 $r_w,s_f$、全部 $h$ 段、真正帽逆伴随或非零锚。
它把原首头的一位第二能量写成可直接继续估计的同源公式；
尚未支付移动 $m,R$ 时的核外返回，原 $N=M$ 继续未证。
