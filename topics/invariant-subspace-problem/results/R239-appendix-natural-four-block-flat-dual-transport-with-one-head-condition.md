# R239 附录：天然四块模型的同一原平坦对偶运输与一次头条件数

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065 / boundary_nonprimitive_1856；AI-assisted，GPT-6 Astra Pro。

状态：原完整测试核的同域比较、四块头的一次条件数、同一原 $(v,c^\flat)$ 的误配及模型天然平坦向量的 Riesz 运输均已证明。本文完成前稿留出的平坦费用运输，但没有证明天然四块模型所需的温和两费用比较，普通 ISP 与 $N=M$ 仍为 OPEN。

依赖：[四块头比较](R239-appendix-four-block-head-comparison-and-quarter-depth-source-elimination.md)与[天然零源旗/裸链运输](R239-appendix-natural-four-block-free-flag-and-bare-chain-transport.md)。下文保留它们的全部原头、原尾、原 $q$ 和天然模型源；不会由两项二次形近似直接推出平坦费用。

## 1. 必须保留的锐小量及扩大后的 primitive 域

固定
$$
m\ge8,\quad d=2^m,\quad p=d/4,\quad4d\le q\le e^{d^3/4}.
$$
令 $A=A_m$，$A_\square$ 为四块比较头，$D=D_m$，
$\nu=\|D_m\|\le1/m$。

本稿使用下列明确上界，而非把粗 $e^{-d^4/20}$ 直接乘头条件数：
$$
\boxed{
\rho=
216\,\eta_{m-3}(2048q^2)^3dp(p+1)^2
e^{11d^4/40}.
}
\tag{1.1}
$$
此前证明给 $\rho\le e^{-d^4/20}<1$，以及对 primitive 输入孔数 $\le q$ 的完整延拓差不超过 $\rho$。

完整对偶测试还含右侧 $q+j$ 的 primitive 输入。本稿直接将共同输入上界增到 $q+d$，最大原像阶仍为 $d-1$。对应常数为
$$
\mathcal L_{\rm ext}
=512\sqrt{q+3d-1}(m+q+3d-1)^{3/2}.
$$
因为 $q\ge4d$、$m\le d$，
$$
q+3d-1\le7q/4,\qquad m+q+3d-1\le2q,
$$
所以
$$
\boxed{
\mathcal L_{\rm ext}\le512\sqrt{7/4}\,2^{3/2}q^2
=512\sqrt{14}\,q^2<2048q^2.
}
\tag{1.2}
$$
原四次卷积预算因而完全保留，得到
$$
\boxed{
\|\mathcal E_A^{\rm full}-\mathcal E_\square^{\rm full}\|
\le\rho
}
\tag{1.3}
$$
于所有头、所有 primitive 输入孔数 $\le q+d$ 的原直和上。没有把 $q+d$ 当成满足原上窗的新参数。

## 2. 四块高二位的精确 3⊕1 相似

记 $b=(m-1)^{-2},c=m^{-2}$，高二位算子
$D_{\rm hi}=bE_0+cE_1$。按物理四基定义
$$
u_0=e_0,\qquad
u_1=\frac{e_1}{2b}+\frac{e_2}{2c},\qquad
u_2=\frac{e_3}{2bc},\qquad
u_*=\frac{e_1}{2b}-\frac{e_2}{2c}.
$$
直接计算给
$$
D_{\rm hi}u_1=u_0,\quad
D_{\rm hi}u_2=u_1,\quad D_{\rm hi}u_0=D_{\rm hi}u_*=0.
$$
以这四列为 $S_{\rm hi}$，则
$$
D_{\rm hi}=S_{\rm hi}(J_3\oplus0)S_{\rm hi}^{-1}.
\tag{2.1}
$$
其中间二列块的奇异值为 $1/(\sqrt2b)$、$1/(\sqrt2c)$，
另两列的奇异值为 $1$、$1/(2bc)$。在当前 $m\ge8$，
$$
\boxed{\kappa(S_{\rm hi})=\frac1{2bc}
=\frac{m^2(m-1)^2}{2}.}
\tag{2.2}
$$
这是原二高位的全部非正交费用。

原低头的同一个无缩放相似满足
$$
A_{m-2}=V_{m-2}J_pV_{m-2}^{-1},\qquad
\boxed{\kappa(V_{m-2})\le e^{221d^4/4096}.}
\tag{2.3}
$$
至此原头条件数只出现一次。

## 3. Jp 加 J3 的明确可支付 Jordan 化

对 $h\ge2$ 定义正对角
$$
D_he_j=
\sqrt{\frac{(h-1-j)!}{j!(h-1)!}}\,e_j,\qquad0\le j<h.
$$
则
$$
L_h=D_hJ_hD_h^{-1},\qquad
L_he_j=\sqrt{j(h-j)}\,e_{j-1},\qquad
\kappa(D_h)=(h-1)!.
\tag{3.1}
$$

说明所需正交分解而不隐藏额外条件数。令
$H_he_j=(h-1-2j)e_j$，则
$[L_h,L_h^*]=H_h$、$[H_h,L_h]=2L_h$。
在 $\mathbb C^p\otimes\mathbb C^3$ 中，两个张量因子的和仍满足这些关系。
总次数零的最高权向量生成长度 $p+2$ 的串；其正交补同时不变于
$L,L^*,H$。总次数一的权空间维数为二，扣掉第一串后留下最高权
$p-1$ 的一个向量，生成长度 $p$ 的串；再在总次数二的三维权空间中扣掉前两串，留下最高权 $p-3$ 的一串，长度为 $p-2$。三个长度之和为 $3p$。

以上串的归一化系数由
$$
\|(L^*)^jv\|^2
=j!\,\ell(\ell-1)\cdots(\ell-j+1)\|v\|^2
$$
直接从交换子归纳得到，其中 $\ell$ 是该最高权。故三串正交后，其降低系数正是 (3.1)，不是未经付费的任意 Jordan 相似。因此存在酉 $U$ 使
$$
L_p\otimes I_3+I_p\otimes L_3
=U(L_{p+2}\oplus L_p\oplus L_{p-2})U^*.
$$
用 (3.1) 在两端还原到无缩放 Jordan 块，得到
$$
J_p\otimes I_3+I_p\otimes J_3
=S_T(J_{p+2}\oplus J_p\oplus J_{p-2})S_T^{-1},
$$
$$
\boxed{\kappa(S_T)\le2(p-1)!(p+1)!.}
\tag{3.2}
$$
将 $S_T$ 乘一个标量，使其范数和逆范数相等后，与剩余的 $J_p$ 暗块作直和，不增加 (3.2) 的条件数。

结合 (2.2)–(2.3)，存在原四块头相似 $S_\square$，把 $A_\square$ 化为
$J_{p+2}\oplus J_p\oplus J_{p-2}\oplus J_p$，并有
$$
\boxed{
\kappa(S_\square)\le K_\square
:=m^2(m-1)^2(p-1)!(p+1)!\,e^{221d^4/4096}.
}
\tag{3.3}
$$
尤其不是 $\kappa(V_{m-2})^2$。

## 4. 模型左费与其完整右费只需一次条件数

本文模型右链始终使用同一个物理宽度 $d$ 联合旗。只考虑首源属于模型天然源空间 $\mathscr R_\square$ 的完整右链；这是闭子空间，首输出映射记为
$$
F_\square:\mathscr C_\square\longrightarrow\mathscr R_\square.
$$
它满射：任一模型左源的规范完整右链已经由前稿构造。固定参数下其最小右逆有界。记
$$
\mathscr U_\square=\operatorname{Ran}F_\square^*,\qquad
c_\square(f)=F_\square^\dagger f,\qquad
\lambda_\square(f)=\|c_\square(f)\|.
\tag{4.1}
$$
只限制源空间，没有删除物理右链中的高出生自由部分。

无缩放 Jordan 头的天然源旗允许显式左原像
$$
(v_f)_{q-j}=(-1)^j(J^*)^{j+1}D^jf.
$$
每块的尾核阶使所有有限端点合法；$\|J^{*k}\|\le1$ 与不同孔层正交给
$\|v_f\|\le(1-\nu^2)^{-1/2}\|f\|$。
变回原头，真正模型左最小费满足
$$
\mu_\square(f)\le
\frac{K_\square}{\sqrt{1-\nu^2}}\|f\|.
$$
任何完整右链的首段都解 $Dc_1=f$，所以
$\lambda_\square(f)\ge\|f\|/\nu$。因此
$$
\boxed{
\mu_\square(f)\le M_\square\lambda_\square(f),
\qquad
M_\square=\frac{\nu K_\square}{\sqrt{1-\nu^2}}
\le K_\square.
}
\tag{4.2}
$$
这里使用相似只为这个左/右测试范数比较。没有把模型右旗与 Jordan 右旗作未经证明的单位识别。

## 5. 完整模型测试核的全部右 primitive 都保留

取任意 $f\in\mathscr R_\square$，令
$$
u_\square(f)=E_{\square,q}^\dagger f,\qquad
c=c_\square(f)\in\mathscr U_\square,
$$
并在左右物理孔层的直和中定义
$$
k_\square=u_\square(f)-c.
$$
它是整个 $(A_\square+D_m)$ 的真核，支持于 $\le q+d$。记
$a_k=P_0k_\square$。其左 primitive 输入可在任何 $\le q$ 孔层，而其右第 $q+j$ 孔层 primitive 头不超过 $d-j$。

完整 Taylor 递推给
$$
k_\square=\mathcal E_\square^{\rm full}a_k.
$$
令
$$
k_A=\mathcal E_A^{\rm full}a_k.
$$
它属于原 $(A_m+D_m)$ 的真核，且仍支持于 $\le q+d$：右第 $q+j$ 层 primitive 头最多为 $d-j$，故施加原严格降头 $A_m^n$ 超过 $d-j$ 次即为零。其每个右输出亦在原联合旗中：来自右第 $j$ 层的第 $n$ 次提升位于段 $j+n$，头最多 $d-j-n$，尾核阶至多 $n+1\le j+n$；来自左输入的项与前稿相同。

因此 $k_A$ 是原左右配对真正允许的测试核，而不是可能越出第 $d$ 段的环境核。由 (1.3)，
$$
\boxed{
\|k_A-k_\square\|\le\rho\|a_k\|
\le\rho\|k_\square\|
=\rho\sqrt{\mu_\square(f)^2+\lambda_\square(f)^2}.
}
\tag{5.1}
$$
特别 (4.2) 给
$$
\|k_A-k_\square\|
\le\rho\sqrt{1+M_\square^2}\,\|c\|.
\tag{5.2}
$$
这一步包含全部右 primitive $q+j$，没有只比较规范左坐标。

## 6. 同一个原 (v,cflat) 的准确误配

取原源 $r$，记
$$
v=E_q^\dagger r,\qquad
c^\flat=F_{\rm flag}^*J_q^{-1}r,\qquad
\mu=\|v\|,\qquad\lambda=\|c^\flat\|.
$$
原准确双配对说明 $(v,c^\flat)$ 与每个上节的 $k_A$ 正交，所以
$$
\begin{aligned}
\left|\langle v,u_\square(f)\rangle
-\langle c^\flat,c_\square(f)\rangle\right|
&=|\langle(v,c^\flat),k_\square-k_A\rangle|\\
&\le
\rho\sqrt{\mu^2+\lambda^2}\sqrt{1+M_\square^2}\,\|c\|.
\end{aligned}
\tag{6.1}
$$

沿天然模型零源旗稿，对同一个 $r$ 做 $\mathscr Y$ 左 Schur，得到
$r_{\rm cut}$、模型天然源 $g=\mathcal B_\square x$ 及其最小左向量
$v_\square=E_{\square,q}^\dagger g$。把该稿中的粗小量换成实际同一个 $\rho$，有
$$
\|v-v_\square\|
\le\rho\lambda+3\rho(1+\rho)\mu.
\tag{6.2}
$$
因此对任意上节测试 $f$，
$$
\begin{aligned}
\left|\langle v_\square,u_\square(f)\rangle
-\langle c^\flat,c_\square(f)\rangle\right|
\le{}&
\bigl[
\rho\sqrt{1+M_\square^2}\sqrt{\mu^2+\lambda^2}\\
&+M_\square(\rho\lambda+3\rho(1+\rho)\mu)
\bigr]\|c_\square(f)\|.
\end{aligned}
\tag{6.3}
$$
所有右侧仍是原同一个 $r$ 的 $v,c^\flat$；没有使用未知的
$c^\flat(r_{\rm cut})$。

## 7. 在正确测试空间中的 Riesz 结论

模型天然平坦向量定义为
$$
c_\square^\flat(g)=F_\square^*J_{\square,q}^{-1}g
\in\mathscr U_\square.
$$
对每个 $c=c_\square(f)\in\mathscr U_\square$，
$$
\langle c_\square^\flat(g),c\rangle
=\langle v_\square,u_\square(f)\rangle.
$$
而 $f\mapsto c_\square(f)$ 到整个闭空间 $\mathscr U_\square$ 为同构。
故 (6.3) 的 Riesz 结论为
$$
\boxed{
\begin{aligned}
\|c_\square^\flat(g)-P_{\mathscr U_\square}c^\flat(r)\|
\le{}&
\rho\sqrt{1+M_\square^2}\sqrt{\mu^2+\lambda^2}\\
&+\rho M_\square\lambda
+3\rho(1+\rho)M_\square\mu.
\end{aligned}}
\tag{7.1}
$$
$P_{\mathscr U_\square}$ 是同一物理右带中的正交投影，故范数不超过一。
这就是所需平坦运输。没有从 $J$ 或 $G$ 的非交换二次形近似推断
$GJ^{-1}$ 近似，也没有假定两个裸投影接近。

## 8. 锐指数确实支付一次 Ksquare

由 (1.1)、(3.3) 和原 $\log\eta_{m-3}$，
$$
\begin{aligned}
\log(\rho K_\square)
\le{}&
-\frac{263}{20480}d^4+\frac{699}{256}d^3-\frac{75}{2}d\\
&+\log\!\bigl[
216\,2048^3dp(p+1)^2m^2(m-1)^2(p-1)!(p+1)!
\bigr].
\end{aligned}
\tag{8.1}
$$
主项的准确相减是
$$
\frac{171}{2560}-\frac{221}{4096}
=\frac{263}{20480}.
$$
最后的对数对 $d\ge256$ 小于 $d^2$。例如用
$(p-1)!(p+1)!\le d^{d/2+2}$、全部多项式因子至多常数乘 $d^8$，
以及 $\log d\le d/4$ 即可。

因此
$$
\frac{263}{20480}-\frac{699}{256d}-\frac1{d^2}
\ge
\frac{263}{20480}-\frac{699}{65536}-\frac1{65536}
>\frac1{500}.
$$
保留的线性项为负，遂得
$$
\boxed{\rho K_\square\le e^{-d^4/500}.}
\tag{8.2}
$$
由于 $M_\square\le K_\square$、$K_\square\ge1$、$\rho<1$，
(7.1) 的右侧至多为
$8\rho K_\square(\mu+\lambda)$。而
$8e^{-d^4/500}\le e^{-d^4/600}$（$d\ge256$）。
置
$$
\sigma=e^{-d^4/600}.
$$
得到可直接使用的
$$
\boxed{
\|c_\square^\flat(g)-P_{\mathscr U_\square}c^\flat(r)\|
\le\sigma(\mu_A(r)+\lambda_{{\rm flat},A}(r)),
}
\tag{8.3}
$$
以及
$$
\boxed{
\lambda_{{\rm flat},\square}(g)
\le(1+\sigma)\lambda_{{\rm flat},A}(r)+\sigma\mu_A(r).
}
\tag{8.4}
$$

## 9. 三种费用的同源模型运输及确切剩余问题

同时保留前稿的天然旗 Schur和裸链运输，得到
$$
\frac{(\mu_A(r)-\rho\lambda_{{\rm flat},A}(r))_+}{1+\rho}
\le\mu_\square(g)\le(1+\rho)\mu_A(r),
\tag{9.1}
$$
$$
\alpha_\square(g)
\le(1+\rho)\alpha_A(r)+\rho\mu_A(r)
 +(1+\rho)\rho^2\lambda_{{\rm flat},A}(r),
\tag{9.2}
$$
以及 (8.4)。三者的 $g$ 都由同一个原 $r$ 的天然旗 Schur 坐标 $x$ 确定，未为各费用另选模型源。

记 $\chi_A^2=\alpha_A^2+\lambda_{{\rm flat},A}^2$，模型同理。
因为 $\rho\le\sigma$，可用略松的合计式
$$
\chi_\square(g)\le(1+2\sigma)\chi_A(r)+\sqrt2\sigma\mu_A(r),
\qquad
\mu_A(r)\le(1+\sigma)\mu_\square(g)+\sigma\chi_A(r).
\tag{9.3}
$$
若后续在这些天然模型来源上证明
$\mu_\square(g)\le\sqrt{C_m}\chi_\square(g)$，且
$\sqrt2\sigma(1+\sigma)\sqrt{C_m}<1$，则原源满足
$$
\boxed{
\mu_A(r)\le
\frac{(1+\sigma)(1+2\sigma)\sqrt{C_m}+\sigma}
{1-\sqrt2\sigma(1+\sigma)\sqrt{C_m}}
\,\chi_A(r).
}
\tag{9.4}
$$
原目标窗口所需的 $C_m=O(e^{d^3/4}/d)$ 会使误差吸收成立。

但是本稿并未给这个模型 $C_m$。仅使用头相似得到的一般裸费比较会带
$K_\square^2$，其四次指数远超该三次窗口门槛，不能用来完成 (9.4)。
新增的是：天然四块模型三种费用均可用同一个原来源运输，并且平坦对偶运输只支付一次 $K_\square$。模型剩余三 Gram / 两费用比较继续是准确的下一研究对象。
