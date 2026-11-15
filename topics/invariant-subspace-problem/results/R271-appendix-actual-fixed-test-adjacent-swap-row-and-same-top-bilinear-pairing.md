# R271 附录：真实固定测试的完整相邻交换行预算与同顶部双线性配对

日期：2026-11-15（UTC）。

作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro。

状态：**已证明。** 本文把[相邻权配平的完整物理投影比较](R271-appendix-adjacent-strong-weight-balancing-and-complete-symmetric-source-schur.md)逐对应用于同一个原模型、同一个固定低位测试，然后对所有相邻对求平方和。得到真实投影输出上的完整交换行能量 $O(1/x)$，并且对全部孔层同时求和、对所有窗口 $Q$ 一致。各对可以重叠；证明不建立同时配平全部对的相似，也不使用其全空间条件数。

第二部分保同一实际顶部，证明固定测试端与原 $w$ 端的准确双线性恒等式及其非零左锚。它给下一联合估计一个已支付的测试端行量；没有宣称顺次 MP、完整返回投影或整个负型已经受该行量控制。

## 1. 原物理空间与单对变形

保原有限头 $A_m$，在其外使用原尾
$$
D_m=\sum_{j\ge m}b_jE_j,\qquad b_j=(j+1)^{-2},\qquad
L_m=A_m+D_m.
\tag{1.1}
$$
所有空间及正交投影均采用原物理内积。

对尾内一对相邻位 $(j,j+1)$，令 $U_j$ 为交换这两个位的物理酉反射，并置
$$
P_j^+=\frac{I+U_j}{2},\qquad P_j^-=\frac{I-U_j}{2}.
\tag{1.2}
$$
本稿的 $P_j^-$ 是交换的反对称正交投影，不是后文顺次 MP 投影。

记 $t=j+1$，把这一对的权换为几何平均 $1/[t(t+1)]$，其他原权全部保持不变。对角正算子
$$
S_j=\operatorname{diag}\left(1,\frac{t}{t+1},\frac{t+1}{t},1\right)
$$
只作用于该对，准确满足
$$
L_mS_j=S_j\widetilde L_m.
\tag{1.3}
$$
在交换对称扇区上，
$$
P_j^+S_j^{\pm1}P_j^+\succeq P_j^+,\qquad
P_j^+S_j^{\pm2}P_j^+\preceq
\cosh(2\vartheta_j)P_j^+,\qquad
\vartheta_j=\log\frac{j+2}{j+1}.
\tag{1.4}
$$

设 $\mathscr E$ 为原模型的一个闭物理空间，且单对配平后有闭空间 $\widetilde{\mathscr E}$，满足
$$
\mathscr E=S_j\widetilde{\mathscr E},\qquad
P_{\widetilde{\mathscr E}}P_j^+
=P_j^+P_{\widetilde{\mathscr E}}.
\tag{1.5}
$$
前稿完整 nuisance 变形引理给
$$
\|(P_{\mathscr E}-P_{\widetilde{\mathscr E}})P_j^+\|
\le\sqrt{\cosh(2\vartheta_j)-1}.
\tag{1.6}
$$
若 $f=P_j^+f$，配平投影的输出也对称，故
$$
\boxed{
\|P_j^-P_{\mathscr E}f\|^2
\le(\cosh(2\vartheta_j)-1)\|f\|^2
=2\sinh^2(\vartheta_j)\|f\|^2
\le\frac{2}{(j+1)^2}\|f\|^2.
}
\tag{1.7}
$$
最后用
$$
\sinh\log(1+1/t)
=\frac{2t+1}{2t(t+1)}\le\frac1t.
$$
(1.6) 来自真正正交投影和完整 Schur 最小化；(1.7) 没有删去反对称源或先压缩再取逆。

## 2. 可用的真实投影及准确量词

(1.5) 适用于前稿已经逐个证明像关系的原空间，包括
$$
K_{m,Q}=\ker L_m\cap\mathcal H_{\mathrm{tail}\le Q},
$$
$$
V_{m,Q}=
\{v\in\mathcal H_{\mathrm{tail}\le Q}:
P_{\mathrm{tail}<Q}L_mv=0\}.
\tag{2.1}
$$
这里是原 $m$ 之后的总尾孔数，任意尾内交换均保持它。

在强位并头写法
$$
C=A_m+D_<,\qquad D=D_>,\qquad h=2^m+R,\qquad x=m+R,
\tag{2.2}
$$
若所选对满足 $j\ge x$，它完全位于远尾，$C$ 保持不变。相同结论也适用于真实远孔左空间 $V_p^C$、有限真核 $K_p^C$，以及已有闭和定义的物理 joined 空间 $\mathscr M_p$。原因是 $S_j$ 与相关孔截断、全部原头旗交换，并逐幂交织远尾 $D$ 的核旗；配平后的空间被 $U_j$ 约化。若使用嵌套投影之差，则下节分别对两个完整物理投影估计。

本稿不把源坐标中的任意正交补、经过 Riordan 逆伴随后又取投影的空间，自动列入 (1.5)。对这些额外对象仍须另证准确像关系或保留完整投影。

固定整数 $x\ge m$、$x\ge1$，令输入 $f$ 在第 $x$ 位及其后的尾为真空。特别，任意固定有限物理测试，在 $m$ 超过其位支撑后可用于所有 $x\ge m$。于是 $P_j^+f=f$ 对每个 $j\ge x$ 同时成立。

## 3. 所有相邻对与全部孔层的共同平方和

定义非负交换行形式
$$
\mathfrak e_x(v)
=\sum_{j\ge x}\|P_j^-v\|^2.
\tag{3.1}
$$
该和可为无穷。其定义域是相应行算子进入 Hilbert 直和的自然域；也可把它读成有限部分和的单调极限。

对 (2.1)–(2.2) 中任何满足上述条件的单个原物理投影，直接对 (1.7) 求和，得
$$
\boxed{
\mathfrak e_x(P_{\mathscr E}f)
\le2\sum_{j\ge x}(j+1)^{-2}\|f\|^2
\le\frac2x\|f\|^2.
}
\tag{3.2}
$$
这里每次只配平一对，其余原权不变，所以所有被估计的左端都是同一个原 $P_{\mathscr E}f$。相邻对重叠并不影响非负平方和；没有将不同配平模型的输出相加。

令
$$
U_{m,Q}=P_{V_{m,Q}}-P_{K_{m,Q}},\qquad u_f=U_{m,Q}f.
\tag{3.3}
$$
$K_{m,Q}\subset V_{m,Q}$，所以 $U_{m,Q}$ 是真实正交投影。在行 Hilbert 空间内用三角不等式和 (3.2)，得到
$$
\boxed{
\mathfrak e_x(u_f)\le\frac8x\|f\|^2.
}
\tag{3.4}
$$
相同常数适用于远孔实际 top $P_{V_p^C}-P_{K_p^C}$，以及已付嵌套物理投影之差。所有界对 $Q,p$、原源出生、头维数和强位数一致。

若采用 (2.2) 且 $u_{f,n}$ 为第 $n$ 个远孔分量，所有 $P_j^-$、$j\ge x$ 与远孔投影交换。因此对任意孔数集合 $I$，
$$
\boxed{
\sum_{n\in I}\sum_{j\ge x}
\|P_j^-u_{f,n}\|^2
\le\frac8x\|f\|^2.
}
\tag{3.5}
$$
这是对全部输出孔层一起支付的预算，不是每层估计后再乘一个 $Q$。

另取任意有限个互不相交的相邻对集合 $\mathcal F\subseteq\{j:j\ge x\}$。其 $P_j^-$ 互相对易。令
$$
N_{\mathcal F}=\sum_{j\in\mathcal F}P_j^-,
\qquad
\Pi_{\mathcal F,\ge r}=\mathbf1_{[r,\infty)}(N_{\mathcal F})
\quad(r\ge1).
$$
谱不等式 $N_{\mathcal F}\succeq r\Pi_{\mathcal F,\ge r}$ 给真正投影后局部化：
$$
\boxed{
\|\Pi_{\mathcal F,\ge r}u_f\|^2
\le\frac8{rx}\|f\|^2.
}
\tag{3.6}
$$
本式不要求 $U_{m,Q}$ 与这些交换投影对易，也不要求它保持孔数或 primitive 出生。

## 4. 同一实际顶部的准确双线性恒等式

仍保 (2.2)，取同一个合法 $Q$。对任意物理输入 $w,f$，置
$$
u_w=U_{m,Q}w,\qquad u_f=U_{m,Q}f.
\tag{4.1}
$$
两者都满足同一个左低方程、同一个总尾支撑上界，并都正交于整个 $K_{m,Q}$；不要求 $f\in W$。

记远孔分量为 $u_{z,n}$，$z=w,f$。对 $p+h+R<Q$，原同顶部源流给
$$
r_{z,p}=Cu_{z,p}=-Du_{z,p+1},\qquad
U_p^C r_{z,p}=P_{\mathrm{far}\le p}u_z.
\tag{4.2}
$$
这里 $U_p^C r$ 表示该源的真实左最小列，与 (3.3) 的顶部正交投影按上下文区分。

在固定孔层定义有界完整单步 MPs $Q_n=D_n^\dagger$，以及顺次投影
$$
\mathcal P_{n,j}
=Q_nQ_{n-1}\cdots Q_{n-j+1}D^j
\quad(1\le j\le h).
\tag{4.3}
$$
用 $f$ 端的同一个真实源构造完整右候选
$$
c_{f,p,j}
=Q_{p+j}\cdots Q_{p+1}(-C)^{j-1}r_{f,p}
=-\mathcal P_{p+j,j}u_{f,p+j}.
\tag{4.4}
$$
它是前稿的同一合法顺次链：$Dc_1=r_{f,p}$、
$Cc_j+Dc_{j+1}=0$、$c_h=0$，且全部头旗满足
$C^{h-j+1}c_j=0$。例如最后一个断言左端准确等于
$$
(-1)^{j-1}Q_{p+j}\cdots Q_{p+1}C^h r_{f,p}
=(-1)^{j-1}Q_{p+j}\cdots Q_{p+1}C^{h+1}u_{f,p}=0.
$$
没有省略该处的一次 $C$。

把左列 $P_{\mathrm{far}\le p}u_f$ 与右侧 $-c_{f,p}$ 拼合，得到原真核向量；其总尾支撑不超过 $p+h+R<Q$。它因此属于 $K_{m,Q}$。以 $u_w\perp K_{m,Q}$ 配对，得到完整复数恒等式
$$
\boxed{
\left\langle
P_{\mathrm{far}\le p}u_w,
P_{\mathrm{far}\le p}u_f
\right\rangle
=
-\sum_{j=1}^{h}
\langle u_{w,p+j},\mathcal P_{p+j,j}u_{f,p+j}\rangle.
}
\tag{4.5}
$$
采用相反的内积线性约定时两边同时取共轭。此式始终把顺次候选放在 $f$ 端，没有交换原最小化或改动 $w$ 端的来源。

对 $a\le p\le b$ 求和，并保
$$
\mathscr A_n
=\sum_{\substack{1\le j\le h\\a\le n-j\le b}}\mathcal P_{n,j},
$$
得到
$$
\boxed{
\sum_{p=a}^{b}
\left\langle
P_{\mathrm{far}\le p}u_w,
P_{\mathrm{far}\le p}u_f
\right\rangle
=
-\sum_{n=a+1}^{b+h}
\langle u_{w,n},\mathscr A_nu_{f,n}\rangle.
}
\tag{4.6}
$$
两端 partial sums 与内部完整和全在同一个 $\mathscr A_n$ 中。这里的 $\mathcal P_{n,j}$ 是顺次 MP 幂等算子，与 (1.2) 的交换投影 $P_j^-$ 严格不同。

## 5. 固定有限测试仍保原非零左锚

现在令 $0\ne w\in W$，并使用原已付合法母窗口。取一个固定有限物理向量 $f$，满足
$$
\|f-w\|\le\frac18\|w\|.
\tag{5.1}
$$
这样的 $f$ 一次选定；随后 $m,Q$ 改变时不再换它。

在原同源源流窗口内，记已付、对 $a\le p\le b$ 一致的物理近似误差为
$$
\|P_{\mathrm{far}\le p}u_w-w\|\le\varepsilon_m\|w\|,
\qquad \varepsilon_m\longrightarrow0.
\tag{5.2}
$$
例如前述晚窗口的实际尾范数加母误差正给出该 $\varepsilon_m$。它只作用于原同一个 $w$，没有乘未付逆。

因为 $U_{m,Q}$ 与远孔截断都是收缩，
$$
\|P_{\mathrm{far}\le p}(u_f-u_w)\|
\le\|f-w\|\le\frac18\|w\|,
\qquad
\|P_{\mathrm{far}\le p}u_w\|\le\|w\|.
$$
取充分大 $m$ 使 $\varepsilon_m\le1/4$，由 Cauchy--Schwarz，
$$
\operatorname{Re}
\left\langle
P_{\mathrm{far}\le p}u_w,
P_{\mathrm{far}\le p}u_f
\right\rangle
\ge
\left(\frac34\right)^2\|w\|^2-\frac18\|w\|^2
=\frac7{16}\|w\|^2.
\tag{5.3}
$$
同时 $m$ 可越过固定 $f$ 的全部位支撑，所以 (3.4)–(3.6) 对这个同一个 $u_f$ 适用。特别 (4.6) 的右端是一个实际双线性强迫量，其左端至少为
$$
\frac7{16}(b-a+1)\|w\|^2,
$$
而测试端具有真正 $Q$ 一致的全部交换行能量 $8\|f\|^2/x$。

## 6. 已付正预算与未付联合步骤

本文已经支付：

- 完整原物理投影后的全部相邻交换行能量，且所有孔层一起求和；
- 真实 top/gap 上的同一预算，以及高反对称计数的准确谱截断；
- 与同一个实际 $u_w$ 共享全部约束的 $u_f$ 端，以及完整双线性源流等式和非零左锚。

但 (3.5) 尚未控制 $\mathscr A_nu_{f,n}$。顺次 MP 一般不与交换投影对易，也不能把原权的物理正交投影换成配平模型中的某个压缩逆。因此本文没有从低交换行能量推出整个负型上界。

特别，前两稿的大负方向含大量近暗对，只说明这个新行量能识别一种实际危险结构；它不是对全部负谱空间的支配证明。下一联合问题准确保留为 (4.6) 右端，其中 $u_w$ 仍是原同一来源，$u_f$ 仍是原真实投影，全部 $\mathscr A_n$ 和边界项都未删除。普通 ISP 与原 $N=M$ 仍为 OPEN。
