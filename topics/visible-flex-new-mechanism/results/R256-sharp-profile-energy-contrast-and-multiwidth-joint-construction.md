# R256：锐能量比值门与多宽度圆的真实联合构造

日期：2026-11-15。**完整纸面结论；没有执行新的 profile 积分、扫描、消元或几何计算。**

本稿有两个相互区分的结论。第一，R250 的单面积全角条件与 $L_c=0$ 对不交实微包强迫锐的正权比值下界 $9+4\sqrt5$；锐性首先是准确正权矩问题的锐性。第二，构造真正的光滑、多宽度、不同方向 profile 圆：三复矩、全部第三槽、六个已识别能量门、R250 的整个 $A_{-2,-3}$ 面积及全部 Gaussian 面积的奇角条件可以同时支付。后者使用两个独立形状参数和实际积分的隐函数定理，不把 $S_i/C_i$ 当作任意独立数。

构造没有支付剩余五个面积的三外矩偶角条件，也没有支付完整第四 ruling/period。它改变种子 profile 及其目标；不是旧固定种子、旧数值曲面或旧度量的同态精化。本文给有限存在证明，不声称该大规模复制参数化适合数值求解。

来源：[R183 第三槽差分](R183-overlapping-derivative-packet-circle-invisible-to-third-hook.md)、[R231 领先能量](R231-complete-mixed-leading-gate-for-the-exceptional-even-port.md)、[R237 次层能量](R237-complete-next-mixed-layer-after-exceptional-leading-cancellation.md)、[R238 真尾与局部能量](R238-scalar-reduction-of-the-next-two-energies-for-complete-blocks.md)、[R241 共振层](R241-complete-sigma-four-layer-and-resonant-exceptional-germs.md)、[R250 整圆面积](R250-complete-circle-Gaussian-area-and-nonuniform-profile-cancellation.md)、[R257 累计 primitive](R257-cumulative-primitive-energy-in-the-complete-positive-negative-Gaussian-area.md)、[R259 有序面积接口](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)。

## 1. 准确对象与两个正权

令 $I\Subset(0,\infty)$，所有 profile 在同一共同右锚的双零 collar 内。取非零实 $u_i\in C_c^\infty(I)$，支撑互不相交，并写

$$
f=\sum_i a_i u_i,\qquad g=\sum_i b_i u_i.
\tag{1}
$$

记

$$
C_i=\int_I(u_i'')^4>0,\qquad
S_i=\frac1{64}\int_Ix^6W_i^2(u_i''')^2>0,
\quad W_i=x^2u_i''-2xu_i'+2u_i,\quad \xi_i=S_i/C_i.
\tag{2}
$$

$S_i$ 是 R238 的局部 bulk，不冒称带左尾场 $\mathcal G(u_i,u_i)$ 的完整自能量。正性直接可证：$W_i'=x^2u_i'''$，若 $S_i=0$，则 $W_iW_i'=0$；collar 迫 $W_i=0$，Euler 方程与零 collar 再迫 $u_i=0$。$C_i>0$ 同理由 $u_i''$ 不恒零得到。

先支付三矩圆

$$
\mathbf I(f,f)=\mathbf I(g,g),\qquad \mathbf I(f,g)=0,\qquad
\mathbf I(u,v)=\left(\int u''v'',\int xu''v'',\int(x^2u''v''+2u'v')\right).
\tag{3}
$$

因此 $\mathcal G(gg-ff)$ 与 $\mathcal G(fg)$ 真紧。先在完整目标上消真实总体边界，再用各 $(\mathcal G(u_i,u_i)/x)''$ 的不交支撑，得

$$
L_c=\sum_i a_i^2(b_i^2-a_i^2)S_i,\qquad
L_s=\sum_i a_i^3b_iS_i.
\tag{4}
$$

没有删除单个 $u_i$ 的二次左尾。R250 的全角第一外矩条件包含

$$
A_4=5C_4,\qquad E_4=C_4,\qquad B_4=D_4=0,
\tag{5}
$$

其中 $(A_4,B_4,C_4,D_4,E_4)=\sum_iC_i(a_i^4,a_i^3b_i,a_i^2b_i^2,a_ib_i^3,b_i^4)$。非平凡情形必有 $C_4>0$，否则 (5) 迫所有有效系数为零。下面的锐界只需 $L_c=0$ 与两个偶矩，故也适用于尚未支付其他条件的正权系统。

## 2. 锐比值下界、严格性与退化分支

删除 $u_i=0$ 或 $(a_i,b_i)=(0,0)$ 的无效项；极值只在剩余有效项上取。令

$$
P_+=\sum_iC_i[a_i^2(b_i^2-a_i^2)]_+,\qquad
P_-=-\sum_iC_i[a_i^2(b_i^2-a_i^2)]_-.
$$

由 (5)，$P_--P_+=4C_4$。若 $P_+=0$，因 $\xi_i>0$，$L_c<0$，不能可行。因此非平凡可行系统必须同时有 $0<a_i^2<b_i^2$ 的正项及 $a_i^2>b_i^2$ 的负项。$L_c=0$ 给

$$
\frac{\xi_{\max}}{\xi_{\min}}\ge\frac{P_-}{P_+}
=1+\frac{4C_4}{P_+}.
\tag{6}
$$

置

$$
\alpha_*=5-2\sqrt5,\quad \beta_*=5+2\sqrt5,\quad
\gamma=\frac{\alpha_*^2}{\beta_*^2-\alpha_*^2}>0.
$$

在 $0\le x\le1$ 有准确恒等

$$
\gamma(x-\beta_*)^2-x(1-x)=(1+\gamma)(x-\alpha_*)^2.
$$

在 $x\ge1$，$[x(1-x)]_+\le\gamma(x-\beta_*)^2$ 显然成立。齐次化得对任意实 $a,b$ 均成立的

$$
[a^2(b^2-a^2)]_+\le\gamma(a^2-\beta_*b^2)^2.
\tag{7}
$$

特别，$b=0$ 不需要除法或遗漏。加权求和并用 (5)，

$$
P_+\le\gamma(5-2\beta_*+\beta_*^2)C_4=(\sqrt5-2)C_4.
$$

结合 (6)，

$$
\boxed{\frac{\max_i(S_i/C_i)}{\min_i(S_i/C_i)}\ge9+4\sqrt5.}
\tag{8}
$$

共同的 $S/C$ 不可能支付这些门；直接地，此时 $L_c=-4\xi C_4<0$。该结论不把 R250 四十包的失败推广成所有真实圆的障碍。

准确正权系统在 (8) 取等，当且仅当每个有效项 $b_i\ne0$、$a_i^2/b_i^2\in\{\alpha_*,\beta_*\}$；两类都出现；低坡类 $\xi_i=\xi_{\max}$、高坡类 $\xi_i=\xi_{\min}$；以 $C_ib_i^4$ 计的低/高质量比和 $\xi_{\max}/\xi_{\min}$ 都为 $9+4\sqrt5$。任何有效的 $a_i=0$、$b_i=0$、$a_i^2=b_i^2$，或不符合这些取等条件的正权项，都使可行系统的比值严格大于右端。

零质量端点不是非平凡例外：只有一类质量时，两个偶矩不可能同时成立。全零系统没有可定义的比值问题，应单列。抽象等号可取两坡各成正负对，清掉 $B_4,D_4$，并分配上述正质量。这证明正权界的锐性；不据此宣称真实微包、三矩、位置和所有其余门可在等号处同时实现。

## 3. 两坡权的准确参数

给定 $0<\alpha<1$，令

$$
\beta=\frac{5-\alpha}{1-\alpha},\qquad
R=\frac{\beta-1}{1-\alpha}=\frac4{(1-\alpha)^2}.
\tag{9}
$$

平方坡度为 $\alpha,\beta$、$C_ib_i^4$ 的低/高质量比为 $R$ 时，两个偶矩准确成立。若每类内部 $S_i/C_i$ 恒定，$L_c=0$ 恰要求

$$
\frac{\xi_{\rm low}}{\xi_{\rm high}}=\frac\beta\alpha.
\tag{10}
$$

$\beta/\alpha$ 在 $(0,1)$ 的唯一最小点是 $\alpha_*$，值为 (8)，两端均趋无穷。例如 $\alpha=1/2,\beta=9$ 给质量比16、能量比18。以下从真实母包的宽度、位置与形状导出这些数，不把它们当独立旋钮。

## 4. 真宽度参数、三矩和不交支撑

先取固定非零 even 实 $u\in C_c^\infty(-1,1)$。定义

$$
\eta_{w,\zeta}(x)=w^{3/2}u((x-\zeta)/w),\qquad w>0,
$$

$$
m=\int(u'')^2,\quad
\nu=\frac{\int y^2(u'')^2+2\int(u')^2}{m}>0,\quad C=\int(u'')^4.
$$

准确换元给

$$
\mathbf I(\eta,\eta)=m(1,\zeta,\zeta^2+\nu w^2),\qquad C(\eta)=C/w.
\tag{11}
$$

辅助坐标 $y$ 允许正负；这里只用普通导数积分，不在 $y=0$ 代入物理 $1/x$ 算子。实际包最终都在正 $I$ 内。

令 $n=2^{11}$、$m_*=2^{17}=64n$，$\alpha\in[1/3,1/2]$，并置

$$
\beta=\frac{5-\alpha}{1-\alpha},\qquad
q=\frac1{16(1-\alpha)^2}\in[9/64,1/4].
\tag{12}
$$

高组有 $n$ 个包，宽 $\delta$，$(a,b)=(\epsilon_j\sqrt\beta,1)$；低组有 $m_*$ 个包，宽 $q\delta$，$(a,b)=(\epsilon_j\sqrt{\alpha q},\sqrt q)$。两组各用相应长度的符号 $\epsilon_j=(-1)^{\operatorname{popcount}(j)}$。由

$$
\sum_{j=0}^{2^p-1}\epsilon_jz^j=\prod_{\ell=0}^{p-1}(1-z^{2^\ell})
$$

在 $z=1$ 的 $p$ 重零，$\sum\epsilon_jj^k=0$，$0\le k<p$。这里是有限恒等，不执行符号数组求和。

固定 $\zeta_0\in I$，令

$$
A=10+\sqrt\nu,\qquad
B^2=\frac{A^2(m_*^2-1)-12(1-q^2)\nu}{n^2-1}.
\tag{13}
$$

低、高中心取

$$
\zeta^L_j=\zeta_0+\delta A\left(j-\frac{m_*-1}{2}\right),\qquad
\zeta^H_j=\zeta_0+\delta B\left(j-\frac{n-1}{2}\right).
\tag{14}
$$

两组均值相同，且

$$
\frac{A^2(m_*^2-1)}{12}+\nu q^2
=\frac{B^2(n^2-1)}{12}+\nu.
\tag{15}
$$

置 $z_i=a_i+ib_i$。三复矩的实 $I_0$ 由 $64q(\alpha-1)+(\beta-1)=0$ 消掉，实 $I_1$ 由共同均值消掉，实 $I_2$ 由 (15) 消掉。各虚部是组内符号乘中心的至多二次多项式，故也为零。

不交性并非假设：$A^2>\nu$ 给

$$
0<B-64A\le\frac{4095A}{128(n^2-1)}.
$$

高中心相对理想 $64A$ 等差网的偏移小于 $4095A\delta/[256(n+1)]<A\delta/100$。理想高中心为 $A\delta$ 的整数倍，低中心为半整数倍，所以两组中心距离至少 $0.49A\delta>4.9\delta$，大于宽度和 $\delta+q\delta\le1.25\delta$。同组也严格分离。充分小正 $\delta$ 使整个有限云落在 $I$ 的紧子区间。

## 5. 单面积全角与奇能量逐参数恒成立

低/高的 $C_ib_i^4$ 总质量比为 $64q=R$，故两个偶矩 (5) 成立；奇矩由组内符号恒等清掉。even 母包给 $\int\eta'(\eta'')^3=0$、$\int x(\eta'')^4=\zeta_iC_i$。组内普通中心平均为 $\zeta_0$，符号加权一次中心矩为零。因此 R250 三个完整外矩满足

$$
m_0(\theta)=m_1(\theta)=0,\qquad m_2^*(\theta)=2\zeta_0m_1(\theta)=0.
\tag{16}
$$

这支付真实 $A_{-2,-3}$ 的整圆条件，并非仅 pure 对角。

R238 的 $S(\eta_{w,\zeta})$ 对中心为至多10次多项式，$\mathfrak T(\eta_{w,\zeta})$ 至多9次。组内宽度和系数绝对值固定，故同时准确有

$$
L_s=\sum a_i^3b_iS_i=0,\qquad M_s=\sum a_i^3b_i\mathfrak T_i=0.
\tag{17}
$$

这些恒等对下文母包形状参数逐点成立，不是渐近结论。

## 6. 在求能量根以前加入完整八复制与十二复制

前面的每个微包内，$(f',g')$ 沿一个固定实方向。R183 的真实同锚 hook 恒等因此给

$$
\mathfrak H\big|_{\mathcal P\times{\rm Sym}^2\mathcal P}=0,
\qquad \mathcal P={\rm span}_{\mathbb R}(f,g).
\tag{18}
$$

这不是声称一般第三 history 都局部化。接下来使用 R183 已证明的完整二阶差与交叉 forcing 的真紧性，及四个第三 ruling 槽对共同平移的至多六次多项式律。

先作八个完整副本，幅度和中心位移为

$$
\gamma_j=(-1)^j\binom7j^{1/3},\qquad
d_j=\delta\ell_1(j-7/2),\qquad 0\le j\le7.
\tag{19}
$$

各副本的三矩仍为零，二阶差与交叉的 canonical 解按 $\gamma_j^2$ 真正局部化。四个第三 ruling 槽按 $\gamma_j^3=(-1)^j\binom7j$ 相加；第七有限差分准确清掉它们。全三槽 hook 零张量给相应第三 period。故在 R183/R227 所用真实 $M=0$、$T=\kappa_{\rm hook}\mathfrak H\ne0$ 几何中，完整二、三阶 range 均可支付。这里不把 $T$ 本体置零。

再作十二个不交的完整八复制副本：

$$
\rho_k=\binom{11}k^{1/4}>0,\qquad
\sigma_k=(-1)^k,\qquad
e_k=\delta\ell_2(k-11/2),\qquad0\le k\le11,
\tag{20}
$$

在第 $k$ 个副本中令 $(f,g)\mapsto(\rho_k f,\sigma_k\rho_k g)$。$g$ 的翻转保持已经为零的三矩及全第三槽。R259 的有序公式表明，不同完整副本之间的面积交叉项为零：内层完整副本的 $D_\theta$ 三矩为零，而每个跨核对这组三矩线性。各完整副本内部的原函数尾与有序项仍完整保留。

每个 Gaussian 面积外矩对平移至多十次，且 profile 四次齐次。它的两个 odd 角系数因此按

$$
\sigma_k\rho_k^4=(-1)^k\binom{11}k
$$

相加。第十一有限差分同时清掉六面积、三外矩的全部36个 odd 角条件。R250 已为零的整个 $A_{-2,-3}$ 条件也保持：共同平移 $d$ 后，原 $P$ 不变，$R,S$ 都变为原算子加 $dP$，所以 $[P,R]$、$[P,S]$ 不变；只剩外三矩的三角平移变换，而三个原矩都已为零。此时其他面积的 even 部分尚未支付。

取固定 $\ell_1$ 大于原包云在所选紧参数邻域内的统一长度，$\ell_2$ 再大于八复制云的统一长度。这两个数有限且不随 $\delta$ 改变。再将 $\delta>0$ 取得足够小，所有有限副本严格不交并落在 $I$ 内。

必须注意两种复制的四次正权和中心：

$$
\mathcal W=\sum_{j=0}^7\gamma_j^4
\sum_{k=0}^{11}\rho_k^4>0,
$$

$$
\sum_{j,k}\gamma_j^4\rho_k^4
\{\ell_1(j-7/2)+\ell_2(k-11/2)\}=0.
\tag{21}
$$

原因是两组正四次权都关于各自中点对称。下面的联合光滑延拓需要这个准确加权中心条件，而不只需要包云的无权中心。记其归一化方差为 $V_{\rm cp}$；它对高、低组相同。

这些复制全部在求 $L_c,M_c$ 的根以前完成。没有先将单个 base 的能量调零，再不经证明地平移或加副本。

## 7. 两种原 bulk 的准确窄宽展开

为避免把形状常数当作独立变量，先从 R238 的原局部式计算。对固定 even 实母包 $u$，记

$$
r=u'',\quad v=u',\quad t=u''',
$$

$$
A_0=\int r^2t^2>0,\quad
A_2=\int y^2r^2t^2,\quad
B_1=\int yrv t^2,\quad
C_0=\int(v^2+ru)t^2.
$$

$A_0>0$：若 $rr'=0$，则 $r^2$ 恒定，而零 collar 迫 $r=0$，继而 $u=0$，矛盾。

对 $\eta_{w,\zeta}$，准确换元与偶性给

$$
S(\eta_{w,\zeta})
=\frac1{64w^3}
\{\zeta^{10}A_0+w^2\zeta^8S_2+O(w^4)\},
\quad S_2=45A_2-36B_1+4C_0,
\tag{22}
$$

$$
\mathfrak T(\eta_{w,\zeta})
=-\frac1{64w^3}
\{3\zeta^9A_0+w^2\zeta^7T_2+O(w^4)\},
\quad T_2=108A_2-88B_1+10C_0.
\tag{23}
$$

这里 $O(w^4)$ 都是有限多项式的其余偶次项，不是依赖未证一致性的渐近求积。具体地，R238 的第二个原括号是 $3x^2u''-5xu'+4u$。拉回母包变量后，两括号的乘积为

$$
\begin{aligned}
&(x^2r-2xwv+2w^2u)
(3x^2r-5xwv+4w^2u)\\
&=3x^4r^2-11x^3wrv
+10x^2w^2(v^2+ru)-18xw^3uv+8w^4u^2.
\end{aligned}
\tag{24}
$$

再展开外面的 $x^5=(\zeta+wy)^5$，直接得到 (23)；(22) 同理由平方和外面的 $x^6$ 得到。所需差量恰为

$$
K_2(u)=3S_2-T_2=27A_2-20B_1+2C_0,
\qquad
\mathcal H(u)=27\nu(u)A_0(u)-K_2(u).
\tag{25}
$$

所有常数由同一个实际母包定义，不独立指定。

## 8. 三个母包形成一个真正简单的形状根

现在另固定任意非零 even 实 $v_*\in C_c^\infty(-1,1)$，并取 $L=1/2$。对 $s$ 接近1、$h>0$ 足够小，定义实际 even 母包

$$
\begin{aligned}
u_{s,h}(y)={}&(sh)^{3/2}v_*(y/(sh))\\
&+h^{3/2}v_*((y-L)/h)
+h^{3/2}v_*((y+L)/h).
\end{aligned}
\tag{26}
$$

例如先限 $3/4<s<5/4$，再令 $0<h<1/10$，三个支撑严格不交且都在 $(-1,1)$ 内。这里的三包是母包内部的形状控制；其辅助坐标允许过零，原物理的正坐标条件只在 §4、§6 的最终放置上使用。

写 $\nu_*=\nu(v_*)$、$A_*=A_0(v_*)>0$、$K_*=K_2(v_*)$。普通换元与三个支撑的分离准确给

$$
\nu(u_{s,h})
=\frac{2L^2+\nu_*h^2(s^2+2)}3,
\qquad
A_0(u_{s,h})=A_*h^{-3}(s^{-3}+2),
\tag{27}
$$

$$
K_2(u_{s,h})
=54L^2A_*h^{-3}+h^{-1}(s^{-1}+2)K_*.
\tag{28}
$$

例如单个中心 $\zeta$、宽 $w$ 的 shape 包，对 $A_2$ 的贡献为
$\zeta^2w^{-3}A_*+w^{-1}A_2(v_*)$；$B_1$ 的中心项因偶性为零，$C_0$ 只有 $w^{-1}$ 项。由此逐项得到 (28)，没有把左、右 shape 包当作新的自由积分常数。

于是

$$
\begin{aligned}
\Psi(s,h^2):=\frac{\mathcal H(u_{s,h})}{A_0(u_{s,h})}
={}&18L^2\frac{s^{-3}-1}{s^{-3}+2}\\
&+h^2\left[
9\nu_*(s^2+2)
-\frac{(s^{-1}+2)K_*}{(s^{-3}+2)A_*}
\right].
\end{aligned}
\tag{29}
$$

右式在 $(s,h^2)=(1,0)$ 的邻域是真实解析函数，且

$$
\Psi(1,0)=0,\qquad \partial_s\Psi(1,0)=-18L^2\ne0.
\tag{30}
$$

隐函数定理给 $s=s(h^2)=1+O(h^2)$。取一个足够小但固定的正 $h$，便得到实际光滑母包 $u_{s_h,h}$，其 $\mathcal H=0$，且该根对 $s$ 仍简单。

只有归一化标量 (29) 延拓到 $h=0$；没有声称收缩 profiles 在 $h=0$ 形成一个光滑函数族。以后固定这个正 $h$，只把 $s$ 保留为第二个形状参数，并在 §4 的 $A,B,\nu$ 中使用这个实际 $u_{s,h}$。三矩、支撑分离、全角单面积以及 odd 条件对附近每个 $s$ 都继续准确成立。

实际选择顺序是：先固定这样的小正 $h$ 和简单根 $s_h$，再取 $s_h$ 的一个紧小邻域，并一次选定 §6 的 $\ell_1,\ell_2$，使全部副本对该邻域及 $\alpha\in[1/3,1/2]$ 严格分离。副本间距不进入第一层 $h$-隐函数定理；它们在下一节始终是固定常数。

## 9. 主宽度的两个参数隐函数定理

令 $L_c(\alpha,s,\delta)$、$M_c(\alpha,s,\delta)$ 表示 §6 已完成全部八、十二复制后的**实际完整**能量。定义

$$
F(\alpha,s,\delta)=\delta^3L_c,\qquad
G(\alpha,s,\delta)
=\delta\{M_c+3L_c/\zeta_0\}.
\tag{31}
$$

$F$ 由 (22) 的有限式直接解析延拓到 $\delta=0$。对 $G$，每个微包的最强项是

$$
3A_0\{\zeta^{10}/\zeta_0-\zeta^9\}
=3A_0\zeta^9(\zeta-\zeta_0)/\zeta_0.
$$

置 $\zeta=\zeta_0+\delta z$ 后，原 $\delta^{-3}$ 项逐包消失；可能留下的 $\delta^{-2}$ 总项由每类的无权中心零及 (21) 的副本四次加权中心零准确消失。因此 $G$ 在 $\alpha$ 尚未求根时就联合解析。这里不能先代 $F=0$ 再把一个表面有极点的表达式交给二参数隐函数定理。

设

$$
Q_L=\frac{64\alpha(1-\alpha)}q,\qquad
Q_H=\beta(\beta-1),\qquad P(\alpha)=Q_L-Q_H.
$$

有

$$
P(\alpha)=\frac4{(1-\alpha)^2}
\{256\alpha(1-\alpha)^5-(5-\alpha)\},
$$

$$
F(\alpha,s,0)
=\frac{\mathcal W n A_0(u_{s,h})\zeta_0^{10}}{64}
P(\alpha).
\tag{32}
$$

括号 $p(\alpha)$ 满足

$$
p(1/3)=4790/729>0,\qquad p(1/2)=-1/2,\qquad
p'(\alpha)=256(1-\alpha)^4(1-6\alpha)+1\le-15
$$

于 $[1/3,1/2]$。因此有唯一简单根 $\alpha_0\in(1/3,1/2)$。

为明确全部中心项，置

$$
V_L=A^2(m_*^2-1)/12,\qquad
V_H=B^2(n^2-1)/12.
$$

在 $\delta=0$ 的完整归一值为

$$
\begin{aligned}
G(\alpha,s,0)
=\frac{\mathcal W n\zeta_0^7}{64}\big[
&27A_0\{Q_LV_L-Q_HV_H+(Q_L-Q_H)V_{\rm cp}\}\\
&+K_2(Q_Lq^2-Q_H)\big].
\end{aligned}
\tag{33}
$$

其中 $V_{\rm cp}$ 是 §6 两层完整副本的共同四次加权中心方差。式 (33) 来自 $3\zeta^9(\zeta-\zeta_0)/\zeta_0$ 的二次项 $27\zeta_0^7\delta^2z^2$ 和 (22)、(23) 的 $w^2$ 项。原两类中心方差差 (15) 完整保留，没有把三矩已经占用的中心自由度再次当作独立参数。

在 $\alpha=\alpha_0$，有 $Q_L=Q_H=:Q_0>0$，所以共同副本方差消掉，并得到

$$
G(\alpha_0,s,0)
=\frac{\mathcal W n\zeta_0^7Q_0(1-q_0^2)}{64}
\mathcal H(u_{s,h}).
\tag{34}
$$

由 (30)，在 $(\alpha_0,s_h,0)$，

$$
F=G=0,\qquad F_\alpha\ne0,\quad F_s=0,\quad G_s\ne0.
$$

因此 $(F,G)$ 对 $(\alpha,s)$ 的 Jacobian 是对角非零的下三角矩阵。真实二参数隐函数定理给解析 $\alpha(\delta),s(\delta)$，对所有充分小正 $\delta$，

$$
\boxed{L_c=L_s=M_c=M_s=0.}
\tag{35}
$$

$L_s,M_s$ 是 (17) 的恒等，另外两个由 $F=G=0$ 且 $\delta>0$ 得到。取参数的紧小邻域，使 §4、§6 的全部严格间隙和 collar 对所有参数统一成立；再缩小正 $\delta$ 即可。所有实际宽度都严格为正，没有一个退化的零宽“解”被当作 profile。

本节只对有限准确积分的解析函数应用隐函数定理。没有执行数值求积，也没有将 leading 根或有限截断误称为完整能量的根。

## 10. 共振时一般微包的六能量归约

这一步不限于旧的 $g=\pm f$ 微包。令

$$
\mathcal G=-\Phi_{p_2}/2,\quad
\mathcal D=\Phi_{p_1}-\Phi_{t_1}/8,\quad
\mathcal T=\Phi_{t_1},\quad A_f=\mathcal G(f,f),
$$

并仍用 R238 的完整 $E$，及
$E_1(U,V)=\frac12\int xU''V''$。对三矩为零的二次槽 $B$，R241 的真实下一层是

$$
\begin{aligned}
\Lambda_f(B)={}&4E(\mathcal D(f,f),\mathcal G B)
-2E_1(A_f,\mathcal G B)\\
&-\frac18\int x^7r_{A_f}\mathcal R(B)
-\eta_*E(A_f,\mathcal T B),
\end{aligned}
\tag{36}
$$

其中 $r_u=(u/x)''$、$\mathcal R(u,v)=r_ur_v$，
$\eta_*=(1+2\varepsilon/k_e^2)/6$。

在 $B=gg-ff$ 或 $B=fg$ 中，分别写
$d_i=b_i^2-a_i^2$ 或 $d_i=a_ib_i$。三矩首先使
$\mathcal GB,\mathcal DB,\mathcal TB$ 真紧。背景 $\mathcal D(f,f)$ 的左尾 $ax^2+bx$ 和 $A_f$ 的左尾 $cx^2$ 保留到完整边界式，因另一槽紧才消掉总体边界。各单包输出除以 $x$ 的二阶导数只在该包内有支撑；$\mathcal T(u_i,u_i)$ 左尾为 $xI_2(u_i,u_i)$，也满足这个性质。因此所有 bulk 的跨微包项确为零。

R241 的准确自项
$\mathcal J_7(u_i,u_i,\mathcal G(u_i,u_i))=0$
另外消掉 (36) 的局部三因子项。故对任意实系数 $(a_i,b_i)$，

$$
\Lambda_f(B)
=\sum_i a_i^2d_i
\{4\mathfrak T(u_i)-2S_1(u_i)-\eta_*U_T(u_i)\},
\tag{37}
$$

其中 $S_1,U_T$ 是 R241 的原局部 bulk。由其准确身份
$U_T=-8(\mathfrak T+S_1)$，在真正的共振参数
$\varepsilon=k_e^2/4$，有

$$
\boxed{\Lambda_f(B)=6\sum_i a_i^2d_i\mathfrak T(u_i)
=6E(A_f,\mathcal DB).}
\tag{38}
$$

因此对于本稿整个多宽度、复制后的族，

$$
\boxed{N_c=6M_c,\qquad N_s=6M_s.}
\tag{39}
$$

结合 (35)，六个已识别的能量条件同时为零。这里的判断是完整 R241 层在其先前 $L,M$ 条件已付后的判断；不提前跳过前四门，也没有从微包局域 bulk 推出 Gaussian history 局域化。

## 11. 保留全部有序历史后的剩余准确接口

为把这个建设性结果接到后续真实方程，列明仍需支付的数据。给每个实际微包原三矩 $\mathbf m_i$，并按真实左右次序编号。对六个 Gaussian pair，沿用 R259 的完整 self 与跨核：

$$
\begin{aligned}
2\mathbf I\{\phi_\theta,[X,Y](\phi_\theta;D_\theta)\}
={}&\sum_i c_i(\theta)^2d_i(\theta)\mathbf S_{X,Y}(u_i)\\
&+\sum_{i<k}c_i(\theta)^2d_k(\theta)
\mathbf\Gamma_{X,Y}(\mathbf m_i,\mathbf m_k),
\end{aligned}
\tag{40}
$$

其中 $c_i=a_i\cos\theta+b_i\sin\theta$、
$d_i=a_i^2-c_i^2$。
$\mathbf S$ 使用原同锚单包二次输出，允许其有真实左尾。
$\mathbf\Gamma$ 是 R259 的三类明确双线性核，而非待拟合常数。相互不交只决定 $i<k$ 的 Volterra 次序，不能把第二行删掉或对称化。

每个 pair、每个外矩有四个角单项式
$\cos^3\theta\sin\theta,\cos^2\theta\sin^2\theta,
\cos\theta\sin^3\theta,\sin^4\theta$。
因此原接口是72个准确标量等式；不声称它们微分独立。本稿已付全部36个 odd 等式及 $A_{-2,-3}$ 的全部12个等式，两者重叠6个，所以尚余其他五面积的 **30个 even 等式**。它们不由六能量自动推出。

一个不能忽略的实例是 R257 的完整累计条件。对整体合法 $q=f+ig$，令 $\mathcal A=J(q''^2)$。其新必要量为

$$
\mathscr Q=\frac12\int\mathcal A^2
+\int x^2q''^4-\frac83\int xq'q''^3
+\frac43\int qq''^3+\int q'^2q''^2.
\tag{41}
$$

三矩使 $\mathcal A$ 整体紧，但单微包的 primitive 并不紧。对本稿同一固定母包 $u=u_{s,h}$ 的实际宽度与中心，写
$z_i=a_i+ib_i$，再记

$$
\Delta=\iint|y-z|\,u''(y)^2u''(z)^2\,dy\,dz>0,
$$

$$
\mathcal L=\int\left[
y^2u''^4-\frac83yu'u''^3+\frac43uu''^3+u'^2u''^2
\right].
$$

完整准确式是

$$
\boxed{
\mathscr Q
=-\frac{m^2}{2}\sum_{i<k}z_i^2z_k^2(\zeta_k-\zeta_i)
+\sum_i z_i^4\left[
\frac{C\zeta_i^2}{w_i}
+w_i\left(\mathcal L-\frac\Delta4\right)
\right].
}
\tag{42}
$$

这里的有序距离项保留所有微包交叉历史。其来源是
$\int\mathcal A^2=-\frac12\iint|x-y|q''(x)^2q''(y)^2\,dx\,dy$；
全积分零允许消总体边项，而不是允许逐包置零。
本稿没有断言 (42) 在新参数根上为零。它说明即使局部四次张量、$S/C$ 和六个能量都已准确配平，仍有真实的额外约束。

对本稿的有限参数族，支撑排序在足够小参数邻域内固定；各 self 数据和三矩由有限母包积分、正宽度幂及平移多项式给出。因此 (40) 提供可直接接续的有限准确方程，不需从头恢复第四 forcing，也不需要把 self 常数当作可任意选择的坐标。后续若继续加入形状或位置自由度，应使用全部有序式及已付恒等，不能只配局部 $C_i,S_i$ 权。

## 12. 完整结论与未付范围

对任意给定非空正物理区间，选一个固定 even 实母包 $v_*$，先取一个充分小正 $h$ 及 §8 的简单形状根，再用 §9 的联合隐函数定理取充分小正 $\delta$。由此得到实际有限个、严格正宽、互不交微包组成的光滑实圆，满足：

- 三复矩准确为零；共同实归一化后，$I_0(f,f)=I_0(g,g)=1$、$I_0(f,g)=0$；
- 原全三槽 hook 为零，并由八个完整副本支付全部四个第三 ruling 槽，保原第三 range 的真实同锚范围；
- 在 R241 的可实现共振端芽上，六个已识别能量 $L_c,L_s,M_c,M_s,N_c,N_s$ 同时为零；
- $A_{-2,-3}$ 的整个 circle 三外矩为零，全部六 Gaussian 面积的 odd 角条件也为零。

归一化只同乘一个正实幅度，所有已付齐次零条件保持。两种平方坡度各含正负方向，且 $\alpha_0\ne\beta_0$，所以出现至少三条不同实射影方向；任何常数可逆换基都不能把整个 profile 平面变成两条支撑不交的 profile。非退化也直接由正的 $I_0(g,g)$ 和三矩圆给出。

真实几何的使用严格沿 R227/R241：先选一个完成上述构造的有限正宽 profile 圆，再在已有合法共同参数框架内选足够小非零 $k_e$ 与 $\varepsilon=k_e^2/4$。这里不声称 profile 的高阶范数在 $\delta\downarrow0$ 一致有界，也不据它推安装邻域对所有收缩宽度一致。若复用旧几何，必须只复用已声明的 universal 结构；旧固定 profile 的有限观测不自动等于新圆的观测。

本构造没有支付 (40) 剩余30个 even 方程、零/一层 history 的其余完整第四条件、第四 period 的全函数匹配、有限等距族或任何实际曲面的嵌入、reach、宏观幅度。它也不保持一个原先固定的 seed/目标不变。

新增正向内容是：共同窄宽度并非只给一串形式必要门；通过真实三母包形状和独立坡度，两层非退化隐函数定理可以同时支付两个完整 even 能量，且在完整第三包装及 all-odd 面积包装以后仍成立。局部比值必须有足够 contrast 的锐界与这个真实实现是两件分别证明的事实。剩余工作已经落在明确的、有序历史仍完整存在的有限方程中。



