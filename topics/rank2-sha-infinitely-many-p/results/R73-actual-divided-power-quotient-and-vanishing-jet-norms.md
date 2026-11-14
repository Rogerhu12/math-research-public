# R73. 实际除幂商格及最后消失 jet 的准确范数

日期：2026-11-12。**状态：指定临界张量的实际评价像、Smith 指数及最后 vanishing jet 范数均已证明。**

取惰性 $p\ge7$，使用 R68 的同一 $U,V$。记
$$
H=V/t,\quad B=U/H,\quad b=B-1,\quad
W=M_1U/((1-4t^2)H^2),\quad T=W/H^p.
$$
有 $B=1-t^2+\cdots$、$W=t^4+\cdots$。
令 $x=t^2$、$r=(p-3)/2$，目标普通偶 jet 格是
$\mathcal J=x^2\mathbb Z_p[x]/(x^{r+3})$。

## 1. 同一个实际有限商

在新 frame $X=H,Y=U-H$ 中，明确评价
$$
P\longmapsto T P(H,U-H),\qquad
X^{p-j}Y^j\longmapsto Wb^j.
$$
这是常系数齐次多项式格的映射，不将它认作任意 $R$ 系数的同一商。
$j>r$ 的像为零，$0\le j\le r$ 的首项是 $(-1)^jx^{j+2}$，
故实际对称幂像 $\mathcal L_{\rm sym}=\mathcal J$，其全部前缀整饱和。

除幂格的混合阶乘为 $p$ 单位，两个端点各有一层 $p$ 分母；
其中 $Y^p$ 已超过截断。因此实际除幂像准确为
$$
\mathcal L_\Gamma
=\mathbb Z_p(W/p)\oplus\bigoplus_{j=1}^{r}\mathbb Z_pWb^j,
\qquad \mathcal L_\Gamma/\mathcal J\simeq\mathbb F_p.
\tag{1}
$$
相对 $\mathcal J$ 的 Smith 指数是 $(-1,0,\ldots,0)$。
指定元素 $(X+Y)^p/p$ 的像为
$$
WB^p/p=W/p+\sum_{j=1}^{r}(\tbinom pj/p)Wb^j.
\tag{2}
$$
它在 (1) 的商中原始且非零，首项为 $t^4/p$；只有指定末系数
$C_{p+1}/p$ 由实际算术整除保证为整。

## 2. 原 Frobenius frame 的全部指数

原条目去掉明确单位后为 $(pU,tH)$。使用同一前因子 $T$，
取明确的偶投影，第 $j=2k$ 列为
$$
p^{p-2k}W x^k B^{p-2k},\qquad 0\le k\le r.
$$
去掉所示 $p$ 幂后是单位三角矩阵。因此
$$
\operatorname{Smith}(\mathcal L_{\rm old},\mathcal J)
=(3,5,\ldots,p).
$$
在 (1) 的同一除幂基中消元，得到更精确的
$$
\operatorname{Smith}(\mathcal L_{\rm old},\mathcal L_\Gamma)
=(3,5,\ldots,p-2,p+1).
\tag{3}
$$
未经归一的原矩阵条目另带公共 $s^p$，在本截断中 $s^p\equiv1\pmod p$；
它同时稳定 $\mathcal J$ 和 $\mathcal L_\Gamma$，故 (3) 也适用于真实条目。
全部结论已经在原 256 项投影之后，因为 $M_1$ 的实际首项仍为 1。

## 3. 真正前缀核上的最后一行

先令 $x^2,\ldots,x^{r+1}$ 系数准确为零，再取 $x^{r+2}$。
按各自列出的原 source quotient 格的系数最大范数，得到
$$
\boxed{\|\mathrm{jet}_{\rm sym}\|=1,\qquad
\|\mathrm{jet}_\Gamma\|=1,\qquad
\|\mathrm{jet}_{\rm old}\|=p^{-3}.}
$$
前两者的核像均为 $\mathbb Z_px^{r+2}$；旧格核像准确为
$p^3\mathbb Z_px^{r+2}$。除幂端点 $W/p$ 已被第一个消失条件杀掉。
若先饱和旧像为 $\mathcal J$，则已改变源范数。

这仍不计算 (2) 的末系数：(2) 的 $W/p$ 坐标为 1，本来不属于该前缀核。
上述实际比较的源次数与前因子依赖 $p$，不能把环境指数或 vanishing 行的单位
直接转成目标 $C_{p+1}/p$ 的非零。
完整证明见 [实际临界除幂商格](../notes/2026-11-12-actual-critical-divided-power-quotient-lattices.md)。
