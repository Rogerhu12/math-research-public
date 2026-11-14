# 六模式第五幂：选定主元候选的严格有理高度下界

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / normal_resume_1cf。
状态：有限整数格的完整证书与证明。下界只针对本稿固定的主元候选；第五自然 Bell 幂的特征零理想归属仍待完成。

## 1. 固定的是哪个有理候选

沿用[第五自然 Bell 幂检查点](2026-11-13-six-mode-fifth-natural-bell-power-modular-checkpoint-1cf.md)的原整数输入，不改变归一化。

记
$$
R_{\mathrm{int}}=77129712412\,R,\qquad
\widetilde B=\kappa B_r,\qquad \kappa\in\mathbb Q\setminus\{0\},
$$
其中准确的 $\kappa$、全部系数和单项式次序均在
[整数生成数据](2026-11-13-six-mode-fifth-power-dixon-integer-generators.json)中。
系数使用首一整数三次关系
$$
t^3-43931504t^2+22651103014400t+729375868200960000=0
$$
约化为 $1,t,t^2$ 三分量。

令 $A\in\mathbb Z^{3003\times4752}$ 为六个
$\partial_{y_i}R_{\mathrm{int}}$ 乘全部七次单项式的系数矩阵，
令 $B\in\mathbb Z^{3003\times3}$ 为 $\widetilde B^5/2^{29}$ 的三个整数系数列。
公共因子 $2^{29}$ 已逐项准确除尽。

[模103种子](2026-11-13-six-mode-fifth-power-mod103-certificate.json)给出有序行列集 $I,J$，均有2918项。设
$$
S=A_{I,J}.
$$
已完成的模103无换行 LU 的所有对角元非零；按所保存的行列顺序，其行列式为 $35\bmod103$。
因此 $S$ 在 $\mathbb Q$ 上可逆，并且逆的所有系数均在 $\mathbb Z_{(103)}$ 中。

定义准确的有理主元候选
$$
\boxed{C_*=S^{-1}B_I\in\mathbb Q^{2918\times3}.}
\tag{1.1}
$$
这一定义只解选中的方阵。在4752列中，将 $J$ 以外1834列的系数全部置零以后，若存在满足原完整矩形方程的这种解，它必等于 $C_*$；本文不假定 $A_JC_*=B$ 的原完整3003行已经成立。

按从零开始的索引，$J_2=2$。原列2对应
$$
y_4^2y_5^5\,\partial_{y_0}R_{\mathrm{int}}.
$$
本稿研究 $C_*$ 的这一行的三个有理数，记为 $(c_0,c_1,c_2)$。

## 2. 与已核模余数的精确联系

固定
$$
p=103,\qquad N=2136,\qquad M=p^N,\qquad W=10^{146}.
$$
在[原 Dixon 程序](2026-11-13-six-mode-fifth-power-dixon-driver-v3.js)中，每一轮使用同一个 $S\bmod p$ 解下一位，并保留完整整数残差。

具体地，令 $X^{(0)}=0$、$r^{(0)}=B$。若第 $n$ 轮的三列数字 $d^{(n)}$ 满足
$$
Sd^{(n)}\equiv r_I^{(n)}\pmod p,
$$
则取
$$
X^{(n+1)}=X^{(n)}+p^nd^{(n)},\qquad
r^{(n+1)}=\frac{r^{(n)}-A_Jd^{(n)}}p.
\tag{2.1}
$$
每次除法都在原完整3003行、三个分量上检查整除。
因此准确归纳得到
$$
B-A_JX^{(n)}=p^nr^{(n)}.
\tag{2.2}
$$
特别，
$$
X^{(N)}\equiv C_*\pmod{p^N}
\quad\text{于 }\mathbb Z_{(103)}.
\tag{2.3}
$$
这一步不需要整个矩形矩阵的有理秩等于模秩。

令 $a_0,a_1,a_2$ 是 $X^{(N)}$ 第2行的标准模 $M$ 余数。
它们的全部整数值已保存于下列高度证书的 JSON 中。
这三个数来自已完整正常返回的提升；也可以从原整数数据、种子、LU与RHS助手按 (2.1) 重算到2136轮后逐项核对。

于是，对任何共同整数分数表示
$$
c_j=\frac{n_j}{d},\qquad n_j\in\mathbb Z,\quad d\in\mathbb Z_{>0},
$$
都有
$$
\boxed{n_j\equiv a_jd\pmod M\qquad(j=0,1,2).}
\tag{2.4}
$$
它特别适用于最小公共分母表示。

## 3. 四维整数格的完整证书

定义
$$
\Lambda=
\left\{
(n_0,n_1,n_2,Wd)\in\mathbb Z^4:
n_j-a_jd\in M\mathbb Z
\right\}.
\tag{3.1}
$$
它的一个原基为
$$
(M,0,0,0),\quad(0,M,0,0),\quad(0,0,M,0),\quad(a_0,a_1,a_2,W),
$$
所以其协体积准确为 $M^3W$。

完整证书文件为：

- [四维整数格数据](2026-11-13-six-mode-selected-pivot-height-lattice.json)，原始 blob：32db9eb62b296838659e01802bf66cb4e8431ee8。
- [独立整数验证器](2026-11-13-six-mode-selected-pivot-height-verify.js)，原始 blob：27e6681af5fddaf65ef4099daaa656b4d63098f5。

数据给出四个具体整数行向量 $b_0,b_1,b_2,b_3$。
验证器逐项完成以下全部检查：
$$
b_i\in\Lambda,\qquad
\left|\det(b_0,b_1,b_2,b_3)\right|=M^3W.
\tag{3.2}
$$
所以这四行恰为整个 $\Lambda$ 的整数基。

令 $G=(\langle b_i,b_j\rangle)$，并令 $D_k$ 为 $G$ 的前 $k$ 阶主子式，$D_0=1$。
验证器还准确检查
$$
\boxed{
D_{k+1}\ge4\cdot10^{6520}D_k>0,
\qquad k=0,1,2,3.
}
\tag{3.3}
$$
全部行列式用有整除检查的 BigInt Bareiss 运算；每个大小比较也是整数比较。
四个 Gram--Schmidt 平方长度的整数部分分别有6522、6523、6523、6523位。
下界使用的是完整 (3.3)，不是仅凭这些位数作判断。

这些整数行由低维格约化找到；结论由 (3.2)–(3.3) 独立验证，不需要把约化算法的数值表现当作证明。

## 4. 严格高度下界

**命题。** 每个非零 $v\in\Lambda$ 满足
$$
\boxed{\|v\|_\infty\ge10^{3260}.}
\tag{4.1}
$$

证明。对任意非零整数线性组合
$$
v=\sum_{i=0}^3z_i b_i,\qquad z_i\in\mathbb Z,
$$
取最大的 $k$ 使 $z_k\ne0$。
将 $v$ 正交投影到 $\operatorname{span}(b_0,\ldots,b_{k-1})^\perp$，得到 $z_kb_k^\perp$。
Gram 行列式公式及 (3.3) 给
$$
\|v\|_2^2
\ge |z_k|^2\|b_k^\perp\|^2
\ge\frac{D_{k+1}}{D_k}
\ge4\cdot10^{6520}.
$$
因为维数为四，
$$
\|v\|_\infty\ge\tfrac12\|v\|_2\ge10^{3260}.
$$
证毕。

把 (2.4) 的共同分数表示代入 (3.1)，向量因 $d>0$ 而非零。
因此得到本稿关于实际主元候选的结论：
$$
\boxed{
\max\{|n_0|,|n_1|,|n_2|,10^{146}d\}\ge10^{3260}.
}
\tag{4.2}
$$
等价地，每一个共同整数分数表示都满足
$$
\boxed{
\max_j|n_j|\ge10^{3260}
\quad\text{或}\quad
d\ge10^{3114}.
}
\tag{4.3}
$$
共同分母不可任意缩小到一个同时具有更小分子的表示；(4.3) 已覆盖最小公共分母。

## 5. 复核与适用范围

将 JSON 读为 data，载入验证器后运行 verifySelectedSolutionHeight(data)，原样输出 all_pass: true；root 已重新执行全部格指数和四条 Gram 不等式，独立通过。
它重核整个格指数和四条 Gram 不等式。
与原有理候选的联系由 §2 的确定整数提升付清；原始输入、主元顺序和可移植重放入口均在[恢复检查点](2026-11-13-six-mode-fifth-natural-bell-power-modular-checkpoint-1cf.md)。

这个下界固定了原整数归一化、行列集 $I,J$ 以及未选列全部置零的选择。
改变自由列、改选主元或改写理想证书，可能得到较小系数，本文不作相应下界。
本稿也没有由大高度推出有理理想归属失败。

当前主元显式有理恢复路线仍以原完整9009项精确重乘为验收；独立的完整特征零理想证书也可另行支付归属，但本文未提供它。
已付的[真实 Bell 有界逆分母桥](../results/R150-appendix-jacobian-certificates-with-actual-bell-inverse-denominators.md)继续等待该前提；本稿不提前宣布原六模式平方或普通 ISP 已完成。
