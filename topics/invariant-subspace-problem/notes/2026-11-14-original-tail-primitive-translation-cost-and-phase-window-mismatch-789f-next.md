# 原连续尾的真实 primitive 平移费用与局部 phase 预算的适用边界

日期：2026-11-14（UTC）。作者：Astra-ISP boundary_core / 789f；AI-assisted，GPT-6 Astra Pro。

状态：本文的精确源公式、核上条件数下界和预算适用范围均已证明。它不反驳真实 phase 界，也不反驳原 graph 的同源 Schur 抵消；只证明不能通过统一物理范数运输，把新局部连续段 phase 界直接移到原高孔窗口。

依赖入口：

- [原尾与 star 的完整费用接口](2026-11-14-original-tail-star-interface-irreducibility-and-full-cost-transport-789f-next.md)，尤其完整左右、裸项与 flat 费用的同源运输。
- [R286](../results/R286-fixed-source-l1-zero-mode-energy-and-uniform-all-height-tail-bounds.md) §7，关于实际祖先 birth 的准确范围。本文也直接重写所需分解。
- [原连续尾宽窗相位定理](2026-11-14-original-continuous-tail-wide-window-exponential-phase-budget-789f-next.md)：原连续偶段长 \(Q\le x\) 时，整个真实上下源的 \(\Phi\preceq25\exp(80Q^2/x)I\)。

## 1. 原尾与行平移是完整原源上的同构

在有限子集 Hilbert 空间的第 \(r\) 层 \(\mathcal H_r\) 上，用正交基 \(e_I\)，其中 \(I\subset\mathbb N_0\)、\(|I|=r\)。固定 \(x'>x>0\)，定义

\[
 b_j=(x+j)^{-2},\qquad
 b'_j=(x'+j)^{-2},\qquad
 D_b=\sum_{j\ge0}b_jE_j,\qquad
 D_{b'}=\sum_{j\ge0}b'_jE_j.
\tag{1.1}
\]

令

\[
 R_re_I=\prod_{j\in I}\frac{b_j}{b'_j}e_I
       =\prod_{j\in I}\left(\frac{x'+j}{x+j}\right)^2e_I.
\tag{1.2}
\]

每个固定 \(r\) 上 \(R_r\) 有界可逆。逐个基向量给

\[
 D_{b'}R_r=R_{r-1}D_b,\qquad
 R_rK_r(b)=K_r(b'),\qquad K_r(b)=\ker D_b|_{\mathcal H_r}.
\tag{1.3}
\]

最后一个等式是满射等式，因为逆对角算子也满足反向交织。这里保留了原物理内积，并未把非酉 \(R_r\) 当作等距。

## 2. 合法 primitive 乘积上的精确费用

把前 \(2s\) 位按相邻两位配对。对 \(0\le l<s\)，令

\[
 u_l=b_{2l+1}e_{\{2l\}}-b_{2l}e_{\{2l+1\}},
 \qquad f_s=u_0\otimes\cdots\otimes u_{s-1},
\tag{2.1}
\]

其余位取真空。每个两位因子均被对应删除算子消去，因此

\[
 f_s\ne0,\qquad D_bf_s=0,\qquad f_s\in K_s(b).
\tag{2.2}
\]

这些向量是原完整 Boolean 源中的合法 primitive，不是任意环境源，也没有先限制完整逆。

两位的物理范数直接计算为

\[
 \|u_l\|^2=b_{2l}^2+b_{2l+1}^2,
\]

\[
 \|R_1u_l\|^2
 =b_{2l}^2b_{2l+1}^2
   \bigl((b'_{2l})^{-2}+(b'_{2l+1})^{-2}\bigr).
\]

故乘积给出精确等式

\[
 \boxed{
 \frac{\|R_sf_s\|^2}{\|f_s\|^2}
 =
 \prod_{l=0}^{s-1}
 \frac{(x'+2l)^4+(x'+2l+1)^4}
      {(x+2l)^4+(x+2l+1)^4}.}
\tag{2.3}
\]

其中每个因子满足

\[
 \left(\frac{x'+2l}{x+2l+1}\right)^4
 \le
 \frac{(x'+2l)^4+(x'+2l+1)^4}
      {(x+2l)^4+(x+2l+1)^4}
 \le
 \left(\frac{x'+2l+1}{x+2l}\right)^4.
\tag{2.4}
\]

若 \(s\ge2\)、\(x\le s/2\)、\(x'\ge2s\)，则

\[
 \frac{x'+2l}{x+2l+1}
 \ge\frac{4s-2}{(5/2)s-1}\ge\frac32.
\]

于是

\[
 \boxed{
 \|R_sf_s\|^2\ge(3/2)^{4s}\|f_s\|^2.}
\tag{2.5}
\]

这个下界已经在真实 primitive 源上成立。

另一方面，把 (2.1) 的全部两位对平移到任意远处，得到仍在 \(K_s(b)\) 的 \(f_{s,N}\)。固定 \(s,x,x'\)，当 \(N\to\infty\) 时，(2.3) 的每个因子趋于一。因此

\[
 \inf_{0\ne f\in K_s(b)}
 \frac{\|R_sf\|^2}{\|f\|^2}=1.
\tag{2.6}
\]

结合 (2.5)，作为两个原物理核空间之间的同构，

\[
 \boxed{
 \operatorname{cond}\bigl(R_s:K_s(b)\to K_s(b')\bigr)
 \ge(3/2)^{2s}.}
\tag{2.7}
\]

共同标量缩放全部新权只会把 \(R_s\) 乘一个标量，不能改变这个条件数。

### 单次行平移的准确量级

对 \(x'=x+1\) 且固定 \(x\)，置 \(P(t)=t^4+(t+1)^4\)。式 (2.3) 成为

\[
 \prod_{l<s}\frac{P(x+2l+1)}{P(x+2l)}.
\]

由于

\[
 \log P(t+1)-\log P(t)=\frac4t+O_x(t^{-2}),
\]

从 \(l=1\) 开始与 \(2/l\) 的差绝对可和，故存在严格正有限常数 \(c_x\) 使

\[
 \boxed{
 \frac{\|R_sf_s\|^2}{\|f_s\|^2}
 =c_xs^2(1+o(1)),\qquad s\to\infty.}
\tag{2.8}
\]

所以即使仅移一行，原 primitive 上的统一物理二次型失真也不能为 \(o(s^2)\)。这不声称平方量级是全核的最优上界。

## 3. 与实际 moving-birth graph 的参数相接

原边界的头维数为 \(d=2^m\)，尾行起点 \(x\) 与 \(m+1\) 只差固定的记号平移。合法窗口为

\[
 4d\le q\le\exp(d^3/4).
\tag{3.1}
\]

原固定物理测试流的第 \(q\) 层祖先由真实正交塔分解给出

\[
 t_q\in
 \bigoplus_{i=0}^{d-3}e_i
   \bigl(E_{d-i-1,q}\ominus E_{1,q}\bigr).
\tag{3.2}
\]

对应非零 tower 高度 \(h\) 与祖先 birth \(s\) 满足

\[
 1\le h\le d-i-2,\qquad s=q-h,
 \qquad q-d+i+2\le s\le q-1.
\tag{3.3}
\]

特别 \(s\ge3q/4\)，而不是 \(s=O(d)\)。

有限完整 Boolean 段上，若要包含这个 birth 以及高度 \(h\) 的真实塔，必须至少有

\[
 Q\ge2s+h.
\tag{3.4}
\]

偶相位定理本身还针对其指定的完整中央上下源；(3.4) 只是最基本的维数必要条件，并非已经证明原任意 birth/height 都可调用该相位定理。

新局部估计

\[
 Q\le x,\qquad
 \Phi\preceq25\exp(80Q^2/x)I
\tag{3.5}
\]

因而不能在原 \(x\asymp m\)、\(s\asymp q\) 的同一尾行直接使用。

如果尝试先用 (1.2) 把尾行改到 \(x'\ge Q\)，再用统一原物理范数界运输所有源，则 \(x'\ge2s\)，且原窗口中最终有 \(x\le s/2\)。式 (2.7) 说明这种统一运输在真实 primitive 上已付至少 \(\exp(cs)\) 的条件数。

当取原大窗口的 \(q\) 与 \(s\asymp q\) 时，这一损失不是 \(d\) 的三次指数预算：例如 \(q=\lfloor e^{d^3/4}\rfloor\) 时，\(\log\operatorname{cond}R_s\ge c'e^{d^3/4}\)。它也远大于当前固定测试共同宽商所提供的、只按有效窗口长度增长的费用预算。

因此：

> 已有的局部连续段 phase 估计，加上对 \(R_s\) 的统一物理范数／逆范数估计，尚不能给出原 moving-birth graph 的所需窗口界。

这里没有把 (3.5) 的显式上界当作 phase 的下界；真正被 (2.7) 强迫的是所述物理运输方法的条件数。

## 4. 为什么这仍不排除同源 Schur 方案

(1.3) 可以准确运输全部左链与完整右链；裸链须按商空间的最小代表运输，因为 \(R_r\) 不保持原正交补。这些均由完整费用接口证明。

若 \(x=R_qr\)，原左、裸和完整右形式在同一新源坐标中分别为

\[
 \widetilde L=R_q^{-*}L_bR_q^{-1},\qquad
 \widetilde B=R_q^{-*}B_bR_q^{-1},\qquad
 \widetilde G=R_qG_bR_q^*.
\tag{4.1}
\]

完整 flat 与两费形式仍是

\[
 \lambda_{\mathrm{flat},b}(r)^2
 =\langle\widetilde L\widetilde G\widetilde Lx,x\rangle,
\qquad
 \Xi_b(r)^2
 =\langle(\widetilde B+\widetilde L\widetilde G\widetilde L)x,x\rangle.
\tag{4.2}
\]

故存在两个尚未支付、但并未被本文排除的可能：

1. 真正的 \(R_s\) 大方向在三个同源度量和实际 graph Schur 中共同消去；
2. 真实固定测试流 \(t_q\) 及其完整回传落在比全 \(K_s\) 更小、且能够付清上述条件数的源类。

不能把 (2.5) 的任意合法 primitive 乘积直接认作实际 \(t_q\)。也不能把局部 phase 在某个有限段上的成立解释成该段是原 \(D,D^*\) 的 reducing 子块。

后继准确目标仍是同一实际源上的完整新层 Schur、左右／裸项／flat 的共同运输，以及原负前缀 graph 的反馈；本文没有删除这些项，也没有关闭 \(N=M\)。
