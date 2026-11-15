# 加权交换的精确二阶 commutator、真 jet 两带及热算子跨旗指数界

作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro  
日期：2026-11-15

## 0. 范围和记号

使用[统一扇形热平滑稿](R271-appendix-weighted-exchange-sectorial-form-all-order-heat-smoothing-and-same-top-pairing.md)中的同一原尾
$$
D=D_x=\sum_{i\ge x}b_iE_i,\qquad b_i=(i+1)^{-2},\qquad x\ge1,
$$
同一加权交换 $V_i=S_iU_iS_i^{-1}$，以及闭直和发生器
$$
\mathcal L=\mathcal L_x=\sum_{i\ge x}(I-V_i),\qquad
\mathcal T=\mathcal T_x=e^{-x\mathcal L/4}.
$$
上述和先在固定孔层上定义有界算子，再取其自然闭直和。本文所有涉及无界 $\mathcal L$ 的交换式，先在有限孔层核心上证明；随后给出足够的有界延拓或自然域说明。

记真正交 jet 旗
$$
\Pi_r=P_{\ker D^r},\qquad \Pi_0=0,\qquad F_r=\Pi_r-\Pi_{r-1}.
$$
不使用顺次 MP 投影来定义 $F_r$。在远孔 $n$ 层只有 $1\le r\le n+1$，且 $\sum_rF_r=I$。

本文得到三个实际估计：

1. $\operatorname{ad}_D^3(\mathcal L^*)=0$，其二阶 commutator 有显式正系数双删除式；
2. $\mathcal L$ 在上述正交旗上只有对角和两个上方带；
3. 令 $\vartheta=17/16$、$\mathsf J=\sum_r rF_r$，则逐孔层加权共轭的热算子统一满足
$$
\boxed{
\|\vartheta^{-\mathsf J}\mathcal T\vartheta^{\mathsf J}\|
<10.
}
\tag{0.1}
$$
因此 $s>r$ 时
$$
\boxed{
\|\Pi_r\mathcal T(I-\Pi_{s-1})\|
\le10(16/17)^{s-r}.
}
\tag{0.2}
$$
(0.1) 的含义是有限孔层上的共轭具有统一范数，从而在其直和上有唯一有界延拓；不声称 $\vartheta^{\mathsf J}$ 在整个原空间有界。

这些是热算子自己的正交旗预算，尚不控制其与非正交顺次 MP 返回 $\mathscr A_n$ 的乘积。

## 1. 原二位矩阵逐项计算

固定相邻位 $i,i+1$，写 $a=b_i$、$b=b_{i+1}$、$\Delta=a^2-b^2>0$。在单占据基 $10,01$ 上
$$
V_i^*=
\begin{pmatrix}0&a/b\\ b/a&0\end{pmatrix},
$$
在 $00,11$ 上为恒等。$D$ 的其余位与该矩阵对易。

一阶 commutator $[D,V_i^*]$ 从一孔到真空的行，以及从双占据到一孔的列，分别是
$$
\Delta(-a^{-1},\,b^{-1}),\qquad
\Delta(-b^{-1},\,a^{-1})^{\mathsf T}.
\tag{1.1}
$$
它在其它本地次数上为零。再下降一次得到
$$
[D,[D,V_i^*]]
=-\frac{2\Delta^2}{ab}\,E_iE_{i+1}.
\tag{1.2}
$$
由于全部 $E_j$ 对易，第三阶 commutator 为零。因此
$$
\boxed{
\operatorname{ad}_D^2(\mathcal L^*)
=2\sum_{i\ge x}
\frac{(b_i^2-b_{i+1}^2)^2}{b_ib_{i+1}}E_iE_{i+1},
\qquad
\operatorname{ad}_D^3(\mathcal L^*)=0.
}
\tag{1.3}
$$

这些交换差在全空间实际上有有界延拓。令
$\theta_i=\log((i+2)/(i+1))$，则
$\Delta=2ab\sinh(2\theta_i)$。由已证
$\sinh(2\theta_i)\le2/(i+1)$，
$$
\|[D,V_i^*]\|
\le\Delta(a^{-1}+b^{-1})
=2(a+b)\sinh(2\theta_i)
\le8(i+1)^{-3},
$$
$$
\frac{2\Delta^2}{ab}
=8ab\sinh^2(2\theta_i)
\le32(i+1)^{-6}.
$$
故绝对收敛给
$$
\boxed{
\|[D,\mathcal L^*]\|\le\frac4{x^2},\qquad
\|\operatorname{ad}_D^2(\mathcal L^*)\|
\le\frac{32}{5x^5}.
}
\tag{1.4}
$$
特别，$D$ 将 $\operatorname{Dom}\mathcal L^*$ 映入自身，且一阶交换式在该域上成立。这由各孔层恒等式
$\mathcal L^*Dv=D\mathcal L^*v-[D,\mathcal L^*]v$
和 (1.4) 的共同平方和直接推出。

## 2. 真正交旗方向和精确带宽

原 $\mathcal L$ 与 $D$ 对易，所以 $\mathcal L\ker D^r\subset\ker D^r$。另一方面，若 $v\in\ker D^r$，由 (1.3) 的有限 Leibniz 展开，
$$
D^{r+2}\mathcal L^*v
=\mathcal L^*D^{r+2}v
+(r+2)[D,\mathcal L^*]D^{r+1}v
+\binom{r+2}{2}[D,[D,\mathcal L^*]]D^rv
=0.
$$
因此
$$
\mathcal L^*(\ker D^r)\subset\ker D^{r+2}.
\tag{2.1}
$$
两种包含关系一起给
$$
\boxed{
F_r\mathcal L F_s=0
\quad\text{除非}\quad r\le s\le r+2.
}
\tag{2.2}
$$
即 $\mathcal L$ 降低或保持 jet 层号，最多下降两层；它不是关于该正交旗自伴或对角的算子。

写
$$
\mathcal L=B_0+B_1+B_2,\qquad
B_j=\sum_rF_r\mathcal L F_{r+j}.
\tag{2.3}
$$
对 $j=1,2$，$\mathcal L$ 的旗不变性还准确给
$$
F_r\mathcal L F_{r+j}
=F_r(\mathcal L-\mathcal L^*)F_{r+j}.
\tag{2.4}
$$
这使非对角两带受真实反自伴交换形式控制；不用 MP 或 $D$ 的小奇值来估计它们。

## 3. 两带的相对交换形式界

记
$$
\mathfrak e(v)=\sum_{i\ge x}\|P_i^-v\|^2,\qquad
\mathfrak e_{\rm flag}(v)=\sum_r\mathfrak e(F_rv),\qquad
a_x=\sum_i\sinh^2(2\theta_i)\le4/x.
$$
每个 $H_iU_i$ 只连接 $P_i^-$ 与 $I-P_i^-$ 两个子空间，因此对任意 $v,w$，
$$
|\langle(\mathcal L-\mathcal L^*)v,w\rangle|
\le2\sqrt{a_x}
\left(\mathfrak e(v)^{1/2}\|w\|
+\|v\|\mathfrak e(w)^{1/2}\right).
\tag{3.1}
$$
这是有限边和上的 Cauchy--Schwarz，再按自然形式域延拓。

由 (2.4)，先逐 $r$ 用 (3.1)，再对 $r$ 用 Cauchy--Schwarz，得到 $j=1,2$ 时
$$
|\langle B_jv,w\rangle|
\le2\sqrt{a_x}
\left(\mathfrak e_{\rm flag}(v)^{1/2}\|w\|
+\|v\|\mathfrak e_{\rm flag}(w)^{1/2}\right).
\tag{3.2}
$$
[整条正交旗交换行引理](R271-appendix-complete-orthogonal-jet-flag-preserves-fixed-test-exchange-row-budget.md)还对任意实际 $v$ 给
$$
\mathfrak e_{\rm flag}(v)^{1/2}
\le\mathfrak e(v)^{1/2}+\frac4{\sqrt x}\|v\|.
\tag{3.3}
$$
取 $w=v$，遂有完整两带各自的相对形式界
$$
\boxed{
|\langle B_jv,v\rangle|
\le\frac8{\sqrt x}\mathfrak e(v)^{1/2}\|v\|
+\frac{32}{x}\|v\|^2,\qquad j=1,2.
}
\tag{3.4}
$$
这里没有乘旗长度、远孔次数或实际窗口宽度。

## 4. 同一个 heat 的跨旗指数预算

在固定孔层上定义 $\mathsf J=\sum_r rF_r$。由 (2.2)，对 $\vartheta>1$，
$$
\vartheta^{-\mathsf J}\mathcal L\vartheta^{\mathsf J}
=\mathcal L+(\vartheta-1)B_1+(\vartheta^2-1)B_2.
\tag{4.1}
$$
置 $b_\vartheta=\vartheta-1+\vartheta^2-1$。原实部界
$\operatorname{Re}\langle\mathcal Lv,v\rangle
\ge2\mathfrak e(v)-2x^{-1}\|v\|^2$
及 (3.4) 给
$$
\begin{aligned}
\operatorname{Re}\langle
\vartheta^{-\mathsf J}\mathcal L\vartheta^{\mathsf J}v,v\rangle
&\ge2\mathfrak e(v)
-\frac{8b_\vartheta}{\sqrt x}\mathfrak e(v)^{1/2}\|v\|
-\frac{2+32b_\vartheta}{x}\|v\|^2\\
&\ge\mathfrak e(v)
-\frac{2+32b_\vartheta+16b_\vartheta^2}{x}\|v\|^2.
\end{aligned}
\tag{4.2}
$$
最后一步只用一次 Young 不等式，保留一个完整 $\mathfrak e(v)$。

取 $\vartheta=17/16$，则 $b_\vartheta=49/256$，且
$$
c_\vartheta:=2+32b_\vartheta+16b_\vartheta^2
=\frac{35681}{4096}<9.
$$
固定层上的有界指数范数微分给
$$
\left\|
\vartheta^{-\mathsf J}e^{-t\mathcal L}\vartheta^{\mathsf J}
\right\|\le e^{c_\vartheta t/x}.
\tag{4.3}
$$
在 $t=x/4$ 得
$$
\left\|\vartheta^{-\mathsf J}\mathcal T\vartheta^{\mathsf J}\right\|
\le e^{35681/16384}<e^{9/4}<10.
$$
常数对孔层统一，故可按 §0 的含义取直和。

对 $s>r$，由
$\|\Pi_r\vartheta^{\mathsf J}\|\le\vartheta^r$、
$\|\vartheta^{-\mathsf J}(I-\Pi_{s-1})\|\le\vartheta^{-s}$，
得到 (0.2)。相反方向因原旗不变性本就有
$(I-\Pi_r)\mathcal T\Pi_r=0$。因此本文给的是实际热算子由高 jet 向低 jet 的统一指数尾，而非对逆映射的估计。

## 5. 真实反向平滑误差

由 (1.4) 与原实时间界
$\|e^{-t\mathcal L^*}\|\le e^{2t/x}$，
固定层 Duhamel 恒等式及统一直和给
$$
[D,e^{-t\mathcal L^*}]
=-\int_0^t
e^{-(t-s)\mathcal L^*}[D,\mathcal L^*]e^{-s\mathcal L^*}\,ds,
$$
从而
$$
\boxed{\|[D,\mathcal T^*]\|\le e^{1/2}/x.}
\tag{5.1}
$$
二阶 Duhamel 同理给
$$
\|\operatorname{ad}_D^2(\mathcal T^*)\|
\le e^{1/2}\left(x^{-2}+\frac8{5x^4}\right).
\tag{5.2}
$$
它们是原物理算子上的有界误差，不是把 $\mathcal T^*$ 当成保持原核旗。

例如在同一个实际 interior 链 $Cu_n+Du_{n+1}=0$ 上，独立 head $C$ 与 $\mathcal T^*$ 对易，故
$$
C\mathcal T^*u_n+D\mathcal T^*u_{n+1}
=[D,\mathcal T^*]u_{n+1}.
$$
任意共同输出带的残量平方和因此至多为
$e\,x^{-2}\sum_n\|u_{n+1}\|^2$。本文不把这个小残量经未经支付的右逆修成合法链。

## 6. 与原返回问题的区别

本文 (0.2) 只控制 $\mathcal T$，不控制 $\mathcal P_{n,j}$、$\mathscr A_n$ 或它们的逆。实际 paired commutator 消零及两端 partial 仍由前述热平滑稿的同源完整 kernel 构造提供，而非由 $\mathcal T$ 与正交旗或 MP 交换。

新增的正预算是：(1.3) 的精确实际 commutator、(3.4) 对两个非对角带的共同形式控制、以及 (0.2) 对所有 jet 层统一的热传播指数尾。原同顶部 mixed 返回仍须在保全部 MP/旗和同源关系的前提下继续估计。
