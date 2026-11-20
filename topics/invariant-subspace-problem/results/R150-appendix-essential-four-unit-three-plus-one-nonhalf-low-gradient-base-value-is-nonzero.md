# R150 附录：单位 3+1 非半权支路的原二次梯度常数项不为零

日期：2026-11-20 UTC。AI-assisted GPT-6 Astra Pro；Astra-ISP-b2a9acde-20261120 / r150_structure，根会话独立复核。

## 1. 精确位置和原必要方程

沿用外均值 essential-four 的原长度五 Frobenius 支撑，
在 rank $H=4$、孤立约化零点、活跃单位 $3+1$ 的情形，
已经排除 $p=0$、半权与 $\alpha=0$；本稿独立限制在 $q\ne0$ 的图，不以 $q=0$ 的闭合为前提。
保持原物理 jets 与前一附录的规范
$$
 p=1,\quad b\ne0,1/2,\quad q\ne0,\quad
 s=B/q+b,\quad x=A+b,\quad
 \alpha=x+b(\kappa-2),\quad \beta_0=1/2-\kappa x.
$$
原 mean 是
$$
 \alpha s+b\beta_0=0,\quad
 R_2+\{b(1+2s)-4s^2\}q^2=0,\quad
 R_P+(1-2s)q^2=0.                                         \tag{1.1}
$$
这里 $R_2,R_P$ 来自原
$E=e-2D_Kd-2d^2+4\phi d$，并非新的自由变量。

原三重点最高阶与二次梯度的系数记作
$p_0,p_1,p_2,n_0,n_1,n_2$。[前一附录](R150-appendix-essential-four-unit-three-plus-one-nonhalf-second-mean-coefficient-zero-branch-is-empty.md)已经直接从原最高阶、
原一次 mean 与原相容式证明
$$
                            s\ne x,\qquad p_0\ne0.          \tag{1.2}
$$
本附录在整个上述范围内证明
$$
                                  n_0\ne0.                  \tag{1.3}
$$
不需要先使用第二 mean 系数 $\gamma\ne0$ 的结论。

原公式给出
$$
 p_0=x^3+\tfrac b2(1-3x),\qquad
 n_0=\tfrac b4\{1-2b+\kappa(2x-b-2x^2)\},
$$
$$
 \frac{n_1}{q}=(x-b)(2xs-b)+2n_0,                            \tag{1.4}
$$
$$
 \frac{c_0}{q}
 =3\{p_0(x-b)(2xs-b)+n_0(2x^2-b)(x-s)\}=0.                 \tag{1.5}
$$
其中 $c_0=3p_0n_1-2n_0p_1$ 仍是原相容式。

先记录一个合法除数：
$$
                               T:=2x^2-b\ne0.               \tag{1.6}
$$
否则 $b=2x^2$，(1.5) 成为
$$
            c_0/q=6x^4(2x-1)^2(s-x).
$$
$b\ne0$ 给 $x\ne0$，$b\ne1/2$ 排除 $x=1/2$，
所以它迫 $s=x$，与 (1.2) 矛盾。

## 2. $n_0=0$ 必须让整个原 $N$ 的交叉部分消失

假设 $n_0=0$。
在三重点常数项，原最高阶和原 $N$ 分别给出
$$
                        p_0=-u_0^3,\qquad n_0=-m u_0^2.
$$
由 (1.2)，$u_0\ne0$，故 $m=0$。
因此原方程 $N=N_{\mathcal B}+mR^2=0$ 在整个曲线上的要求，
特别包含
$$
                              n_1=n_2=0.                    \tag{2.1}
$$
这比只使用代数相容式更强，而且没有除去任何尚未合法的值。

由 (1.4)、$q\ne0$，
$$
                           (x-b)(2xs-b)=0.                  \tag{2.2}
$$
以下分别排除它的两个完整分支。

## 3. $x=b$ 分支

此时
$$
 n_0=\tfrac b4(1-2b)(1+b\kappa).
$$
由 $b(1-2b)\ne0$，有 $\kappa=-1/b$。
原一次 mean 变为
$$
                        -(b+1)s+\tfrac32b=0.
$$
$b=-1$ 不满足这个原等式，所以
$$
 b+1\ne0,\qquad s=\frac{3b}{2(b+1)}.
$$
原单点 mean 在此处给
$$
 R_P=(1-2b)/2,\qquad 1-2s=\frac{1-2b}{b+1},
$$
因而
$$
                              q^2=-\frac{b+1}{2}.            \tag{3.1}
$$
所有除数均已逐一证明非零。

把这些关系代入原 $N_{\mathcal B}$ 的二阶局部系数，
不是代入某个范数或消元必要条件，直接得到
$$
                         n_2=-\frac{b^2(2b-1)^2}{16(b+1)}.  \tag{3.2}
$$
由 $b(2b-1)(b+1)\ne0$，(3.2) 非零，违反原 (2.1)。
故整个 $x=b$ 分支为空。

## 4. $x\ne b$ 分支

由 (2.2) 有 $2xs=b$。因为 $b\ne0$，所以 $x\ne0$，并且
$$
 s=\frac{b}{2x},\qquad
 \kappa=\frac{2(x-b)}{T},\qquad T=2x^2-b\ne0.                \tag{4.1}
$$
后一个关系直接来自原一次 mean。

令
$$
 G(b,x)=4b^2-(6x+1)b-4x^3+6x^2.
$$
把 (4.1) 代入原常数系数有
$$
                             n_0=\frac{bG(b,x)}{4T}.         \tag{4.2}
$$
所以假设 $n_0=0$ 必有 $G=0$。

现在 $1-2s=(x-b)/x\ne0$，可以用原单点 mean
唯一消去 $q^2=-R_P/(1-2s)$。
把这个值代入原另一 mean，恰得到
$$
 R_2-\frac{b(1+2s)-4s^2}{1-2s}R_P
   =\frac{T\{x^2-2bx+b/2\}}{x(x-b)}.                        \tag{4.3}
$$
这是原有理恒等式，不需要先模 $G$ 约减。
因为右侧所有分母及 $T$ 非零，原 mean 迫
$$
                             x^2-2bx+b/2=0.
$$
$4x-1=0$ 不满足此式，所以
$$
                            b=\frac{2x^2}{4x-1}.
$$
最后回到原 (4.2) 所需的 $G=0$：
$$
 G\!\left(\frac{2x^2}{4x-1},x\right)
       =-\frac{8x^2(2x-1)^3}{(4x-1)^2}.                     \tag{4.4}
$$
因 $x\ne0$，(4.4) 迫 $x=1/2$，继而 $b=1/2$，
与非半权假设矛盾。故这个分支也完整排除。

## 5. 可复核结论

配套短 QQ 源从原 $\tau,K_{\mathcal B},P,N_{\mathcal B},E$
重建全部局部系数，逐一核 (1.4)–(1.6)、(3.1)、(3.2)、
(4.1)–(4.4)。它只用有理恒等式展开，不需要结式、Gröbner、
范数或有限域计算，不持久化可重算输出表。

因此，在本附录的活跃单位 $3+1$ 原临界候选中，
$n_0\ne0$。同时由 $p_0=-u_0^3\ne0$，有
$$
                            u_0\ne0,\qquad m\ne0.
$$
这使后续在这个原曲线基点上使用立方与平方的比例成为合法步骤。
它没有声称余下的一般支为空，也不改变其他支路与普通 Hilbert ISP 的状态。


## 6. 完整原源的实际执行

[原QQ验证源](../notes/2026-11-20-essential-four-unit-three-plus-one-n-zero-verify.py)在[run44737090302](https://github.com/Rogerhu12/math-research-public/actions/runs/44737090302)、job136291084777的标签 `unit31_n_zero` 独立成功，exit0；源内计时1.019秒，外层1.4423512640000027秒。冻结触发提交 `407bc3459de35815ac85b18640397eb60843e272`，原K/τ/mean/P/N全部从公式构造后核恒等式。

源SHA-256 `de6f7b9b56e9420cf8d7a836e2fd4ff4dd2035654784a6b52f7a772f01b0f8c9`；独立stdout SHA-256 `893cf35efd2f34823cb491d5e305b496401b7ee9c3373abbd173f16b6848edc0`。原源无抽样、无有限域、无未知邻域；两个子分支的每次除法与T=0返回由正文先行证明。运行与依赖元数据见[批次身份](../notes/2026-11-20-exact-source-run44737090302-b2a9.json)，不保存可重算的展开数组。
