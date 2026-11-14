# R66. 全权一临界行与固定除法单位模型

日期：2026-11-12。**状态：实际对象、尺度、整模型及两条除素数行已证明；无穷非零未证明。**

## 1. 真正中央 Borel 的固定秩二周期表达

保留 R47 的实际权一模形式与全中央 Borel，取其偶部分。
在模参数 $t=\lambda_{\rm Leg}-1/2$ 中，令
$$
s=1-4t^2,\qquad sy''-8ty'-y=0,
$$
$K(0)=1,K'(0)=0,L(0)=0,L'(0)=1$，并置 $J=L/t,u=L/K$。
准确的 Cayley 缩放为 $q_0=-8i17^{3/2}$。
由 R51 的实际平方常数得到
$$
\mathcal B_1(u)=K(t(u))M_1(t(u))=\sum C_mu^m,
$$
$$
\boxed{C_m=\frac{m!\beta_m^2}{24\,17^{m-4}}\quad(4\mid m),
\qquad C_m=0\quad(4\nmid m).}
\tag{1}
$$
这里 $A_1=\sum\beta_mz^m$ 是同一个实际次数十七截面。
$M_1=t^4+(7/2)t^6+\cdots$ 是 $\mathbb Q(t^2)$ 上的固定代数 germ。
这使用真正的全权一模形式，没有把半权 Taylor 乘积当成系数逐项平方。

Wronskian $KL'-K'L=s^{-1}$ 给
$$
\boxed{C_n=[t^n]\frac{M_1K^n}{sJ^{n+1}}
 =-\operatorname{res}_{t=0}M_1K(K/L)^{n-1}d(K/L).}
\tag{2}
$$
惰性 $n=p+1$ 的残数含整数幂 $(K/L)^p$；普通 $n=p-1$ 的指数为 $p-2$。

## 2. 原 256 标签的明确整模型

在 $E_\lambda:y^2=x(x-1)(x-\lambda)$ 上取 $\omega=dx/(2y)$、$D=d/\omega$，
并取固定全 $N=68$ 级覆盖。R47 的全部 256 个标签组成 $\mathcal S$。
令 $\Psi_N=\sigma(Nz)/\sigma(z)^{N^2}$ 为除法函数。对每个非零 $N$ 挠点，
$$
\boxed{U_P=-\frac{D^2\Psi_N(P)}{2N^2D\Psi_N(P)}.}
\tag{3}
$$
证明是比较 $D\log\Psi_N(P+z)=z^{-1}-N^2U_P+O(z)$ 的常数项。
其中 $U_P=\zeta(P)-r_P\eta_1-s_P\eta_2$，保留原固定标签。

记 $S=\sum_{\mathcal S}U_P$，将标签 $(r,s)$ 旋转为 $(s,-r)$ 后的和记为
$S_{\rm rot}$。完整周期规范给
$$
\boxed{M_1=\frac{c_*}{2}(S-iS_{\rm rot}),\qquad
c_*=\frac{\sqrt2\,17^{17/4}}{4800f},\quad f=34(1+i).}
\tag{4}
$$
这里 $\omega$ 的周期为 $2\mathbf K(\lambda)=\pi\vartheta_3^2$；在 CM 点它为
$\sqrt2\Omega_0$，而 $24e_4q_0^4=4800/17^4$。这些恒等式逐项确定 (4)。

对 $p\ne2,17$，非零 $E[68]$ 的约化仍互异且非零，除法函数保持简单零点，
所以 $D\Psi_N(P)$ 在所选未分歧形式分支上为单位。(3) 因而整，(4) 给
$$
\boxed{M_1\in\mathbb Z_p[[t]]\qquad(p\notin\{2,3,5,17\}).}
\tag{5}
$$
没有额外未经计算的有限坏素数集合。

更具体地，$v(Z)=-x(Z)/y(Z)=z+O(z^3)$，
$$
r_P(Z)=\frac{\Psi_N(P+Z)}{D\Psi_N(P)v(Z)},\qquad
r_P(O)=1,\quad D_Z\log r_P(O)=-N^2U_P.
$$
这些是 $E_\lambda\setminus(E_\lambda[N]\setminus\{O\})$ 上的真实有理单位。
该开族的 $H^1_{\rm dR}$ 秩为 $4624$；这些 $d\log$ 类给秩 $4622$ 的水平
Tate 部分。实际组合非零可由一个未被两组标签覆盖的点的留数 $256(1-i)$ 证明。
不过原目标取指定代表在 $O$ 的切向值；普通 cohomology 中丢掉的 exact 项会改变它。

## 3. 普通与惰性的准确除素数行

置
$$
B=K/J,\quad\ell=\log B,\quad
W_i=\frac{M_1K}{sJ^2},\quad W_o=\frac{M_1}{sK}.
$$
则准确有 $C_{p+1}=[t^{p+1}]W_iB^p$、$C_{p-1}=[t^{p-1}]W_oB^p$。
由于 $M_1$ 四阶零，所需周期 jet 分别只到 $p-3$、$p-5$，递推、对数和
指数展开均不引入额外 $p$ 分母。

对惰性 $p\ge7$，
$$
\frac{C_{p+1}}p\equiv[t^{p+1}]\mathcal G_i\pmod p,
\qquad
\mathcal G_i=(t\partial_t-1)^{-1}W_i+W_i\ell.
\tag{6}
$$
齐次的一次项取零。由 (1)，$v_p(C_{p+1})=1+2v_p(\beta_{p+1})$，故
(6) 非零恰等价 $\beta_{p+1}$ 为单位，足以惰性初级有限。
Legendre $P_{(p-1)/2}$ 及明确第二解可以模 $p^2$ 替换全部所需周期 jet。

对普通 $p\ge13,p\ne17$，
$$
\frac{C_{p-1}}{p^2}\equiv[t^{p-1}]\mathcal G_o\pmod p,
$$
$$
\mathcal G_o=(t\partial_t+1)^{-2}W_o
 +(t\partial_t+1)^{-1}(W_o\ell)+\tfrac12W_o\ell^2.
\tag{7}
$$
证明须将 $B^p$ 展开到模 $p^3$。实际 $C_{p-1}\in p^2\mathbb Z_p$ 保证
三个项的总和整；不能逐项假设整。(7) 非零恰等价 $v_p(\beta_{p-1})=1$，
同样只是完整普通导数非零的首层充分证书。

固定标量行的首坏项仍必然存在：惰性在 $p+5$，剩余为
$\frac54pK_{p+1}$；普通在 $p+3$，剩余为 $-\frac14pJ_{p-1}$。
二者均为单位，不依赖目标临界系数是否非零。

完整证明见[全权临界行](../notes/2026-11-12-full-weight-one-gm-critical-rows.md)
及[固定除法单位模型](../notes/2026-11-12-weight-one-division-unit-relative-model.md)。
[精确有理脚本](../scripts/check-full-weight-one-gm-row.py)由独立整数流重建实际输入，
根端复跑六个素数的尺度、两条行及全部首坏项通过；不作无穷性证据。
