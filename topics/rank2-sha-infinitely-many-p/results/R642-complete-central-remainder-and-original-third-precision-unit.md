# R642 — 完整中央余因子在原第三精度上的整单位运输

日期：2026-11-15。**状态：已证明。** 本篇支付准确的有限范围运输；主目标及原指定余类仍未完成。

本记录只比较 R639 的完整中央正规部与原三块。
首 Gaussian 仍保留在原 $\epsilon$ 模型中。
它不声称删除整个中央因子后仍得到原矩阵的整等价。

## 1. 精确比较对象

取 $p=6s-1>101$、$1\le\ell<s-13$，
原 $X=w^s$、$\epsilon=X/p$，并用原完整目标
$$
\Gamma^+=
\mathcal O[w,\epsilon]/
(w^s-p\epsilon,\epsilon^3,w^{\ell+13}\epsilon^2).
\tag{1}
$$
其标准整块为
$$
f=f_0(w)+f_1(w)\epsilon+f_2(w)\epsilon^2,
\quad\deg f_0,\deg f_1<s,\quad\deg f_2<\ell+13.
$$
原 $M$ 的全部 $w^{13}/U_0/P_{134}$ 已在这些实际行中。
来源始终是已有整性证明覆盖的同一个有限原格，原次数帽和适用的 $f_D<p$ 门保持。

R639 定义同一个
$$
F=\log(\sigma/z),\quad c=[w^s]F,\quad
F_{\rm c}(X)=\sum_{h\ge1}F_{hs}X^h,\quad
E_{\rm c}=\exp F_{\rm c}.
$$
置
$$
D_{\rm c}=E_{\rm c}/e^{cX}.
$$
先用已付原 Gaussian 规范 $\kappa=34c$、$a=p\kappa$。
其它合法整重标必须同时保原 $a$ 和正规部的对应运输。

设 $F_i$ 为原矩阵的一条实际物理列，
其总 sigma degree 为 $34q_i$。
例如原 $\mathcal W_D$ 的第 $n$ 权有 $q_i=n+40$；
真实 $T$、$U$ 扩源分别再加 $36j/17$、$4k$。
定义用于有限比较的辅助列
$$
F_i^{\rm c}=D_{\rm c}(X)^{-34q_i}F_i.
\tag{2}
$$
这正是改用完整中央正规部、随后仍恢复同一个首 Gaussian 的列。
若连完整 $E_{\rm c}$ 也恢复，原物理列本来就不变；
若完全删除 $E_{\rm c}$，则不是 (2) 的比较问题。

## 2. 第一个剩余中央系数确实整

R618 的原 $U=e^{F-cX}$ 满足
$$
v_p([w^n]U)\ge-\lfloor6n\tau_2\rfloor,\qquad
\tau_2=(2p-1)/(p(p^2-1)).
$$
对 $n\le2s$，右侧为零。
而 $2s<p$，所以到这一阶形成 $\log U$ 时，
全部分母 $1,\ldots,2s$ 都是 $p$ 单位。
因此
$$
\boxed{F_{2s}\in\mathcal O.}
\tag{3}
$$
不能仅因 $F_{\rm c}$ 的首项有一个 $p$ 分母，
便把第二项也当作相同分母。

在 (1) 的原截断中，所有 $X^h$、$h\ge3$ 都准确为零。
所以同一完整中央余因子准确化为
$$
D_{\rm c}^{-34q_i}
=1-34q_iF_{2s}p^2\epsilon^2.
\tag{4}
$$
更高正式系数即使有分母，也因其原 $w$ 次数超出目标而为零；
这里没有在无限级数中删去未知尾。

## 3. 用真正标准块定义运输算子

定义整线性算子
$$
\boxed{
B(f_0,f_1,f_2)=(0,0,\pi_{\ell+13}f_1).}
\tag{5}
$$
它是原标准基上的整映射，并满足 $B^2=0$。
它不是未经检验便放到 (1) 上的裸 $\partial_\epsilon$：
后者不保持 $w^s-p\epsilon$，不能直接使用。

一条原列模 $p$ 的 Gaussian 形状是
$A_i(w)e_2(aq_i\epsilon)$。
其中 $A_i$ 包括完整 $G_0$ 的普通因子和原 $w^{13}$。
标准块中的普通 carry 带外部 $p$，所以模 $p$ 准确有
$$
\boxed{B(\bar F_i)=a q_i\,\epsilon^2\bar F_i.}
\tag{6}
$$
右端只读取同一个实际普通首块。
所有低十三条自由行和另外两条十三行仍在 (1)、(5) 中，
没有对 $m_{13}$ 作非整逆。

由 (4)–(6)，整个有限矩阵逐列满足
$$
\boxed{
M_{\rm c}\equiv
\left(I-\frac{34F_{2s}}a\,p^2B\right)M\pmod{p^3}.}
\tag{7}
$$
所列目标算子整可逆，逆为
$I+(34F_{2s}/a)p^2B$，因为 $B^2=0$。

(7) 对任意上述真实总 charge 同时成立。
它只支付这个原第三精度目标，
不由此声称整个 $\mathcal C_p$ 或任意连续饱和前缀也有相同运输。

## 4. 同一个 P、R 与旧第二类

来源标签和有限帽在 (7) 中未变。
若同一个 $Q_2=P+pR$ 已满足 $MQ_2\in p^2\Gamma^+$，
则 (7) 给
$$
M_{\rm c}Q_2\equiv MQ_2\pmod{p^3}.
$$
所以同一个首次修正的第二代表准确不变：
$$
\boxed{
\overline{M_{\rm c}(P+pR)/p^2}
=\overline{M(P+pR)/p^2}.}
\tag{8}
$$
特别，原两条十三行必须先付清的条件没有消失，
也没有允许分别更换 $R$ 的两个高尾。

这说明 R639 的完整中央余因子虽然扩大了其原解析盘，
在保首 Gaussian 的旧第三精度比较中只给 (7) 的目标整单位。
它本身不改变 R593/R597 中指定 forcing 是否在原实际像内，
也没有为两中央零增加独立的旧 $d_2$ 约束。
首 Gaussian 的野因子、原完整中央值和旧实际 Padé 高尾仍在。

依赖：[R639](R639-complete-original-central-gauge-and-full-formal-disc-stokes.md)、
[R618](R618-original-second-gaussian-exact-radius-and-newton-tail.md)、
[R434](R434-original-angular-high-coordinates-and-carry-unit-schur-transport.md)、
[R593](R593-original-critical-carry-completion-and-actual-second-normal-tail.md)。
