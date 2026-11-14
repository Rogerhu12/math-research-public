# 中间头与纯位混合的自然高旗预算及 rank 变化守卫

日期：2026-11-13（UTC）。作者：boundary_resume；AI-assisted，GPT-6 Astra Pro。
状态：以下混合头相似、自然旗右逆与数值预算已完整证明，root 已逐式独立核验并全文核对所引 R249；未将其运输到原 $m$ 头的旗或实际返回源。

本笔记只支付一个具体辅助构造。它不声称原二形式比较已改进，也不把不同维数的像旗当作同一空间做 Neumann 反演。

## 1. 混合头

取 $m>n\ge2$，令
$$
r=2^n,\qquad k=m-n,\qquad \nu=r+k.
$$
在 $m$ 位头空间上定义
$$
\widetilde A
=A_n\otimes I+I\otimes
\sum_{j=n}^{m-1}b_jE_j,\qquad b_j=(j+1)^{-2}.
\tag{1.1}
$$
$A_n$ 是两个原模型之一的真实 $n$ 位头；后 $k$ 个头位仅在本辅助算子中换成纯删除。准确有 $\widetilde A^\nu=0$。

按 [R249](../results/R249-balanced-true-head-jordan-similarity-and-exact-carry-margin.md) §§1、4，记
$$
A_n=S_n(\lambda_nJ_r)S_n^{-1},\qquad
\lambda_n=e^{20-L_n},\quad
L_n=\frac{25r^4}{2(r-2)},
$$
$$
\kappa_n=\|S_n\|\|S_n^{-1}\|\le e^{\Psi_n},
\qquad
\Psi_n=\left(\frac{35}{6}+o(1)\right)r^4.
\tag{1.2}
$$
保留 R249 的准确 $\Psi_n$ 也可使用全部下列有限不等式。

## 2. 转成标准有限 sl2 串

定义正对角矩阵
$$
Ue_i=u_ie_i,\qquad
u_i=\sqrt{\frac{i!(r-1)!}{(r-1-i)!}},
\quad0\le i<r.
$$
因为 $u_i/u_{i-1}=\sqrt{i(r-i)}$，
$$
U^{-1}J_rU=T_r,\qquad
T_re_i=\sqrt{i(r-i)}e_{i-1}.
\tag{2.1}
$$
各因子至少为 $1$，故
$$
\|U\|\|U^{-1}\|=(r-1)!.
$$

在每个纯位上取
$$
V_j=\operatorname{diag}(1,\lambda_n/b_j).
$$
于是 $V_j^{-1}b_jE_jV_j=\lambda_nE_j$。置
$V=\bigotimes_{j=n}^{m-1}V_j$，得到
$$
\widetilde A
=K_0\lambda_n\left(T_r\otimes I+
I\otimes\sum_{j=n}^{m-1}E_j\right)K_0^{-1},
\qquad K_0=(S_nU)\otimes V.
\tag{2.2}
$$
一般准确条件数上界为
$$
\kappa(K_0)\le
\kappa_n(r-1)!
\prod_{j=n}^{m-1}
\max\{b_j/\lambda_n,\lambda_n/b_j\}.
\tag{2.3}
$$
在下文使用的 $n=\lfloor2m/3\rfloor$、充分大 $m$ 范围，
$\lambda_n\le m^{-2}\le b_j$，所以
$$
\boxed{\kappa(K_0)\le
\kappa_n(r-1)!\lambda_n^{-k}.}
\tag{2.4}
$$
没有把它当作酉相似。

记括号内的算子为 $T$。令头串指标与纯位孔数之和为 $N$，逐基计算
$$
[T,T^*]=(\nu-1)I-2N.
$$
因此 $T$ 有完整正交有限串分解；每条串长为某个 $\ell\le\nu$，其下降权为
$$
\sqrt{i(\ell-i)},\qquad1\le i<\ell.
\tag{2.5}
$$
为说明完整性，可用与等权池相同的有限 ladder 证明：primitive 向量经 $T^*$ 上升，相邻范数由显示交换关系逐次确定；不同出生或不同 primitive 基向量产生正交串。取一条已生成串的正交补，它同时约化 $T,T^*,N$，在最小仍非零的等级取 primitive 向量并重复；有限维过程终止，穷尽全空间。最高等级为 $\nu-1$，所以最大串长不超过 $\nu$。

故存在酉矩阵 $O$ 使
$$
O^*TO=\bigoplus_\gamma T_{\ell_\gamma}.
$$
令 $K=K_0O$。则
$$
\boxed{
K^{-1}\widetilde AK
=\bigoplus_\gamma\lambda_n T_{\ell_\gamma},
\qquad
\kappa(K)\le\kappa_n(r-1)!\lambda_n^{-k}.
}
\tag{2.6}
$$

## 3. 只在这些自然串旗上构造高右逆

令 $D$ 为纯尾删除，$E_{h,p}=\ker D^h\cap\mathcal H_p$，并设
$\|D\|\le1$。本节孔数 $q\ge0$ 任意。

先在 (2.6) 的参考串空间中，对每个长度 $\ell$ 的块定义高输入、输出
$$
\mathscr X^{(\ell)}_{H,q,t}
=W_{\ell-t+1}\otimes E_{t-1,q+t}
\quad(2\le t\le\ell),
$$
$$
\mathscr Y^{(\ell)}_{H,q,t}
=W_{\ell-t}\otimes E_{t-1,q+t}
\quad(2\le t<\ell).
\tag{3.1}
$$
把各块正交直和，再经 $K\otimes I$ 送回原 Hilbert 空间。这就是本笔记的自然高旗。其孔层仍不变，范数始终取送回后的原范数。

$\lambda_nT_\ell$ 在其像上的最小右移逆记为 $R_\ell$。
由于 (2.5) 的非零权至少为 $\lambda_n$，
$$
\|R_\ell^j\|\le\lambda_n^{-j}.
\tag{3.2}
$$
取仅第 $t$ 段非零的参考高输出 $f_t$，定义
$$
c_{t-j}=(-1)^j R_\ell^{j+1}D^j f_t,
\qquad0\le j\le t-2.
\tag{3.3}
$$
头位置不越界；$D^j f_t\in E_{t-1-j,q+t-j}$。相邻输出逐项消去，而最左输出由 $D^{t-1}f_t=0$ 消失。首边界和最末头输出均为零。因此 (3.3) 是完整高旗右逆，而不是只解内部的一部分方程。

按同一个 $j$ 分组，不同输入段与不同参考串正交；使用 (3.2) 后只须对 $j$ 作三角不等式。变回原范数得到
$$
\boxed{
\|\widetilde{\mathcal Q}_{H,q}\|
\le C_{\rm mix}
:=\kappa(K)\sum_{j=0}^{\nu-3}
\lambda_n^{-j-1}\|D\|^j
\le \nu\,\kappa_n(r-1)!\lambda_n^{-(r+2k-2)}.
}
\tag{3.4}
$$
这里最后一个指数已经包含 (2.4) 的 $\lambda_n^{-k}$。
常数与 $q$ 无关；空高空间时右逆问题为空。

## 4. 中间尺度确在 d³ 以下

由 (3.4)，准确有
$$
\log C_{\rm mix}
\le
\Psi_n+\log((r-1)!)
+(r+2k-2)(L_n-20)+\log\nu.
\tag{4.1}
$$
当 $n=\lfloor2m/3\rfloor$ 时，$k/r\to0$，所以
$$
\boxed{
\log C_{\rm mix}
\le\left(\frac{55}{3}+o(1)\right)r^4
+O(kr^3)
=O(d^{8/3}),\qquad d=2^m.
}
\tag{4.2}
$$
这里给出的是明确上界，不宣称右逆最优性。

R249 §5 的准确原进位为
$$
-\log\eta_{n-1}
=\frac{175}{2}r^4-\frac{315}{4}r^3+150r.
$$
因此上述明确上界满足
$$
\boxed{
C_{\rm mix}^2\eta_{n-1}
\le
\exp\!\left[-\left(\frac{305}{6}+o(1)\right)r^4\right].
}
\tag{4.3}
$$
按 R249 §6 压到 $m$ 位头，原两模型都有
$$
\|A_m-\widetilde A\|\le26\eta_{n-1}.
\tag{4.4}
$$
所以 (4.3) 也支付其范数误差的相同乘积尺度。

## 5. 这仍不是原旗上的 Neumann 论证

(3.4) 的定义域和值域是 (3.1) 经 $K$ 运输后的自然旗。混合头通常有多个 Jordan 块，因此它的各次像维数与原正规单链 $A_m$ 不同；尤其不能把它们直接等同于原
$$
\operatorname{Ran}A_m^t=W_{d-t}.
$$
虽然 (4.4) 在整个头 Hilbert 空间中成立，误差
$A_m-\widetilde A$ 不一定保持 (3.1) 的运输旗。故 (4.3) 并不自动使
$\widetilde{\mathcal Q}_{H,q}(A_m-\widetilde A)$ 成为同一高问题上的 Neumann 扰动。

直接在原高旗模仿向左构造也会遇到这个区别：输出头方向未必属于混合头相应像。改用 $D$ 上补需要真正受限的删除原像预算；全环境的联合能量下界不能代替该预算。

本笔记已经证明的是混合头本身的短 nilpotence、原范数相似成本和它自身自然高旗上的全孔数右逆。若以后能只对原实际 $B_Aa$ 证明丢失的头方向由两侧源度量支付，(4.2) 的尺度才有机会用于原
$L_{\rm eff}\le C_m(I+Q_-)$ 门槛。当前没有完成这一步。
