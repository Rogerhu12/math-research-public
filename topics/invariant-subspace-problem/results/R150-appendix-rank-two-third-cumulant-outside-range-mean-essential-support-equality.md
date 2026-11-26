# R150 附录：低秩第三累积量的外像均值必属于高维第三矩本质支撑

日期：2026-11-26（UTC）。作者：Astra-ISP-347c-20261126 / prior_results_map；AI-assisted GPT-6 Astra Pro。

**状态：已证明。** 这是原第三矩的纯张量恒等式后果，不使用临界性、不假定 Hankel 共同支撑，也不需要新的计算。对 rank $V=2$ 的待解本质四、五、六维层，它证明均值在 $\operatorname{ess}(T_3)$ 内，并且该空间就是前三阶累积量的实际共同线性支撑。

## 1. 原张量与精确结论

在原六维空间 $E_0=\mathbb C^6$ 中，取原对称累积量 $y,H,V$，仍定义
$$
T_3=y^{\otimes3}-2\operatorname{Sym}_{\Sigma}(y\otimes H)+4V
    =y^3-6yH+4V.
\tag{1.1}
$$
第二种写法使用对称代数的通常乘积；第一种的 $\operatorname{Sym}_{\Sigma}$ 是把 $y$ 放入三个位置的三项之和。置
$$
U=\operatorname{ess}(V)=\operatorname{Ran}V,\quad r=\dim U,\quad
W=\operatorname{ess}(T_3),\quad
E=\mathbb Cy+\operatorname{Ran}H+U.
$$
这里本质支撑是支持相应对称张量的最小线性子空间；$\operatorname{Ran}$ 指一对其余指标的展平像。始终有 $W\subset E$。

**定理。** 若
$$
y\notin U,\qquad \dim W>r+1,
\tag{1.2}
$$
则
$$
\boxed{y\in W,\qquad W=\mathbb Cy+\operatorname{Ran}H+\operatorname{Ran}V.}
\tag{1.3}
$$
因此对任意原完整临界点，
$$
\operatorname{rank}V=2,\quad y\notin\operatorname{Ran}V,\quad
\dim\operatorname{ess}(T_3)\in\{4,5,6\}
$$
必有 (1.3)。这里没有从 $V$ 自身的低秩支撑推出 $y,H,V$ 共用一个长度二物理除子；(1.3) 只识别它们实际共同**线性**支撑，它的维数仍可大于二。

## 2. 先证明均值属于第三矩本质支撑

对 $\lambda\in W^\perp\subset E_0^*$，张量缩并 $(T_3)_\lambda=0$。记 $h=H\lambda$。由 (1.1) 得原精确二阶恒等式
$$
0=\lambda(y)y^2-2\lambda(y)H-4yh+4V\lambda.
\tag{2.1}
$$
假如存在这样的 $\lambda$ 使 $\lambda(y)\ne0$，把它除以这个非零标量，使 $\lambda(y)=1$。解出
$$
H=\tfrac12y^2-2yh+2V\lambda.
\tag{2.2}
$$
再用同一个 $\lambda$ 缩并一次。对称乘积满足
$$(yh)\lambda=\tfrac12\{\lambda(y)h+\lambda(h)y\},$$
所以 (2.2) 给
$$
2h=\bigl(\tfrac12-\lambda(h)\bigr)y+2V(\lambda,\lambda,\cdot).
\tag{2.3}
$$
右边属于 $\mathbb Cy+U$，于是 $h$ 属于该空间。(2.2) 随即说明 $H\in\operatorname{Sym}^2(\mathbb Cy+U)$。而 $y,V$ 也支持于同一空间，因此
$$
W\subset\mathbb Cy+U,\qquad \dim W\le r+1,
$$
与 (1.2) 矛盾。故每个 $\lambda\in W^\perp$ 都满足 $\lambda(y)=0$，也就是 $y\in W$。

## 3. 无任何支撑预设地取得共同支撑等式

现在对任意 $\lambda\in W^\perp$，(2.1) 化为
$$
V\lambda=y(H\lambda).
\tag{3.1}
$$
左边属于 $\operatorname{Sym}^2U$。因 $y\notin U$，有
$$
\operatorname{Sym}^2U\cap yE_0=\{0\}.
\tag{3.2}
$$
为直接核验这一步，选 $\psi\in E_0^*$ 使 $\psi|_U=0,\psi(y)=1$。若 $yh\in\operatorname{Sym}^2U$，缩并 $\psi$ 得
$0=(h+\psi(h)y)/2$。再施加 $\psi$ 得 $\psi(h)=0$，故 $h=0$。这也说明没有暗中除以任何未知张量系数。

从 (3.1)—(3.2) 得
$$
H\lambda=0,\qquad V\lambda=0.
$$
对称张量的展平核正是其本质支撑的湮灭子，因此 $\lambda$ 同时湮灭 $\operatorname{Ran}H$ 与 $U$；前节又给它湮灭 $y$。于是
$$
W^\perp\subset E^\perp.
$$
而始终成立的 $W\subset E$ 给反向包含。两个湮灭子相等，故 $W=E$，定理证毕。

## 4. 对当前秩二分支的准确作用

[整个 rankV2 内均值分类](R150-appendix-rank-two-third-cumulant-all-inside-mean-complete-classification.md)已经关闭 $y\in\operatorname{Ran}V$，其完整 $T_3$ 为零。对留下的 $y\notin\operatorname{Ran}V$、本质维数至少四的点，本定理说明 $y\in W$。所以这整层与要求 $y\notin W$ 的[一般本质四维外均值长度五路线](R150-appendix-essential-four-outer-mean-length-five-algebra-and-rank-defects.md)确实分离，不能把那里已经支付的外均值结论直接移来代替内均值论证。

本稿没有消去这些四、五、六维临界点，也没有给 Bell 统一自然幂或算子逆。它是继续研究原完整梯度的支撑恒等式。所有结论仅来自显示的 (1.1) 与有限维对称张量缩并，故无需重跑任何既有计算门。
