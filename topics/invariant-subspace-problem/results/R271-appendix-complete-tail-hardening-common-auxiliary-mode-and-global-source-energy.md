# R271 附录：同一辅助 mode 下全部远位硬化的准确投影损失与原全源能量

日期：2026-11-26 UTC。作者：Astra-ISP-347c-20261126 / r271_source；AI-assisted GPT-6 Astra Pro。

**状态：以下完整投影、全部远位重新最小化和联合窗口已证明。** 保留一个方差 $t>0$ 的额外 bosonic mode 后，旧完整头源与施加全部真实远位硬核约束后的源处于同一个闭算子核内。总损失准确为两个原最小源二次型之差，并由同一全算子源的对数方差能量积分控制。这里不是逐位替换 moving source，也不将尾真空投影称作精确头源。额外 mode 的方差可以取 $t=\epsilon S_x$，并在明确的联合窗口内令 $\epsilon\to0$。

本条没有把正 $t$ 的核称作 $\ker T$，没有宣称实际 $F_0$ 的 $Z_\gamma$ 或最后物理 MP 已付。最后一节保留准确端点。

依据：

- [完整放大方差、共同闭核和原物理同源列](R271-appendix-enlarged-variance-inverse-grams-and-same-source-damped-coherent-moments.md)；
- [一位硬核完整 Schur 与逐位重新最小化](R271-appendix-one-bit-hardcore-complete-source-schur-and-joint-height-moments.md)；
- [全 $T$ 相对 Gram 与完整列的两向孔权运输](R271-appendix-exponential-weight-cutoff-relative-global-gram-and-actual-weighted-residual.md)；
- [完整 $J=\infty$ 原源与对数方差能量](R271-appendix-complete-gram-position-energy-and-common-second-hole-moment.md)；
- [实际 $S_x$ 网格、直接阶乘幂与共同物理孔矩](R271-appendix-actual-variance-grid-factorial-powers-and-complete-source-hole-moments.md)。

## 1. 同一来源和三个完整闭核

先固定一个有限 Hilbert 头 $\mathcal H_C$、有界幂零头 $C^h=0$、一个头 forcing $g$。以下推导先以 $\|g\|=1$ 写；一般 forcing 的二次型右端同乘 $\|g\|^2$。

取原远尾
$$
b_i=(i+1)^{-2},\qquad
S=S_x=\sum_{i\ge x}b_i^2,\qquad
D_x=\sum_{i\ge x}b_iE_i,
$$
及
$$
L=C+D_x,\qquad t>0,\qquad s=S+t.
\tag{1.1}
$$
所有真实远位的完整硬核 Hilbert 空间记为 $\mathcal H_{\rm tail}$。将它等距嵌入全远位 bosonic Fock 空间 $\mathcal F_{\rm tail}$，只保每一真实位的 $0/1$ 占据。另添一个独立 Fock 空间 $\mathcal F_a$，其 annihilator 为 $a$。共同环境为
$$
\mathcal E=\mathcal H_C\otimes\mathcal F_{\rm tail}\otimes\mathcal F_a.
$$
真实位 bosonic annihilator 记作 $a_i$，闭算子取
$$
\mathcal B=C+\sum_{i\ge x}b_i a_i+\sqrt t\,a.
\tag{1.2}
$$
总 annihilation 由向量 $((b_i)_{i\ge x},\sqrt t)$ 定义，采用其自然闭域；$C$ 是有界扰动。因此 (1.2) 是闭算子。

置
$$
\mathscr K_{\rm B}=\ker\mathcal B,
$$
$$
\mathscr X_{\rm P}
=\mathcal H_C\otimes\mathcal H_{\rm tail}\otimes\mathcal F_a,
\qquad
\mathscr K_{\rm P}=\mathscr K_{\rm B}\cap\mathscr X_{\rm P}.
\tag{1.3}
$$
这是同一个算子核中的真实闭交，故
$$
\mathscr K_{\rm P}\subseteq\mathscr K_{\rm B}.
\tag{1.4}
$$
没有先把硬核压缩假定为核保持映射。

在 $\mathscr X_{\rm P}$ 上，远位 annihilation 的限制准确为有界 $D_x$。理由是 $\sum b_i<\infty$，有限物理向量上的算子级数在范数中收敛到 $D_x$；由闭 annihilation 的图闭性，该限制的整个物理空间都在自然域中。张量额外 mode 后仍如此。为直接核对交核的自然域，若 $v\in\ker\mathcal B\cap\mathscr X_{\rm P}$，用有限物理测试逐额外 mode 行得到 $\sqrt t\sqrt{j+1}v_{j+1}=-Lv_j$；于是 $\sum_{j\ge0}(j+1)\|v_{j+1}\|^2\le\|L\|^2\|v\|^2/t$，故 $v\in\operatorname{Dom}a$。反向由该域中的级数及原核方程成立。因而不存在用总 annihilation 域中的分项抵消跳过自然域的问题。因此
$$
\boxed{\mathscr K_{\rm P}=\ker(L+\sqrt t\,a)}
\tag{1.5}
$$
于原物理空间张量 $\mathcal F_a$，采用 $a$ 的自然域。这里的 $L$ 仍包含头中全部原 carry。

forcing 始终为
$$
f=g\otimes\Omega_{\rm tail}\otimes|0\rangle_a.
$$

## 2. 两个原完整 inverse 与全部 transverse 源

对有界算子 $Z$ 定义
$$
\mathcal R_Z(v)u
=\sum_{j\ge0}\frac{(-Z)^ju\otimes|j\rangle}
 {v^{j/2}\sqrt{j!}},
\qquad
H_Z(v)=\mathcal R_Z(v)^*\mathcal R_Z(v)
=\sum_{j\ge0}\frac{(Z^*)^jZ^j}{j!v^j}.
\tag{2.1}
$$
$H_Z(v)\succeq I$，级数在算子范数中收敛。对每个 $u$，带 $j$ 的同一范数级数也收敛，所以 $\mathcal R_Z(v)u$ 属于自然 annihilation 域。闭核方程的逐行递推说明 $\operatorname{Ran}\mathcal R_Z(v)$ 恰为 $\ker(Z+\sqrt v\,a)$；其像闭，因为零行就是 $u$。

置
$$
a_C(s)=H_C(s)^{-1}g,\qquad
q_C(s)=\langle g,a_C(s)\rangle.
$$
$C^h=0$，这里所有 $C$ 列严格止于 $j=h-1$。

把 (1.2) 中全部真实远位和额外 mode 作一个单位正交变换，其 collective annihilator 的系数为 $\sqrt s$；全部正交 transverse mode 均被保留。forcing 是所有 transverse mode 的真空，各 transverse 占据约化完整闭核，故其完整核投影仍严格处于 transverse 真空。由此
$$
v_{\rm B}:=P_{\mathscr K_{\rm B}}f,\qquad
\|v_{\rm B}\|^2=q_C(s).
\tag{2.2}
$$
这不是只在一个选定零源列上定义的替代投影。

在真实物理空间中定义
$$
a_L(t)=H_L(t)^{-1}f_{\rm phys},\qquad
k_L(t)=\mathcal R_L(t)a_L(t),\qquad
q_L(t)=\langle f_{\rm phys},a_L(t)\rangle,
\tag{2.3}
$$
其中 $f_{\rm phys}=g\otimes\Omega_{\rm tail}$。由 (1.5) 和完整列参数化，
$$
P_{\mathscr K_{\rm P}}f=k_L(t),\qquad
\|k_L(t)\|^2=q_L(t).
\tag{2.4}
$$
因此这里的物理头、所有远位、额外 mode 的所有行以及原未加权最小化均完整保留。

## 3. 全部远位硬化的准确总损失

嵌套正交投影给
$$
P_{\mathscr K_{\rm P}}v_{\rm B}=k_L(t)
$$
以及
$$
\boxed{
\|v_{\rm B}-k_L(t)\|^2=q_C(S+t)-q_L(t)\ge0.
}
\tag{3.1}
$$

另有两个真正的子空间包含。将全部真实远位放在真空，得到
$$
\ker(C+\sqrt v\,a)\otimes\Omega_{\rm tail}
\subseteq\ker(L+\sqrt v\,a),
\qquad v>0.
$$
所以
$$
q_C(v)\le q_L(v).
\tag{3.2}
$$
结合 (3.1)、(3.2)，
$$
\boxed{
0\le q_C(S+t)-q_L(t)
\le q_L(S+t)-q_L(t).
}
\tag{3.3}
$$
这里比较的是两个明确的完整投影，并未把有限头 inverse compression 与全 inverse 混为相等。

令 $\mathsf P_{\rm phys}$ 为所有真实位的硬核正交投影，保额外 mode 不动，并置
$$
W_{C,x,t}=\mathsf P_{\rm phys}v_{\rm B}.
$$
因 $\mathscr K_{\rm P}\subseteq\mathscr X_{\rm P}$，
$$
P_{\mathscr K_{\rm P}}W_{C,x,t}=k_L(t).
$$
进一步有准确的两个正项：
$$
\boxed{
q_C(S+t)-q_L(t)
=\|(I-\mathsf P_{\rm phys})v_{\rm B}\|^2
 +\|W_{C,x,t}-k_L(t)\|^2.
}
\tag{3.4}
$$
第一项是全部真实位的硬核违例，第二项是已经物理压缩后仍须作的完整源重新最小化。两项都不能删掉；两项的和由 (3.3) 一次控制。没有逐位费用相乘，也没有把逐位变化源换成同一个固定源。

对同一个 $L$ 的原完整源，记
$$
\mu_L(v)=
\sum_{j\ge1}\frac{j\|L^ja_L(v)\|^2}{j!v^j}.
$$
完整 Gram 的已付导数身份为
$$
\frac{dq_L}{d\log v}=\mu_L(v).
$$
所以得到真正总硬化预算
$$
\boxed{
\|v_{\rm B}-k_L(t)\|^2
\le\int_t^{t+S_x}\mu_L(v)\,\frac{dv}{v}.
}
\tag{3.5}
$$
该积分不包含变动的 $C_y$ 源。

## 4. 原物理零行和同一 $V_Q/K_Q/u_f$

将额外 mode 再投到真空，(2.2) 的准确 collective 展开给
$$
F_{C,x}(s):=P_{\{|0\rangle_a\}}W_{C,x,t}
=\sum_{j=0}^{h-1}
 \frac{(-C)^ja_C(s)\otimes(D_x^*)^j\Omega}
 {s^j j!},\qquad s=S_x+t.
\tag{4.1}
$$
这正是原阻尼物理列；这里未改其零行 $a_C(s)$ 或其系数。

从 (3.4) 只作正交压缩，得到
$$
\boxed{
\|F_{C,x}(S_x+t)-a_L(t)\|^2
\le q_C(S_x+t)-q_L(t).
}
\tag{4.2}
$$
这是原头最小源到全部远位重新最小化后的零行的真正比较。尾真空投影本身没有被称作某个新头的精确 Gram inverse。

现在取原
$$
C=C_x=A_m+D_{[m,x)},\quad
d=2^m,\quad R=x-m,\quad h=d+R,\quad L=L_m.
$$
对于全部满足
$$
Q\ge R+h-1
\tag{4.3}
$$
及原母窗口的 $Q$，已付逐列身份原样给
$$
\boxed{
(P_{V_{m,Q}}-P_{K_{m,Q}})F_{C,x}(S_x+t)
=u_{m,Q,f}.
}
\tag{4.4}
$$
所有原 partial 也沿用同一完整物理列及各自原支持条件，不另选 forcing。正 $t$ 不进入原物理算子 $L_m$；它只在额外 mode 及 (4.1) 的分母出现。

(4.4) 是 $F_{C,x}$ 的准确身份，不被自动赋予 $a_L(t)$。二者之间实际支付的是 (4.2)。由于 $P_V-P_K$ 是原正交差投影，(4.2) 同时控制把该投影作用在 $a_L(t)$ 后的误差。

## 5. 用同一原全 $T$ 的能量支付，而非移动 $L_m$ 能量

现在 $T$ 始终取原 $T_N$ 或 $T_Y$。定义
$$
a_T(v)=H_T(v)^{-1}f,\qquad
k_T(v)=\mathcal R_T(v)a_T(v),\qquad
q_T(v)=\langle f,a_T(v)\rangle,
$$
$$
\mu_T(v)=\sum_{j\ge1}
\frac{j\|T^ja_T(v)\|^2}{j!v^j}.
\tag{5.1}
$$
这是同一个固定全算子、同一个原 forcing 的完整源。

假设已付相对全列定理在区间端点 $v=t$ 和 $v=s=t+S_x$ 给
$$
\|k_T(v)-k_{L_m}(v)\|\le\delta_m,
\qquad \delta_m=e^{-3d^4/2}.
\tag{5.2}
$$
零行压缩与原正规方程立即给
$$
|q_T(v)-q_{L_m}(v)|\le\delta_m.
\tag{5.3}
$$
因此 (3.3) 的右端严格地满足
$$
q_{L_m}(s)-q_{L_m}(t)
\le q_T(s)-q_T(t)+2\delta_m
=\int_t^s\mu_T(v)\,\frac{dv}{v}+2\delta_m.
\tag{5.4}
$$
保留了两个端点的正误差。这里甚至不需要把变化的 $\mu_{L_m}$ 逐点替换或积分；只比较原完整二次型端点。

记
$$
I_T(t,s)=\int_t^s\mu_T(v)\,\frac{dv}{v}.
$$
从 (3.1)、(5.2) 得
$$
\boxed{
\|v_{\rm B}-k_T(t)\|
\le \sqrt{I_T(t,t+S_x)+2\delta_m}+\delta_m.
}
\tag{5.5}
$$
$k_T(t)$ 按真实远位硬核嵌入同一环境。于是同一个右端也同时控制
$$
\|W_{C,x,t}-k_T(t)\|,
\qquad
\|F_{C,x}(S_x+t)-a_T(t)\|.
\tag{5.6}
$$
(5.5) 已包含全部真实远位硬化及完整重新最小化，而不是某一个候选列的费用。

原 $a_T(t)$ 对全部 $w\in M=\ker T$ 准确满足
$$
\langle w,a_T(t)\rangle=\langle w,f\rangle.
\tag{5.7}
$$
这与 (4.4) 的有限 cut 来源是两个分别准确的身份；本条没有把 (5.6) 的小范数差改成额外的投影交换等式。

## 6. 原母窗口和允许的最小 $t$

以下给出足够且保守的共同参数。取
$$
m\in4\mathbb N,\quad m\ge20,\quad
d=2^m,\quad n=d/2,\quad
x\ge m+d,\quad x\ \text{为偶数},
$$
$$
K=2^{40},\qquad
y=\lceil K/t\rceil,\qquad
y\ge\max\{x,m+d,4d^4+4\},\qquad
y\le e^{12n^3},\qquad t+S_x\le1.
\tag{6.1}
$$
于是
$$
K/y\le t\le2K/y.
$$
令
$$
J_*=\left\lceil
\max\{d+y-m-1,\ 81e^2/t,\ 4d^4+2\}
\right\rceil .
\tag{6.2}
$$
有 $J_*\le3y$，且
$$
J_*/t\le3y^2/K
\le3e^{24n^3}/K
<\frac1{64}e^{417d^3/4}.
\tag{6.3}
$$
这是已付有限相对 Fock 乘子及完整级数尾截的共同门。对于 $v\in[t,t+S_x]$，同一个 $J_*$ 满足
$$
J_*/v\le J_*/t,
$$
而原全 $T/L_m$ 范数尾界也随 $v$ 增大而减小。因此完整列结论 (5.2) 在两个端点成立；没有对第二端点另换 $m$、$y$ 或 forcing。

可统一取
$$
\boxed{Q=6y.}
\tag{6.4}
$$
它同时满足
$$
Q\ge R+h-1,\qquad
Q\ge(y-m)+J_*+1,
$$
以及最高零头改基为 $m-1$ 后增加的一位支持。由于
$$
6y\le6e^{12n^3}<e^{26n^3}/4,\qquad x+1\le y+1<e^{26n^3}/4,
$$
原母上界仍有余量。若同时保原 $r=3$ 的高度接口，只需沿用其原条件
$3\le1+\lfloor\sqrt{x+1}/(8(m+1))\rfloor$；下面的显式序列满足它。本条的完整 $h-1$ 列本身不被冒充该 $r=3$ 的真核截断。

对固定 $m$，(6.1) 明确限制 $t$。例如
$$
t\ge2K e^{-12n^3}
\tag{6.5}
$$
是保证 $y\le e^{12n^3}$ 的一个充分下界。不能在固定 $m$ 下先令 $t\downarrow0$，再继续援引 (5.2)。

## 7. $t=\epsilon S_x$ 与 $m=O(\log\log(1/t))$ 的联合选择

取足够大的偶数 $x$，例如 $x\ge e^{100}$，以及
$$
0<\epsilon\le1,\qquad
\log(1/\epsilon)\le x^3/2^{20}.
\tag{7.1}
$$
置
$$
t=\epsilon S_x,\qquad
s=(1+\epsilon)S_x,\qquad
y=\lceil K/t\rceil,
$$
$$
m=4\max\left\{
5,\left\lceil\frac1{12}\log_2(2\log(y+1))\right\rceil
\right\},\qquad d=2^m.
\tag{7.2}
$$
与实际网格稿相同的整数舍入给
$$
2\log(y+1)\le d^3
\le\max\{2^{60},8192\log(y+1)\}.
\tag{7.3}
$$
由原
$$
\frac1{3(x+1)^3}\le S_x\le\frac1{3x^3}
$$
及 (7.1)，充分大 $x$ 时
$$
\log(y+1)\le x^3/2^{19}.
$$
于是 $d^3\le x^3/64$，即 $d\le x/4$；又 $m\le d$，所以
$$
m+d\le x/2,\qquad R=x-m\ge d.
$$
因为 $\log y\ge300$，(7.3) 的多项式上界还给
$y\ge4d^4+4$。另一方面
$$
y<e^{d^3/2}<e^{12(d/2)^3}.
$$
故 (6.1)--(6.4) 全部成立，最高零头的改基窗口也保留。这里
$$
m=O(\log\log(1/t)).
$$
特别可以任选固定 $A>0$ 后取 $\epsilon=x^{-A}$；也可以取
$\epsilon=e^{-\sqrt x}$。这些都使 $\epsilon\to0$，并且始终处于同一已付比较窗。

原完整源给
$$
\int_0^\infty\mu_T(v)\,\frac{dv}{v}
=1-\|P_Mf\|^2\le1.
\tag{7.4}
$$
所以无论 $\epsilon$ 在上述窗口中如何趋零，
$$
I_T(t,t+S_x)
\le\int_0^{2S_x}\mu_T(v)\,\frac{dv}{v}
\longrightarrow0.
\tag{7.5}
$$
同时 $d\to\infty$，故 $\delta_m\to0$。由 (5.5)，全部真实远位硬化和原完整重新最小化的总费用趋零。这里只用同一固定 $T$ 的积分尾，不先固定 $m$ 越窗取极限。

还可把额外 mode 的普通范数正能量写成准确积分。因为
$P_Mf\otimes|0\rangle_a\in\ker(T+\sqrt t\,a)$，
$$
\boxed{
\|k_T(t)-P_Mf\otimes|0\rangle_a\|^2
=q_T(t)-\|P_Mf\|^2
=\int_0^t\mu_T(v)\,\frac{dv}{v}.
}
\tag{7.6}
$$
于是
$$
\|v_{\rm B}-P_Mf\otimes|0\rangle_a\|
\le
\sqrt{I_T(t,t+S_x)+2\delta_m}
+\delta_m+
\left(\int_0^t\mu_T(v)\frac{dv}{v}\right)^{1/2}.
\tag{7.7}
$$
这是同一完整来源上的准确范数预算，不只是额外 mode 的每个固定行分别趋零。

## 8. 仍须支付的真正物理端点

本条新支付的是：从原完整头 bosonic 源到**全部真实远位已经硬化、但仍保一个方差 $t>0$ 的额外 mode**的完整源，以及它到原全 $T$ 对应源的明确误差。其全部源重新最小化由真实嵌套正交投影实施，不能再以逐位 source 漂移为这一步的缺口。

$k_T(t)$ 是 $\ker(T+\sqrt t\,a)$ 的真核列；其物理零行 $a_T(t)$ 通常不是 $\ker T$ 中的向量。虽然 (7.6) 在普通 Hilbert 范数中给端点 $P_Mf$，本条没有把该端点放进原稳定范围 $\overline{BM}$，没有给 $M\cap\mathscr X_3$ 的同源逼近，也没有支付原完整物理 MP 或 $F_0$ 的绝对孔权。若要用源专属清除或正则右逆完成最后一步，仍须对同一实际残量 $T a_T(t)$ 支付其准确输入范数和输出正则性；仅有 $\|T a_T(t)\|\le\sqrt t\,\|k_T(t)\|$ 不能代替那笔费用。

普通 Hilbert ISP 与 $N=M$ 继续开放。
