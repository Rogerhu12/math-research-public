# R44. 实际二型的有限 $C^2$ 改变量预算

## 1. 问题与结论范围

R37 的一个径向主符号 chart 使用实际第二基本形式系数 $N<0$。
仅控制某个候选的 $C^0$ metric 残差不能保证这个符号条件。
本条给出对**有限实际几何改变量**的逐点、连续 $C^2$ 预算，
并给出实际 Gaussian 型别在严格非零区域的保持条件。

以下命题不要求 $F$ 已精确等距，也不要求其 metric 径向。
它只控制同一坐标和同一法向定向下的浸入、二型 chart 和严格型别。
转折根的简单性/非特征性、闭嵌入及 reach 不在本命题结论中。
这些另有 R36、R37 的相应接口。

## 2. 逐点有限改变量界

**命题 44.1。** 设 $F:U\to\mathbb R^3$ 为 $C^2$ 浸入，
采用坐标 $(x,\theta)$，并记
$$
X=F_x,\quad Y=F_\theta,\quad C=Y\times X,\quad A=|C|>0,
$$
$$
l=C\cdot F_{xx},\qquad m=C\cdot F_{x\theta},\qquad
n=C\cdot F_{\theta\theta}.
$$
令 $W:U\to\mathbb R^3$ 为任意 $C^2$ 函数，且新图**确为**
$F_*=F+W$。星号量由 $F_*$ 用完全相同的定义得到。
定义非负量
$$
q=|Y|\,|W_x|+|X|\,|W_\theta|+|W_x|\,|W_\theta|,           \tag{44.1}
$$
$$
\begin{aligned}
r_l&=q|F_{xx}|+(A+q)|W_{xx}|,\\
r_m&=q|F_{x\theta}|+(A+q)|W_{x\theta}|,\\
r_n&=q|F_{\theta\theta}|+(A+q)|W_{\theta\theta}|.
\end{aligned}                                                   \tag{44.2}
$$
则逐点有
$$
|C_*-C|\le q,\quad A-q\le A_*\le A+q,                    \tag{44.3}
$$
$$
|l_*-l|\le r_l,\quad |m_*-m|\le r_m,\quad |n_*-n|\le r_n. \tag{44.4}
$$
特别地，若
$$
q<A,\qquad n+r_n<0,                                    \tag{44.5}
$$
则 $F_*$ 在该点仍浸入，且相对于
$\nu_*=C_*/A_*$ 的系数
$N_*=\nu_*\cdot F_{*,\theta\theta}=n_*/A_*$ 严格为负。

记
$$
D=ln-m^2,\qquad
\mathcal E_D=|n|r_l+|l|r_n+r_lr_n+2|m|r_m+r_m^2.         \tag{44.6}
$$
则
$$
|D_*-D|\le\mathcal E_D.                                 \tag{44.7}
$$
因此在 $q<A$ 的条件下：

- 若 $D>\mathcal E_D$，则 $F_*$ 的 Gaussian 曲率严格为正；
- 若 $D<-\mathcal E_D$，则 $F_*$ 的 Gaussian 曲率严格为负。

**证明。** 精确展开
$$
C_*-C=Y\times W_x+W_\theta\times X+W_\theta\times W_x.
$$
使用 $|u\times v|\le|u|\,|v|$ 和三角不等式即得
$|C_*-C|\le q$；正、反三角不等式给出 (44.3)。
又有精确恒等式
$$
l_*-l=(C_*-C)\cdot F_{xx}+C_*\cdot W_{xx}.
$$
结合 $|C_*|\le A+q$ 得到第一条 (44.4)，另两条相同。
若 (44.5) 成立，则 $A_*\ge A-q>0$，
$n_*\le n+r_n<0$，所以 $N_*<0$。

令 $\ell=l_*-l$、$\mu=m_*-m$、$\nu=n_*-n$。精确展开给出
$$
D_*-D=n\ell+l\nu+\ell\nu-2m\mu-\mu^2.
$$
代入 (44.4) 并取绝对值即得 (44.7)。
最后，$F_*$ 的第一基本形式行列式为 $A_*^2$，
归一化第二基本形式行列式为 $D_*/A_*^2$，所以
$$
K_*=\frac{D_*}{A_*^4}.
$$
其符号就是 $D_*$ 的符号，从而得到最后两个结论。$\square$

## 3. 便于验证的统一多项式门

**推论 44.2。** 在一个区域上，设有真正的连续界
$$
|X|\le X_0,\quad |Y|\le Y_0,\quad A\le A_0,\quad
A\ge a_0>0,\quad |F_{\theta\theta}|\le Z_0,\quad n\le-\eta<0.
$$
若有限实际改变量满足
$$
|W_x|,\ |W_\theta|,\ |W_{\theta\theta}|\le\varepsilon,
$$
令
$$
Q(\varepsilon)=(X_0+Y_0)\varepsilon+\varepsilon^2,
$$
$$
P(\varepsilon)=
\bigl((X_0+Y_0)Z_0+A_0\bigr)\varepsilon
+\bigl(Z_0+X_0+Y_0\bigr)\varepsilon^2+\varepsilon^3.        \tag{44.8}
$$
只要
$$
Q(\varepsilon)<a_0,\qquad P(\varepsilon)<\eta,            \tag{44.9}
$$
新图在该区域浸入，并有统一负裕量
$$
N_*\le-\frac{\eta-P(\varepsilon)}{A_0+Q(\varepsilon)}<0.  \tag{44.10}
$$

**证明。** 由 (44.1) 得 $q\le Q(\varepsilon)$。
由 (44.2)，
$$
r_n\le Q(\varepsilon)Z_0+
\bigl(A_0+Q(\varepsilon)\bigr)\varepsilon=P(\varepsilon).
$$
使用命题 44.1 可得浸入和 $n_*\le-(\eta-P)$。
另一方面 $A_*\le A_0+Q$；因为分子严格为负，除以上界便得到
(44.10)。$\square$

若还已知 $|F_{xx}|$、$|F_{x\theta}|$、
$|l|,|m|,|n|$ 的连续上界以及 $|D|$ 的正下界，
可将同样的 $Q$ 和有限二 jet 上界代入 (44.2)、(44.6)，
从而以一个显式多项式门保持严格型别。这里没有额外的微分损失。
根处 $D=0$ 不具正下界，故这一推论不代替转折理论。

## 4. 线性方向不能冒充有限实际改变量

设 $p\mapsto F_p$ 在 $C^2(U)$ 中二次可微，$F_0=F$，
$V=\partial_pF_p|_{p=0}$。有限参数 $p$ 的实际改变量是
$$
W_p=F_p-F=pV+R_p,\qquad
R_p=\int_0^p(p-s)\,\partial_s^2F_s\,ds.                  \tag{44.11}
$$
这条恒等式按 Banach 空间的微积分基本定理成立。若在参数区间内
$\|\partial_s^2F_s\|_{C^2}\le B$，则
$$
\|R_p\|_{C^2}\le\tfrac12p^2B.                           \tag{44.12}
$$
因此可用 $|p|\|V\|_{C^2}+\frac12p^2B$ 作为推论 44.2 的
$\varepsilon$。只检查线性预测 $N+p\,\delta N<0$，
并不能免去 (44.11) 的二阶余项。

在 R33 的 phase 表示中，固定保存的 radius shift，沿控制向量直线
有 $a_s=a+s\dot a$、$z_s=z+s\dot z$、
$B_s=B+s\dot B$、$\psi_s=\psi+s\dot\psi$，而
$$
F_s=z_s e_z+a_s\mathcal P T(B_s,\psi_s).
$$
$\mathcal P$ 可以是精确的零均值角原函数，或者固定节点数的同一个
有限原函数算子；二者都在参数中线性。精确恒等式为
$$
\partial_s^2F_s
=2\dot a\,\mathcal P(\partial_sT_s)
 +a_s\mathcal P(\partial_s^2T_s),                        \tag{44.13}
$$
$$
\partial_s^2T_s
=T_{BB}\dot B^2+2T_{B\psi}\dot B\dot\psi
 +T_{\psi\psi}\dot\psi^2.                               \tag{44.14}
$$
它们可再求实际径向、角向二阶导数，用 R33 的原函数预算给出
(44.12) 的 $B$。若使用有限原函数，必须另付它与精确无限定义的
截断/混叠及舍入误差，不能把有限原函数的导数直接写成精确 $aT$。

## 5. 使用本条时的精确口径

命题 44.1 和推论 44.2 是连续陈述：输入若是真正的逐点或区间包络，
结论就是连续保证。把 $q,r_l,r_m,r_n$、$N$ 或 $K$ 仅在若干浮点
节点上求值，只得到节点诊断，并未满足“连续包络”的前提。

本课题对应的实际探索记录位于
notes/2026-11-12-phase24-core-type-predictor-and-c2-gates.md。
该记录同时保留了“外环转正但中央 $N$ 翻号”的失败预测步，
以及加入实际二型线性门后通过全有限 body 样本的后一个预测步。
二者都没有被本定理自动升级成精确解或连续认证。
