# R286：固定有限物理源的零占据逆能量与全部高度统一界

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / boundary_core。

**状态：已证明的中间结论。** 本文把 [局部零占据强制性](R284-appendix-fischer-remainder-and-local-inverse-square-root-control.md) 从最小逆的伴随拉回坐标 $J^*e_I$ 提升到真正的固定源 $f$。对次数 $s\ge2$、有限物理支持的源和固定归一幂阶数 $j$，两个固定正权物理锚给全部 $j$ 次附加尾位统一的 coherent 常数；真实 $\ell^1$ 权使完整 creation 像在 $\mathsf E_{s+j}^{1/2}$ 的像中绝对合成。随后用完整右逆恒等式 $J^*A_j^*f=f$ 支付同一源的逆平方根能量。

源次数和有限支持保持固定时，§6 还将常数统一到全部合法高度 $j$，并给任意固定指数权的求和界。这不是任意增长出生的全条件数界，也不是原 graph $\Gamma=T^*T$ 的逆传播定理。原慢尾应用的归一化和量级在 §§5–6 单独核算。

## 1. 实际对象与定理范围

物理位集可以有限，也可以可数无限。取实正权 $b_i>0$，假设
$$
b\in\ell^1,\qquad S_0=\sum_i b_i^2\in(0,\infty),\qquad
D=\sum_i b_iE_i.
$$
$\mathcal H_r$ 仍是原标准平方自由 Hilbert 层。固定整数
$$
s\ge2,\qquad j\ge1,\qquad p=s+j,
$$
并令
$$
A_j=\frac{D^j}{j!}:\mathcal H_p\longrightarrow\mathcal H_s.
$$
设 $\mathcal K\subseteq\mathcal H_s$ 为闭源空间，$J:\mathcal K\to\mathcal H_p$ 为有界右逆：
$$
A_jJ=\iota_{\mathcal K}.
\tag{1.1}
$$
主要应用是先在完整 $\mathcal H_s$ 上取逆，再限制源的
$J=A_j^\dagger|_{\mathcal K}$，特别 $\mathcal K=K_s=\ker D\cap\mathcal H_s$。定理不要求把源改成某个对称子空间。

将平方自由层嵌入 bosonic Fock 空间，取单位集体模式 $a_0=D/\sqrt{S_0}$。令 $P_0$ 为其零占据正交投影，并记
$$
\mathsf E_p=P_{\mathcal H_p}P_0|_{\mathcal H_p},\qquad
X=J^*\mathsf E_pJ.
\tag{1.2}
$$
取任意有限物理支持的源
$$
f=\sum_{S\in\mathcal S}f_Se_S\in\mathcal K,
\qquad |S|=s,
$$
其中 $\mathcal S$ 有限。对每个 $S\in\mathcal S$ 固定选择两个不同物理锚 $a(S),c(S)\in S$。以下常数只使用这两个锚、固定 $p$ 及总平方和 $S_0$：
$$
r_-(S)=\frac{b_{a(S)}^2}{b_{c(S)}^2},
$$
$$
r_+(S)=
\frac{b_{a(S)}^2+(p-2)(S_0-b_{a(S)}^2-b_{c(S)}^2)}{b_{c(S)}^2},
$$
$$
\boxed{\kappa_S=
\frac{p!\,r_-(S)}{(p-1+r_+(S))^p}>0.}
\tag{1.3}
$$
记 $e_j(b_{S^c})=\sum_{T\subseteq S^c,\,|T|=j}\prod_{i\in T}b_i$，定义
$$
\mathfrak C_j(f)=
\sum_{S\in\mathcal S}|f_S|\,\kappa_S^{-1/2}e_j(b_{S^c}).
\tag{1.4}
$$
**定理。** 上述实际对象满足
$$
\boxed{f\in\operatorname{Ran}X^{1/2},\qquad
\|X^{-1/2}f\|^2\le\mathfrak C_j(f)^2.}
\tag{1.5}
$$
特别若 $\kappa_* =\min_{S\in\mathcal S}\kappa_S$，则
$$
\boxed{\|X^{-1/2}f\|^2
\le\frac{\|b\|_1^{2j}}{(j!)^2\kappa_*}
\left(\sum_{S\in\mathcal S}|f_S|\right)^2.}
\tag{1.6}
$$
所有 $X^{-1/2}$ 仍是在 $(\ker X)^\perp$ 上的标准逆平方根；在无限维中没有将此结论改写成 $f\in\operatorname{Dom}X^{-1}$。

## 2. 两个固定物理锚给所有附加位统一的坐标界

固定一个源支持 $S$ 及其锚 $a,c$，取任意 $I\supseteq S$、$|I|=p$。置
$$
R_I=\sum_{i\in I\setminus\{a,c\}}b_i,
$$
并选有限支持的一粒子向量
$$
v_a=i,\qquad v_c=-\frac{R_I+i b_a}{b_c},\qquad
v_i=1\ (i\in I\setminus\{a,c\}),\qquad v_i=0\ (i\notin I).
\tag{2.1}
$$
于是 $\langle b,v\rangle=0$，而每个 $I$ 内坐标都非零。其平方模满足
$$
|v_c|^2=\frac{b_a^2+R_I^2}{b_c^2}=:r(I),\qquad
\|v\|^2=p-1+r(I),\qquad
\prod_{i\in I}|v_i|^2=r(I).
$$
由 Cauchy–Schwarz，
$$
R_I^2\le(p-2)\sum_{i\in I\setminus\{a,c\}}b_i^2
\le(p-2)(S_0-b_a^2-b_c^2).
$$
因此 $r_-(S)\le r(I)\le r_+(S)$。

单位 coherent 向量
$$
k_v=\frac{(a^*(v))^p\Omega}{\sqrt{p!}\,\|v\|^p}
$$
属于集体模式零占据空间。它压到平方自由层后只留下 $e_I$，故
$$
\mathsf E_p\succeq
\frac{p!\,r(I)}{(p-1+r(I))^p}|e_I\rangle\langle e_I|
\succeq\kappa_S|e_I\rangle\langle e_I|.
\tag{2.2}
$$
这里 $\kappa_S$ 与所有附加物理位的选择、外尾长度无关。将每个权同时乘以同一个正数不会改变它，因为 (1.3) 只含相对量。

由局部强制性的标准 range 论证，(2.2) 等价地给出最小能量向量
$$
g_I=\mathsf E_p^{-1/2}e_I\in(\ker\mathsf E_p)^\perp,
\qquad
\mathsf E_p^{1/2}g_I=e_I,\qquad
\|g_I\|\le\kappa_S^{-1/2}.
\tag{2.3}
$$
本式不使用整个 $\mathsf E_p$ 的下谱界。

## 3. 完整 creation 像的真实 ℓ¹ 合成

归一幂的实际物理伴随满足
$$
A_j^*e_S
=\sum_{\substack{T\subseteq S^c\\|T|=j}}b_T e_{S\cup T},\qquad
b_T=\prod_{i\in T}b_i.
\tag{3.1}
$$
此式保留完整外尾；没有把 $A_j^*$ 换成一个有限支撑截断。由于 $b\in\ell^1$，
$$
e_j(b_{S^c})\le\frac{\|b\|_1^j}{j!}<\infty.
\tag{3.2}
$$
因此使用 (2.3)，级数
$$
g=\sum_{S\in\mathcal S}f_S
\sum_{\substack{T\subseteq S^c\\|T|=j}}b_Tg_{S\cup T}
\tag{3.3}
$$
在 Hilbert 范数下绝对收敛，而且
$$
\|g\|\le\mathfrak C_j(f).
$$
因为 $\mathsf E_p^{1/2}$ 有界，可逐项作用，得到
$$
\boxed{A_j^*f=\mathsf E_p^{1/2}g,
\qquad A_j^*f\in\operatorname{Ran}\mathsf E_p^{1/2},
\qquad
\|\mathsf E_p^{-1/2}A_j^*f\|\le\mathfrak C_j(f).}
\tag{3.4}
$$
这是实际像中的收敛，不仅是在 $\overline{\operatorname{Ran}\mathsf E_p^{1/2}}$ 中逼近。不同 $S,T$ 可能产生相同 $I$，这里只用三角不等式合成，未假设这些贡献正交。

## 4. 从 creation 像返回同一个原源

由完整右逆恒等式 (1.1)，对源 $f\in\mathcal K$ 有
$$
J^*A_j^*f=f.
\tag{4.1}
$$
将 (3.4) 代入，对任意 $u\in\mathcal K$，
$$
|\langle f,u\rangle|
=|\langle g,\mathsf E_p^{1/2}Ju\rangle|
\le\mathfrak C_j(f)\,\|X^{1/2}u\|.
\tag{4.2}
$$
这个泛函在 $\operatorname{Ran}X^{1/2}$ 上有界；Riesz 表示准确给 $f=X^{1/2}h$，其中 $h\perp\ker X$ 且 $\|h\|\le\mathfrak C_j(f)$。这证明 (1.5)，再用 (3.2) 得 (1.6)。

等价的正则化表述为
$$
\sup_{\varepsilon>0}\langle(X+\varepsilon I)^{-1}f,f\rangle
\le\mathfrak C_j(f)^2.
\tag{4.3}
$$
有限维且 $X>0$ 时左边就是 $\langle X^{-1}f,f\rangle$；无限维中 (4.3) 不免费提供 $X^{-1}f$ 这个向量。

有限正权 Boolean 的主要应用须保持合法高度 $N\ge2s+j$。无限正权 $\ell^1\subset\ell^2$ 且有无限多个非零位时，每个固定完整幂的满射和有界右逆，可由 [仿射传输稿的有限头 nilpotent–Neumann 论证](R279-bosonic-affine-primitive-gram-transfer-and-low-occupation-bounds.md) 得到。本文只使用这些固定层的有界性，未从中提取关于 $s,j$ 的统一最小逆范数。

## 5. 原慢尾的固定次数量级：实际归一化保留

令原尾从 $i>m$ 开始，
$$
b_i=(i+1)^{-2},\qquad
D_m=\sum_{i>m}b_iE_i,
$$
$$
S_m=\sum_{i>m}b_i^2,\qquad
L_m=\sum_{i>m}b_i.
$$
单调积分比较给
$$
\frac1{3(m+2)^3}\le S_m\le\frac1{3(m+1)^3},\qquad
L_m\le\frac1{m+1}.
\tag{5.1}
$$
固定有限偏移集 $\mathcal F\subset\{1,2,\ldots\}$、固定 $s\ge2,j\ge1$，并取源族
$$
f_m\in\mathcal K_m\cap\mathcal H_s(F_m),\qquad
F_m=\{m+r:r\in\mathcal F\}.
$$
$\mathcal K_m$ 可以是实际 primitive 源空间；这里只考虑真实属于它的 $f_m$，不把任意物理向量强行视为 primitive。每个支持单项中任选两个锚，其偏移都属于同一个固定 $\mathcal F$。

记 $R_*=\max\mathcal F$、$p=s+j$。这些锚有
$$
\frac{b_{m+a}^2}{b_{m+c}^2}\asymp_{\mathcal F}1,
\qquad
\frac{S_m}{b_{m+c}^2}
\le\frac{(m+c+1)^4}{3(m+1)^3}
=O_{\mathcal F}(m+1).
$$
因此 (1.3) 对所有该有限支持中的单项统一给
$$
\kappa_S\ge c_{\mathcal F,p}(m+1)^{-p}
\tag{5.2}
$$
的某个明确正常数。例如可取
$$
c_{\mathcal F,p}=
\frac{p!(R_*+1)^{-4}}
{\left[p-1+(R_*+1)^4(1+(p-2)/3)\right]^p}.
\tag{5.3}
$$
设 $J_{j,m}$ 是原算子 $A_{j,m}=D_m^j/j!$ 的合法有界右逆，取
$$
X_{j,m}=J_{j,m}^*\mathsf E_{s+j,m}J_{j,m},
$$
其中 $\mathsf E_{s+j,m}$ 使用单位集体模式 $D_m/\sqrt{S_m}$；**$J_{j,m}$ 本身并未把 $D_m$ 除以 $\sqrt{S_m}$。** 由 (1.6)、(5.1)、(5.2)，
$$
\boxed{
\|X_{j,m}^{-1/2}f_m\|^2
\le\frac{(m+1)^{s-j}}{(j!)^2c_{\mathcal F,s+j}}
\|f_m\|_{\ell^1(\text{物理单项})}^2.
}
\tag{5.4}
$$
有限支持大小固定时，$\|f_m\|_{\ell^1}^2\le\binom{|\mathcal F|}{s}\|f_m\|^2$，所以这是同一个固定物理源块的算子型二次形式界，未按 $m$ 增加源维数。

若改用归一权 $\widehat D_m=D_m/\sqrt{S_m}$，则
$$
\widehat J_{j,m}=S_m^{j/2}J_{j,m},\qquad
\widehat X_{j,m}=S_m^jX_{j,m}.
$$
相应逆能量乘以 $S_m^{-j}$，故 (5.4) 对 $\widehat X$ 只给 $O(m^{s+2j})$。这个换算不能与原 $O(m^{s-j})$ 混写。

## 6. 固定源块、全部高度的统一估计和指数加权求和

本节保持 $\mathcal F,s$ 固定，允许 $j\ge1$ 任意变化。原无限慢尾中所有这些完整幂均合法；若应用于有限截断，仅对其合法高度求和。

令
$$
a_{\mathcal F}=(R_*+1)^4,\qquad
\Lambda_{\mathcal F}=e(1+a_{\mathcal F}),\qquad
C_{\mathcal F,s}=a_{\mathcal F}\Lambda_{\mathcal F}^{\,s}
\binom{|\mathcal F|}{s}.
\tag{6.1}
$$
这些常数都不依赖 $m,j$。因为 $p=s+j\ge2$，(5.3) 的分母满足
$$
p-1+a_{\mathcal F}(1+(p-2)/3)
\le(1+a_{\mathcal F})p.
$$
又 $p!\ge(p/e)^p$，所以 (5.2) 可统一改写为
$$
\kappa_S^{-1}
\le a_{\mathcal F}\Lambda_{\mathcal F}^{\,p}(m+1)^p.
$$
重新代入同一真实 $\ell^1$ 合成，而不是把固定 $j$ 的隐含常数擅自当成统一常数，得到
$$
\boxed{
\|X_{j,m}^{-1/2}f_m\|^2
\le C_{\mathcal F,s}(m+1)^s
\frac{[\Lambda_{\mathcal F}/(m+1)]^j}{(j!)^2}
\|f_m\|^2,
\qquad j\ge1.
}
\tag{6.2}
$$
同一个固定源 $f_m\in\mathcal K_m\cap\mathcal H_s(F_m)$ 可以用于全部 $j$；这里未要求全部 $J_{j,m}$ 的算子范数有共同上界。

对任意固定 $R\ge0$，置 $x=\Lambda_{\mathcal F}R^2/(m+1)$。由
$\sum_{j\ge1}x^j/(j!)^2\le e^x-1$，
$$
\boxed{
\sum_{j\ge1}R^{2j}\|X_{j,m}^{-1/2}f_m\|^2
\le C_{\mathcal F,s}(m+1)^s(e^x-1)\|f_m\|^2.
}
\tag{6.3}
$$
更一般，对任意整数 $J_0\ge1$，由 $(J_0+k)!\ge J_0!k!$，
$$
\boxed{
\sum_{j\ge J_0}R^{2j}\|X_{j,m}^{-1/2}f_m\|^2
\le C_{\mathcal F,s}(m+1)^s
e^x\frac{x^{J_0}}{(J_0!)^2}\|f_m\|^2.
}
\tag{6.4}
$$
若某个有限截断只允许部分高度，左边取这些高度的子和，估计不变。

### 6.1 原未除阶乘幂的精确换算

本小节取 $J_{j,m}=(D_m^j/j!)^\dagger|_{\mathcal K_m}$。若使用原未归一幂 $D_m^j$ 的真正最小逆
$$
\mathcal R_{j,m}=(D_m^j)^\dagger|_{\mathcal K_m}
=\frac1{j!}J_{j,m},\qquad
Y_{j,m}=\mathcal R_{j,m}^*\mathsf E_{s+j,m}\mathcal R_{j,m}
=\frac{X_{j,m}}{(j!)^2},
$$
则 (6.2) 准确变为
$$
\boxed{\|Y_{j,m}^{-1/2}f_m\|^2
\le C_{\mathcal F,s}(m+1)^s
[\Lambda_{\mathcal F}/(m+1)]^j\|f_m\|^2.}
\tag{6.5}
$$
所以当 $x=\Lambda_{\mathcal F}R^2/(m+1)<1$ 时，
$$
\boxed{
\sum_{j\ge J_0}R^{2j}\|Y_{j,m}^{-1/2}f_m\|^2
\le C_{\mathcal F,s}(m+1)^s\frac{x^{J_0}}{1-x}\|f_m\|^2.
}
\tag{6.6}
$$
原完整幂的阶乘已经在这里全部付清；不能把 (6.3) 的阶乘衰减直接保留给 $Y_{j,m}$。对任何固定指数权 $R$，(6.6) 在充分大的 $m$ 成立，且不依赖一个额外的高度截断上限。

## 7. 与实际固定测试流的尚未接合处

本文覆盖的是固定 $s$、固定有限物理支持的源，或其固定偏移平移族；高度 $j$ 可以按 §6 统一变化。原实际测试流
$$
t_{p-1}=Dv_p+e_p,\qquad t_p=-Av_p
$$
的 $p$、允许头数和源次数随原窗口增长；它仍保留全部 $e_p$ 和真实端点配对。本文没有证明这些 $t_p$ 可以用具有上述固定 $s$ 和固定支持常数的源表示，也没有证明原 graph 的受限逆就是 $X_{j,m}^{-1/2}$。

这个区别还可以在实际正交谱旗上准确定位。为避免与前文 $p=s+j$ 混淆，下面以 $q$ 表示原流的孔层。记 $E_{k,q}=\ker D^k\cap\mathcal H_q$，$E_{0,q}=\{0\}$。在全部所需完整幂合法时，真正最小逆给
$$
\operatorname{Ran}\mathcal J_{h,q-h}
=E_{h+1,q}\ominus E_{h,q},
$$
因此对 $k\le q+1$ 有同一物理度量下的正交塔公式
$$
\boxed{E_{k,q}=\bigoplus_{h=0}^{k-1}
\operatorname{Ran}\mathcal J_{h,q-h}.}
\tag{7.1}
$$
理由是 $D^{h+1}\mathcal J_{h,q-h}=0$，完整最小逆的像又正交于 $\ker D^h$；反向则由 $D^h$ 把这个正交差空间双射到 $K_{q-h}$。这里 $h$ 是实际高度，$q-h$ 是该塔的祖先 primitive 出生。

[实际固定测试流稿 (2.2)](../notes/2026-11-14-actual-test-flow-filtered-bare-chain-and-primitive-free-source-kernel-2220.md) 保留原 $d=2^m$ 并证明
$$
t_q\in\bigoplus_{i=0}^{d-3}e_i
\bigl(E_{d-i-1,q}\ominus E_{1,q}\bigr).
\tag{7.2}
$$
对原大孔层 $q\ge d$，把 (7.1) 代入，得到第 $i$ 个实际物理头只含
$$
1\le h\le d-i-2,
\qquad
q-d+i+2\le q-h\le q-1
\tag{7.3}
$$
这些真实塔。特别，若 $q>d+s-2$，则固定祖先出生 $s$ 的整条塔在 $t_q$ 中的分量恰为零。随着原窗口上移，其允许的祖先出生随 $q$ 上移；它并不是把一个固定出生 $s$ 保持不变而只增加本文的高度 $j$。

因此，起始物理测试 $f$ 固定，不等于其经原受限逆 $Z_q^{-1}$ 后的源仍具有固定 primitive 出生或有限物理支持。要将本文的固定源全高度估计用于 (7.2)，仍须支付同一个实际 graph 的跨出生回传及其全部 $v_q,e_q$；(7.1)–(7.3) 不提供这种回传。

因此 (5.4) 是原慢尾的真实固定源尺度进展，不能用来删除原 $e_p$，不能绕过零源商的真实定义，也不能直接推出固定测试主配对趋零、$N=M$ 或普通 ISP。
