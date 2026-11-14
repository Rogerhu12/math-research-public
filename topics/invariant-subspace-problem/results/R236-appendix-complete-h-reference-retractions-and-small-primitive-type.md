# R236 附录：保完整理想的h基准全层正常cb余式与较小primitive上型

日期：2026-11-14 UTC。作者：Astra-ISP-0c017065 / normal_full_columns_1856；AI-assisted，GPT-6 Astra Pro。

状态：**已证明的固定原理想全层预算。** 本稿保留同一原 S,Z、同一 U 和完整尾理想，不强制每层都用高次数有限倒数正规化。独立的已付 h 行可以冗余加入每个完整尾理想，再作原物理余式。因此正多项式递推依然完整保留，同时实际 primitive、其原双源、完整交换子余式及余式缺陷的原双源映射都取得上型 $140/9$。完整尾生成元及其原双源取得上型 $175/6$。这些仍是随层增长的范数预算，不是统一有界提升或统一正常锚。

## 1. 固定输入与一条独立的已付 h 行链

固定[额外 k 提升稿](R236-appendix-next-k-lagrange-correction-and-paid-original-normal-anchor.md)
的同一 n，并记
$$
s=16^n,\qquad k_0=n+3,\qquad j_0=n+4,\qquad c=7/2.
$$
原 $S=\sum_{i\ge n}a_iN_i$、
$Z=\sum_{i>n}a_i^2N_i$、$a_i=(i+1)^{-2}$、U 和全部原双源均保持不变。

该稿 §§6–7 已支付实际初行
$$
P_{k_0}^{h}=N_{k_0}+R_{k_0}^{h}
=S\mathcal U_{k_0}^{h}+Z\mathcal V_{k_0}^{h},
$$
$$
\|R_{k_0}^{h}\|\le e^{210000s},\qquad
\|\mathcal U_{k_0}^{h}\|,\|\mathcal V_{k_0}^{h}\|\le e^{590000s}.
\tag{1.1}
$$
定义确定的实预算
$$
L_{k_0}=210000s,\qquad
L_{j+1}=4L_j+2u_j+\log8,\qquad
u_j=1400\,16^j-630\,8^j+300\,2^j,
$$
并置 $A_n=e^{380000s}$。

对 (1.1) 逐层应用[carry 稳定 h 修正](R236-appendix-carry-stable-recursive-h-corrections-and-actual-sources.md)
§§2–3，得到所有 $j\ge k_0$ 的实际行及全部原双源：
$$
\boxed{
P_j^{h}=N_j+R_j^{h}
=S\mathcal U_j^{h}+Z\mathcal V_j^{h},
\qquad R_j^{h}\in\mathcal B_{j+1},\quad\chi(R_j^{h})=0,
}
$$
$$
\boxed{
\|R_j^{h}\|\le e^{L_j},\qquad
\|\mathcal U_j^{h}\|,\|\mathcal V_j^{h}\|
\le A_n c^{j-k_0}e^{L_j}.
}
\tag{1.2}
$$

这里每个实际逆仍明确支付。若
$R_j^{h}=p+N_{j+1}b$，$\tau=\eta_j$、$t=\eta_{j+1}N_{j+2}$，则
$$
q=\tau^2I+4tb^4,\qquad
A_j=[4b^2N_{j+1}-(\tau I+2pb)]q^{-1},
$$
$$
R_{j+1}^{h}
=[-2bp^3-\tau p^2+6tb^3p-5\tau tb^2]q^{-1},
$$
$$
(\mathcal U_{j+1}^{h},\mathcal V_{j+1}^{h})
=(\mathcal U_j^{h},\mathcal V_j^{h})(R_j^{h}-N_j)A_j.
\tag{1.3}
$$
初值 $L_{k_0}<240\,16^{k_0}$，同一实际归纳给
$L_j\le240\,16^j$，并且
$$
4\eta_{j+1}e^{4L_j}\eta_j^{-2}
\le4e^{-8560\,16^j}<1/2.
\tag{1.4}
$$
所以 $\|q^{-1}\|\le2\eta_j^{-2}$。
原源的一步因子界 $28e^{3L_j}\eta_j^{-2}$ 与目标的一步界
$8e^{4L_j}\eta_j^{-2}$ 相除，正好给 (1.2) 中的 $c=7/2$。
没有使用任何 $A_j^{-1}$。

显式有限求和为
$$
L_j=4^{j-k_0}L_{k_0}
+2\sum_{i=k_0}^{j-1}4^{j-1-i}u_i
+\frac{\log8}{3}(4^{j-k_0}-1).
\tag{1.5}
$$
因此固定 n 时
$$
\boxed{\lim_{j\to\infty}\frac{L_j}{16^j}=\frac{700}{3}.}
\tag{1.6}
$$

## 2. 同一个 U 的全层实际尾代表及较小原双源

初始 $v_{j_0}=u_*$ 来自额外 k 提升稿，满足
$$
U-v_{j_0}=S\mathcal E_S+Z\mathcal E_Z,\qquad
\|v_{j_0}\|\le e^{104100s},\quad
\|\mathcal E_S\|,\|\mathcal E_Z\|\le e^{483020s}.
$$
定义
$$
\mu_{j_0}=104100s,\qquad
\boxed{\mu_{j+1}=\mu_j+L_j+\log2.}
\tag{2.1}
$$
若当前实际 $v_j=A+N_jB$，用独立 h 行 (1.2) 定义
$$
\boxed{
v_{j+1}=A-R_j^{h}B,\qquad
\mathbf C_{j+1}=\mathbf C_j+B(\mathcal U_j^{h},\mathcal V_j^{h}),
}
\tag{2.2}
$$
其中 $\mathbf C_j$ 是 $U-v_j$ 的原源对。
准确身份为
$$
U-v_{j+1}=(U-v_j)+P_j^{h}B.
$$
物理块提取给 $\|A\|,\|B\|\le\|v_j\|$，所以全部层实际满足
$$
\boxed{
v_j\in\mathcal B_j,\quad\chi(v_j)=0,\qquad
\|v_j\|\le e^{\mu_j},
}
$$
$$
\boxed{
U-v_j=S\mathbf C_{j,S}+Z\mathbf C_{j,Z},\qquad
\|\mathbf C_j\|_{\max}\le A_n c^{j-k_0}e^{\mu_j}.
}
\tag{2.3}
$$
原源界的归纳使用
$(1+e^{L_j})e^{\mu_j}\le e^{\mu_{j+1}}$。
初值也满足
$e^{483020s}\le A_nc^{j_0-k_0}e^{104100s}$。
这里没有把 $U$ 的商像范数用作物理代表范数。

由于
$$
\mu_j=104100s+\sum_{i=j_0}^{j-1}L_i+(j-j_0)\log2,
$$
(1.6) 给
$$
\boxed{
\lim_{j\to\infty}\frac{\mu_j}{16^j}
=\frac{700/3}{15}=\frac{140}{9}.
}
\tag{2.4}
$$
故实际 primitive 及其两个原源的上型都不超过 $140/9$。

[固定起点正多项式稿](R236-appendix-fixed-start-positive-tail-recursion-and-paid-growth.md)
的全部不变量继续成立：$f_{j+1}=f_j+h_jg_j$、
$g_{j+1}=g_j+\beta_jz^{d_j}/\kappa_j$ 以及原线性尾 $W_j,Q_j$ 无需修改。
三个实际成员 $W_j-f_j(v_j)$、$Q_j+g_j(v_j)$、
$v_j^{d_j}-\kappa_jN_j$ 的原双源仍由该稿 (3.2) 给出。
改变的只是为移除当前物理位所选的已付成员。
因此并未丢弃第二行或完整高次关系。

## 3. 完整理想每层保留，生成元费用也同步变小

初始完整理想为
$$
\mathcal J_{j_0}=(h_*,k_*,f_*)_{\mathcal C_{j_0}},
$$
每个生成元目标范数不超过 $e^{2060000s}$，
两个原源各不超过 $e^{2500000s}$。
每个 $P_j^{h}$ 都有原实际双源且属于 $\mathcal C_j$，
因此是同一完整 $\mathcal J_j$ 的成员，可以冗余加入而不删旧生成元。

若当前完整生成组为 $G_{j,1},\ldots,G_{j,k}$，
准确写 $G_{j,i}=a_i+N_jb_i$，则定义下一组
$$
\boxed{
G_{j+1,0}=(R_j^{h})^2-\eta_jN_{j+1},\qquad
G_{j+1,i}=a_i-R_j^{h}b_i.
}
\tag{3.1}
$$
全部原双源是
$$
(R_j^{h}-N_j)(\mathcal U_j^{h},\mathcal V_j^{h}),\qquad
\mathbf G_{j,i}-b_i(\mathcal U_j^{h},\mathcal V_j^{h}).
\tag{3.2}
$$
正常物理余式
$$
r_j(a+N_jb)=a-R_j^{h}b
\tag{3.3}
$$
给完整代数、范数和超弱闭包身份
$$
\boxed{
\mathcal J_j\cap\mathcal C_{j+1}=\mathcal J_{j+1},\qquad
\mathcal J_j=r_j^{-1}(\mathcal J_{j+1}),
}
$$
$$
\boxed{
\overline{\mathcal J_j}^{\,\nu}
=r_j^{-1}(\overline{\mathcal J_{j+1}}^{\,\nu}),
\qquad \nu=\|\cdot\|\text{ 或 }uw.
}
\tag{3.4}
$$
证明用 $X-r_jX=P_j^{h}b$ 及各实际生成元的乘积余式。
从始至终未用 h 行源因子的反向单位。

定义完整生成组的实预算
$$
\gamma_{j_0}=2060000s,\qquad
\boxed{\gamma_{j+1}=\max\{2L_j,\gamma_j+L_j\}+\log2.}
\tag{3.5}
$$
置 $B_n=e^{440000s}$。由 (3.1)–(3.2) 逐项归纳，
全部 $j-n-1$ 个生成元均满足
$$
\boxed{
\|G_{j,i}\|\le e^{\gamma_j},\qquad
\|\mathbf G_{j,i}\|_{\max}\le B_n c^{j-k_0}e^{\gamma_j}.
}
\tag{3.6}
$$
旧生成元的余式用
$(1+e^{L_j})e^{\gamma_j}$ 控制，新 h 生成元用
$2e^{2L_j}$ 控制；源界用 $B_n\ge A_n$ 和同一二项估计。
初值 $B_nc^{j_0-k_0}e^{\gamma_{j_0}}$ 也覆盖 $e^{2500000s}$。

将 (3.5) 展开，$\gamma_j$ 是初始项加后续 L 之和，
以及各层新项 $2L_i$ 加其后 L 之和的最大值。
(1.6) 于是给
$$
\boxed{
\lim_{j\to\infty}\frac{\gamma_j}{16^j}
=\frac18\cdot\frac{700}{3}
=\frac{175}{6}.
}
\tag{3.7}
$$
例如若用主项 $L_i\sim a16^i$，
在第 i 层新生的贡献到第 j 层为
$a(16^j/15+14\,16^i/15)$，最大者为 $i=j-1$，
给 $a/8$；有限初始项只给 $a/15$。
此式计算的是显式预算序列，未声称实际目标一定达到该上型。

## 4. 从完整原交换子出发的实际正常 cb 余式

这一节将完整原 $\mathcal C_n$ 的任意右目标送入远尾，不局限于范数多项式或指定首列。
所有 cb 界均来自实际物理块压缩及固定算子乘法，所以同时支付每个有限矩阵放大，
不改变 Hilbert 度量。

先把前两次原尾消元写出费用。令 $x=n+1$，
$F=\sum_{i\ge n+1}a_iN_i$。
原 $S/a_n=N_n+F/a_n$ 的下一尾代表范数至多 x，
原 $Z/a_{n+1}^2=N_{n+1}+V$ 的代表范数也至多 x。
相应两次物理余式的复合记为 $R_{\rm pre}:\mathcal C_n\to\mathcal C_{n+2}$。
准确有
$$
\|R_{\rm pre}\|_{\rm cb}\le(1+x)^2\le4x^2,
$$
$$
X-R_{\rm pre}X=S A_{\rm pre}(X)+ZB_{\rm pre}(X),
\qquad
\|A_{\rm pre}\|_{\rm cb},\|B_{\rm pre}\|_{\rm cb}\le32x^5.
\tag{4.1}
$$
第一原源为首奇块除 $a_n$；第二原源为首余式之后的奇块除
$a_{n+1}^2$，所以第二项至多
$(x+1)^4(1+x)\le32x^5$。
所有映射正常。

[已付 U 坐标稿](R236-appendix-paid-u-coordinate-and-complete-three-generator-tail.md)
§§4–5 的余式 $r_*:\mathcal C_{n+2}\to\mathcal C_{j_0}$
由有限实际块提取和尾乘子构成，故其同一证明给
$$
\|r_*\|_{\rm cb}\le e^{1040000s}.
$$
该稿 (4.2)、(5.5) 的原双源缺陷映射 cb 范数分别不超过
$e^{1410000s}$；没有使用任意给定元素的小范数理想分解。
将其与 (4.1) 复合，得到
$$
\mathfrak R_{j_0}=r_*R_{\rm pre}:\mathcal C_n\to\mathcal C_{j_0},
$$
$$
\boxed{
\|\mathfrak R_{j_0}\|_{\rm cb}\le e^{1041000s},\qquad
X-\mathfrak R_{j_0}X
=S\mathcal A_{j_0}(X)+Z\mathcal B_{j_0}(X),
}
$$
$$
\boxed{
\|\mathcal A_{j_0}\|_{\rm cb},\|\mathcal B_{j_0}\|_{\rm cb}\le e^{1411000s}.
}
\tag{4.2}
$$
小的多项式因子已吸收；例如 $\log(4x^2)\le4s$。

随后定义实际正常映射
$$
\boxed{\mathfrak R_{j+1}=r_j\mathfrak R_j.}
\tag{4.3}
$$
特别 $\mathfrak R_j(U)=v_j$：初始两次物理余式固定 U，U 坐标余式把 U 送到 $u_*$，后续恰为 (2.2) 的同一实际更新。
因 $\|r_j\|_{\rm cb}\le1+e^{L_j}$，(2.1) 给
$$
\boxed{\|\mathfrak R_j\|_{\rm cb}\le e^{936900s}e^{\mu_j}.}
\tag{4.4}
$$
$\mathfrak R_j$ 在真实 $\mathcal C_j$ 上为恒等。
同时保留实际源映射
$$
X-\mathfrak R_jX=S\mathcal A_j(X)+Z\mathcal B_j(X).
$$
由
$$
\mathfrak R_jX-r_j\mathfrak R_jX
=P_j^{h}\,[\mathfrak R_jX]_{\rm odd},
$$
其明确更新是把
$(\mathcal U_j^{h},\mathcal V_j^{h})[\mathfrak R_jX]_{\rm odd}$
加到上一原源对。物理奇块提取完全收缩，故
$$
\boxed{
\|\mathcal A_j\|_{\rm cb},\|\mathcal B_j\|_{\rm cb}
\le e^{1317000s}c^{j-k_0}e^{\mu_j}.
}
\tag{4.5}
$$
这里 $e^{1317000s}$ 同时覆盖初始缺陷除以 $e^{\mu_{j_0}}$
以及后续乘因子
$A_ne^{936900s}=e^{1316900s}$。
每个映射都是有限次正常操作的复合或有限和，正常性也被保留。

因此 (2.4) 给完整正常余式和两个实际原源映射的统一上型
$$
\boxed{
\limsup_{j\to\infty}\frac1{16^j}
\log\max\{1,\|\mathfrak R_j\|_{\rm cb},
\|\mathcal A_j\|_{\rm cb},\|\mathcal B_j\|_{\rm cb}\}
\le\frac{140}{9}.
}
\tag{4.6}
$$
这是实际物理全交换子的费用，未从某个固定正常表示中的收缩像反推提升常数。

## 5. 完整反向理想身份与给定尾分解的原来源

令 $\mathcal I_0=(S,Z)_{\mathcal C_n}$。
从前两次原尾消元、U 坐标余式以及 (3.4) 逐次复合，准确有
$$
\boxed{
\mathcal I_0=\mathfrak R_j^{-1}(\mathcal J_j),\qquad
\mathcal I_0\cap\mathcal C_j=\mathcal J_j.
}
\tag{5.1}
$$
对 $\nu=\|\cdot\|$ 或 $uw$ 同时有
$$
\boxed{
\overline{\mathcal I_0}^{\,\nu}
=\mathfrak R_j^{-1}(\overline{\mathcal J_j}^{\,\nu}).
}
\tag{5.2}
$$
这是正常连续余式的前像身份，不是一般地交换闭包和交。
从右到左直接把尾理想中的逼近网加上固定
$X-\mathfrak R_jX\in\mathcal I_0$ 即可。

若给定一个实际尾分解
$$
\mathfrak R_jX=\sum_iG_{j,i}b_i,\qquad b_i\in\mathcal C_j,
$$
则 (4.5) 与 (3.6) 明列原来源，并给每个原源的范数界
$$
\boxed{
e^{1317000s}c^{j-k_0}e^{\mu_j}\|X\|
+e^{440000s}c^{j-k_0}e^{\gamma_j}\sum_i\|b_i\|.
}
\tag{5.3}
$$
同一不等式对每个有限矩阵放大成立。
它支付所给实际分解的返回费用；没有声称每个 $\mathcal J_j$ 元素都自动有
统一小范数的生成元分解，也没有给某个商映射一个未证明的统一右逆。

## 6. 原正常态、条件锚与准确范围

同一个原正正常 $\rho$ 若湮灭 $S\mathcal A'+Z\mathcal A'$，
则全部实际源身份保留它对 primitive 缺陷、完整尾生成元、h 行及其全部右倍数的湮灭。
尾部分迹也沿原物理分解进行；没有更换正态或 Hilbert 度量。

h 行的条件锚仍是
$$
\Theta_j^{h}=2P_j^{h}(I+N_j)^{-2},\qquad
e_j^*\Theta_j^{h}e_j=I,\qquad\omega_j(\Theta_j^{h})=1.
$$
其目标和原源分别可用
$9(1+e^{L_j})$ 和 $9A_nc^{j-k_0}e^{L_j}$ 控制。
因而条件锚归一后的下界仍可随 j 衰减，未得到统一正下界。

本稿同时保留了三个不同的实际费用尺度，不能混用：

|实际对象|固定 n 后的统一上型，尺度为 $16^j$|
|---|---:|
|$v_j$ 及 $U-v_j$ 的两个原源|$140/9$|
|完整正常 cb 余式及其缺陷的两个原源映射|$140/9$|
|完整尾生成元及其两个原源|$175/6$|
|用于本步消元的 $P_j^{h}$ 及其原源|$700/3$|

其中前两项已经覆盖完整原交换子和有限放大。
上型有限仍不等于一致有界目标；这些费用能否与实际正常见证的残量和一个不消失的锚接合，
仍需额外证明。本稿没有用完整理想的每层非零性或固定表示中的像相等来替代该步骤。

