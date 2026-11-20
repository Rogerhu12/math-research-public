# R271 补录：最高方向单位因子不改变完整真核极限、辅助分级与真实能量预条件

作者：Astra-ISP-b2a9acde-20261120（root 与 r271_cost）；AI-assisted GPT-6 Astra Pro。日期：2026-11-20 UTC。状态：本条明确范围已证明。

## 0. 范围

本条先证明一个完整核结构事实：
最高 carry 的实际方向中，可逆旧头多项式因子 $U(A)$ 不改变真核极限 $F_0$。
这对全部强尾链同时成立，不限于已经解析的长链。

因此，只作旧头相似以后，完整 $F_0$ 严格保持一个辅助次数。
原物理 Galerkin 仍保全部旧头度量；该度量可在每级精确预条件，
由此得到合法的带宽/正谱界及实际源的一个定量尾界。
本条不以辅助分级冒充原物理孔分级，不把非正交 primitive 分块当正交 Galerkin。

所用输入为[完整奇高度简单极点](R271-appendix-odd-height-highest-carry-full-mp-simple-pole.md)、[完整 Galerkin 极点判据](R271-appendix-complete-galerkin-highest-carry-pole-and-cancellation-criterion.md)，以及[原883费用稿中的真实头相似和最高参考头公式](R271-appendix-odd-height-highest-carry-explicit-883-cost-and-d-sized-budget.md)。
普通 Hilbert ISP、原 $\gamma<1/16$ 源费用门仍未闭。

## 1. 原最高头及完整 Schur 映射

设旧头 $A$ 为循环幂零 $n$ 维矩阵，$n$ 偶数。
令
$$
H_t(V)=\begin{pmatrix}A&bI+tV\\0&A\end{pmatrix},
\quad b>0,\quad
C_t(V)=H_t(V)+D_R,
$$
其中 $R$ 为偶数，$D_R$ 是整个原正权 Boolean 强尾。
取奇数 $r\ge1$，
$$
X_t(V)=C_t(V)^r=X_0+tX_1(V).
$$
最高位只能通过一次，所以最后一式精确线性。
记
$$
K=\ker X_0,\qquad
F_0(V)=\lim_{t\downarrow0}\ker X_t(V).
$$
对原实际N/Y最高方向，完整奇高度结果保证全部新增秩在一阶打开，因而
$$
F_0(V)=\ker E_V,\qquad
E_V:K\longrightarrow\mathcal H/\operatorname{Ran}X_0,
\quad
E_Vv=[X_1(V)v].
\tag{1.1}
$$
使用商空间只是避免在代数恒等式中误交换非正交投影；它与物理余核Schur映射有同一个核。此时(1.1)的真核极限等式只援引在原实际方向上；对下面的规范方向，先证明Schur核的代数等式，再在第3节用相同generic维数证明其真核极限等式，避免扩大父定理范围。

## 2. 循环头的有限维交换子商

定义
$$
\mathscr L_A(V)=\sum_{j=0}^{n-1}A^jVA^{n-1-j}.
\tag{2.1}
$$
取一个真实相似 $A=WJ_nW^{-1}$，令
$$
V_\circ=WE_{n-1,0}W^{-1}.
$$
则
$$
\mathscr L_A(V_\circ)=I.
\tag{2.2}
$$

### 引理 2.1

$$
\boxed{\ker\mathscr L_A=\{[A,Z]:Z\in M_n(\mathbb C)\}.}
\tag{2.3}
$$
$\mathscr L_A$ 的像是 $A$ 的整个交换子代数，
即所有次数小于 $n$ 的多项式 $U(A)$。

**证明。** 望远镜求和给
$$
[A,\mathscr L_A(V)]=A^nV-VA^n=0,
$$
所以像在 $A$ 的交换子代数中。
循环头的交换子代数维数为 $n$；
(2.2) 以及
$\mathscr L_A(V_\circ A^k)=A^k$
给满射。
故核维数为 $n^2-n$。
另一方面
$\mathscr L_A([A,Z])=A^nZ-ZA^n=0$，
而 $\operatorname{im}\operatorname{ad}_A$ 也有维数 $n^2-n$。
两者相等。证毕。

对实际 N/Y 头，已证
$$
\mathscr L_A(V)=U(A)=\rho\,g(B)^n,\qquad
\rho=d_{m-2}^2,\quad g(z)=F(z)/z.
\tag{2.4}
$$
$g(0)\ne0$，故 $U(A)$ 可逆。
因此存在 $Z$ 使
$$
V=V_\circ U(A)+[A,Z].
\tag{2.5}
$$

## 3. 可逆单位因子不改变原完整 $F_0$

### 定理 3.1

对实际 (2.4) 的任何可逆 $U(A)$，
$$
\boxed{F_0(V)=F_0(V_\circ).}
\tag{3.1}
$$
这是原完整物理空间中的同一个子空间。
因此固定 $C_0,H_r(C_0,S),f$ 时，完整极限 Galerkin 解
$a_0$ 与原残余 $\xi_0=f-H_ra_0$ 也完全相同。

**证明。**

先去掉 (2.5) 的交换子项。
将 $Z$ 放在最高上右块，记
$$
N_Z=\begin{pmatrix}0&Z\\0&0\end{pmatrix}\otimes I.
$$
它与所有最高方向的乘积均为零，且 $N_Z^2=0$。
所以用 $I-tN_Z$ 作精确相似，恰移除 $t[A,Z]$；
没有 $t^2$ 余项。
该相似在 $t\downarrow0$ 趋于恒等，故不改变真核的物理极限。

现在只需比较 $V_\circ U(A)$ 与 $V_\circ$。
令 $\mathcal A=\operatorname{diag}(A,A)\otimes I$；
它与 $C_0,X_0$ 交换，因而在 $K$ 及商空间上诱导作用。
将 $V_\circ$ 放入最高上右块，记为 $N_\circ$。
由于最高 Boolean 项和强尾均与 $N_\circ$ 交换，
$$
[\mathcal A,N_\circ]=[C_0,N_\circ].
$$
上述交换子恒等式事实上对任何上右块方向都成立。对幂的导数求和，得到
$$
[\mathcal A,X_1(V_\circ)]
=[X_0,N_\circ].
\tag{3.2}
$$
右侧作用于 $K$ 后落入 $\operatorname{Ran}X_0$。
所以完整 Schur 映射 $E_\circ$ 是 $\mathcal A$ 的模同态：
$$
\overline{\mathcal A}E_\circ=E_\circ\mathcal A.
\tag{3.3}
$$
特别是 $\ker E_\circ$ 对 $\mathcal A$ 不变。

另一方面，因 $U(\mathcal A)$ 与 $C_0$ 交换，
$$
X_1(V_\circ U(A))=X_1(V_\circ)U(\mathcal A),
$$
从而
$$
E_U=E_\circ U(\mathcal A).
$$
$U(\mathcal A)$ 及其逆都是 $\mathcal A$ 的多项式，
都保持 $K$ 和 $\ker E_\circ$。
故 $\ker E_U=\ker E_\circ$。
最后补齐规范族真核极限的维数。任意方向的极限核总包含于该方向的 $\ker E$：若 $v_t\in\ker X_t$ 且 $v_t\to v$，则 $v\in K$，而投影到余核后 $P_{\operatorname{coker}X_0}X_1v_t=0$，取极限即可。

对 $V_\circ U(A)$，直接由(2.1)及 $A^n=0$ 得
$
H_t(V_\circ U)^{2n-1}
=\begin{pmatrix}0&t\,U(A)A^{n-1}\\0&0\end{pmatrix}\ne0
\quad(t\ne0).
$
该 $2n$ 维头因此是单一长度 $2n$ 的幂零链；$U=I$ 时亦然。实际头经前面的精确相似有同一Jordan型。加上同一个 $D_R$ 后，各非零 $t$ 的 $\ker C_t^r$ 维数完全相同，故它们的极限维数相同。交换子方向对 $E$ 的贡献是 $[X_0,N_Z]$，在 $K$ 到余核的映射中为零；上面又已证明 $\ker E_U=\ker E_\circ$。原实际方向的(1.1)于是给
$
\dim F_0(V_\circ)=\dim F_0(V)=\dim\ker E_V=\dim\ker E_\circ.
$
与一般包含关系合起来，$F_0(V_\circ)=\ker E_\circ=F_0(V)$，即(3.1)。证毕。

本条只替换用于计算同一个极限核的方向。
一般 $q_{-1}$、$q_t$ 不保持不变：
$U^{-1}$ 仍会出现在实际最高极点的逆费用中。
也没有把上面的趋恒等相似说成原 $t$ 处免费的物理等距。

## 4. 完整真核极限的准确辅助分级

仅作旧头相似
$$
\mathcal W=\operatorname{diag}(W,W)\otimes I_{\rm strong}.
$$
在新坐标中，规范退化算子是
$$
C_\circ=J_n+bE_{\rm high}+D_R.
\tag{4.1}
$$
定义辅助次数
$$
q=(\text{旧 Jordan 坐标 }0,\ldots,n-1)
+(\text{最高位孔 }0,1)+(\text{强尾孔数}).
\tag{4.2}
$$
$C_\circ$ 严格降一级。
规范最高方向（最高位降低一次、旧Jordan级从零升到$n-1$）升 $n-2$ 级，
故 $X_1(V_\circ)$ 改变辅助级恰为 $n-r-1$。

$\ker C_\circ^r$ 与标准余核均保持辅助级；
完整 Schur 映射是齐次的。
因此由定理 3.1，
$$
\boxed{
F_\circ:=\mathcal W^{-1}F_0
\text{ 在辅助次数 }q\text{ 下严格分级。}
}
\tag{4.3}
$$
于是标准正交投影 $P_{F_\circ}$ 与辅助级投影交换。

这里没有对原物理 $P_{F_0}$ 作相同断言。
$\mathcal W$ 不是酉变换；原物理度量必须保留在下一节。

## 5. 原完整 Galerkin 的分级能量预条件

记
$$
G=\mathcal W^*\mathcal W=(W^*W)\otimes I.
$$
原 $a_0=\mathcal Wa_\circ$，而完整方程恰为
$$
K_G a_\circ=P_{F_\circ}\mathcal W^*f,
$$
$$
K_G=
P_{F_\circ}
\sum_{j=0}^{r-1}
\frac{(C_\circ^*)^jGC_\circ^j}{j!S^j}
\bigg|_{F_\circ}.
\tag{5.1}
$$
这包含全部强尾物理 Gram 混合项。
没有按 primitive 拆 Galerkin。

可选任意正的旧 Jordan 对角度量 $D$，再张量所有其它位的恒等。
它保持辅助级。定义真正的分级参考能量
$$
K_D=
P_{F_\circ}
\sum_{j=0}^{r-1}
\frac{(C_\circ^*)^jDC_\circ^j}{j!S^j}
\bigg|_{F_\circ}.
\tag{5.2}
$$
因 $D>0$，$K_D>0$，且 $K_D^{\pm1/2}$ 保辅助级。

令
$$
\alpha=\lambda_{\min}(D^{-1/2}GD^{-1/2}),\qquad
\beta=\lambda_{\max}(D^{-1/2}GD^{-1/2}).
$$
逐项正形式比较给
$$
\alpha K_D\le K_G\le\beta K_D.
$$
所以真实预条件算子
$$
\boxed{\mathcal A_D=K_D^{-1/2}K_GK_D^{-1/2}}
\tag{5.3}
$$
满足
$$
\boxed{\alpha I\le\mathcal A_D\le\beta I,}
\tag{5.4}
$$
与 $S,R$ 无关。

$G$ 只混合旧头的 $n$ 个 Jordan 坐标。
故 (5.3) 的辅助级带宽至多
$$
w=n-1.
\tag{5.5}
$$
压缩投影及预条件都保级，因而没有隐藏的投影带宽缺口。
选择 $D=I$ 恢复完整 $\kappa(W)^2$ 条件数上界；
选择其它 $D$ 则把保级幅度变化精确保留在每级能量中。

## 6. 一个真实、全 $S,R$ 的辅助尾界

原本支 forcing 的确切定义来自
[原完整来源定义](R271-appendix-dual-tower-kernel-only-error-pure-far-height-representatives-and-joint-reciprocal-budget.md)
§1：
$f_1=e_1\otimes\Omega$，$Ce_1=e_0$、$Ce_0=0$。
这里的 $e_1$ 是最低整数坐标，不是任意一孔 $e_{2^j}$。

$\mathcal W^*f_1$ 只在旧头中变化，辅助级不超过 $n-1=w$。
(4.3)、(5.2) 保证预条件右端仍支撑于 $q\le w$。

置
$$
\chi=\sqrt{\beta/\alpha},\qquad
\vartheta=\frac{\chi-1}{\chi+1}\in[0,1).
\tag{6.1}
$$
对次数 $k$ 的 Chebyshev 逆逼近 $p_k$，有
$$
\|\mathcal A_D^{-1}-p_k(\mathcal A_D)\|
\le\frac2\alpha\vartheta^{k+1}.
\tag{6.2}
$$
这是直接有限区间证明：
取归一 Chebyshev 剩余多项式 $R_{k+1}$，
令 $p_k(x)=(1-R_{k+1}(x))/x$；
$\sup|R_{k+1}|\le2\vartheta^{k+1}$，再除以 $x\ge\alpha$。
$\alpha=\beta$ 时算子是标量，尾项直接为零。

由带宽，$p_k(\mathcal A_D)$ 作用于右端后的支撑至多 $(k+1)w$。
此外
$$
\|\mathcal W K_D^{-1/2}\|\le\sqrt\beta,
$$
因为 $G$ 是 (5.1) 的 $j=0$ 正项，且 $K_G\le\beta K_D$。
右端的范数也至多 $\sqrt\beta\|f_1\|$。
强尾孔数不超过辅助次数，且 $\mathcal W$ 不动强尾。
因此整个物理 Galerkin 解满足
$$
\boxed{
\|P_{\rm strong>(k+1)w}a_0\|
\le2(\beta/\alpha)\vartheta^{k+1}\|f_1\|.
}
\tag{6.3}
$$

令
$$
h=\sum_{j=0}^{r-1}\frac{\|C_0\|^{2j}}{j!S^j}.
$$
每项 $(C_0^*)^jC_0^j$ 至多改变 $j$ 个强尾孔。
原残余 $\xi_0=f_1-H_ra_0$ 因而满足
$$
\boxed{
\|P_{\rm strong>(k+1)w+r-1}\xi_0\|
\le2h(\beta/\alpha)\vartheta^{k+1}\|f_1\|.
}
\tag{6.4}
$$
这是实际 $S$、实际全部强权、完整物理 $F_0$ 的界，
不是固定参数 Taylor 阶数。

例如，若 $\gamma\in(0,1]$ 满足
$$
\vartheta\gamma^{-w}<1,
\tag{6.5}
$$
则按每 $w$ 个强孔分块、再用总物理头孔至多 $m$，得到
$$
\begin{aligned}
\left\|\sum_{g\ge0}\gamma^{1-g}P_g\xi_0\right\|^2
\le\ &\gamma^{4-2m-2w-2r}\|f_1\|^2\\
&\cdot\left[
(h+1)^2+
\frac{4h^2(\beta/\alpha)^2
(\vartheta\gamma^{-w})^2}
{1-(\vartheta\gamma^{-w})^2}
\right].
\end{aligned}
\tag{6.6}
$$
所需高孔源 $\mathcal Z_\gamma$ 只是一部分，故也受 (6.6) 控制。

仅代入 R239 的完整相似上界，会使允许的 $\gamma$ 非常接近 $1$，
目前不能把 (6.6) 用到高孔费用门所需的 $\gamma<1/16$。
必须进一步估计真正的跨级度量或利用原特定右端；本条不把整体条件数的粗界称为最优障碍。

## 7. 保级对角缩放不能自动删除全部混级成本

下面是 R239 显式链相似本身的准确小头检验。
原 N 四头
$$
A_t=\begin{pmatrix}
0&1&b&0\\0&0&t&b\\0&0&0&1\\0&0&0&0
\end{pmatrix},\qquad b=\tfrac14.
$$
其真实伴随链 $K e_j=(A_t^*)^j e_0$ 给
$$
K=
\begin{pmatrix}
1&0&0&0\\
0&1&0&0\\
0&b&t&0\\
0&0&2b&t
\end{pmatrix},
\qquad W=K^{-*}.
$$
$W$ 的第 $2,3$ 列（省去共同零坐标）为
$$
w_2=t^{-1}(-b,1,0),\qquad
w_3=t^{-2}(2b^2,-2b,t).
$$
归一后的相关系数满足
$$
\boxed{
\rho^2=\frac{4b^2(1+b^2)}{4b^2(1+b^2)+t^2}
=\frac{17/64}{17/64+t^2}.
}
\tag{7.1}
$$
任何对角列缩放都不改变 $|\rho|$。
这两列的归一 Gram 条件数为
$$
\frac{1+|\rho|}{1-|\rho|}
\ge\frac{17}{64}\,t^{-2}.
\tag{7.2}
$$
更一般的不等幅对角缩放只会增加这个两列 Gram 的最小可能条件数。

所以这条显式真实相似的坏条件数，并非全是保级对角幅度；
其中确有跨级列趋平行的物理成本。
逆芽在一个小解析圆盘接近线性，不能免费解释为原物理相对混级接近恒等。

(7.1)–(7.2) 只限制上述自动简化。
它不否定更细的块预条件、保留低 core 的完整能量、
或利用原 forcing 不激发某些坏方向的源专属改进。
本条的实际未闭门仍是 $\gamma<1/16$ 下可支付的原完整 $\mathcal Z_\gamma$。
