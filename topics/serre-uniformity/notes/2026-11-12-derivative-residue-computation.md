# R73 工作检查点：退化素数处的一阶辅助导数

日期：2026-11-12。目标 $p=43,q=49019$，尝试辅助素数 $r=859$。
R70 已实际证明 $\kappa_0|q=0$、$\kappa_0|r\ne0$。
本文件先记录可计算公式；数值完成前不宣称 $r$ 满足第二辅助条件。

## 已推导的结构

令 $\mathfrak m=(1+i)^3p$。完整扩张
$K(\mathfrak mr)/K(\mathfrak m)$ 的群为
$\mathbb F_{r^2}^{\times}$。其唯一 $p$ 次商的核 $H$ 包含
$\mathbb F_r^\times$，因为 $p\mid r+1$、$p\nmid r-1$。
惰性有理 $q$ 的 Frobenius 是标量 $-q\in\mathbb F_r^\times$。
因此 $T(r)/T$ 在 $q$ 自动完全分裂；完整 $r$ 除法域则未必。
当前 $\operatorname{ord}_{859}(-49019)=33$，所以完整点可在
$\mathbb F_{49019^{66}}/\mathbb F_{49019^2}$ 的三十三次扩张中计算。

选择 $R\ne0\in A[r]$、$S=[i]R$。循环 $r$ 子群按
$G_s=\langle R+[s]S\rangle$（$s\in\mathbb F_r$）及
$G_\infty=\langle S\rangle$ 枚举。选择
$\vartheta:\mathbb F_{r^2}^{\times}\to\mu_p$，
$\vartheta(a)=a^{(r^2-1)/p}$ 及其根基，记
$j_G=\log\vartheta(1+si)$、$j_\infty=\log\vartheta(i)$。
其核就是 $H$。这同时固定 Kolyvagin 算子
$D_r=\sum_{j=1}^{p-1}j\sigma^j$ 的生成元取向。

对每条线用规范 Vélu 同源 $\phi_G:A\to A_G$。
由除数比较，模与 $P$ 无关的常数有
$$
\prod_{U\in G\setminus\{O\}}\Psi_A(P+U)
=\frac{\Psi_{A_G}(\phi_GP)}{\Psi_A(P)}.
$$
常数在 $p$ 侧的非平凡 $\chi_0$ 投影中消失。
完整 Norm 的 $H$ 轨道由 $(r+1)/p=20$ 条线组成。
将 $D_r$ 展开后每条线的权正是 $j_G$；
$\sum_Gj_G=20\sum_{j=0}^{42}j\equiv0\bmod43$，
所以分母的原曲线项消失。

令 $P_a=P_2+[a]P_p$，保持 R70 在 $q$ 的基选择。于是
模去所记基选择后，来自模数 $\mathfrak m$ 的原始导数的局部坐标为
$$
Z_r(q)=\sum_Gj_G\sum_{a\in\mathbb F_{p^2}^{\times}}
a^{-p}\log_\zeta\left(
\psi_{11,A_G}(\phi_G P_a)^{(q^2-1)/p}\right).
$$
这里 Robert 倒数的负号与 $|C|^{-1}=-1$ 相消。
$r\equiv-1\bmod\mathfrak m$，故由原始点 $1$ 得到的
模 $\mathfrak m$ 分量与 $P_a$ 差一个负号；范数中的 $-1\in H$
及函数的偶性消除此差异。
R65 模数额外的 $(7)$ 在导数下降后作用为 $1-\chi_0(7)^{-1}=8/7=38$；
也可注意 $(7)$ 的 $r$ 侧 Frobenius 本来就是标量，故其 $\Gamma_r$ 分量为一。

因 $T(r)/T$ 在 $q$ 分裂，Hilbert 90 下降修正是当地 $p$ 次幂。
所以以上直接剩余符号检测的是下降类，未用含 $p$ 的扩域次数去杀局部类。
若 $Z_{859}(49019)\ne0$，R65 的 $p$ 校正不改变它，
因而 $859$ 是经两项局部条件实际验证的辅助素数。

## 轻量实现方案

取三十三次不可约多项式 $X^{33}+X+c$（计划在小 $c\in\mathbb F_q$ 中
用 Rabin 判据找出）。其在 $\mathbb F_{q^2}$ 上仍不可约，且
$$\operatorname{Tr}(z)=33z_0-32z_{32}.$$
在扩域中找到 $r$ 挠点，只需以群指数 $q^{33}+1$ 投影。
Frobenius 在 $r$ 挠点上为标量 $\lambda=-q$，阶三十三。
$\mathbb F_r^\times/\langle-1,\lambda\rangle$ 有十三个代表。
每条核的全部 Vélu 求和因此只需十三个扩域点并取 trace。
十三条等差点序列 $[k]R+[s][k]S$ 可以依次覆盖全部线。

每条同源只计算 $\phi_G(P_2),\phi_G(P_p),\phi_G([i]P_p)$ 三点，
随后在商曲线的基域中枚举 $1848$ 点。第三个像不以商曲线上的
某个未经证明的 $[i]$ 自同态代替。
预计约 $11180$ 次扩域点更新和 $860\cdot1848$ 次基域除法多项式求值；
使用标准 C++，不安装数论系统。环境没有 Boost 头文件，
已用仅支持乘小整数和除小整数的 radix-$2^{32}$ 正整数实现全部指数。

**当前状态：数值已完成。**
$X^{33}+X+41$ 通过不可约性判据；
全部 $860$ 条核线得
$$Z_{859}(49019)=31+12i,\qquad
\frac87 Z_{859}(49019)=17+26i\ne0.$$
未加权的全部线之和为零，符合完整范数关系。
因此 $r=859$ 已经通过 R65 二阶补救的两个实际局部条件。
完整程序为 "verify_r73_derivative_residue.cpp"，
完整证书为 "r73_derivative_residue_certificate.json"；
证明与严格适用范围见 R73。
