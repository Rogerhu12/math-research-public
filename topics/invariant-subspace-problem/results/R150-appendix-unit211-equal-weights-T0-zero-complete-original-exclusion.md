# R150：一般等权的整个 T0=0 原分支排除及可逆二次主子式

日期：2026-11-27（Asia/Taipei）；Astra-ISP-8542378f-20261127；AI-assisted GPT-6 Astra Pro。

**已证明：** 在原一般 LS 的 $b=c$ 图，整个 $T_0=0$ 分支没有物理解。由此，四个原二次式中指定的一个二次主子式在剩余等权图上为单位。一般等权及普通 ISP 尚未完成。

## 1. 直接使用有限原 Gram

本稿回到相互独立的 $x,y,t$，不使用它们的最高次代替有限方程。置
$$
b=c=m/2,\quad a=1-m,\quad d=1-Q,\quad r^2=d,\quad
p=1+r,\quad q=1-r,\quad X=x+ry,\quad Y=x-ry.
$$
原物理单位包括
$$
m(m-1)Q(Q-1)P_{02}\ne0,\qquad
P_{02}=m(m-1)(2m+3Q-4).
$$
原 $f$ 与四条 Gram 行为
$$
f=\frac{x+dy}{2}-\frac{1+d-2m}{4},\quad
r_G=X-ap-ct,\quad s_G=Y-aq-bt,
$$
$$
A_G=2f-2bX-2cY+2bct,\quad
k_0=(0,0,p,q),\quad k_1=(0,A_G,r_G,s_G),
$$
$$
k_B=(p,r_G,0,t),\quad k_C=(q,s_G,t,0).
$$
乘法仍为原 dual-number 加两 singleton，迹
$\tau(v)=av_0+v_1+bv_B+cv_C$。原均值及 $N_4,P_2,\lambda,T$ 的定义见[同值原返回](R150-appendix-unit211-equal-weights-same-value-linear-remainders-and-six-projections.md)，本稿源也直接从这些乘法重建。

写 $E_B=E_{Be}+rE_{Bo}$；原 $E_C$ 为其同一商代数内的共轭。源核对原 E0 恒等为零、三个均值和 N/P 的完整同源性，没有先要求 $E_{Bo}=0$ 来改写输入。

四条必要式 $E_1,E_{Be},E_{Bo},N_H$ 关于 $(x,y,t)$ 都是二次；同点加权 $N_S,P_S$ 为三次。清分母只使用原已付单位。新原输入完整构建实际 1.220 秒。

## 2. 需要关闭的首项恰为 T0

原
$$
V_2=2m-mQ,\qquad T_0=V_2-2m^2=-mJ,\qquad
J=2m+Q-2.
$$
四原二次式按 $(x^2,xy,xt,y^2,yt,t^2)$ 取最高次系数。以源的准确规范行
$$
2E_1,\quad2E_{Be},\quad E_{Bo},\quad
\frac{2P_{02}N_H}{m^2}
$$
组成矩阵，列 $(x^2,xy,xt,t^2)$ 的完整子式为
$$
\Delta_2=-16m^2(m-1)^2J^2.
\tag{2.1}
$$
它的唯一未付因子就是 J。全部 15 个四阶头子式都已从上述原行精确计算；本页只需要 (2.1)。

这也不是整个头矩阵的秩降面。另一列组 $(x^2,xy,xt,yt)$ 的子式为
$$
-128m^3(m-1)(Q-1)R_2,\qquad
R_2=J^2-2(m-1)(2m-1).
$$
直接多项式恒等式
$$
(1-2Q)J^2+(2m+2Q-3)R_2
=2(m-1)(Q-1)^2
$$
给出两个头图的完整覆盖。不过为了在同一个有限乘法图中使用 (2.1)，下面返回整个 J=0 原支，而不直接删去它。

## 3. J=0 上的原 N1 分裂和三个完整有限分支

在 J=0 上，
$$
Q=2-2m,\qquad d=2m-1,\qquad
m(m-1)d\ne0,\qquad P_{02}=-2m(m-1)d.
$$
记 $a_0=x-y$。取以下准确规范的原行：
$$
\mathcal E_1=E_1,\quad
\mathcal E_b=2E_{Be},\quad
\mathcal E_o=E_{Bo},\quad
\mathcal N=-\frac2m N_H.
$$
直接从同一有限 Gram 得到
$$
\boxed{\mathcal N=(mt-2a_0)(mt-2d a_0).}
\tag{3.1}
$$
原 singleton 均值还给
$$
\mathcal E_b
=mt^2+2m(m-1-x)t+4d a_0y.
$$
对 $r_0=1,d$，下面是完整多项式身份：
$$
\begin{aligned}
m\mathcal E_b
&-(mt-2r_0a_0)\{mt+2r_0a_0+2m(m-1-x)\}\\
&=
\begin{cases}
4(m-1)a_0\{m(1+2y)-a_0\},&r_0=1,\\
4d(m-1)a_0(a_0+m),&r_0=d.
\end{cases}
\end{aligned}
\tag{3.2}
$$
两个原组合均已逐项乘回。因为 m、m−1、d 为单位，(3.1)–(3.2) 覆盖所有原点，且只留下三种情形：
$$
\begin{array}{c|c}
a_0 & t\\ \hline
0&0\\
m(1+2y)&2(1+2y)\\
-m&-2d
\end{array}
\tag{3.3}
$$
第一行包含两个线性因子同时为零的全部点。后两行若与它相交，仍按第一行处理，没有丢失相交纤维。

## 4. 第一分支直接违反原不同值单位

在 $a_0=t=0$ 上，
$$
\mathcal E_o=2(m-1)\{2y^2-2y+1-m\}.
$$
原不同值量始终为
$$
D_{\rm val}=m(2\lambda^2-2\lambda+1)-T^2\ne0.
$$
同一 Gram 的精确恢复给
$$
\boxed{D_{\rm val}=m\{2y^2-2y+1-m\}.}
$$
所以原均值 $\mathcal E_o=0$ 迫 $D_{\rm val}=0$，矛盾。这里的不同值量与均值使用同一 $\lambda,T$；没有改用另一个根的范数。

源以原多项式分子
$$
P_{02}^2D_{\rm val}
=m(2L^2-2LP_{02}+P_{02}^2)-(L-P_{02}-J_0)^2
$$
计算。其规范行在 J=0 上为 $16dD_{\rm val}/m$，在此分支准确等于
$16d(2y^2-2y+1-m)$，与上式一致。

## 5. 第三分支留有原非零常数

在 $a_0=-m,\ t=-2d$ 上，完整原 $E_1$ 返回为
$$
\boxed{\mathcal E_1=4m^2(m-1)d.}
$$
所有因子均是原单位，故这一整支不可能。

## 6. 第二分支只有一个新末点，原 N 仍不为零

在 $a_0=m(1+2y),\ t=2(1+2y)$ 上，
$$
\mathcal E_1=4m^2(m-1)(1-4y^2),\qquad
\mathcal E_o=2(m-1)\{2y^2+2(m-1)y+1\}.
$$
若 $a_0=0$，已经属于第 4 节排除的第一支。其余点有 $1+2y\ne0$，所以原 $\mathcal E_1=0$ 迫 $y=1/2$；再由 $\mathcal E_o=0$ 得 $m=-1/2$。原变量唯一为
$$
(m,Q,x,y,t)=(-1/2,3,-1/2,1/2,4).
$$
同一原加权 N 行在此准确返回
$$
\boxed{N_S=-\frac{125}{16}\ne0.}
$$
源中的必要规范行是 $8d^2N_S/m$，在这个点等于 500；这是同一原行的已付单位倍，不把规范值 500 冒称为原 $N_S$。原 P 行也返回 $P_S=-29/16$，但一个非零原 N 值已经足够。

因此第二支也排除，(3.3) 的全部有限点都已覆盖。

## 7. 后续可用的原二次主子式

三个分支的原矛盾证明整个 J=0，即 T0=0，没有物理解。于是剩余一般等权图合法满足 J≠0，(2.1) 为单位；可以用原 cofactor 精确恢复首项为 $x^2,xy,xt,t^2$ 的四条二次关系。

这一步只支付指定的原二次头。后续 cubic overlap 的首项、原商的生成元、原 N/P 余行及全部同点值条件仍须实际计算；这里没有先把后续商宣称为自由模或空集。

## 8. 精确源和实际回执

六个新函数体位于 notes，统一前缀 2026-11-27-unit211-equal-weight：

- original-affine-quadratics-8542.js：独立原有限 Gram 和全部七行。
- original-quadratic-heads-8542.js：完整 15 个原头子式。
- T0zero-original-line-8542.js：整 J=0 原参数线。
- T0zero-original-branches-8542.js：三个同点分支全部原行。
- T0zero-original-cover-trace-8542.js：原分裂及 (3.2) 完整组合。
- T0zero-original-last-point-8542.js：最后一个原点的准确值。

全部使用 BigInt 有理数，按函数体的输出顺序传入后继；不依赖 scratch 或外部 CAS。小 JSON 保存每段源 SHA、规范输出 SHA 和真实执行范围。实际时间依次为 1.220、0.059、0.091、0.034、0.001 秒；末点调用正常返回，未单独记录内部墙钟，不编造时长。

末点脚本初稿的局部变量 P 与类名冲突，发生于 Function 编译阶段，未开始数学运算；准确失败源哈希和更名后成功的源分别记录。没有把这一编写错误作为数学反例或运行成功。整个原 QQ 大消去的既有 600 秒未决结果保持冻结；本页用了新的原低度分裂及同点返回。
