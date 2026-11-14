# 同一真核的横向切口平方和及固定测试滑动核投影预算

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / literature_audit；AI-assisted，GPT-6 Astra Pro。

**状态：已证明的中间结论。** 本稿将[真核集体占据矩](2026-11-14-true-kernel-collective-occupation-moments-and-one-bit-rotation-789f-next.md)直接转成所有切口的同源正预算。先固定一个真核向量，再以一个明确的 Fourier 区间乘子处理原固定测试的滑动核投影 \(k_{q+w}=P_{\mathcal K_{q+w}}f\)，不把随切口变化的向量冒当同一个向量。原头 \(d=2^m\)、\(w=d\) 时，总预算只有 \(O(m^3)\)。

同时给出一个保整个左前缀的有限物理向量及其真实方程残量。它不是精确右链；没有使用未付的硬核交集角度或删去高返回。

## 1. 两个交换的次数投影与准确层计数

保持前稿的完整 bosonic 嵌入、真实平方自由空间 \(\mathcal H_{\rm hc}\)、原 \(A_m+D_m\) 和真核
\[
\mathcal K=\ker(A_m+D_m).
\]
设 \(Q_{\rm hc}\) 为原平方自由正交投影，\(N_0\) 为集体模式占据，
\(N_\perp\) 为横向总粒子数。完整总次数为
\[
N_{\rm tot}=N_0+N_\perp.
\]
二者强交换。对整数 \(q\ge0\) 定义
\[
P_q=1_{\{N_{\rm tot}\le q\}},\qquad
R_q=1_{\{N_\perp\le q\}}.
\]
因此
\[
P_qR_q=R_qP_q=P_q,\qquad P_q\preceq R_q.
\tag{1.1}
\]
\(P_q\) 保持原平方自由空间；\(R_q\) 一般不保持它。

在联合谱点 \(N_\perp=b,N_0=j\) 上，\(R_q-P_q\) 恰在
\[
b\le q<b+j
\]
时等于 \(1\)，一共出现 \(j\) 次。所以对任意 \(v\in\operatorname{Dom}N_0^{1/2}\)，正项单调求和给
\[
\boxed{\sum_{q\ge0}\|(R_q-P_q)v\|^2
=\langle N_0v,v\rangle.}
\tag{1.2}
\]
若 \(v\in\mathcal K\)，前稿实际占据界给 \(k_0=\max(2m,16)\)，从而
\[
\boxed{
\sum_{q\ge0}\|(R_q-P_q)v\|^2\le k_0\|v\|^2.
}
\tag{1.3}
\]

## 2. 真 bosonic 核切口的实际硬核缺陷

横向投影 \(R_q\) 与 \(A_m+\sqrt S a_0\) 交换。故
\[
y_q=R_qv
\]
仍是真 bosonic 核向量；由于真核的集体占据至多 \(d-1\)，它的完整总次数至多 \(q+d-1\)。

原 \(v\) 平方自由，而且 \(P_qv\) 也平方自由。因此
\[
(I-Q_{\rm hc})R_qv
=(I-Q_{\rm hc})(R_q-P_q)v.
\]
由收缩性及 (1.3)，
\[
\boxed{
\sum_{q\ge0}
 \|(I-Q_{\rm hc})R_qv\|^2\le k_0\|v\|^2.
}
\tag{2.1}
\]
这是到原硬核空间的距离预算，不是到
\(\mathcal K\cap\operatorname{Ran}P_{q+d-1}\) 的距离预算。

## 3. 保整个左前缀的物理向量及真实残量

置
\[
\widetilde v_q=Q_{\rm hc}R_qv.
\]
它具有准确支撑和左端身份
\[
\boxed{
\operatorname{supp}\widetilde v_q\subseteq[0,q+d-1],
\qquad P_q\widetilde v_q=P_qv.
}
\tag{3.1}
\]
第二式用 \(P_q\le R_q\)、\(P_qQ_{\rm hc}=Q_{\rm hc}P_q\) 及 \(v\in\mathcal H_{\rm hc}\)。

这里需要支付投回硬核后的真实方程误差。完整 annihilator
\(\mathcal B=\sum_i b_i a_i\) 的碰撞回流块有全空间有界延拓
\[
\mathcal C=Q_{\rm hc}\mathcal B(I-Q_{\rm hc}),\qquad
\boxed{\|\mathcal C\|\le\sqrt{2S}.}
\tag{3.2}
\]
短证：只有“恰有一个位置占据 \(2\)，其余占据 \(0/1\)”的输入能经一次删除回到硬核。对输出子集 \(I\)，其输入纤维为
\(e_{1_I+\mathbf e_i}\)、\(i\in I\)，相应系数为 \(\sqrt2 b_i\)。
不同 \(I\) 的这些输入纤维正交。逐纤维 Cauchy--Schwarz 给
\[
\left|\sum_{i\in I}\sqrt2b_i u_{I,i}\right|^2
\le2\left(\sum_{i\in I}b_i^2\right)
       \sum_{i\in I}|u_{I,i}|^2
\le2S\sum_{i\in I}|u_{I,i}|^2.
\]
求和即得 (3.2)，故未用可能随总孔数增长的环境 annihilator 范数。

由 \((A_m+\mathcal B)y_q=0\) 及
\(\mathcal B|_{\mathcal H_{\rm hc}}=D_m\)，准确得到
\[
\boxed{
(A_m+D_m)\widetilde v_q
=-\mathcal C(I-Q_{\rm hc})R_qv.
}
\tag{3.3}
\]
所以
\[
\boxed{
\sum_{q\ge0}\|(A_m+D_m)\widetilde v_q\|^2
\le2S k_0\|v\|^2.
}
\tag{3.4}
\]
残量仍在同一个原物理空间；由 (3.1)，它低于第 \(q\) 孔的部分为零。
本文不将 (3.4) 的小残量直接变成一个同费用的精确修复。

## 4. 原固定测试的滑动核投影：不能直接套固定向量求和

定义真实有限前缀零源核
\[
\mathcal K_j=\mathcal K\cap\operatorname{Ran}P_j,
\qquad \mathcal K_{-1}=0.
\]
它们闭且递增。对同一个固定物理测试 \(f\)，置
\[
k_j=P_{\mathcal K_j}f.
\]
这些正是原测试流中的零源核投影。一般 \(k_{q+w}\) 随 \(q\) 改变，故不能把 (1.3) 的右端直接写成 \(k_0\|f\|^2\)。

以下给出其完整预算。对每个整数 \(w\ge1\)，
\[
\boxed{
\sum_{q\ge0}\|(R_q-P_q)k_{q+w}\|^2
\le k_0(1+\log w)^2\|f\|^2.
}
\tag{4.1}
\]
相应地，
\[
\boxed{
\sum_{q\ge0}\|(I-Q_{\rm hc})R_qk_{q+w}\|^2
\le k_0(1+\log w)^2\|f\|^2.
}
\tag{4.2}
\]

### 完整 Fourier 乘子证明

令
\[
\Pi_j=P_{\mathcal K_j}-P_{\mathcal K_{j-1}}.
\]
这是两两正交的投影，和为到
\(\mathcal K_{\rm fin}=\overline{\bigcup_j\mathcal K_j}\) 的投影；本证明不需要预先把 \(\mathcal K_{\rm fin}\) 认成整个 \(\mathcal K\)。

定义分析算子
\[
\mathscr F:\mathcal K_{\rm fin}\to\bigoplus_{q\ge0}\mathcal F,
\qquad
(\mathscr Fv)_q=(R_q-P_q)v.
\]
(1.3) 给 \(\|\mathscr F\|\le\sqrt{k_0}\)。若 \(j\le q\)，则
\(\mathcal K_j\subseteq\operatorname{Ran}P_q\)，故
\[
(R_q-P_q)\Pi_j=0.
\tag{4.3}
\]
因此目标分析算子的第 \(q\) 行恰为
\[
\sum_{q<j\le q+w}(R_q-P_q)\Pi_jf.
\tag{4.4}
\]

在输入正交分解上取酉
\(U_{\rm in}(t)=\sum_j e^{ijt}\Pi_j\)，
在输出第 \(q\) 行上取相位 \(e^{iqt}\)，记为 \(U_{\rm out}(t)\)。
设
\[
D_w(t)=\sum_{r=1}^w e^{irt}.
\]
则弱算子积分
\[
\frac1{2\pi}\int_{-\pi}^{\pi}
 D_w(t)\,U_{\rm out}(t)\mathscr F U_{\rm in}(t)^*\,dt
\tag{4.5}
\]
的 \((q,j)\) 块准确只保留 \(1\le j-q\le w\)，即 (4.4)。

又
\[
|D_w(t)|\le\min(w,\pi/|t|)
\quad(0<|t|\le\pi),
\]
所以
\[
\frac1{2\pi}\int_{-\pi}^{\pi}|D_w(t)|\,dt
\le1+\log w.
\tag{4.6}
\]
(4.5) 的范数至多 \((1+\log w)\sqrt{k_0}\)，得 (4.1)。
也可先在有限输入／输出分解上证明，再作强极限；常数不变。
(4.2) 由逐行投影收缩得出。

## 5. 对齐实际同窗测试及物理残量

对同一个固定 \(f\)，令
\[
\widetilde k_q=Q_{\rm hc}R_qk_{q+w}.
\]
它保留 \(k_{q+w}\) 的全部 \(\le q\) 左前缀，且支撑至多 \(q+d-1\)；
由 (3.3)、(4.2)，
\[
\boxed{
\sum_q\|(A_m+D_m)\widetilde k_q\|^2
\le2S k_0(1+\log w)^2\|f\|^2.
}
\tag{5.1}
\]

对原宽 \(w=d=2^m\)，
\[
k_0(1+\log d)^2=O(m^3).
\tag{5.2}
\]
若同时固定 \(n\) 个正交单位物理测试，逐测试求和即得
\(n k_0(1+\log d)^2\) 的共同预算。因此任意含 \(K_{\rm win}\) 个合法切口的同一窗口上，至少一个切口的总硬核缺陷平方不超过
\[
\frac{n k_0(1+\log d)^2}{K_{\rm win}}.
\tag{5.3}
\]
可以把这些非负量同原已有两费及固定测试耗散一起加权平均，以选择同一个切口。这里没有在不同切口重新挑物理测试，也不把切口变化的 \(k_j\) 当成固定向量。

仍须保留的缺口是：\(\widetilde k_q\) 只有 (5.1) 的真实残量，未被证明为完整 bare 或普通右可行链。已有四头例子显示，硬核像与横向次数旗的交集角度不能只用头上重构常数来支付。因此本稿不删除 boundary 的正返回块 \(E^{\rm ret}\)，也不由这些总预算宣称 \(N=M\)。
