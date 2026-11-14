# 真实头越界源的双宽零源投影与准确能量下降

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065 / boundary_resume。
状态：本稿识别真实 Schur 后越界源的可去核分量，并计算其准确能量；没有得到剩余分量的无权上界或窗口收敛速度。

本稿继续[完整 L 核拼合与合法测试](../results/R239-appendix-full-l-kernel-completion-and-legal-m-tests.md)
以及 [R271 联合旗通量](../results/R271-appendix-joint-flag-right-inverse-energy-and-head-jump-flux.md)。
固定同一个 $m,q$，不改变相邻修复问题的头。

## 1. 同源的宽 d 与宽 2d 极小链

取原合法参数
$$
m\ge5,\qquad d=2^m,\qquad4d\le q\le e^{d^3/4},
\qquad L=A+D,\quad A=A_m,\quad D=D_m.
$$
令 $v=v_{m,q}(w)$，$r=Lv=Av_q$ 为真实低输出残量。
也可以先对任意属于原准确源旗 $\mathscr R_q$ 的 $r$ 作以下纯代数讨论。

记同源的两个原 Hilbert 极小修复为
$$
c_d=\underset{\substack{Lc=r\\\operatorname{supp}c\subset[q+1,q+d]}}{\arg\min}\|c\|,
\qquad
c_{2d}=\underset{\substack{Lc=r\\\operatorname{supp}c\subset[q+1,q+2d]}}{\arg\min}\|c\|,
$$
$$
\lambda_d=\|c_d\|,\qquad\lambda_{2d}=\|c_{2d}\|.
\tag{1.1}
$$
原准确源旗为 $\mathscr R_q=\bigoplus_{i=0}^{d-2}e_i\otimes(\ker D^{d-i-1}\cap\mathcal H_q)$。对任意 $Lc=r\in\mathscr R_q$，由头矩阵严格上三角，先有 $Dc_{d-1}=0$，再沿头坐标从大到小归纳：将第 $i$ 行方程作用 $D^{d-i-1}$，源项为零，所有 $j>i$ 的项也由已得 $D^{d-j}c_j=0$ 消失。因此 $D^{d-i}c_i=0$ 对全部头坐标准确成立，附加旧 $D^dc=0$ 不改变可行集。
在真实 $r=Lv$ 上，亦可用原低输出 $v$ 的同一联合旗及 $v-c\in\ker L$ 得到这一点。
旧候选使两集非空；它们都是闭仿射集，故极小元存在唯一。

令
$$
\boxed{
Z_{2d}=\ker L\cap\mathcal H_{[q+1,q+2d]}^{(m)},\qquad P_Z=P_{Z_{2d}}.
}
\tag{1.2}
$$
这是准确的双宽零源闭子空间。两套可行集之间的差向量属于它。
因此已有的嵌套最小值 Pythagoras 给
$$
c_{2d}=c_d-P_Zc_d,\qquad
\lambda_d^2-\lambda_{2d}^2=\|P_Zc_d\|^2.
\tag{1.3}
$$
(1.3) 本身不是本稿的新结论；新增的是把该投影准确识别为旧真实越界源的投影。

## 2. 旧 Schur 后头源与完整伴随

令 $y,z_t$ 是原宽 $d$ 的真正最优对偶链，$1\le t\le d-1$，取 $z_d=0$。
用原物理头的正交基，记
$$
\mathcal E_p=\bigoplus_{j=0}^{d-1}e_j(\ker D^{d-j}\cap\mathcal H_p^{(m)}),
\qquad \mathcal P_p=P_{\mathcal E_p},
$$
$$
H_t=P_{W_{d-t}}A(I-P_{W_{d-t+1}}),\qquad
W_k=\operatorname{span}(e_0,\ldots,e_{k-1}).
$$
实际越界源为
$$
h_t=\mathcal P_{q+t}H_t^*P_{\ker D^{t-1}}z_t,\qquad
h=\sum_{t=2}^{d-1}h_t,
\tag{2.1}
$$
其中 $h_t$ 放在第 $q+t$ 孔层。
$h_1=0$，并且
$$
h_t\in\bigoplus_{j=d-t+1}^{d-1}e_j(\ker D^{d-j}\cap\mathcal H_{q+t}^{(m)}).
$$
故 $h$ 与 $c_d$ 逐层头支撑正交：
$$
\boxed{\langle h,c_d\rangle=0.}
\tag{2.2}
$$

由于每个输出头指标 $j\ge d-t+1$ 的尾投影阶数为 $d-j\le t-1$，
嵌套纯核投影还给准确等式
$$
\mathcal P_{q+t}H_t^*z_t=h_t.
\tag{2.3}
$$
这里不需要真实 $w$ 的近似；这是两个投影的代数身份。

写完整伴随向量
$$
\psi=y-\sum_{t=1}^{d-1}z_t,
\qquad
g=P_{[q+1,q+d]}L^*\psi.
$$
$y$ 放在第 $q$ 层，$z_t$ 放在第 $q+t$ 层。
原最小链满足 $c_d=P_{\mathscr C_d}g$，其中 $\mathscr C_d$ 是旧联合旗修复域。
$L^*\psi$ 的其余部分只有第 $q$ 层的 $A^*y$；因 $z_d=0$，不存在 $q+d+1$ 层。

双宽联合旗修复域可写为
$$
\mathscr C_{2d}
=\bigoplus_{t=1}^{2d}
\bigoplus_{j=0}^{\min(d-1,2d-t)}
e_j(\ker D^{d-j}\cap\mathcal H_{q+t}^{(m)}).
\tag{2.4}
$$
它在前 $d$ 段允许全部头坐标。式 (2.4) 的末端头条件来自
$A^{2d-t+1}c_t=0$；逐头纯核条件来自完整的 $L$ 核关系。
因此 $Z_{2d}\subset\mathscr C_{2d}$，没有把旧宽 $d$ 的三角头域原样当作新域。

在前 $d$ 段，$D^*y$ 与 $D^*z_{t-1}$ 已在旧允许头范围内。
所以扩大头域只新增 $-A^*z_t$ 的越界部分。
再用 (2.3) 及完整纯核投影，得到
$$
\boxed{P_{\mathscr C_{2d}}g=c_d-h.}
\tag{2.5}
$$
所有纯删除核投影余项已被该准确投影处理；没有额外的环境替代。

对 $k\in Z_{2d}$，
$$
\langle g,k\rangle
=\langle L^*\psi,k\rangle
=\langle\psi,Lk\rangle=0,
$$
因为 $k$ 没有第 $q$ 层分量。
由 $Z_{2d}\subset\mathscr C_{2d}$ 和 (2.5)，
$$
\boxed{c_d-h\perp Z_{2d}.}
\tag{2.6}
$$

## 3. 越界源的准确零源分量

结合 (1.3)、(2.6)，得到本稿的识别：
$$
\boxed{
P_Zh=P_Zc_d=c_d-c_{2d}.
}
\tag{3.1}
$$
因此
$$
\boxed{
\|P_Zh\|^2=\lambda_d^2-\lambda_{2d}^2,
\qquad
\langle h,c_{2d}\rangle
=-(\lambda_d^2-\lambda_{2d}^2).
}
\tag{3.2}
$$
第二式用 (2.2) 及正交投影自伴性，右端是实非正数。

不可去的部分
$$
h^\perp=(I-P_Z)h=h-c_d+c_{2d}
$$
具有准确范数
$$
\boxed{
\|h^\perp\|^2
=\|h\|^2-\lambda_d^2+\lambda_{2d}^2.
}
\tag{3.3}
$$
它仍在双宽窗口内。式 (3.2) 的负配对不允许把实际 $w$ 在其他配对中换成 $c_{2d}$；
$w\perp N$ 并没有给出 $h\perp N$。

再令完整补核稿中的
$$
K_{\rm tot}=\sum_{t=2}^{d-1}\mathcal K_{q+t}(h_t),\qquad
\widetilde C_{\rm tot}=K_{\rm tot}-h.
$$
每项都属于 $\ker L$，支撑于 $[q+2,q+2d-2]$，故 $K_{\rm tot}\in Z_{2d}$。
于是
$$
\boxed{
P_Z\widetilde C_{\rm tot}
=K_{\rm tot}-c_d+c_{2d},
\qquad
(I-P_Z)\widetilde C_{\rm tot}=-h^\perp.
}
\tag{3.4}
$$
特别，
$$
\boxed{
\inf_{k\in Z_{2d}}\|\widetilde C_{\rm tot}-k\|
=\|h^\perp\|.
}
\tag{3.5}
$$
这是完整非中央合成量在双宽零源商中的准确最小范数。
它不是旧宽 $d$ 极小性对任意高尾零源的正交宣称。

## 4. 实际 W 配对与仍未取得的估计

对 $w\in W=M\ominus N$，原逐头 lift 可作用于所有 $Z_{2d}$：
$$
q+2d\le e^{d^3/3},\qquad
\|P_Wk\|\le e^{-75d^4}\|k\|\quad(k\in Z_{2d}).
$$
将其用于 (3.1) 的实际核向量，得到
$$
\boxed{
|\langle w,h\rangle-\langle w,h^\perp\rangle|
\le e^{-75d^4}\|w\|
\sqrt{\lambda_d^2-\lambda_{2d}^2}.
}
\tag{4.1}
$$
该误差只支付已知能量下降，不使用 $K_{\rm tot}$ 的粗范数。

令
$$
\beta_{2d}=\|P_{[q+1,q+2d]}^{(m)}w\|,
\qquad E=\|v\|^2+\lambda_d^2.
$$
原 R271 正通量与 (2.1) 的逐头投影代价给
$$
|\langle w,h\rangle-E|
\le
\left(2e^{-70d^4}+6e^{-72d^4}\right)\|w\|\sqrt E.
$$
将 (3.3)、(4.1) 代入，$d\ge32$ 时可以统一写成
$$
\boxed{
E\le
\beta_{2d}
\sqrt{\|h\|^2-\lambda_d^2+\lambda_{2d}^2}
+4e^{-70d^4}\|w\|\sqrt E.
}
\tag{4.2}
$$
这是实际缺陷、真正旧最优链及真正双宽最优能量之间的关系。

目前只有 $\|h\|\le6e^{2d^4}\lambda_d$ 的旧预算，故 (4.2) 尚不给无权增长界。
(3.1)–(3.5) 识别的是已去核部分与剩余商范数；没有证明
$h^\perp$ 很小、窗口加倍后的能量下降比例统一，或多次窗口扩大可在已付 lift 范围内收敛。
若把剩余部分进一步移到更远的真实末端通量，仍须另外支付新的对偶链与窗口范围。
普通 ISP 与原 $N=M$ 继续开放。
