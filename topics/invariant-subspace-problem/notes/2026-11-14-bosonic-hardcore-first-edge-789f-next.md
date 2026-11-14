# 首边的完整硬核纤维、联合最小化与全部坐标下降

日期：2026-11-14。作者：Astra-ISP-789f / boundary_core。局部硬核方程与 root 同步推导。

**状态：本文的纤维恒等式、仿射下界、Euler/MP 正交身份及两个适用范围障碍已证明；一般首边常数 1 或任意有限统一常数仍未证明。** 没有另加有限权组的正性结论。前一轮独立权搜索的三个文件保持冻结。

## 1. 实际完整层与玻色模式

取任意 $N\ge2s+2$、$b_i>0$，原 Boolean 删除为
$$
D=\sum_{i=1}^N b_iE_i,\qquad S=\sum_i b_i^2.
$$
使用 [完整低占据比较稿 §3](../results/R271-appendix-all-birth-low-occupation-bosonic-minimal-gram-comparison.md) 的等距嵌入：原平方自由层 $\mathcal H_p$ 嵌入标准 $N$ 模式玻色层 $\mathscr F_p$。记玻色删除为 $a_i$，则
$$
\mathcal H_p=\bigcap_i\ker a_i^2\cap\mathscr F_p,
\qquad a_i|_{\mathcal H_p}=E_i.
\tag{1.1}
$$
因此硬核空间同时对全部 $a_i$ 不变，不只对它们的一个线性组合不变。

先把 $D$ 除以 $\sqrt S$，使 $S=1$；第 4 节还原尺度。置
$$
a_0=\sum_i b_i a_i,
\qquad c_i=a_i-b_i a_0.
$$
于是
$$
\sum_i b_i c_i=0,\qquad
[c_i,c_j^*]=\delta_{ij}-b_i b_j,
\qquad [a_0,c_i]=[a_0,c_i^*]=0.
\tag{1.2}
$$
用 $\mathscr V_p$ 表示总次数 $p$ 且 $a_0$ 模式占据数为零的玻色空间。沿这个模式有正交分解
$$
\mathscr F_p=\bigoplus_{k=0}^p |k\rangle_0\otimes\mathscr V_{p-k}.
\tag{1.3}
$$
下文省略张量符号。原 primitive 恰为
$$
K_p=\ker D\cap\mathcal H_p
=\{f\in\mathscr V_p:c_i^2f=0\text{ 对全部 }i\}.
\tag{1.4}
$$
这里 $c_i$ 也保持原硬核空间，因为它是 $a_i,a_0$ 的线性组合。

一直采用完整层 MP：
$$
\mathcal J_{j,s}=(D^j/j!:\mathcal H_{s+j}\to\mathcal H_s)^\dagger|_{K_s},
\qquad \Gamma_{j,s}=\mathcal J_{j,s}^*\mathcal J_{j,s}.
\tag{1.5}
$$
合法范围中的满射由[有限模型归约](../results/R271-appendix-universal-adjacent-height-constants-finite-models-and-continuous-tail.md)给出。没有以 primitive 压缩的逆替换 (1.5)。

## 2. 第一阶的唯一最小硬核修正

定义行算子
$$
R_p:\mathscr V_p\to\bigoplus_{i=1}^N\mathscr V_{p-2},
\qquad R_p g=(c_i^2g)_i,
$$
$$
C_p:\mathscr V_p\to\bigoplus_{i=1}^N\mathscr V_{p-1},
\qquad C_p g=(2b_i c_i g)_i.
\tag{2.1}
$$
负次数目标空间取零，故 $R_0,R_1,C_0$ 为零。由 (1.4)，$K_p=\ker R_p$。

若 $D u=f\in K_s$，玻色模式分解强制
$$
u=|1\rangle_0f+|0\rangle_0g.
\tag{2.2}
$$
不存在更高 $a_0$ 占据分量，因为删除一次之后它们仍有正占据数，不能出现在 $f$ 中。原硬核条件 $a_i^2u=0$ 准确变成
$$
c_i^2g=-2b_i c_i f\quad\text{对全部 }i,
\qquad R_{s+1}g=-C_s f.
\tag{2.3}
$$
这些约束可解，来自原完整层满射。所有解相差 $K_{s+1}$；最小范数解为
$$
\boxed{L_s=-R_{s+1}^{\dagger}C_s|_{K_s},\qquad
g=L_s f\perp K_{s+1}.}
\tag{2.4}
$$
所以
$$
\boxed{\mathcal J_{1,s}f=|1\rangle_0f+|0\rangle_0L_sf,
\qquad \Gamma_{1,s}=I+L_s^*L_s.}
\tag{2.5}
$$
这里的 MP 在有限玻色层内完全明确。它只是实际完整 Boolean MP 的正交模式表达，没有扩大实际可行集。

## 3. 第二阶必须作一次联合最小化

若 $(D^2/2)u=f\in K_s$，则唯一可能的模式形状为
$$
u=\sqrt2|2\rangle_0f+|1\rangle_0g_1+|0\rangle_0h.
\tag{3.1}
$$
对 $a_i^2=(b_i a_0+c_i)^2$ 逐占据分量展开，硬核条件等价于
$$
c_i^2g_1=-4b_i c_i f,
$$
$$
c_i^2h=-2b_i^2f-2b_i c_i g_1.
\tag{3.2}
$$
由第一条和 (2.4)，准确有
$$
g_1=2L_sf+z,\qquad z\in K_{s+1}.
\tag{3.3}
$$
令
$$
T_s f=(2b_i^2f)_i,\qquad
F_s=-2C_{s+1}L_s-T_s,
$$
$$
\mathcal A_s:K_{s+1}\oplus\mathscr V_{s+2}
\longrightarrow\bigoplus_i\mathscr V_s,
\qquad
\mathcal A_s(z,h)=C_{s+1}z+R_{s+2}h.
\tag{3.4}
$$
第二条约束正是
$$
\mathcal A_s(z,h)=F_s f.
\tag{3.5}
$$
原完整二阶满射保证 $F_s(K_s)\subset\operatorname{Ran}\mathcal A_s$，包括最短合法长度 $N=2s+2$。这里没有假设任意选定的 $z$ 都能延拓为 $h$。

因 $L_sf\perp K_{s+1}$，(3.1)–(3.3) 的完整范数为
$$
\|u\|^2=2\|f\|^2+4\|L_sf\|^2+\|z\|^2+\|h\|^2.
$$
因此真正的联合最小量为
$$
\boxed{M_s=\mathcal A_s^\dagger F_s,
\qquad
\Gamma_{2,s}=2I+4L_s^*L_s+M_s^*M_s.}
\tag{3.6}
$$
等价地，置 $P_{s+1}=P_{K_{s+1}}$，
$$
\mathcal W_s=R_{s+2}R_{s+2}^*
+C_{s+1}P_{s+1}C_{s+1}^*.
$$
则
$$
\boxed{M_s^*M_s=F_s^*\mathcal W_s^\dagger F_s.}
\tag{3.7}
$$
逆只在实际像上取 MP；(3.5) 的范围条件保留。把 $z,h$ 分开最小化或预先置 $z=0$，一般会改变 (3.6)。

### 3.1 下一出生可延拓时的真正 Schur 形式

若 $N\ge2s+3$，下一出生的 $L_{s+1}$ 也存在，且
$$
C_{s+1}|_{K_{s+1}}=-R_{s+2}L_{s+1}.
$$
这时 $F_sf\in\operatorname{Ran}R_{s+2}$，可写
$h_0=R_{s+2}^\dagger F_sf$。联合约束化为
$$
h=h_0+L_{s+1}z
$$
加上一个可直接由最小化删除的 $K_{s+2}$ 自由量。准确最小化给
$$
z=-(I+L_{s+1}^*L_{s+1})^{-1}L_{s+1}^*h_0,
$$
$$
h=(I+L_{s+1}L_{s+1}^*)^{-1}h_0,
$$
$$
\|M_sf\|^2
=\langle h_0,(I+L_{s+1}L_{s+1}^*)^{-1}h_0\rangle.
\tag{3.8}
$$
从原 MP 正交也可直接看到 $z+L_{s+1}^*h=0$。
最短端 $N=2s+2$ 不存在这个下一出生的第一逆，故只使用 (3.4)–(3.7)，不能虚构 $L_{s+1}$ 后套 (3.8)。

## 4. 已可推出的全参数仿射下界与真正缺口

记 $H_s=L_s^*L_s\succeq0$。由 (2.5)、(3.6) 立即有
$$
\boxed{\Gamma_{2,s}\succeq4\Gamma_{1,s}-2I\qquad(S=1).}
\tag{4.1}
$$
还原共同尺度得到任意正权、任意合法出生的准确下界
$$
\boxed{
\Gamma_{1,s}\succeq S^{-1}I,\qquad
\Gamma_{2,s}\succeq\frac4S\Gamma_{1,s}-\frac2{S^2}I.
}
\tag{4.2}
$$
右边严格正，因此还给
$$
\Gamma_{1,s}\Gamma_{2,s}^{-1}\Gamma_{1,s}
\preceq
\frac{(S\Gamma_{1,s})^2}{4S\Gamma_{1,s}-2I},
\tag{4.3}
$$
右式按同一个正算子的函数演算理解。
特别，条件
$$
S\Gamma_{1,s}\preceq(2+\sqrt2)I
\tag{4.4}
$$
足以推出首边常数 1。本文没有证明 (4.4) 对任意正权成立；事实上首阶 Gram 在极端权下可以很大。

所需一般首边在该纤维中准确等价于
$$
\boxed{
M_s^*M_s\succeq H_s^2-2H_s-I.
}
\tag{4.5}
$$
或等价的能量形式
$$
\|H_sf\|^2\le\|f\|^2+2\|L_sf\|^2+\|M_sf\|^2.
$$
仅由 $M_s^*M_s\succeq0$ 不能支付任意大的 $H_s^2$。这就是尚缺的真实联合硬核控制。

## 5. 全部坐标删除给两级 Euler/MP 身份

此节继续归一 $S=1$，所有 $a_i$ 在硬核层上就是物理 $E_i$。为避免与 $D$ 混淆，把 primitive 上的全坐标下降行记为
$$
\partial_s:K_s\to\bigoplus_iK_{s-1},\qquad
\partial_s f=(a_i f)_i.
$$
原次数恒等式给
$$
\partial_s^*\partial_s=sI.
\tag{5.1}
$$
定义真正第一自由分量
$$
\mathsf K_{i,s}=P_{K_s}a_i\mathcal J_{1,s}:K_s\to K_s.
$$
因为 $D$ 与所有 $a_i$ 交换，有正交分解
$$
\boxed{
a_i\mathcal J_{1,s}
=\mathcal J_{1,s-1}a_i+\mathsf K_{i,s}.
}
\tag{5.2}
$$
记 $\mathsf K_s=(\mathsf K_{i,s})_i$。Euler 范数恒等式和第一 MP 的核正交给
$$
\boxed{
(s+1)\Gamma_{1,s}
=\partial_s^*(I_N\otimes\Gamma_{1,s-1})\partial_s
+\mathsf K_s^*\mathsf K_s,
\qquad
\mathsf K_s^*\partial_{s+1}=0.
}
\tag{5.3}
$$
第二条的证明是将
$\langle\mathcal J_{1,s}f,k\rangle=0$、$k\in K_{s+1}$
乘以次数 $s+1$，再逐坐标使用 (5.2)。较低出生的第一逆部分与 $a_i k\in K_s$ 正交。

与第 2 节的横向量相联系，准确有
$$
\mathsf K_{i,s}=b_iI+T_{i,s},\qquad
T_{i,s}=c_iL_s-L_{s-1}c_i:K_s\to K_s,
\qquad\sum_i b_iT_{i,s}=0.
$$
所以 (5.3) 也可写成
$$
\boxed{
(s+1)L_s^*L_s
=\sum_i c_i^*L_{s-1}^*L_{s-1}c_i
+\sum_iT_{i,s}^*T_{i,s}.
}
\tag{5.4}
$$

### 5.1 第二阶保留全部跨出生项

置
$$
Z_s=D\mathcal J_{2,s}-2\mathcal J_{1,s}:K_s\to K_{s+1}.
\tag{5.5}
$$
它正是第 3 节最小量中的 $z$。定义
$$
\mathsf R_{i,s}
=2\mathsf K_{i,s}+a_iZ_s-Z_{s-1}a_i.
\tag{5.6}
$$
再定义 $\mathsf Q_{i,s}$ 为下式的剩余项：
$$
\boxed{
a_i\mathcal J_{2,s}
=\mathcal J_{2,s-1}a_i
+\mathcal J_{1,s}\mathsf R_{i,s}
+\mathsf Q_{i,s},
\qquad\operatorname{Ran}\mathsf Q_{i,s}\subset K_{s+1}.
}
\tag{5.7}
$$
证明：先施加 $D^2/2$，第一项具有同一源；其差在 $\ker D^2$。再施加 $D$，使用 (5.2)、(5.5)，其 primitive 源恰为 (5.6)。最后剩余项在 $\ker D$。三项是同一物理层中三个真实核高度，物理正交。

令 $\mathsf R_s,\mathsf Q_s$ 为相应坐标行，得到
$$
\boxed{
(s+2)\Gamma_{2,s}
=\partial_s^*(I_N\otimes\Gamma_{2,s-1})\partial_s
+\mathsf R_s^*(I_N\otimes\Gamma_{1,s})\mathsf R_s
+\mathsf Q_s^*\mathsf Q_s.
}
\tag{5.8}
$$
第二 MP 的两个实际核正交分别给
$$
\boxed{\mathsf Q_s^*\partial_{s+2}=0,}
\tag{5.9}
$$
以及在 $N\ge2s+3$ 时
$$
\boxed{
\partial_{s+1}^*(I_N\otimes\Gamma_{1,s})\mathsf R_s
+\mathsf K_{s+1}^*\mathsf Q_s=0.
}
\tag{5.10}
$$
(5.10) 来自 $\mathcal J_{2,s}K_s\perp\mathcal J_{1,s+1}K_{s+1}$，再对同一次数 $s+2$ 用 Euler。最短端没有 $\mathcal J_{1,s+1}$，故不写虚假的全 $K_{s+1}$ 关系。

对 $s=0$，所有负出生项按零处理。更高 primitive 空间为零时，对应行自然为零，不要求额外满射。

### 5.2 还有真实的坐标交换约束

物理 $a_i a_j=a_j a_i$ 和 $a_i^2=0$ 作用于硬核层。将它们作用在 (5.2)，并利用真实最小逆分解，得
$$
\boxed{
a_i\mathsf K_{j,s}-a_j\mathsf K_{i,s}
=\mathsf K_{j,s-1}a_i-\mathsf K_{i,s-1}a_j,
}
\tag{5.11}
$$
$$
\boxed{a_i\mathsf K_{i,s}=-\mathsf K_{i,s-1}a_i.}
\tag{5.12}
$$
这些是实际坐标行的约束，不能将 $\mathsf K,\mathsf R,\mathsf Q$ 当作任意满足几条范数式的矩阵。当前尚未从 (5.3)、(5.8)–(5.12) 得到保持同一源度量的首边归纳。

## 6. 一个必须保留交叉项的实际 Boolean 障碍

若将 (5.8) 作粗行 Cauchy 而要求
$$
\sum_i\mathsf K_{i,s}^*\Gamma_{1,s}^{-1}\mathsf K_{i,s}
\preceq C I
\tag{6.1}
$$
具有与权无关的常数，那么即使 $N=4,s=1$ 也失败。下面是准确原 Boolean 计算，不是数值探针。

取权 $(r,1,1,1)$、$r>0$，并在 $K_1=b^\perp$ 中取
$$
f=(3,-r,-r,-r),\qquad\|f\|^2=3(r^2+3).
$$
固定 primitive 线 $\mathbb Cf$ 上
$$
\Gamma_1=\lambda_f:=\frac{r^2+1}{r^2+3};
$$
普通三位的标准支
$\{(0,x_1,x_2,x_3):x_1+x_2+x_3=0\}$ 上
$$
\Gamma_1=\lambda_0:=\frac1{r^2+1}.
$$
这些来自完整 $DD^*$ 的逆：固定二维物理块为
$\begin{pmatrix}3&\sqrt3r\\\sqrt3r&r^2+4\end{pmatrix}$，行列式为 $12$。

完整第一最小逆 $\mathcal J_1f$ 的三个强弱二孔坐标为 $1$，三个弱弱二孔坐标为 $-r$。因此
$$
\mathsf K_{0,1}f=-\frac r{r^2+3}f.
$$
对普通位 $i=1,2,3$，其固定支为
$$
\frac{2r^2+3}{3(r^2+3)}f,
$$
标准支为 $r(e_i-\tfrac13(1,1,1))$。逐正交支相加得到
$$
\boxed{
\frac{\displaystyle\sum_i
\langle\Gamma_1^{-1}\mathsf K_{i,1}f,
\mathsf K_{i,1}f\rangle}{\|f\|^2}
=\frac{4r^2+3}{3(r^2+1)}
+\frac{2r^2(r^2+1)}{3(r^2+3)}
\sim\frac23r^2.
}
\tag{6.2}
$$
例如 $r=2$ 时准确为 $111/35>2=s+1$。共同缩放全部权不改变左式，故也可归一到 $S=1$。

这里的真实首边早已由出生一普遍定理支付。因而 (6.2) 只否定将 $\mathsf K$ 单独按逆源度量控制的捷径，不能用于反驳首边本身。必须保留 (5.6) 的 $Z$ 交叉和 (5.8) 的 $\mathsf Q$ 费用。

## 7. 单个玻色删除不变性本身甚至没有统一首边常数

本节只核查入口假设的范围，**不是 Boolean 反例**。在两模式标准正交玻色基 $e_{r,k}$ 中，令 $a_0e_{r,k}=\sqrt r\,e_{r-1,k}$。对 $t>0$ 取分级空间
$$
\mathcal M_0=\mathbb Ce_{0,0},\quad
\mathcal M_1=\mathbb Ce_{0,1},\quad
\mathcal M_2=\mathbb C u_t,\quad
\mathcal M_3=\mathbb C v_t,
$$
$$
u_t=e_{1,1}+t e_{0,2},\qquad
v_t=\sqrt2e_{2,1}+2t e_{1,2}.
$$
直接有
$$
a_0u_t=e_{0,1},\qquad a_0v_t=2u_t.
$$
所以 $\mathcal M$ 对 $a_0$ 不变。令 $D=a_0|_{\mathcal M}$，则
$$
D^*=P_{\mathcal M}a_0^*|_{\mathcal M},\qquad
(D^*)^j=P_{\mathcal M}(a_0^*)^j|_{\mathcal M}.
$$
后一个等式来自 $\mathcal M^\perp$ 对 $a_0^*$ 不变。完整的一阶、二阶映射到 $\mathcal M_1$ 均满射，且源 primitive 为 $\mathcal M_1$。其唯一归一最小原像分别为 $u_t,v_t$，故
$$
\boxed{\Gamma_0=1,\quad\Gamma_1=1+t^2,\quad\Gamma_2=2+4t^2,}
$$
$$
\frac{\Gamma_1^2}{\Gamma_2}
=\frac{(1+t^2)^2}{2+4t^2}\longrightarrow\infty.
\tag{7.1}
$$
$t^2=3$ 已给 $16/14>1$。

该空间不对第二个模式的删除不变，例如删除 $u_t$ 的第二模式产生含 $e_{1,0}$ 的分量，不在 $\mathcal M_1$。它不满足 (1.1)、(5.1) 的全部真实局部结构。此例严格说明：单个玻色嵌入、不变性和创建幂投影身份不足以证明首边。实际硬核联合项 $M_s$ 或全部坐标身份必须承担额外控制。

## 8. 当前实际缺口

保留的可继续接口是 (3.4)–(3.7) 的同一纤维，以及 (5.3)、(5.6)、(5.8)–(5.12) 的完整坐标行。它们都含实际 source、原 MP 正交和跨出生项。

尚未证明 (4.5)，也未把 $\mathsf K_s^*(I_N\otimes\Gamma_{1,s})\mathsf R_s$ 化成可由低出生归纳支付的同源正 Gram。(6.2) 阻止先丢交叉再对 $\mathsf K$ 作统一逆度量行界；(7.1) 阻止只用单模式玻色嵌入。原全部出生首边、全高度比较、graph $\Gamma$ 逆传播与普通 ISP 仍然开放。
