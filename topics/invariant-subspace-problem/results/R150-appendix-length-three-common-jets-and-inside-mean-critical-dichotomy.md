# R150 附录：共同长度三 jets 的完整临界分类与内均值二分归约

日期：2026-11-13（UTC）。作者：normal_rebuild / Astra-ISP-1cf8c51d。

状态：**已证明。** 原完整六模式立方临界点若有非割线一次矩，且前三阶累积量共用长度三的曲线 jet 支撑，则支撑必为三个不同点，且恰为 $W_+$ 或 $W_-$。所有非约化长度三支撑均已排除。进一步，若普通第三矩的本质三空间 $W$ 包含这个非割线均值，则只余 $W=W_\pm$，或二、三阶累积量共用准确长度二的支撑而均值在其外。后一类仍开放。

## 1. 原核的完整接触阶数

仍用
$$
k(z,s)=v(z)^{\mathsf T}Kv(s)=-(z-s)^2q(z,s),
\qquad q(s,s)=-s^2(s+6)(s-2).
$$
有限点处令 $u_0=v(s),u_1=v'(s),u_2=v''(s)$，不除以阶乘，并置
$$
p_j(z)=u_j^{\mathsf T}Kv(z).
$$
在 $\infty$ 用局部曲线 $\widetilde v(t)=(t^5,t^4,\ldots,1)$ 在零处的同样导数。原精确接触表为：

| 物理点 $s$ | $\operatorname{ord}_s p_0$ | $\operatorname{ord}_s p_1$ | $\operatorname{ord}_s p_2$ |
|---|---:|---:|---:|
| $q(s,s)\ne0$ | $2$ | $1$ | $0$ |
| $s=2,-6$ | $3$ | $2$ | $1$ |
| $s=0,\infty$ | $4$ | $3$ | $2$ |

特别，对每个射影点都有
$$
\boxed{\operatorname{ord}_s p_0=\operatorname{ord}_s p_1+1,
\qquad \operatorname{ord}_s p_1\ge1.}
\tag{1.1}
$$

这不是数值判断。一般点的三个首系数为 $-q(s,s),2q(s,s),-2q(s,s)$。简单对角根处，令 $a=q_z(s,s)=q_s(s,s)\ne0$，首系数为 $-a,a,2a$。两个双重对角根处，完整局部多项式是
$$
\begin{array}{lll}
s=0:&p_0=5t^4-t^5,&
p_1=-32t^3+5t^4-t^5,\quad p_2=108t^2-8t^3+10t^4,\\
s=\infty:&p_0=-t^4-t^5,&
p_1=5t^3+5t^4+5t^5,\quad p_2=-16t^2-8t^3-64t^4.
\end{array}
\tag{1.2}
$$
[整数接触验证器](../notes/2026-11-13-six-mode-physical-jet-contact-verify.py)直接从原 $K$ 生成所有例外数据。

## 2. 非割线均值及真实 jet 累积量

一次矩的假设是
$$
\operatorname{rank}(y_{j+k})_{0\le j\le3,\ 0\le k\le2}=3.
\tag{2.1}
$$
对 $2s+t$、$s\ne t$ 型支撑，写
$$
y=a u_0+b u_1+c w,\qquad w=v_{\mathrm{hom}}(t).
$$
则 $b,c$ 都非零；否则一次矩只需长度至多二的子支撑，违反 (2.1)。对 $3s$ 型，写 $y=a u_0+b u_1+c u_2$，则同样有 $c\ne0$。

以下 Hankel 累积量形式来自对 $v(s)^{\otimes d}$ 求零、一、二阶导数，也可由有限多项式除法得到。所有累积量系数允许为零；不附加 $H$ 或 $V$ 的秩假设。

## 3. 排除双点加不同点

在基 $(u_0,u_1,w)$ 的对偶变量 $X,Y,Z$ 中，
$$
H=h_0X^2+2h_1XY+h_2Z^2,\qquad
V=v_0X^3+3v_1X^2Y+v_2Z^3.
$$
完整普通三次矩是
$$
T_3=(aX+bY+cZ)^3-6(aX+bY+cZ)H+4V.
\tag{3.1}
$$
最高原梯度要求
$$
T_3(p_0(z),p_1(z),p_t(z))\equiv0,
\qquad p_t(z)=w^{\mathsf T}Kv(z).
\tag{3.2}
$$

先设 $k(s,t)\ne0$，于是 $p_t$ 在 $s$ 为单位。置
$$
B=c^2-2h_2,\qquad C=c^3-6ch_2+4v_2.
$$
式 (3.1) 的 $Z^3,YZ^2,XZ^2$ 系数分别为 $C,3bB,3aB$。在 $s$ 评价先得 $C=0$。记 $r=\operatorname{ord}_s p_1\ge1$；由 (1.1)，$\operatorname{ord}_s p_0=r+1$。剩余最低可能阶数 $r$ 只有 $3bB p_1p_t^2$，所以 $B=0$。

此后含 $Z$ 的项恰为
$$
3b^2cY^2Z+6c(ab-2h_1)XYZ+3c(a^2-2h_0)X^2Z.
$$
代回的阶数为 $2r,2r+1,2r+2$；不含 $Z$ 的三次项至少为 $3r>2r$。唯一最低项 $3b^2c p_1^2p_t$ 的系数非零，矛盾。因此
$$
k(s,t)=0.
\tag{3.3}
$$

在 $t$ 处，$p_0(t)=p_t(t)=0$。令 $l=u_1^{\mathsf T}Kw=\partial_s k(s,t)$，最高条件只剩 $b^3l^3=0$，所以 $l=0$。这又使 $p_t$ 在 $s$ 至少二重。

若 $g=u_1^{\mathsf T}Ku_1=2q(s,s)\ne0$，接触表给 $p_1$ 一阶，而 $p_0,p_t$ 至少二阶。(3.1) 的唯一三阶项是 $b^3p_1^3$：均值乘二阶累积量至少四阶，三阶累积量至少五阶。故 $g=0$。

结合 $u_0^{\mathsf T}Ku_0=u_0^{\mathsf T}Ku_1=w^{\mathsf T}Kw=0$，已经得到
$$
K|_{\operatorname{span}\{u_0,u_1,w\}}=0.
$$
但[长度三曲线 jet 全等向平面的完整分类](R150-appendix-classification-of-isotropic-length-three-curve-jets.md)排除了每个 $2+1$ 型全等向三空间。故该支撑没有满足 (2.1) 的完整临界点；事实上最高条件已将它排除。

## 4. 排除三重点

在基 $(u_0,u_1,u_2)$ 中，累积量为
$$
H=h_0X^2+2h_1XY+2h_2XZ+2h_2Y^2,
$$
$$
V=v_0X^3+3v_1X^2Y+3v_2X^2Z+6v_2XY^2.
\tag{4.1}
$$
普通三次矩仍是 (3.1)，现在 $c\ne0$ 为均值的第二 jet 系数。

若 $q(s,s)\ne0$，在 $s$ 有 $p_0=p_1=0,p_2\ne0$。最高条件的值为 $c^3p_2^3\ne0$，矛盾。

若 $s=2,-6$，三个接触阶数为 $(3,2,1)$。均值首项由 $c p_2$ 给出，阶数一；(4.1) 的二阶累积量至少四阶，三阶累积量至少七阶。所以普通第三矩的三阶首项 $c^3p_2^3$ 无法抵消。

若 $s=0,\infty$，接触阶数为 $(4,3,2)$。均值阶数二，二阶累积量至少六阶，三阶累积量至少十阶。普通第三矩的唯一六阶首项仍为 $c^3p_2^3$；其他项至少八阶。

所有射影点已覆盖，故三重点也不可能产生满足 (2.1) 的完整临界点。

## 5. 共同长度三支撑的完整结论

长度三有效除子只有三个不同点、$2+1$、$3$ 三种类型。后两种已排除；[三个不同点的完整临界分类](R150-appendix-three-distinct-physical-support-complete-critical-classification.md)证明，前一种在 (2.1) 下完整临界性强迫三个点两两正交。因此
$$
\boxed{\text{共同长度三支撑与 (2.1)}
\quad\Longrightarrow\quad W=W_+\ \text{或}\ W=W_-.}
\tag{5.1}
$$
原三个有实际 first 逆的方向满足两个平面的二次条件，所以其匹配普通第三矩在此整类临界点上为零。本稿没有从值消失直接声称统一 Jacobian 幂数。

## 6. 本质三空间含均值时，剩余支撑只有准确长度二

现在只假设完整临界点的普通第三矩本质支撑 $W$ 三维，满足 (2.1)，且 $y\in W$。[二次差分归约](R150-appendix-essential-cubic-conormal-and-four-jet-support-reduction.md)已给
$$
\operatorname{Ran}(H-yy^{\mathsf T}/4)\subset W.
$$
故 $H,V$ 都由 $W$ 支撑。特别，$H$ 的矩阵秩及 $V$ 的一阶展平秩都至多三。

这里真正将低秩 Hankel 张量化为 jets，而不预设它们共用一个支撑。对 $D=10$ 的二阶矩或 $D=15$ 的三阶矩，令有限二元矩泛函为 $\Lambda_D:S_D\to\mathbb C$，$I_k$ 为互补次数配对的核，$b_k=\dim S_k/I_k$。有 $b_k=b_{D-k}$。若 $a$ 是首次非零关系次数，则 $b_{a-1}=a$；从该处起，两个坐标移位使理想子空间每阶至少增长一，故 $b_k$ 不增。

对非零张量，若原 $5$ 阶展平秩为 $1\le r\le3$，则 $b_5=r$ 且 $a\le5$。对称性给 $b_{D-a+1}=a$，于是
$$
a=b_{a-1}\ge b_5=r\ge b_{D-a+1}=a.
$$
所以 $a=r$，平台上 $b_r=r$，$I_r$ 恰一维。唯一关系 $g_r$ 使 $\Lambda_D$ 杀掉 $g_rS_{D-r}$。有限除法与中国剩余定理给准确长度 $r$ 的射影 jet 表示；每点最高 jet 系数非零，否则出现较低次数关系。展平像正是该 jet 空间。零张量单独取空支撑。

由此 $H,V$ 分别有唯一最小除子 $D_H,D_V$，长度均至多三。令 $D$ 为其并除子，每点取重数最大值。最初总长度至多六。五次有理正规曲线任意总长度至多六的不同或合流 jets 都线性无关：次数五多项式对该有限除子的插值映射满射，取对偶即得。它们的张成空间却包含于三维 $W$，故
$$
\deg D\le3.
\tag{6.1}
$$

若 $\deg D=3$，其 jet 空间就是 $W$。因为 $y\in W$，前三阶累积量真正共用这个长度三支撑，(5.1) 给 $W=W_\pm$。

若 $\deg D\le2$，记其 jet 空间为 $U$。普通三次张量
$$
T_3=y^{\otimes3}-2\operatorname{Sym}_{\Sigma}(y\otimes H)+4V
$$
由 $U+\mathbb Cy$ 支撑。其本质维数为三，故必须
$$
\boxed{\deg D=2,\qquad y\notin U,\qquad W=U+\mathbb Cy.}
\tag{6.2}
$$
这里 $\operatorname{Sym}_{\Sigma}$ 是三个不同位置之和。没有将 $y$ 免费加入较低秩张量的 jet 支撑。

因此在原非割线均值、$y\in W$ 及本质维数三的假设下，完整二分为
$$
\boxed{
W=W_\pm\quad\text{或}\quad
H,V\text{ 的最小并支撑准确长度二，且 }y\notin U.
}
\tag{6.3}
$$

## 7. 仍须处理的情形

后一类包含两个不同点与一个双 jet，允许 $H,V$ 各自继续降秩。本稿没有排除它，没有证明原三个匹配方向在该类都取零。均值在本质三空间之外的长度四问题，以及均值在二点割线簇、本质维数四至六的情形，保持各自已有范围。

这些结果只是原完整标量临界集的支撑识别与严格归约，没有新增实际算子分母，没有完成原 $F^3$ 全局 Jacobian 证书或普通 ISP。

