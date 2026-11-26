# R143：相关体能量后的最优二维必要筛查

2026-11-26，`visible-exact-astra-198c63d15049-20261126 / correlated_energy`。

**已证明（纯代数）：** 对 [CV](R138-supplement-correlated-v-eta-four-vertex-body-Gram.md)
的新四顶点体预算，或同一非负费用格式中的其他体预算，下面给出准确的
二维必要筛查。它比只检查第一对角项或 RX 的固定方向更强，不需要构造
任何新根 Gram，也不调用旧科学目标。新 CV 全域常数的实际值在执行前未知。

## 1. 完整根预算保留的最有利矩阵

写 $a=a_{EE}\ge0$、$b=a_{EB}\ge0$、$c=a_{BB}\ge0$，并令 $d=1-c$。
这些是算法选定的完整上界常数，不是实际残差的下界。
[RN.14](R138-supplement-root-anchored-spectral-budget-necessary-screen.md)
对当前真实高 Schur 与标量容量格式给出

$$
b_{EE}>\frac{37}{30},\qquad b_{EB},b_{BB}\ge0.
\tag{OC.1}
$$

这里完整 mean、物理角、source、原根端与全部接口都保留；它们在该格式中
产生的费用为非负。实际待吸收的矩阵因此为

$$
\mathcal M=
\begin{pmatrix}
2-a-b_{EE}&-(b+b_{EB})/2\\
-(b+b_{EB})/2&d-b_{BB}
\end{pmatrix}.
\tag{OC.2}
$$

若 $d\le0$，第二主子式已不能严格为正。设 $d>0$。对每个 $s\ge0$，

$$
(1,s)\mathcal M(1,s)^t
<\frac{23}{30}-a-bs+ds^2.
\tag{OC.3}
$$

右端在非负半轴上的准确最小值位于 $s_*=b/(2d)$，所以

$$
\boxed{\quad
\mathcal M\succ0\ \Longrightarrow\ d>0,\qquad
\mathcal N(a,b,c):=\frac{23}{30}-a-
\frac{b^2}{4(1-c)}>0.
\quad}
\tag{OC.4}
$$

证明只需把 $s_*$ 代入 (OC.3)。若 $\mathcal N\le0$，左端在这个
非负方向严格为负。没有使用错误的全空间 Loewner 比较：含非负交叉费用
的矩阵差未必半正定，(OC.3)只在实际使用的 $s\ge0$ 上成立。
这里的方向是预算矩阵的代数见证，不是声称某个 PDE 解能任选 $E/B$ 比例。

在同一 $a,b,c$ 下，$\mathcal N$ 不大于 CV.6 的 $(1,3/10)$ 测试值，
因为它是右端二次式对所有 $s\ge0$ 的最小值。因此 (OC.4)已包含那个
固定方向的全部排除能力。通过 (OC.4)仍只是尚未被这一必要筛查排除。

## 2. 保存整球后的严格实现

假设保存整球分别包含选定常数 $a,b,c$，并且其有向下端为
$a_-,b_-,c_-$，满足 $b_-,c_-\ge0$、$c_-<1$。旧完整 GB 已给实际
选定 $c<1$。令 $d_+=1-c_->0$。由于

$$
a\ge a_-,\quad b\ge b_-,\quad 0<1-c\le d_+,
$$

有完整上界

$$
\mathcal N(a,b,c)\le
\frac{23}{30}-a_--\frac{b_-^2}{4d_+}
\le N_+,
\tag{OC.5}
$$

其中 $N_+$ 是最后一式的有向舍入上端。保存这个完整新球并读回后，
若其上端不大于零，(OC.4)严格排除当前 CV/RA/非负费用组合。
若它为正，绝不把这个结果称为根正定、完整逆或闭曲面存在性。
保存 lower 只是为了向有利方向放宽所选预算；没有将任何实际物理上界
误当成物理下界，也没有把独立源置零。

## 3. 作为体常数的准确单变量阈值

SG.14–SG.15中，令 $w=w_E$ 并保留旧的完整 $w_B,h_E,h_B,E_0,E_1$。
则

$$
a=E_0w^2+E_1h_Ew,\qquad
b=\beta w+\gamma,
$$
$$
\beta=2E_0w_B+E_1h_B,\qquad
\gamma=E_1w_Bh_E.
\tag{OC.6}
$$

于是 $\mathcal N=A-Bw-Cw^2$，其中

$$
A=\frac{23}{30}-\frac{\gamma^2}{4d},\qquad
B=E_1h_E+\frac{\beta\gamma}{2d},\qquad
C=E_0+\frac{\beta^2}{4d}>0.
\tag{OC.7}
$$

若 $A\le0$，任意 $w\ge0$ 都不通过。若 $A>0$，准确必要条件是

$$
0\le w<w_*:=\frac{2A}{B+\sqrt{B^2+4CA}}.
\tag{OC.8}
$$

这是唯一正根的有理化表达式，避免两个接近正数相减。
因 $w=L(\sqrt{C_{corr}}+\sqrt{C_H}h_E)$，
$L=(5/2)\Gamma\sqrt{A_\Theta}>0$，当 $w_*/L>\sqrt{C_H}h_E$ 时还必须

$$
C_{corr}<\left(\frac{w_*}{L}-\sqrt{C_H}h_E\right)^2.
\tag{OC.9}
$$

若右侧括号非正则任何 $C_{corr}\ge0$ 都不能通过。
本篇不给这些阈值赋未经执行的十进制数值。

## 4. 新完整 CV 计算与既成输入

新脚本 `fourfold_codazzi_correlated_gram_body_budget.py` 只消费原
positive4+germ1完整容器，在全部4651片上按 CV.5保留同一个 $|v|$ 的四个
相关角点。完整新最大值完成后才与既成 SG 的整球 upper 取较小值。
完整 X/Y/GB/RS/SG 的原值、成功/失败资格与 source/mean/真实根接口只读。

它依次保存新的 $C_{corr},w_{E,corr},a_{EE,corr},a_{EB,corr}$，然后保存
(OC.5)的新上界；只有原 body 三门全部严格成立时才形成条件性 allowance
下界。原 SG.12 循环、旧 CE/漂移/积分/残差/根迹目标均不重算。

新的五条 upper 与条件性第六条 lower 是体预算和必要筛查。
即使这些检查全通过，真实根型、所有源交叉项、全物理边界逆、负侧、
真实 $\nu$、非线性迭代和同一闭曲面上的最终 matching 仍须实际完成。
