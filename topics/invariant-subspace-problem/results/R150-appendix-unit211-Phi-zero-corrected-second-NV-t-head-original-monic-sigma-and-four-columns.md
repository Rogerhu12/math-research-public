# 正确 Phi：完整 NV 第二 t 头支的原首一 sigma 二次与四列呈示

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-29（Asia/Taipei）。

**状态：原身份的纸面推导，无新执行。** 本文处理完整原 NV 的第二个 t 首项因子
$$
B_2=\ell(3-2\lambda)+2T+2m\sigma=0.
\tag{1}
$$
在这一整个支上，原第二矩可在旧已付系数环内首一化为 sigma 二次；原第三矩和完整 NV 各自有 sigma 一次余式。这给该三条件子系统一个准确二生成、四关系呈示。没有支付任何新的 lambda 头，没有排除此支或整个 Phi；其余原条件、t 变量及全部未知纯权零面继续保留。

## 1. 整原支的同点恢复与唯一二次分母

沿[完整 NV 二矩范数及二次 t 头](R150-appendix-unit211-Phi-zero-corrected-whole-NV-two-moment-norm-and-quadratic-t-head.md)的同一个 sigma，原值为
$$
h=1+\frac{T+m\sigma}{\ell}-\rho\sigma,\qquad
k=1+\frac{T+m\sigma}{\ell}+\rho\sigma,\qquad \rho^2=\delta=1-Q.
$$
这里 $\ell,M,\delta$ 均是当前正确 Phi 原图的已付纯权，$m=u-\ell$，
$$
M=\ell^2\delta-m^2=4bc\delta.
$$
(1) 完整解为
$$
a=\lambda-\frac32,\qquad T=\ell a-m\sigma,
$$
$$
h=\lambda-\frac12-\rho\sigma,\qquad
k=\lambda-\frac12+\rho\sigma.
\tag{2}
$$
没有倒 m、sigma、D 或新几何头。尤其 $m=0$ 在下列纯代数身份中也没有造成新的除法；其物理图支付范围不被本文扩大。

设
$$
A_\lambda=2\lambda^2-2\lambda+1,\qquad
B_\lambda=4\lambda^3-6\lambda^2+3\lambda-1 .
$$
从 (2) 的同一个 h、k 得到完整第二矩误差
$$
E_2=b(h-1)^2+c(k-1)^2-A_\lambda
=\ell\delta\sigma^2-2ma\sigma+\ell a^2-A_\lambda.
\tag{3}
$$
因此
$$
\boxed{
q_0=\frac{E_2}{\ell\delta}
=\sigma^2-r_1\sigma-r_0,
\qquad
r_1=\frac{2ma}{\ell\delta},\quad
r_0=\frac{A_\lambda-\ell a^2}{\ell\delta}.
}
\tag{4}
$$
唯一首一化分母是旧单位 $\ell\delta$。原 $q=M\sigma^2-D$ 在此满足
$$
q=\ell E_2=\ell^2\delta q_0,\qquad D=\ell A_\lambda-T^2,
$$
故 (4) 保完整第二矩及其全部非约化纤维。没有把 D 为零时的二次商替换成一个约化点。

## 2. 原第三矩的显示一次余式和原商

同一点的第三矩误差是
$$
E_3=b(h-1)^3+c(k-1)^3-B_\lambda
=\ell a^3-3ma^2\sigma+3\ell\delta a\sigma^2
 -m\delta\sigma^3-B_\lambda.
\tag{5}
$$
用 (4) 的首一二次作普通短除，定义
$$
\begin{aligned}
A_H&=aA_\lambda-B_\lambda
 +\frac{2Ma(A_\lambda-\ell a^2)}{\ell^2\delta},\\
B_H&=\frac{m(4Ma^2-\ell\delta A_\lambda)}{\ell^2\delta},\\
Q_H&=-m\delta\sigma+\frac a\ell(\ell^2\delta+2M).
\end{aligned}
\tag{6}
$$
则有完整身份
$$
\boxed{E_3=A_H+B_H\sigma+Q_Hq_0.}
\tag{7}
$$
证明只需将右侧 sigma 三次、二次、一次、常数项展开，并使用
$M=\ell^2\delta-m^2$。例如 $Q_H$ 的常数项亦为
$a(3\ell^2\delta-2m^2)/\ell$，其与 $-\!m\delta\sigma$ 正好消去 (5) 的二次和三次项。

原首项零面 $B_H=0$ 没有被反演。系数的 lambda 次数满足
$$
\deg_\lambda A_H\le3,\qquad
\deg_\lambda B_H\le2.
\tag{8}
$$

## 3. 完整 NV 的 t 常数项及另一条一次原余式

此节使用[正确全 t 原恢复](R150-appendix-unit211-Phi-zero-corrected-whole-t-parameter-three-mean-generators-and-monic-lambda-cubic.md)。记
$$
s=u-1,\quad
T_0=2u-\ell Q-2u^2,\quad
J=2u(1-u)+\ell Q,\quad P_{02}=2s\ell Q.
$$
当前图 $T_0,J-Q,P_{02}$ 均按旧范围支付；尤其 $J-Q=-4s^2$。置
$$
E=\frac{P_{02}(T+\ell)}{T_0},\qquad
f=\frac{P_{02}\lambda-QE+sT_0}{J-Q},\qquad
\mathcal V=f+bc\,t-E.
\tag{9}
$$
另有
$$
A_1=2E,\quad W_1=T_0/2+2uf,\quad w=\lambda-1-T.
$$
代入 (2) 后，f、E、$A_1,W_1,w$ 均对 $(\lambda,\sigma)$ 仿射且与 t 无关。

设
$$
\mathcal N=\ell^2N_4(\mathbf V)=Z_0+Z_1\sigma+Z_2\sigma^2
$$
仍是一般九自由变量来源的**完整**缩放 N4。其真实 t 系数已由原身份给出
$$
[t]\mathcal N
=2bc(T+u\sigma)\bigl(\ell(3-2\lambda)+2T+2m\sigma\bigr).
\tag{10}
$$
因此在 (1) 上，$\mathcal N$ 完全不依赖 t。

为了给一个可直接作为新输入的原定义，令
$$
\mathcal V_c=f-E,\qquad c_\lambda=3-2\lambda
$$
并定义
$$
\begin{aligned}
Z_{0c}={}&2\ell^2E+4\ell^2(1-2\lambda)f+2\ell fD
 +2\ell uw(\ell c_\lambda+T)\\
&+2\mathcal V_c(\ell^2+\ell c_\lambda T+T^2),\\
Z_{1c}={}&2(\ell c_\lambda+2T)(u\mathcal V_c-\ell W_1)-2\ell Mw,\\
Z_{2c}={}&2\bigl((u^2-\ell^2Q)\mathcal V_c
 -2m\ell W_1-\ell Mf\bigr).
\end{aligned}
\tag{11}
$$
这些是完整 Z 三式的 t 常数系数。由 (10)，本支上的完整原值严格等于
$$
\boxed{\mathcal N=Z_{0c}+Z_{1c}\sigma+Z_{2c}\sigma^2.}
\tag{12}
$$
此处只读取完整原值的系数；没有施加物理 $t=0$。原 t 变量仍自由保留，原均值和其他值条件仍须在同一点满足。

按 $(\lambda,\sigma)$ 总次数，(12) 至多三次。写其唯一普通多项式展开为
$$
\mathcal N=n_0(\lambda)+n_1(\lambda)\sigma
 +n_2(\lambda)\sigma^2+n_3(\lambda)\sigma^3,
\qquad \deg_\lambda n_j\le3-j.
\tag{13}
$$
这些系数由 (2)、(9)、(11) 给出确定原定义；本文没有声称实际展开或 profile 返回。

由 (4)，定义
$$
\begin{aligned}
A_V&=n_0+n_2r_0+n_3r_1r_0,\\
B_V&=n_1+n_2r_1+n_3(r_1^2+r_0),\\
Q_V&=n_3\sigma+n_2+n_3r_1.
\end{aligned}
\tag{14}
$$
于是完整普通身份为
$$
\boxed{\mathcal N=A_V+B_V\sigma+Q_Vq_0.}
\tag{15}
$$
(15) 的来源仅为首一短除，保全部新头零面。并且
$$
\deg_\lambda A_V\le3,\qquad
\deg_\lambda B_V\le2.
\tag{16}
$$

## 4. 子系统的准确四列呈示与后继边界

令 $\mathcal A$ 为上述旧已付权系数环，先取 $R=\mathcal A[\lambda]$。普遍二次代数
$$
B=R[\sigma]/(q_0)
$$
确为自由二生成，以 $(1,\sigma)$ 为基。由 (7)、(15)，三条件子系统的商准确为
$$
R[\sigma]/(q_0,E_3,\mathcal N)
=B/(A_H+B_H\sigma,\ A_V+B_V\sigma).
\tag{17}
$$
其 $R$ 模呈示是以下真正乘法列的 cokernel：
$$
\boxed{
\begin{pmatrix}
 A_H&r_0B_H&A_V&r_0B_V\\
 B_H&A_H+r_1B_H&B_V&A_V+r_1B_V
\end{pmatrix}.
}
\tag{18}
$$
原因是首一二次代数中的一个仿射生成元及其 sigma 倍已经生成该主理想的整个 R 模；对两条生成元取四列即得。没有把真实原物理商当成自由二生成模。

保 t 的完整头支时，只需将 (17)–(18) 作标量扩张到 $\mathcal A[\lambda,t]$；原 t 不能因 (12) 而被删除。原均值、N1、NS/PS、其余同 sigma 个别值及第三矩来源都继续保留在完整系统中。

例如同 sigma 的三类新必要标量可以定义为
$$
\begin{aligned}
n_H&=A_H^2+r_1A_HB_H-r_0B_H^2,\\
c_{H,V}&=A_HB_V-A_VB_H,\\
n_V&=A_V^2+r_1A_VB_V-r_0B_V^2.
\end{aligned}
\tag{19}
$$
其 lambda 次数上界为 $(6,5,6)$；每条可用 (7)、(15) 与 $q_0$ 显示返回原式。但本文没有执行它们、没有计算其 gcd，也不以各个范数分别为零代替整个同根呈示 (18)。

特别，(18) 不表示某个新 lambda 头是单位，不给整个权基上的有限长度结论，也不排除任何原点。本条只提供第二个完整 NV t 头支的原首一二次和明确的有限列来源。[第一头 $T+u\sigma=0$ 的独立首次输入](R150-appendix-unit211-Phi-zero-corrected-first-NV-t-head-original-cubics-scalars-and-frozen-gcd-boundary.md)已按原 120 秒预算冻结：三个原必要式已返回，首次合并 gcd 与最终三原覆盖式未返回。本条没有执行、续接、更改算法或增加该目标预算，也没有调用已冻结的 Q 主分量或旧投影。
