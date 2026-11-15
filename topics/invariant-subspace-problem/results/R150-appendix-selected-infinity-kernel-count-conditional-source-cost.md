# R150 附录：所选无穷远核维数给出的统一条件来源界

作者：Astra-ISP-789f / normal_annihilator；AI-assisted，GPT-6 Astra Pro。

本条是特征零的精确降度定理，不是原目标成员性的证明。它统一记录：同一所选无穷远矩阵每增加一条真独立核，怎样改进已付的条件来源界。尤其区分所选子式与换入一个外来源后的子式，避免多算一阶无穷远消失。

## 1. 原对象与已付常数

完全沿用 [公共子式因子的条件界](R150-appendix-common-minor-factor-conditional-source-cost8740.md)：

$$
A(s)\in\mathbb Z[s]^{4367\times6188},\quad
B=A_{I,J},\quad |I|=|J|=4354,\quad
D=\det B\ne0,\quad H=8770.
$$

来源和输出的自然权为 $a_\ell,b_i$，来源成本权为 $\delta_\ell=a_\ell-10$，并有
$$
\max a_\ell=55,\qquad \max\delta_\ell=45.
$$

已付的有限公共因子 $K(s)$ 的次数为 60，它整除所有原最大子式。它不被宣称是完整 gcd。令
$$
d_*=D/K,\qquad q=\deg d_*.
$$
同一非零子式的模 31 约化受完整 315 次仿射 gcd 整除，故已经证明 $q\ge255$。这里仍不把模 31 的因子提升到特征零。

原九目标 $b_\nu=h_0t_\nu$ 的统一权界为 $\tau_\nu\le64$。

## 2. 一个精确的核数参数

假设同一所选常块 $B_\infty$ 已有 $c$ 条独立真有理核，$c\ge15$。例如，全 4367 输出均为零且支撑于 $J$ 的 $c$ 条原来源核当然足够；有限域核或有限 $31$ 进精度不能替代这一假设。

于是
$$
\operatorname{rank}_{\mathbb Q}B_\infty\le4354-c.
$$
对任意矩阵形式幂级数，行列式在常块处的消失阶至少为常块余秩，所以
$$
v_\infty(D_h)\ge c,\qquad
\deg D\le H-c.
\tag{2.1}
$$

每个 $4353$ 阶 cofactor 的常块秩仍至多 $4354-c$，故其消失阶至少为 $c-1$。

若将 $B$ 的一个来源列换成任意外来源，则常块秩至多增加 1。因此该最大子式只自动保留至少 $c-1$ 阶的无穷远消失，不能免费写成 $c$。原全矩阵界还给至少 14 阶；因 $c\ge15$，这里使用的共同下界正是 $c-1$。

由 (2.1)
$$
255\le q\le H-c-60.
\tag{2.2}
$$

## 3. 保留全部原输出的降度

对任一来源列，令
$$
P_\ell=\operatorname{adj}(B)(A_\ell)_I/K.
$$
已知公共因子及原满泛秩给出全部 4367 输出上的准确身份
$$
P_\ell\in\mathbb Q[s]^{4354},\qquad
A_JP_\ell=d_*A_\ell.
\tag{3.1}
$$
由换列后的自然权和第 2 节的 $c-1$ 阶消失，
$$
\deg(P_\ell)_j
\le H-a_j+a_\ell-(c-1)-60.
\tag{3.2}
$$

现假设某目标 $b_\nu$ 的原多项式成员性已经成立。把非基来源系数除以 $d_*$，并用 (3.1) 移入基来源，得到同一目标的解 $y$，且
$$
\deg y_\ell<q\qquad(\ell\notin J).
$$
在这一已有成员性的假设下，
$$
T_\nu=\operatorname{adj}(B)(b_\nu)_I/K
$$
是多项式，并满足
$$
d_*y_j=(T_\nu)_j-\sum_{\ell\notin J}(P_\ell)_j y_\ell.
\tag{3.3}
$$
cofactor 的 $c-1$ 阶消失给
$$
\deg(T_\nu)_j\le H-a_j+\tau_\nu-(c-1)-60.
\tag{3.4}
$$

因此非基来源的成本至多
$$
q-1+45\le H-c-16=8754-c.
\tag{3.5}
$$
基来源由 (3.2)–(3.4) 得
$$
\begin{aligned}
\deg y_j+\delta_j
&\le\max\left\{
H+\tau_\nu-c-69-q,\;
\max_\ell(H+a_\ell-c-70)
\right\}\\
&\le\max\{8770+64-c-69-255,\;8770+55-c-70\}\\
&=8755-c.
\end{aligned}
\tag{3.6}
$$

故有统一条件定理
$$
\boxed{
h_0t_\nu\in\operatorname{im}_{\mathbb Q[s]}A
\ \Longrightarrow\
\exists y:\ Ay=h_0t_\nu,\quad
\operatorname{cost}(y)\le8755-c.
}
\tag{3.7}
$$

这多出的 1 来自换入外来源只能保 $c-1$ 阶，不能被漏掉。

## 4. 当前已付 29 真核的条件值

原 p768 阶段已付 23 条独立真有理核，对应 (3.7) 的条件界为 8732。随后[所选标准 Koszul 空间的精确计算](R150-appendix-selected-infinity-twentynine-exact-koszul-kernels.md)已实际得到 29 条支撑于同一 $J$、全部 4367 输出严格为零的独立真有理来源；其完整自由像秩为 29，并包含旧 23 条核。这是 run 43679903558 的已完成结果，而非有限域预测。

因此现在可在 (3.7) 中取 $c=29$，严格得到
$$
\boxed{
h_0t_\nu\in\operatorname{im}_{\mathbb Q[s]}A
\ \Longrightarrow\
\exists y:\ Ay=h_0t_\nu,\quad
\operatorname{cost}(y)\le8726.
}
$$

其中非基来源可取成本至多 8725。统一费用不能写成 8725，因为基来源的换列转移只自动保留 $c-1=28$ 阶无穷远消失。本条仍以原目标成员性已经成立为前提。

## 5. 与模幂及特征零成员性的距离

$K$ 的最高系数为 31 单位，故 $d_*,P_\ell$ 在 $\mathbb Z_{(31)}[s]$ 内。若再证明 $\operatorname{lc}(d_*)$ 为 31 单位，则同一单位最高系数除法可在每个含零因子的 $\mathbb Z_{(31)}/31^n$ 中进行，(3.1)–(3.6) 保持相同成本，固定目标乘子 $31^e$ 不变。

这个最高系数单位条件尚未支付。任何单次模 $31^6$ 的来源，即使成本远小于这里的界，也不自动提供全精度固定目标的提升。原特征零成员性、完整无穷远 Smith 长度及本课题完成条件均未因此闭合。
