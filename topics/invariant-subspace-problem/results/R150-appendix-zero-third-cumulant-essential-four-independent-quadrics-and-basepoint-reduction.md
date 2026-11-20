# R150 附录：第三累积量为零的本质四维支必有独立双二次关系和唯一基点

日期：2026-11-20（UTC）。作者：Astra-ISP-b2a9acde-20261120 / literature；AI-assisted，GPT-6 Astra Pro。

**状态：以下原完整临界条件下的进一步归约已证明。** 若原第三累积量 $V=0$，而第三普通矩 $T_3$ 的本质维数为四，则：
1. 原 $H$ 秩四、$y\in E=\operatorname{Ran}H$，并有唯一准确长度四公共 jet divisor $D$；
2. 最高式给出的 $C=yy^{\mathsf T}-6H$ 与原二阶梯度张量 $N$ 必线性无关，特别 $N\ne0$；
3. $E$ 的物理投影必有且仅有一个简单基点，投影曲线是非退化的双有理有理四次曲线。

本稿完整排除的是第二步中看似可能的 $N=0$、四维限制型秩二的例外。它不将剩余有基点分支宣布为空，也未证明该剩余支的三个匹配 Bell 值均零。

## 1. 原记号及已付起点

使用 [原 Schur 稿](R150-appendix-six-mode-cubic-bell-third-moment-schur-reduction.md) 的非退化六阶对称 $K$、原曲线 $v(z)=(1,z,\ldots,z^5)^{\mathsf T}$、原 Hankel 累积量 $y,H,V$。写
$$
F=\tfrac12y^{\mathsf T}Ky,\quad p=Ky,\quad h=Hp,\quad
b=p^{\mathsf T}Hp,\quad \tau_2=\operatorname{tr}((KH)^2).
$$
在 $V=0$ 时
$$
T_3(r)=(y^{\mathsf T}r)
       \big[(y^{\mathsf T}r)^2-6H(r,r)\big].
\tag{1.1}
$$

[秩三外值域排除](R150-appendix-zero-third-cumulant-rank-three-outer-range-exclusion.md) 已从完整原梯度证明：本质维数四时
$$
\operatorname{rank}H=4,\qquad y\in E=\operatorname{Ran}H,
\tag{1.2}
$$
而 $E$ 为由 $H$ 唯一确定的准确长度四曲线 jet 空间，包括全部重根和无穷远。

同稿从原可逆 $J_2$ 及最高式保留
$$
P(z)^2=6v(z)^{\mathsf T}KHKv(z),\qquad
P(z)=y^{\mathsf T}Kv(z),
\tag{1.3}
$$
$$
\boxed{\ \tau_2=b/6.\ }
\tag{1.4}
$$
原 Hankel 性还给 $\operatorname{tr}(KH)=0$。

令
$$
C=yy^{\mathsf T}-6H,
$$
$$
N=Fyy^{\mathsf T}-2FH
 -2(yh^{\mathsf T}+hy^{\mathsf T})+4HKH.
\tag{1.5}
$$
两者均由 $E$ 支撑；原最高及二阶梯度给
$$
v(z)^{\mathsf T}KCKv(z)=
v(z)^{\mathsf T}KNKv(z)=0.
\tag{1.6}
$$
下面使用原这些张量，不任取新的投影二次式。

## 2. 若两个二次式相关，只可能出现一个明确的 $N=0$ 型

取满列秩的六乘四矩阵 $U$，使
$$
H=UU^{\mathsf T},\qquad y=Ux.
$$
置
$$
S=U^{\mathsf T}KU,\qquad a=Sx,\qquad \mu=x^{\mathsf T}x.
\tag{2.1}
$$
则
$$
h=Ua,\quad 2F=x^{\mathsf T}a,\quad b=a^{\mathsf T}a,\quad
\operatorname{tr}S=0,\quad \operatorname{tr}S^2=b/6.
\tag{2.2}
$$
并且 $\operatorname{rank}S\ge2$：四维 $E$ 在六维非退化空间中的根空间维数至多二。

在 $U$ 坐标中，
$$
C_E=xx^{\mathsf T}-6I_4,
$$
$$
N_E=Fxx^{\mathsf T}-2FI_4
 -2(xa^{\mathsf T}+ax^{\mathsf T})+4S.
\tag{2.3}
$$
反设 $N=\lambda C$。对 (2.3) 的等式取迹，并乘以 $x$，分别得到
$$
(\mu-16)F+(24-\mu)\lambda=0,
\tag{2.4}
$$
$$
2(2-\mu)a=(6-\mu)(F-\lambda)x.
\tag{2.5}
$$

若 $\mu\ne2$，(2.5) 给 $a=\sigma x$。若 $\mu=0$，则 $F=0$，由 (2.4)、(2.5) 得 $\lambda=0,a=0$，再由 (2.3) 得 $S=0$，矛盾。若 $\mu\ne0$ 但 $\sigma=0$，同样先得 $F=0$；除 $\mu=24$ 外由 (2.4) 得 $\lambda=0$，在 $\mu=24$ 时由 (2.5) 仍得 $\lambda=0$，又矛盾。

所以此时 $\mu\sigma\ne0$。因 $x$ 非等向，$\mathbb C^4=\mathbb Cx\oplus x^\perp$，而 (2.3) 在 $x^\perp$ 上迫
$$
S|_{x^\perp}=\frac{F-3\lambda}{2}I.
$$
由 $\operatorname{tr}S=0$，该标量为 $-\sigma/3$。于是
$$
\operatorname{tr}S^2=\frac43\sigma^2,\qquad
b=\sigma^2\mu.
$$
(1.4) 迫 $\mu=8$，从而 $F=4\sigma$。在 $x^\perp$ 上比较给
$\lambda=14\sigma/9$，而在 $x$ 上比较 $N_E=\lambda C_E$ 给
$-4\sigma=2\lambda$，即 $\lambda=-2\sigma$。矛盾。

因此只可能 $\mu=2$。由 (2.5) 得 $F=\lambda$，再由 (2.4) 得 $F=\lambda=0$。所以
$$
S=\tfrac12(xa^{\mathsf T}+ax^{\mathsf T}),\qquad
x^{\mathsf T}a=0.
$$
其平方迹为 $a^{\mathsf T}a=b$，再用 (1.4) 得 $b=0$。$a$ 不能为零，否则 $S=0$。综上，相关性只可能导致
$$
\boxed{\ N=0,\quad F=b=0,\quad
x^{\mathsf T}x=2,\quad a\ne0,\quad
x^{\mathsf T}a=a^{\mathsf T}a=0,\quad
S=\tfrac12(xa^{\mathsf T}+ax^{\mathsf T}).\ }
\tag{2.6}
$$
下面保留这个例外的全部原物理约束，并将它排除。

## 3. 用原满秩 $H$ 作 Frobenius 配对

设 $D$ 的长度为四。选一个不经过其支撑的射影无穷远位置，以原齐次曲线在该图中的正规列 $u(t)$ 表示原向量。令
$$
\mathcal A=\mathbb C[t]/(g(t))
  \simeq\prod_i\mathbb C[\epsilon_i]/(\epsilon_i^{n_i}),
\qquad \sum_i n_i=4.
\tag{3.1}
$$
取 $H$ 自己的原 jet 泛函 $\tau$，则
$$
H(r,s)=\tau(X_rX_s),\qquad X_r=r^{\mathsf T}u(t)\bmod g.
\tag{3.2}
$$
原 $H$ 秩四，故各局部最高 jet 系数非零，配对
$(X,Y)\mapsto\tau(XY)$ 非退化。原五次式向 $\mathcal A$ 的映射满射，因此存在唯一 $f\in\mathcal A$，使
$$
y^{\mathsf T}r=\tau(fX_r).
\tag{3.3}
$$
令
$$
q=X_p,\qquad
k(s,t)=u(s)^{\mathsf T}Ku(t)\bmod(g(s),g(t)).
\tag{3.4}
$$
从 (2.1) 的坐标或直接由 (3.2) 的非退化配对，
$$
\tau(f^2)=x^{\mathsf T}x=2,\quad
\tau(q^2)=b=0,\quad \tau(fq)=2F=0,\quad q\ne0.
\tag{3.5}
$$

原 $N=0,F=0$ 是完整张量身份
$$
HKH=\tfrac12(yh^{\mathsf T}+hy^{\mathsf T}).
$$
将两侧分别与任意 $r,s$ 收缩，再用双重 Frobenius 配对的非退化性，精确得到
$$
\boxed{\ k(s,t)=\tfrac12\big(f(s)q(t)+q(s)f(t)\big)
\quad\text{于 }\mathcal A\otimes\mathcal A.\ }
\tag{3.6}
$$
物理恒等式 $u(t)^{\mathsf T}Ku(t)=0$ 在对角乘法后给
$$
fq=0\quad\text{于 }\mathcal A.
\tag{3.7}
$$

还必须使用同一原最高式 (1.3)，而非仅用 (3.6)。把物理参数也限制到 $D$，得到
$$
q(s)^2=6\tau_t(k(s,t)^2).
$$
由 (3.5)、(3.6)，右端恰为 $3q(s)^2$。所以
$$
\boxed{\ q^2=0,\qquad fq=0,\qquad
\tau(f^2)=2,\qquad q\ne0.\ }
\tag{3.8}
$$
这些是在同一个原长度四局部代数中的等式；没有更换 $H$ 或删除任何最高 jet 系数。

## 4. 全部长度四重数型：只暂余 $2+1+1$

使用已付的 [全等向长度三曲线 jets 分类](R150-appendix-classification-of-isotropic-length-three-curve-jets.md)：原 $K$ 的全等向长度三 jet 空间只可能是两个 $W_\pm$，且它们均由三个不同点构成，无重根、无无穷远类型。

式 (3.6) 有如下直接后果：若 $q$ 在某个长度三子 divisor $D_0\le D$ 的全部 jets 上为零，则
$$
k|_{D_0\times D_0}=0,
$$
所以 $E_{D_0}$ 全等向。逐个原重数型应用 (3.8)：

| $D$ 的型 | 从 $q^2=fq=0,\ \tau(f^2)=2$ 得到的后果 |
|---|---|
| $1+1+1+1$ | 约化代数中 $q^2=0$ 迫 $q=0$，矛盾。 |
| $4s$ | $q$ 的局部阶至少二。若阶为二，$fq=0$ 迫 $f$ 阶至少二，故 $f^2=0$，矛盾。因此 $q$ 阶三，$3s$ 是全等向长度三子 divisor，违反旧分类。 |
| $3s+t$ | $q$ 在三重点阶至少二，在单点为零。因此 $2s+t$ 全等向，违反旧分类。 |
| $2s+2t$ | 若 $q$ 在两块都非零，则 $f$ 在两块都阶至少一，故 $f^2=0$，矛盾。因此 $q$ 只在一块非零；在另一块恒零，产生全等向 $s+2t$ 或 $2s+t$，仍违反旧分类。 |
| $2s+t+u$ | $q$ 只可能在双点块上为非零一阶项；于是 $s+t+u$ 全等向，必恰为 $P_+$ 或 $P_-$ 的三个不同根。 |

这里“阶”在各有限局部代数中理解；射影换图不改变阶，也没有遗漏原无穷远点。最后一型的三点因旧分类已自动为原有限的三个不同根。

## 5. $2+1+1$ 的真正 double jet 被原最高式排除

只剩
$$
D=2s+t+u,\qquad
D_0=s+t+u=\operatorname{div}(P),
\quad P=P_+\ \text{或 }P_-,
\tag{5.1}
$$
其中
$$
P_+(z)=z^3-5z^2+\tfrac{32}{5}z-\tfrac85,\qquad
P_-(z)=z^3+27z^2+\tfrac{864}{5}z+\tfrac{864}{5}.
$$
$q$ 在双点块为非零一阶项，由 $fq=0$，$f(s)=0$。在原 $H$ 泛函中，双点的最高系数非零。式 (3.3) 因此表明 $y$ 在该双点块只含 $v(s)$，不含 $v'(s)$。于是
$$
y\in L=\operatorname{span}\{v(s),v(t),v(u)\}=W_\pm.
\tag{5.2}
$$

写 $k_a(z)=v(a)^{\mathsf T}Kv(z)$，
$\dot k_s(z)=v'(s)^{\mathsf T}Kv(z)$。
$L$ 的全部物理 polars 被 $P$ 整除，而原 $H$ 的确切表示为
$$
H=c_0v(s)^2+c_1\big(v(s)v'(s)^{\mathsf T}
 +v'(s)v(s)^{\mathsf T}\big)
 +c_tv(t)^2+c_uv(u)^2,
\qquad c_1\ne0.
\tag{5.3}
$$
由 $y\in L$，最高式左端 $P(z)^2$ 的记号易混淆，故此处改写为
$(y^{\mathsf T}Kv(z))^2$：它被支撑多项式 $P^2$ 整除。(5.3) 除 double-jet 交叉项外的全部物理项也被 $P^2$ 整除。因此原最高式强迫
$$
P\mid (k_s/P)\,\dot k_s.
\tag{5.4}
$$

[任意长度四单基点定理](R150-appendix-length-four-physical-projections-have-at-most-one-basepoint.md) §§2–4 已证明：两个不同原物理 polars 不可能有四次公共因子。因 $k_s,k_t$ 都被 $P$ 整除，且 $k_t$ 在 $t$ 至少二重，若 $(k_s/P)(t)=0$，两者的公共因子就包含 $P(z)(z-t)$，矛盾。因此
$$
(k_s/P)(t)\ne0,\qquad (k_s/P)(u)\ne0.
\tag{5.5}
$$
由 (5.4)，$\dot k_s(t)=\dot k_s(u)=0$。物理自极线的一阶导数还给
$\dot k_s(s)=v'(s)^{\mathsf T}Kv(s)=0$。于是
$$
P\mid\dot k_s.
\tag{5.6}
$$
但 $K$ 可逆，且 $L$ 的三维 polar 空间已恰为 $P S_2$，所以 (5.6) 迫 $v'(s)\in L$。这与原长度四 jets
$v(s),v'(s),v(t),v(u)$ 的独立性矛盾。

至此，(2.6) 的全部长度四类型均被排除，故
$$
\boxed{\ C,N\text{ 必线性无关，特别 }N\ne0.\ }
\tag{5.7}
$$

## 6. 只剩唯一简单基点的四次物理投影

$C_E=xx^{\mathsf T}-6I_4$ 的秩为四或三，绝不会低于三。因此它是不可约的复二次式。由 (5.7)，它与 $N_E$ 无共同二次因子，二次曲面交的次数为四。

若 $E$ 的四个物理五次式没有公共基点，则原 [长度四投影定理](R150-appendix-length-four-physical-projections-have-at-most-one-basepoint.md) 说明其像是非退化的双有理五次曲线。该曲线不可能包含于上述两条独立二次曲面的交：与一般射影平面相交后，将有五个曲线点同时落在两条没有公共成分的平面二次曲线上，违反次数四的交点界。

因此物理投影有基点。该已付定理又保证基点最多一个且简单，故现在准确有
$$
\boxed{\ \delta_E=1,\qquad \deg C_E=4,\qquad
\mathbb P^1\longrightarrow C_E\text{ 双有理}.\ }
\tag{6.1}
$$
该点记为 $s_0$。原支撑多项式 $g$ 必满足
$$
g\mid k(s_0,\cdot).
\tag{6.2}
$$
按照同一已付定理，全部支撑精确来自
$$
g=\Delta_{s_0}q_{\rm pol}(s_0,\cdot),
\quad\text{或}\quad
g=\Delta_{s_0}^2
 \frac{q_{\rm pol}(s_0,\cdot)}{\Delta_t},
\qquad q_{\rm pol}(s_0,t)=0,
\tag{6.3}
$$
包含重根及射影边界；这里
$k(s,z)=-\Delta_s(z)^2q_{\rm pol}(s,z)$ 是原极化核，符号
$q_{\rm pol}$ 不同于 §3 的局部代数元素 $q$。

剩余工作是将原 $H=J_2^{-1}\mathbf d_2(y)/6$、完整 mean 以及两条独立二次关系同时代入这些原有基点支撑。没有把 (6.3) 的所有成员视为临界点，也未将该归约扩展到 $V\ne0$、本质五/六维或完整普通 ISP。
