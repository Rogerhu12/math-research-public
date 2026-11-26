# R150 附录：孤立零点加单位三重点与单点的完整 rank H=4 支路为空

日期：2026-11-26 UTC。AI-assisted GPT-6 Astra Pro；Astra-ISP-347c-20261126 / unit31_general。
状态：以下明确范围已证明。

## 1. 结论与已有边界

在外均值 essential-four 的原长度五 Frobenius 支撑中，考虑
rank $H=4$、$L$ 在一个孤立约化点为零、其余单位补空间类型为 $3+1$ 的情形。
**这个完整支路没有原临界点。**

先前附录已分别排除：基本跨点配对 $p=0$、半权 $b=1/2$、
第一 mean 系数 $\alpha=0$、一阶跨点配对 $q=0$、第二 mean 系数 $\gamma=0$。
另已从原最高梯度与二次梯度证明 $s-x\ne0$、$p_0\ne0$、$n_0\ne0$。
这些结论的完整证明分别为：

- [零基本配对](R150-appendix-essential-four-unit-three-plus-one-isolated-zero-zero-base-pairing-branch-is-empty.md)；
- [半权](R150-appendix-essential-four-unit-three-plus-one-half-isolated-zero-branch-is-empty.md)；
- [第一 mean 系数零](R150-appendix-essential-four-unit-three-plus-one-nonhalf-vanishing-mean-coefficient-branch-is-empty.md)；
- [一阶跨点配对零](R150-appendix-essential-four-unit-three-plus-one-nonhalf-zero-first-jet-pairing-branch-is-empty.md)；
- [第二 mean 系数零及 $s-x,p_0$ 非零](R150-appendix-essential-four-unit-three-plus-one-nonhalf-second-mean-coefficient-zero-branch-is-empty.md)；
- [原二次梯度基值非零](R150-appendix-essential-four-unit-three-plus-one-nonhalf-low-gradient-base-value-is-nonzero.md)。

本稿关闭余下的一般图，并把此前已经执行成功、尚未单独登记的
$x=0,L=0$ 两个边界写成完整论证。
不增加关于实际物理支撑、原最高梯度或原低梯度的充分性假设。

## 2. 同一原代数和完整必要方程

将 $p\ne0$ 规范为 $p=1$。仍在原物理 jets 的允许局部参数下使用
$$
 \mathcal B=\mathbb C[\epsilon]/(\epsilon^3)\oplus\mathbb C,
 \qquad 1=(1,0,0,1),
 \qquad \tau(z)=(1-b)z_0+z_2+bz_3,
$$
$$
 K=\begin{pmatrix}
 0&0&A&1\\
 0&-2A&B&q\\
 A&B&C&r\\
 1&q&r&0
 \end{pmatrix}.
 \tag{2.1}
$$
这里 $b\ne0$ 是单位单点 Frobenius 权的非退化条件；
允许 $1-b=0$，没有删除三重点的任何特殊权。
以下乘法均为 $\mathcal B$ 内的乘法。

设 $k_i$ 为 $K$ 的第 $i$ 行，视作列向量，并定义
$$
 (D_Kz)_i=\tau(k_i z),\qquad d=D_K1,\qquad \phi=\tau(d)/2,
$$
$$
 P(z)=\tfrac12\tau\!\left((z-\tau(z)1)^3\right),
$$
$$
 N_{\mathcal B}(z)
 =\tfrac12\tau\bigl((d-\phi1)z^2\bigr)
 -(\tau z)\tau(dz)+\phi(\tau z)^2+\tfrac14\tau(zD_Kz).
 \tag{2.2}
$$
原活跃 mean 方程为
$$
 E=e-2D_Kd-2d^2+4\phi d=0,
$$
$$
 e=\bigl(\tau(k_0^2),\ 2\tau(k_0k_1),\
 2\tau(k_0k_2)+\tau(k_1^2),\ \tau(k_3^2)\bigr).
 \tag{2.3}
$$

令
$$
 \delta=1-2b,\quad x=A+b,\quad
 \kappa=2(\phi-x)/b.
$$
原常数 mean 精确给出
$$
 A=x-b,\quad r=x(1+\kappa)-\delta/2,\quad
 C=b\{\delta+\kappa(1-2x)\},\quad \phi=x+b\kappa/2.
 \tag{2.4}
$$
因 $q\ne0$，置
$$
 s=B/q+b,\quad \alpha=x+b(\kappa-2),\quad
 \beta_0=\tfrac12-\kappa x,\quad
 \gamma=\alpha+2b\beta_0.
$$
这里 $s$ 是 Gram 配对的比值，不是物理曲线的仿射坐标。
所有物理无穷远点已包含在原局部 jets 规范中，不因本稿的 $s$ 丢失。

原三个非恒零 mean 分别是
$$
 \alpha s+b\beta_0=0,
 \qquad R_2+\{b(1+2s)-4s^2\}q^2=0,
 \qquad R_P+(1-2s)q^2=0,
 \tag{2.5}
$$
其中 $R_2=E_2|_{B=q=0}$、$R_P=E_3|_{B=q=0}$，均按 (2.1)–(2.4) 定义。
从第一式有 $1-2s=\gamma/\alpha\ne0$。

在三重点定义完整的前三个原系数：
$$
 P(k_0+t k_1+t^2k_2)=p_0+p_1t+p_2t^2+O(t^3),
$$
$$
 N_{\mathcal B}(k_0+t k_1+t^2k_2)
      =n_0+n_1t+n_2t^2+O(t^3).
$$
原最高梯度与原二次梯度分别是 $P+R^3$、$N_{\mathcal B}+mR^2$。
若 $R=u_0+u_1t+u_2t^2+O(t^3)$，必有
$$
 (p_0,p_1,p_2)=(-u_0^3,-3u_0^2u_1,-3u_0^2u_2-3u_0u_1^2),
$$
$$
 (n_0,n_1,n_2)=(-mu_0^2,-2mu_0u_1,-m(2u_0u_2+u_1^2)).
$$
因此两个不含除法的必要相容式是
$$
 c_0=3p_0n_1-2n_0p_1=0,
 \qquad c_1=6p_0n_2+p_1n_1-4n_0p_2=0.
 \tag{2.6}
$$
另外，在活跃单点置 $p_s=P(k_3),n_s=N_{\mathcal B}(k_3)$。
若该点的 $R$ 值为 $z$，则 $p_s=-z^3,n_s=-mz^2$，于是
$$
 \chi=n_0^3p_s^2-n_s^3p_0^2=0.
 \tag{2.7}
$$
(2.7) 没有除以 $z,p_s,n_s$，其零值边界全部保留。
本稿始终只将 (2.5)–(2.7) 用作原临界点的必要条件。

由 (2.2) 直接展开，
$$
 p_0=x^3+\tfrac b2(1-3x),\qquad
 n_0=\tfrac b4\{1-2b+\kappa(2x-b-2x^2)\},
$$
$$
 \frac{c_0}{q}
 =3\{p_0(x-b)(2xs-b)+n_0(2x^2-b)(x-s)\}.
 \tag{2.8}
$$

## 3. 完整的 $x=0$ 边界

假设 $x=0$。由第一 mean 与 (2.8)，分别得到
$$
 (\kappa-2)s=-\tfrac12,
 \qquad (1-4b)s+\tfrac52b=0.
$$
因为 $b\ne0$，第二式先证明 $1-4b\ne0$，于是
$$
 s=-\frac{5b}{2(1-4b)},\qquad
 \kappa=\frac{1+6b}{5b}.
 \tag{3.1}
$$
此时
$$
 1-2s=\frac{1+b}{1-4b}\ne0,
$$
所以 $b+1\ne0$；由原单点 mean 可以合法地解得
$$
 q^2=\frac{32b^2-36b+7}{10(b+1)}.
 \tag{3.2}
$$
将 (3.1)、(3.2) 回代原另一 mean 和原 $c_1$，精确得到
$$
 E_2=\frac{M_4(b)}{50(4b-1)(b+1)},\qquad
 c_1=\frac{3b^2C_4(b)}{400(4b-1)(b+1)},
$$
$$
 M_4=3456b^4-1136b^3+981b^2-56b-4,
$$
$$
 C_4=-7232b^4+1672b^3+8b^2+447b-32.
$$
在 $\mathbb Q[b]$ 中，两四次多项式的 monic gcd 为 $1$。
所有前因子和分母均已非零，故 $E_2=c_1=0$ 不可能。
因此整个 $x=0$ 边界排除。

这些原恒等式及 QQ gcd 已由
[既有 regular-chart 源](../notes/2026-11-20-essential-four-unit-three-plus-one-regular-chart-verify.py)
在 run44738311930 的独立标签 `unit31_regular_chart` 完整执行通过。

## 4. 完整的 $L=0$ 边界与合法两参数图

因为 $b(s-x)\ne0$，第一 mean 唯一给出
$$
 \kappa=\frac{s(2b-x)-b/2}{b(s-x)}.
 \tag{4.1}
$$
定义
$$
 L=-4b^3+(16x^2+x+1)b^2-20x^3b+4x^4(x+1),
$$
$$
 C_b=(\tfrac52-4x)b^2+(6x^2-4x)b-6x^4+4x^3.
 \tag{4.2}
$$
将 (4.1) 代入原 (2.8)，直接约分给出
$$
 \frac{c_0}{q}=\frac34(Ls+bC_b).
 \tag{4.3}
$$
若 $L=0$，因 $b\ne0$ 必有 $C_b=0$。完整原有理计算给出
$$
 \operatorname{Res}_b(L,C_b)=-200x^6(2x-1)^7.
$$
第 3 节已排除 $x=0$，所以 $x=1/2$。
但 $C_b(b,1/2)=(b-1/2)^2/2$，于是 $b=1/2$，矛盾。
故 $L\ne0$，整个一般图可以合法地写成
$$
 s=-\frac{bC_b}{L},\qquad
 \kappa=\frac{s(2b-x)-b/2}{b(s-x)},\qquad
 Q:=q^2=-\frac{R_P}{1-2s}.
 \tag{4.4}
$$
这里 $b,L,s-x,1-2s$ 全部已经证明非零，未删去未分析的分母零点。
上述结式及 $x=1/2$ 的原返回也属于同一既有 regular-chart 成功源。

## 5. 三个完全由原式定义的两变量多项式

下面给出可直接重新生成三个多项式的定义；无需存储其展开系数表。
对非零 $F\in\mathbb Q(b,x)$，令 $\operatorname{pn}(F)$ 表示：
先在 $\mathbb Q(b,x)$ 约分，再将分子化为整数本原多项式，
并使字典序 $(b,x)$ 的首项系数为正。

将 $B=(s-b)q$ 代入 (2.6)，直接展开有
$$
 c_1=c_{10}+c_{12}q^2,
 \qquad p_s=p_{s0}+p_{s2}q^2,
 \qquad n_s=n_{s0}+n_{s2}q^2.
 \tag{5.1}
$$
这三个式子没有一次 $q$ 项，也没有高于二次的 $q$ 项；
所有系数均由 (2.1)–(2.6) 定义，属于 $\mathbb Q[b,x,\kappa,s]$。
令 $\iota$ 表示先按 (4.4) 将 $s,\kappa$ 代为有理函数。
定义
$$
 M=\operatorname{pn}\bigl(\iota(R_2)
      +\iota(b(1+2s)-4s^2)Q\bigr),
$$
$$
 C=\operatorname{pn}\bigl(\iota(c_{10})+\iota(c_{12})Q\bigr),
$$
$$
 P_s=\iota(p_{s0})+\iota(p_{s2})Q,
 \qquad N_s=\iota(n_{s0})+\iota(n_{s2})Q,
$$
$$
 X_{\rm full}=\operatorname{pn}
 \bigl(\iota(n_0)^3P_s^2-N_s^3p_0^2\bigr),
 \qquad P_0=2x^3-3bx+b.
 \tag{5.2}
$$
原多项式有精确整除 $P_0^2\mid X_{\rm full}$。
定义
$$
                     X=\operatorname{pn}(X_{\rm full}/P_0^2).
 \tag{5.3}
$$
这里 $P_0=2p_0\ne0$ 已由已有原梯度引理证明。
故每一个本图内的原临界点必须满足
$$
                             M=C=X=0.
 \tag{5.4}
$$
分母约分不能增加分母的零点；(5.2) 的所有输入除数均来自 (4.4) 的已付非零条件。
(5.3) 所去掉的因子也有单独的原非零性证明。
因此 (5.4) 没有漏掉该图内的任何候选。

原源精确生成的双次数是
$$
 (\deg_bM,\deg_xM)=(13,22),\quad
 (\deg_bC,\deg_xC)=(15,26),\quad
 (\deg_bX,\deg_xX)=(42,75).
 \tag{5.5}
$$

## 6. 两个特征零结式与全部特殊纤维

完全在 $\mathbb Q$ 上计算
$$
 U(x)=\operatorname{Res}_b(M,C),\qquad
 V(x)=\operatorname{Res}_b(M,X).
 \tag{6.1}
$$
其次数分别为 $395,1142$，原生有理多项式运算得到精确 monic gcd
$$
 \gcd(U,V)
       =x^{193}(x-\tfrac12)^{172}(x+1)^6(x+\tfrac{15}{8}).
 \tag{6.2}
$$
(6.2) 是一次完整特征零运算，不是抽样、插值，或根据有限域 gcd 猜测特征零答案。
多项式 (5.2)、(5.3) 及结式 (6.1) 的全部输入均在正文定义。
配套源码只由这些定义生成，在内存中作有理多项式整除、完整结式及 gcd，并逐项断言 (5.3)、(5.5)、(6.2)。

若 $(b,x)$ 是 (5.4) 的公共零点，两个 Sylvester 行列式必为零。
这只使用公共根给行列式为零的必要性；
即使特殊 $x$ 处关于 $b$ 的首项降阶，这个必要性仍然成立。
故 (6.2) 给出
$$
                  x\in\{0,\tfrac12,-1,-\tfrac{15}{8}\}.
$$
逐一回到三个原两变量多项式，在 $\mathbb Q[b]$ 求 gcd，得到：

| $x$ | $\gcd(M(b,x),C(b,x),X(b,x))$，monic |
|---|---|
| $0$ | $b^9$ |
| $1/2$ | $(b-1/2)^{11}$ |
| $-1$ | $b^2$ |
| $-15/8$ | $b+25/64$ |

前三行分别要求 $b=0,b=1/2,b=0$，均与本图的已有条件矛盾。
最后一行只留下
$$
                       b=-25/64,\qquad x=-15/8.
$$
必须将它回代原有理图，而不能把结式必要条件当成充分条件。
直接由 (4.2) 得
$$
 L=-5640625/65536,\qquad C_b=-225625/2048,
$$
从 (4.4) 得
$$
                 s=1/2,\qquad \kappa=-4/5,\qquad \alpha=-25/32.
$$
因而 $1-2s=0$，等价于 $\gamma=0$，违反本图中已证明的 $\gamma\ne0$。
最后一个候选也排除，证明一般图为空。

## 7. 执行来源、费用与结论范围

第 3、4 节原有理恒等式及其两个小 QQ 门的成功执行身份为
[run44738311930](https://github.com/Rogerhu12/math-research-public/actions/runs/44738311930)，
job136295226651，独立标签 `unit31_regular_chart`，exit0，
触发提交 `71e86b47cb04a2fffe6ee39331f660feb954ae0d`。
源码 SHA-256 为 `93fb802a18416e0deb692e6890fd99b64b36626ef03bda55b242b04da596dd8b`；
独立 stdout SHA-256 为 `c6e252e07b9472da3a6498a3f1504e3600423220bcdccb7d402ce8c0f98d1b22`。

第 5、6 节的新增完整源为
[原一般图特征零排除](../notes/2026-11-26-unit-three-plus-one-regular-exclusion-347c.py)。
命令是 `PYTHONPATH=<python-flint位置> python <该源> --wall-seconds 180 --memory-mib 1024`。
源从同一 $\mathcal B,\tau,K,P,N,E$ 重建系数，全部在 $\mathbb Q$ 中运算；
不复跑此前已成功的 $x=0,L=0$ 排除。
本地独立标签 `unit31_regular_exclusion_347c` 首次完整成功，exit0，
内层6.846828秒、峰值77456 KiB，原结式和全部纤维返回均通过。
源码 SHA-256 为 `d5063761a14020c545bee415e8c40804cc18788f960bd803066d45d870d647e3`；
完整 stdout SHA-256 为 `e7baa2a993756242ddca10728f8008d0fa36aea3a895538915c58643be144986`。
执行环境为 Python 3.12.14、SymPy 1.14.0、python-flint 0.9.0。
不保存可重算的系数表或结式数组，只保存源码、参数、运行身份及 SHA。

把本稿与第 1 节已完成的全部边界合并，**整个孤立零点加单位 $3+1$ 的 rank $H=4$ 支路为空**。
结论包括所有原 Frobenius 权、零单点值、物理合流与物理无穷远情形。
仍未关闭单位 $2+1+1$、单位 $1+1+1+1$、rank $H=5$、内均值与 essential 5/6，
也没有给出全局 Jacobian 自然幂来源或普通 Hilbert ISP 的完整答案。
