# 双逆分支的闭像障碍与无限维约化近核

日期：2026-11-12（UTC）。作者：literature。

状态：完整实际必要条件，不另编号。
本稿使用 R197 的坐标 $C^*$ 边界和 R164 的无非零紧元性质，
不证明实际慢分支核为零。

## 1. 一个 $C^*$ 边界下的闭像判据

设 $\mathfrak D\subseteq B(H)$ 是含单位的 $C^*$ 代数，
$\pi:\mathfrak D\to B(K)$ 为含单位 $*$ 同态。
取 $T\in\mathfrak D$。
如果 $\pi(T)$ 单射而不有界下界，则
$$
\boxed{\operatorname{Ran}T\text{ 不闭}.}
\tag{1.1}
$$

证明：
若 $\operatorname{Ran}T$ 闭，
则 $T$ 在 $(\ker T)^\perp$ 上有正的最小模。
于是对某个 $\gamma>0$，
$$
(T^*T)^2\ge\gamma T^*T.
\tag{1.2}
$$
施正的 $*$ 同态，
$$
(\pi(T)^*\pi(T))^2
\ge\gamma\pi(T)^*\pi(T).
$$
令 $B=\pi(T)^*\pi(T)$。
正算子的谱因此包含于 $\{0\}\cup[\gamma,\infty)$。
又 $\ker B=\ker\pi(T)=0$，
故0的谱投影为零，得到 $B\ge\gamma I$。
这与 $\pi(T)$ 没有有界下界矛盾。

特别，如果 $\pi(T)$ 是非零单射拟幂零算子，
则它不可能有界下界：
若 $\|\pi(T)x\|\ge c\|x\|$，
则 $\|\pi(T)^nx\|\ge c^n\|x\|$，
谱半径至少为 $c>0$。
因此这种边界值自动满足 (1.1) 的假设。

这是通过实际正矩阵 $T^*T$ 的谱隙得到的结论，
不是对未知核投影施加边界。

## 2. 没有紧元时，每个正的小谱片都无限维

再假设
$$
\mathfrak D\cap\mathcal K(H)=\{0\}.
\tag{2.1}
$$
在 §1 的假设下，对每个 $\delta>0$，
$$
\boxed{
\dim E_{T^*T}((0,\delta))H=\infty.
}
\tag{2.2}
$$

由 (1.1)，$T^*T$ 的谱不可能在0附近有正谱隙。
所以每个 $(0,\delta)$ 内都有正谱点。
取一个非零连续函数 $f$，
支撑于该区间内，并在一个实际谱点处非零。
则
$$
0\ne f(T^*T)\in\mathfrak D.
$$
若 (2.2) 中的谱空间有限维，
$f(T^*T)$ 的像包含其中，因而为非零有限秩算子，
与 (2.1) 矛盾。

这些谱空间均正交于 $\ker T$。
故对每个 $\epsilon>0$，
存在无限维闭子空间
$$
E\subseteq(\ker T)^\perp
$$
使
$$
\|Tx\|\le\epsilon\|x\|
\qquad(x\in E).
\tag{2.3}
$$
例如取 $E=E_{T^*T}((0,\epsilon^2))H$。

还可递归选正交单位向量
$$
x_n\in(\ker T)^\perp,\qquad\|Tx_n\|\le1/n.
\tag{2.4}
$$
于是 $x_n\rightharpoonup0$。
这排除了仅把有限维核或有限个特殊方向移走后建立统一下界的办法。

同样论证适用于 $T^*$，
只要 $\pi(T)^*$ 也单射而没有有界下界。
在拟幂零且稠密像的边界值情形，这两个条件同样成立。

## 3. 实际双逆分支算子

采用 R196/R197 的实际两不交正方向：
$$
T_+=X_{b^+}+H_+,\qquad T_-=X_{b^-}+H_-,
\qquad L_\pm=T_\pm^{-1},
$$
其中各行非负、非绝对可和、平方可和，
支持不交，且 $H_\pm\in\mathfrak U\cap\{A\}'$。
两逆有 R197 的坐标边界：
$$
\Pi_+(L_+)=0,\quad\Pi_+(L_-)=L_-,
\qquad
\Pi_-(L_-)=0,\quad\Pi_-(L_+)=L_+,
$$
并且均固定整个 $\mathfrak U$。

取一个全局有界分支 $Y\in\mathfrak U\cap\{A\}'$，
按 R196 的相同常数规范记 $Z=Y-a_*I$。
对应的有界双逆算子是
$$
\mathcal K_Y
=L_+-L_-+L_+ZL_-.
\tag{3.1}
$$
真实最大闭图及分支核的等价由 R196 处理；
这里仅研究这个明确有界算子的范数结构。

坐标边界精确给
$$
\boxed{
\Pi_+(\mathcal K_Y)=-L_-,
\qquad
\Pi_-(\mathcal K_Y)=L_+.
}
\tag{3.2}
$$
$L_\pm$ 均单射、稠密像、拟幂零；
所以 §1 同时适用于 $\mathcal K_Y$ 及其伴随。
得到
$$
\boxed{
\operatorname{Ran}\mathcal K_Y
\text{ 与 }\operatorname{Ran}\mathcal K_Y^*
\text{ 均不闭}.
}
\tag{3.3}
$$

这些算子所在的
$$
C^*(\mathfrak U,L_+,L_-)
\subseteq C^*(\mathfrak U,\{A\}')
$$
属于 R164 的实际无非零紧元 $C^*$ 代数；
其 Calkin 表示忠实。
因此 §2 适用，得到对每个 $\delta>0$，
$$
\boxed{
\begin{aligned}
\dim E_{\mathcal K_Y^*\mathcal K_Y}((0,\delta))H&=\infty,\\
\dim E_{\mathcal K_Y\mathcal K_Y^*}((0,\delta))H&=\infty.
\end{aligned}
}
\tag{3.4}
$$

## 4. 有限矩阵版本

上述证明在每个有限矩阵放大中不变。
$*$ 同态逐项放大仍保正，
而 R164 的 Calkin 忠实性也保持有限矩阵放大。

因此，对一个实际有界矩阵符号 $T$，
只要某个已构造的坐标边界值是单射且不有界下界，
便得到相同的闭像失败。
若边界值及其伴随均单射，
则两侧约化近核的结论同时成立。

这里要求具体边界矩阵具有所列性质；
不能仅由某个行列式形式不为零就省略这个条件。

## 5. 对尚未解决的核问题意味着什么

(3.3)—(3.4) 无论 $\ker\mathcal K_Y$ 最终是否为零都成立。
它们给出的近核向量明确在真核的正交补内，
所以不能通过先移去未知真核再取得闭像下界。

这仍不是非零核的构造。
也没有将 $\Pi_\pm$ 降到未知核空间或把不同边界的目标合并。
实际慢分支是否有核，仍需新的论证。
