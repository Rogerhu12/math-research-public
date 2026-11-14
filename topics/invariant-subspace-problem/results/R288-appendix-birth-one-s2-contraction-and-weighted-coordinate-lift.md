# R288 附录：任意正权出生一 S2 的实际收缩与带权坐标提升

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / literature_audit。

**状态：已证明。** 对任意 $M\ge3$ 和任意独立正权，本稿证明 R275 首边加强充分式中的 (S2)，并给实际两塔映射的统一平方范数上界 $2/3$。这个上界未声称最优。证明使用同一实际物理层中的显式向量及其正交投影，不以已有出生一相邻定理代替更强的 (S2)。一般出生的 (S2)、(S1) 及一般相邻不等式仍未因此证明。

本稿接续[逐物理位完整 creation 行](R288-coordinate-occupation-collision-and-creation-joint-grams.md)。§7 同时保存无权共享右算子的严格阻碍，并构造一个真正满足两矩条件且具有上述范数界的带权坐标行。

## 1. 实际模型、归一与目标

取
$$
d=\sum_{i=1}^M b_iE_i,\qquad b_i>0,\qquad
\sum_{i=1}^M b_i^2=1,\qquad M\ge3.
$$
均匀缩放全部 $b_i$ 不改变下面 (S2) 的无量纲两塔映射，因此这个归一不损失一般性。记真空为 $\Omega$，标准一孔基为 $e_i$，并把
$$
b=\sum_i b_ie_i=d^*\Omega,\qquad
K=K_1=b^\perp\subset\mathcal H_1,\qquad L=K_0=\mathbb C\Omega.
$$
设 $P=I-bb^*$ 为 $K$ 上的正交投影。定义
$$
p_i=b_i^2,\quad m_r=\sum_i p_i^r,\quad
a=e_2(p)>0,\quad c=e_3(p)>0,
$$
以及
$$
r=P(b_i^3)_i,\qquad v=\|r\|^2=m_3-m_2^2.
\tag{1.1}
$$
用归一真幂最小逆
$\mathcal J_{j,t}=(d^j/j!)^\dagger|_{K_t}$，记
$$
J=\mathcal J_{1,1},\qquad G_1=J^*J,\qquad C_1=G_1^{-1},
\qquad J_2=\mathcal J_{2,0}.
$$
真空的前三级完整 Gram 是
$$
L_1=1,\qquad L_2=a^{-1},\qquad L_3=c^{-1},
\qquad J_2\Omega=\frac{(d^*)^2\Omega}{2a}.
\tag{1.2}
$$
这是完整行 $d^j/j!$ 的系数为 $\prod_{i\in I}b_i$、平方范数为 $e_j(p)$ 的直接计算。

三次桥 $B:K\to L$ 的真实伴随为 $B^*\Omega=r$，所以
$$
Q=B^*L_2=\frac r a,\qquad
A=\frac12(C_1Q+QL_3^{-1}L_2)
=\frac{C_1r}{2a}+\frac{cr}{2a^2}.
\tag{1.3}
$$
此处把 $K\leftarrow L$ 的单列映射与它在 $\Omega$ 上的值等同。目标实际映射为
$$
\mathcal T=JA+J_2a:L\longrightarrow\mathcal H_2.
\tag{1.4}
$$
两塔范围正交，因此 (S2) 准确为
$$
\|\mathcal T\|^2=A^*G_1A+a\le1.
\tag{1.5}
$$
下面证明更强的 $\|\mathcal T\|^2\le2/3$。

## 2. 首精度的完整物理矩阵与两塔身份

令 $d_2=d|_{\mathcal H_2}:\mathcal H_2\to\mathcal H_1$。在标准一孔基中，
$$
F=d_2d_2^*=\operatorname{diag}(1-2p_i)+bb^*.
\tag{2.1}
$$
对 $M\ge3$，$d_2^*$ 单射：若 $d_2^*z=0$，则对每个 $i\ne j$ 有
$b_iz_j+b_jz_i=0$。除以 $b_ib_j$ 后，三个不同指标即迫所有 $z_i/b_i=0$。故 $F>0$，而
$$
J=d_2^*F^{-1}|_K,\qquad G_1=P F^{-1}|_K.
\tag{2.2}
$$
设 $H_0=P\operatorname{diag}(1-2p_i)|_K$。因为
$$
m_2=1-2a,\qquad Fb=4ab-2r,
$$
在同一正交分解 $\mathcal H_1=K\oplus\mathbb Cb$ 中，实际矩阵为
$$
F=\begin{pmatrix}H_0&-2r\\-2r^*&4a\end{pmatrix}.
$$
因此真正完整逆的 Schur 补给
$$
\boxed{C_1=H_0-\frac{rr^*}{a}>0.}
\tag{2.3}
$$
另有精确的两塔身份
$$
\boxed{d_2^*r=JC_1r-J_2v.}
\tag{2.4}
$$
确切地，$d_2^*r\perp\ker d_2$；其在 $J K$ 上的系数由
$J^*d_2^*|_K=(d_2J)^*=I_K$ 给出为 $C_1r$。在剩余真空第二塔上，
$$
\frac{d^2}{2}d^*r=-Br=-\|r\|^2=-v,
$$
故系数是 $-v$。也可由 (2.1)–(2.3) 直接逐项核验 (2.4)。没有把非正交源坐标当作正交基。

## 3. 一个同源的显式物理试向量

对 $i<j$，置
$$
q_{ij}=1-p_i-p_j,\qquad
\mu_{ij}=\sum_{\ell\ne i,j}p_\ell^2,\qquad
k_{ij}=q_{ij}^2+2\mu_{ij}\ge0.
\tag{3.1}
$$
定义实际二孔向量 $z$：
$$
\boxed{
z=\sum_{i<j}b_ib_j
\left(1+\frac{c}{a^2}-\frac{k_{ij}}{3a}\right)e_{ij}.
}
\tag{3.2}
$$
它是同一个物理空间中的向量，尚未先投到两塔。下面准确计算其两个塔系数。

先定义辅助向量
$$
u=\sum_{i<j}b_ib_j f_{ij}e_{ij},\qquad
f_{ij}=\frac{1-4m_2+p_i+p_j+2(p_i-p_j)^2}{6}.
\tag{3.3}
$$
对每个固定 $i$，直接展开给
$$
\sum_{j\ne i}p_j f_{ij}
=\frac{1-3m_2+2m_3}{6}=c.
$$
因此
$$
d_2u=cb.
\tag{3.4}
$$
令
$$
w=2au-\frac c2d_2^*b.
\tag{3.5}
$$
由 $Fb=4ab-2r$，得到
$$
d_2w=cr,\qquad d^2w=0.
\tag{3.6}
$$
于是 $w-cJr\in K_2:=\ker d_2$。这个差可能非零；本稿保留它的额外费用。

由 (2.4)，向量
$$
\widetilde z=\frac{d_2^*r+J_2v}{2a}
+\frac{w}{2a^2}+J_2a
\tag{3.7}
$$
具有准确分解
$$
\boxed{
\widetilde z=JA+J_2a+
\frac{w-cJr}{2a^2},\qquad
\frac{w-cJr}{2a^2}\in K_2.
}
\tag{3.8}
$$
三个分量正交。这已经给出第一塔系数 $A$、第二塔系数 $a$，并保留全部高出生 primitive 余项。

最后验证 $\widetilde z=z$，使试向量完全显式。使用
$$
v=a+3c-4a^2,\qquad
f_{ij}=\frac{q_{ij}}2-\frac{k_{ij}}3,
$$
及 $d_2^*b$ 的 $e_{ij}$ 系数 $2b_ib_j$，(3.7) 的系数准确化为 (3.2)。所以
$$
\boxed{P_{K_2^\perp}z=\mathcal T\Omega,
\qquad \|\mathcal T\|^2\le\|z\|^2.}
\tag{3.9}
$$
当 $M=3$ 时 $K_2=0$，同样有效；无需构造不存在的上出生第二高度。

还可以不经过 $u,w$ 直接计算删除系数。令
$P_p=\operatorname{diag}(p_i)$，则 (2.3) 与 $v=a+3c-4a^2$ 给
$$
A=\left(2-\frac c{a^2}\right)r-\frac1aP P_pr.
\tag{3.10}
$$
对每个 $i$，逐项展开 (3.1) 得
$$
\sum_{j\ne i}p_jk_{ij}=1-3p_i+3p_i^2-m_3,
\qquad m_3=1-3a+3c.
$$
代入 (3.2)，再使用 $r_i=b_i(p_i-m_2)$，准确得到
$$
\boxed{d_2z=A+2ab-r,\qquad d^2z=2a.}
\tag{3.11}
$$
由于 $dJ_2=2b-r/a$，(3.11) 也直接证明
$z-JA-J_2a\in K_2$。这再次核定了同一物理向量的两个塔系数与归一因子。

## 4. 显式向量的统一范数预算

首先有准确的加权一阶矩
$$
\boxed{\sum_{i<j}p_ip_jk_{ij}=3c.}
\tag{4.1}
$$
一种逐单项式核验是令 $e_4=e_4(p)$（$M<4$ 时为零），则
$$
\sum_{i<j}p_ip_jq_{ij}^2=c+8e_4,
\qquad
\sum_{i<j}p_ip_j\mu_{ij}=c-4e_4.
$$
两式按 (3.1) 合并即得 (4.1)。因此 (3.2) 的范数准确为
$$
\boxed{
\|z\|^2
=a+\frac1{9a^2}\sum_{i<j}p_ip_jk_{ij}^2
-\frac{c^2}{a^3}.
}
\tag{4.2}
$$
这里还可直接看到 $\sum_{i<j}p_ip_j(1+c/a^2-k_{ij}/(3a))=a$，与第二塔系数吻合。

因为 $0\le q_{ij}\le1$、$\mu_{ij}\le m_2=1-2a$，
$$
\boxed{0\le k_{ij}\le1+2m_2=3-4a.}
\tag{4.3}
$$
故 (4.1) 给
$$
\sum_{i<j}p_ip_jk_{ij}^2\le3(3-4a)c.
$$
置 $x=c/a^2$，于是
$$
\|z\|^2\le x+a\left(1-\frac{4x}{3}-x^2\right).
\tag{4.4}
$$
参数范围为 $0<a\le1/2$、$0<x\le2/3$。后一界无需引用额外定理：由 $\sum_i p_i=1$，直接展开
$$
\boxed{
2a^2-3c
=2\sum_{i<j}p_i^2p_j^2
+\sum_{i<j<k}p_ip_jp_k(p_i+p_j+p_k)\ge0.
}
\tag{4.5}
$$

令 $h(x)=1-4x/3-x^2$。若 $h(x)\le0$，(4.4) 至多为 $x\le2/3$；若 $h(x)\ge0$，用 $a\le1/2$ 得
$$
x+ah(x)\le\frac12+\frac x3-\frac{x^2}{2}
=\frac59-\frac12\left(x-\frac13\right)^2\le\frac59.
$$
结合 (3.9)，得到所需定理：
$$
\boxed{
A^*G_1A+L_1L_2^{-1}L_1
=\|\mathcal T\|^2\le\|z\|^2\le\frac23<1.
}
\tag{4.6}
$$
此处所有坐标、最小逆与正交投影属于同一个实际任意正权模型。

## 5. 非零第一塔确已覆盖

若 $b_i$ 不全相等，则 $r=P(b_i^3)_i\ne0$：否则 $b_i^3$ 与 $b_i$ 成比例，正权会迫所有 $b_i^2$ 相等。又
$$
A=\frac1{2a}\left(C_1+\frac ca I_K\right)r,
$$
括号严格正定，所以此时 $A\ne0$。(4.6) 因此确实控制了一个非零的第一塔及第二塔的共同范数，不是仅验证等权 $B=0$ 情形。

## 6. 原问题中的准确适用范围

本稿证明的是 [R275 三块充分式](R275-appendix-first-edge-three-block-equivalence-and-parameter-free-sos.md)中的 (S2)，在旧上出生 $s=1$、下出生为真空、$M\ge3$ 的全部独立正权模型上成立。它比单纯引用已有出生一普通相邻定理更强，但没有证明 (S1)。R275 的一步归纳还必须保留 (S1) 与所需旧相邻块；本稿不把一个已付分量当成整个一般归纳已经闭合。

同样，$2/3$ 只是上述显式试向量估计给出的统一常数，没有证明它最优，也没有把有限出生一证明称作 ISP 的完成。

## 7. 无权共享行的阻碍与一个真正可解的带权行

沿用 R288 的实际删除 $R_i=E_i|_K:K\to L$。当 $s=1$ 时，
$$
R_i^*\Omega=e_i-b_i b.
\tag{7.1}
$$
因此无权共享右算子 $Y_i=R_i^*Y$ 产生
$$
\sum_iE_i^*R_i^*Y
=-(d^*)^2\Omega\,Y,
\tag{7.2}
$$
完全位于第二塔，没有第一塔。§5 已证明一般非等权 $A\ne0$，故这种无权共享右算子不能满足 R288 的第一矩条件。这个严格阻碍并不排除带权或不同右算子的共同提升。

现在给一个对全部正权实际可解且已付范数的带权行。定义
$$
v_0=F^{-1}A+\frac b2\in\mathcal H_1,\qquad
\theta_i=-\frac{(v_0)_i}{b_i},\qquad
Y_i=\theta_iR_i^*:L\to K.
\tag{7.3}
$$
$F>0$ 已在 §2 用完整实际矩阵证明，且所有 $b_i>0$，因此 (7.3) 没有隐藏的逆域条件。利用 $E_i^{*2}=0$，
$$
\begin{aligned}
\sum_iE_i^*Y_i\Omega
&=-\sum_i\theta_i b_iE_i^*b\\
&=d_2^*v_0
=JA+\frac12d_2^*b
=JA+J_2a
=\mathcal T\Omega.
\end{aligned}
\tag{7.4}
$$
所以这些同一模型中的 $Y_i$ 同时满足 R288 的两矩条件
$$
\sum_iA_iY_i=A,\qquad
-\sum_i b_i^2R_iY_i=L_2^{-1}L_1=a,
$$
而共同物理范数已由 (4.6) 支付：
$$
\left\|\sum_iE_i^*Y_i\right\|^2\le\frac23.
$$
这里没有把各列范数分别相加；交叉抵消保持在一个共同物理映射中。$\theta_i$ 不要求同号。

最后，对任意合法出生，都有
$$
P_{K_{s+1}}E_i^*R_i^*=0.
\tag{7.5}
$$
其伴随是实际 primitive 删除的逐位平方零
$R_i^{(s)}R_i^{(s+1)}=0$。故任意 $Y_i=R_i^*Z_i$ 类型的共同提升都没有最高 primitive 塔；但一般出生的两矩条件及其实际收缩仍未由这一点得到。
