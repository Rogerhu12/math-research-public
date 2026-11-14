# R239 附录：完整首个三维块分解与最小修复能量

日期：2026-11-13（UTC）。作者：boundary_resume / Astra-ISP-0c017065；AI-assisted，GPT-6 Astra Pro。状态：完整恒等分解、趋于 1 的分析/合成常数以及准确分支最小能量比较已证明；非原始分支的真实能量及头跃迁通量仍开放。

本稿继续[原始块消去及完整原始投影障碍](../results/R239-appendix-unweighted-primitive-removal-high-rank-blocks-and-full-projection-obstruction.md)、[移动窗口修复](../results/R239-appendix-moving-primitive-windows-and-double-width-repair.md)及 [R271 真实头跃迁通量](../results/R271-appendix-joint-flag-right-inverse-energy-and-head-jump-flux.md)。这里给出一个真正覆盖整个空间的有界分解。它保留非原始分支，因此不等于固定前缀的完整原始投影，也不与后者的指数范数障碍冲突。

## 1. 一个相邻块的准确几何

固定 $m\ge5$，对第 $i$ 个相邻块
$$
I_i=\{n_i,n_i+1\},\qquad n_i=m+2(i-1)
$$
置 $a_i=(n_i+1)^{-2}$、$b_i=(n_i+2)^{-2}$、$s_i=\sqrt{a_i^2+b_i^2}$。在一孔层定义三个单位向量
$$
h_i=\frac{b_i|10\rangle-a_i|01\rangle}{s_i},\qquad
g_i=\frac{a_i|10\rangle-b_i|01\rangle}{s_i},\qquad
t_i=\frac{b_i|10\rangle+a_i|01\rangle}{s_i}.
\tag{1.1}
$$
令
$$
\rho_i=\frac{2a_ib_i}{a_i^2+b_i^2},\qquad
\delta_i=\frac{a_i^2-b_i^2}{a_i^2+b_i^2}.
$$
准确有
$$
\rho_i^2+\delta_i^2=1,\qquad
\langle g_i,t_i\rangle=0,\qquad
h_i=\rho_i g_i-\delta_i t_i,\qquad
\langle h_i,t_i\rangle=-\delta_i.
\tag{1.2}
$$
定义整个四维块上的幂等算子
$$
P_i=\frac{|h_i\rangle\langle g_i|}{\rho_i},
\qquad Q_i=I-P_i.
\tag{1.3}
$$
对 $D_i=a_iE_{n_i}+b_iE_{n_i+1}$，
$$
D_iP_i=P_iD_i=0,\qquad D_iQ_i=Q_iD_i.
\tag{1.4}
$$
其中
$$
\operatorname{Ran}Q_i=g_i^\perp
=\operatorname{span}\{\Omega_i,t_i,|11\rangle_i\}.
\tag{1.5}
$$
这个三维子空间有显示的原 Hilbert 正交基；$P_i$ 与 $Q_i$ 彼此互补，但不是正交投影。直接在其二维一孔层算范数，得到 $\|P_i\|=\|Q_i\|=\rho_i^{-1}$。

记 $G_i=|g_i\rangle\langle g_i|$。由 (1.2)，
$$
Q_i=(I-G_i)+\frac{\delta_i}{\rho_i}|t_i\rangle\langle g_i|.
\tag{1.6}
$$
另对任意 $u\in\operatorname{Ran}Q_i$，
$$
\||h_i\rangle\langle h_i|u\|\le\delta_i\|u\|.
\tag{1.7}
$$

## 2. 首个非原始块给完整恒等分解

对任意有限整数 $n\ge1$，在前 $n$ 个相邻块及其全部外部因子上定义
$$
T_i=P_1\cdots P_{i-1}Q_i\quad(1\le i\le n),\qquad
T_\infty=P_1\cdots P_n.
\tag{2.1}
$$
未写出的块上取恒等算子。所有不同块算子交换，且 $P_iQ_i=Q_iP_i=0$。所以
$$
\boxed{I=T_\infty+\sum_{i=1}^nT_i,}
\qquad
T_\alpha T_\beta=0\quad(\alpha\ne\beta),\qquad
T_\alpha^2=T_\alpha.
\tag{2.2}
$$
这是在整个 Hilbert 空间上的有限恒等式。$T_i$ 保留首个三维分支，此后各块完全自由；没有继续展开成所有 $2^n$ 种原始/非原始模式。

所有 $T_\alpha$ 保尾孔次数并与 $D_m$ 交换。它们只作用于纯尾，所以也与原头 $A_m$ 及 $L_m=A_m+D_m$ 交换。因此它们保低输出空间、准确残量旗以及每个固定修复窗的可行链。这里不声称它们与实际 $T$ 或 $P_M,P_N$ 交换。

记
$$
R_n=\prod_{i=1}^n\rho_i^{-1},\qquad
S_n=\sum_{i=1}^n\delta_i^2,\qquad
S'_n=\sum_{i=1}^n\frac{\delta_i^2}{\rho_i^2}.
\tag{2.3}
$$
下面的分析和合成常数只用这些平方和。

## 3. 完整分析算子的统一界

对任意向量 $x$，在输入侧按正交的 $g_i$ 与 $g_i^\perp$ 作首次离开分解。具体地令
$$
x_i=(\langle g_1|\otimes\cdots\otimes\langle g_{i-1}|
     \otimes(I-G_i)\otimes I)x,
$$
$$
v_i=(\langle g_1|\otimes\cdots\otimes\langle g_i|
     \otimes I)x.
$$
省略了无关的头或其他外部因子。正交性给
$$
\sum_{i=1}^n\|x_i\|^2+\|v_n\|^2=\|x\|^2,\qquad
\|v_i\|\le\|x\|.
\tag{3.1}
$$
由 (1.6)，去掉单位输出因子 $h_1\otimes\cdots\otimes h_{i-1}$ 后，
$T_ix$ 的剩余向量准确为
$$
\left(\prod_{j<i}\rho_j^{-1}\right)
\left(x_i+\frac{\delta_i}{\rho_i}t_i\otimes v_i\right),
\tag{3.2}
$$
而 $T_\infty x$ 的剩余向量为 $R_nv_n$。

对所有分量的外直和使用三角不等式，再用 (3.1)，得到
$$
\boxed{
\left(\sum_{i=1}^n\|T_ix\|^2+\|T_\infty x\|^2\right)^{1/2}
\le A_n\|x\|,\qquad
A_n=R_n(1+\sqrt{S'_n}).
}
\tag{3.3}
$$
第二项只付
$\sum_i(\delta_i/\rho_i)^2\|v_i\|^2
\le S'_n\|x\|^2$，没有用 $\sum_i|\delta_i|$。这正是停止在首个非原始块后得到的控制。

## 4. 完整合成算子的统一界

取任意
$$
y_i\in\operatorname{Ran}T_i,\qquad
y_\infty\in\operatorname{Ran}T_\infty.
$$
可唯一写成
$$
y_i=h_1\otimes\cdots\otimes h_{i-1}\otimes u_i,
\qquad
u_i\in g_i^\perp\otimes H_{>i},
$$
且 $\|u_i\|=\|y_i\|$。把 $u_i$ 按第 $i$ 块的 $h_i^\perp$ 与 $h_i$ 正交分成
$u_i^\perp+u_i^\parallel$。由 (1.7)，
$$
\|u_i^\parallel\|\le\delta_i\|u_i\|.
$$
所有
$h_1\otimes\cdots\otimes h_{i-1}\otimes u_i^\perp$
及 $y_\infty$ 彼此正交。平行部分则由一次 Cauchy--Schwarz 控制：
$$
\left\|\sum_i h_1\otimes\cdots\otimes h_{i-1}
                        \otimes u_i^\parallel\right\|
\le\sqrt{S_n}\left(\sum_i\|u_i\|^2\right)^{1/2}.
$$
因此
$$
\boxed{
\left\|y_\infty+\sum_{i=1}^ny_i\right\|
\le B_n
 \left(\|y_\infty\|^2+\sum_{i=1}^n\|y_i\|^2\right)^{1/2},
\qquad B_n=1+\sqrt{S_n}.
}
\tag{4.1}
$$
这是完整合成界；不是只估各投影的单独范数。

## 5. 实际物理系数使两个常数一致趋于 1

令 $z_i=(n_i+2)/(n_i+1)$。准确有
$$
\delta_i=\tanh(2\log z_i),\qquad
\rho_i^{-1}=\cosh(2\log z_i),\qquad
\frac{\delta_i}{\rho_i}=\sinh(2\log z_i).
$$
对 $n_i\ge5$，
$$
\delta_i\le\frac2{n_i+1},\qquad
\frac{\delta_i}{\rho_i}\le\frac3{n_i+1},\qquad
\log\rho_i^{-1}\le\frac2{(n_i+1)^2}.
\tag{5.1}
$$
前后两条来自 $\tanh u\le u$、$\log\cosh u\le u^2/2$ 和
$\log(1+x)\le x$；中间一条也可直接用
$\sinh(2\log(1+x))=((1+x)^2-(1+x)^{-2})/2\le3x$
对 $0\le x\le1/6$ 验证。

积分比较给
$$
\sum_{i\ge1}\frac1{(m+2(i-1)+1)^2}
\le\frac1{(m+1)^2}+\frac1{2(m+1)}
\le\frac2{3(m+1)}.
$$
因此，对所有 $n$ 一致有
$$
R_n\le e^{2/(m+1)},\qquad
S_n\le\frac3{m+1},\qquad
S'_n\le\frac6{m+1}.
\tag{5.2}
$$
结合 (3.3)、(4.1)，
$$
\boxed{
A_n\le e^{2/(m+1)}
       \left(1+\sqrt{\frac6{m+1}}\right),\qquad
B_n\le1+\sqrt{\frac3{m+1}}.
}
\tag{5.3}
$$
特别它们都为 $1+O(m^{-1/2})$，不含 $n$、$q$ 或分支数的增长。

没有把一串一般的近正交变基直接相乘；那样会支付不可求和的一阶角度。这里的两次证明都使用了首个离开位置的正交分解。

## 6. 完整最小修复能量与分支能量

固定原合法 $m,q$，令 $r=L_mv$，其中准确取
$$
v\in\mathcal V_{m,q}:=\mathcal H_{\le q}^{(m)}\cap\ker(P_{\le q-1}L_m).
$$
这是原低输出精确核，不是任意低孔向量。修复宽度先取原 $d=2^m$；也可取任意预先指定的 $h\ge d$。统一写
$$
\mathcal C^{[h]}(r)=
\{c\in\mathcal H_{[q+1,q+h]}^{(m)}:
  L_mc=r,\ D_m^dc=0\},
\qquad
\lambda^{[h]}(r)=\min_{\mathcal C^{[h]}(r)}\|c\|.
\tag{6.1}
$$
旧宽度 $d$ 的相容修复保证非空。宽度 $h>d$ 时按 (6.1) 定义，不把旧 $d$ 段三角链旗原样搬过去。

对分解 (2.1)，定义真正受限分支最小值
$$
\mu_\alpha^{[h]}(r)=
\min\{\|c\|:\ c\in\mathcal C^{[h]}(T_\alpha r),
                   \ c\in\operatorname{Ran}T_\alpha\}.
\tag{6.2}
$$
每个集合非空：把任意整体修复施加 $T_\alpha$ 即得候选。它也是闭仿射集，因为 $T_\alpha$ 是有界幂等算子。故每个最小元存在唯一。

把整体最小元 $c^{\min}$ 代入各分支并用 (3.3)，得到
$$
\sum_\alpha \mu_\alpha^{[h]}(r)^2
\le\sum_\alpha\|T_\alpha c^{\min}\|^2
\le A_n^2\lambda^{[h]}(r)^2.
$$
反过来，各分支最小元之和由 (2.2) 是整体合法修复，故 (4.1) 给
$$
\lambda^{[h]}(r)^2
\le B_n^2\sum_\alpha\mu_\alpha^{[h]}(r)^2.
$$
因此
$$
\boxed{
B_n^{-2}\lambda^{[h]}(r)^2
\le
\mu_\infty^{[h]}(r)^2+\sum_{i=1}^n\mu_i^{[h]}(r)^2
\le
A_n^2\lambda^{[h]}(r)^2.
}
\tag{6.3}
$$
这里比较的是准确最小能量，且覆盖全部残量。没有把不受限的分支最小元擅自认作在 $\operatorname{Ran}T_\alpha$ 内；(6.2) 显式保留这个条件。

## 7. 真实源的终端原始分支可以删去

现沿原全部整数参数 $m=m(q)$，取 $n=q$。$T_\infty$ 正是前 $2q$ 尾位的配对原始投影：
$$
T_\infty=\frac{|h_1\otimes\cdots\otimes h_q\rangle
                   \langle g_1\otimes\cdots\otimes g_q|}
                  {\rho_1\cdots\rho_q}.
$$
对实际 $w\in M$ 和 $r=L_mv_{m,q}(w)$，已证相容真空 jets 修复处于 $\operatorname{Ran}T_\infty$，并满足
$$
\mu_\infty^{[h]}(r)
\le\sqrt{K_{m+2q,d}}R_q
 [\tau_q(w)+e^{-70d^4}\|w\|]
\longrightarrow0
\quad(h\ge d).
\tag{7.1}
$$
指数常数在这里保守放宽；首项常数依然趋于 $1$。这是受限分支能量的合法上界。

由 (6.3)，
$$
\boxed{
B_q^{-1}\lambda^{[h]}(r)-\mu_\infty^{[h]}(r)
\le
\left(\sum_{i=1}^q\mu_i^{[h]}(r)^2\right)^{1/2}
\le A_q\lambda^{[h]}(r).
}
\tag{7.2}
$$
所以完整实际最小能量，除一个趋零分量外，等价于全部首个三维分支能量的平方和，比较常数为 $1+o(1)$。这个结论适用于原宽 $d$、移动稿宽 $2d$ 以及其他明确选择的有限宽度。

这比仅给出一个高秩受控投影多了完整覆盖，但尚未给右侧平方和的新增长上界。

## 8. 每个非原始分支有准确三维头接口

在 $\operatorname{Ran}T_i$ 中，前 $i-1$ 块固定为单位原始张量
$h_1\otimes\cdots\otimes h_{i-1}$。第 $i$ 块的正交基是
$$
f_0=\Omega_i,\qquad f_1=t_i,\qquad f_2=|11\rangle_i.
$$
其删除矩阵准确为
$$
D_if_0=0,\qquad
D_if_1=\alpha_if_0,\qquad
D_if_2=\beta_if_1,
$$
$$
\alpha_i=\frac{2a_ib_i}{s_i}=\rho_i s_i,\qquad
\beta_i=s_i.
\tag{8.1}
$$
不是把三维链的两个系数偷换成同一个数。

设 $D_{>i}$ 为物理位号 $m+2i$ 及之后的纯尾，置
$$
B_i=A_m+D_{>i}.
$$
真实 $x=T_iw$ 满足
$$
L_mx=T_iE_mw=:\epsilon,\qquad
\|\epsilon\|\le26R_q\eta_{m-1}\|w\|.
\tag{8.2}
$$
按 $f_0,f_1,f_2$ 分解后，
$$
B_ix_0+\alpha_ix_1=\epsilon_0,\qquad
B_ix_1+\beta_ix_2=\epsilon_1,\qquad
B_ix_2=\epsilon_2.
\tag{8.3}
$$
因此
$$
x_1=-\alpha_i^{-1}B_ix_0+\alpha_i^{-1}\epsilon_0,
$$
$$
x_2=(\alpha_i\beta_i)^{-1}B_i^2x_0
     -(\alpha_i\beta_i)^{-1}B_i\epsilon_0
     +\beta_i^{-1}\epsilon_1,
$$
$$
\boxed{
B_i^3x_0=B_i^2\epsilon_0-\alpha_iB_i\epsilon_1
                         +\alpha_i\beta_i\epsilon_2.
}
\tag{8.4}
$$
这些是原 Hilbert 正交坐标内的准确身份。其局部源在剩余自由次数
$q-(i-1)$ 处；不能对所有分支一律把远尾当成真空。

同样不能从 $w\perp N$ 推出 $T_iw\perp N$，因为尚未证明 $T_i$ 保 $N$。R271 最优头通量仍须在原整体实际向量上使用；(6.3) 与 (7.2) 提供了完整源专属的最小能量接口，而不是逐分支缺陷正交性的替代品。

目前已把一个整体能量问题准确拆成平方可和、近等距的完整分支问题，并删除其中的全原始分支。剩余是控制这些三维分支的真实最小能量之和，或在该分解下控制真正最优对偶链的有限头跃迁。未证明其增长足以触发全部整数倒数发散准则，故 $N=M$ 及普通 Hilbert ISP 仍开放。


[完整工作源](../notes/2026-11-13-complete-first-triplet-resolution-and-minimal-energy-boundary-resume.md)。
