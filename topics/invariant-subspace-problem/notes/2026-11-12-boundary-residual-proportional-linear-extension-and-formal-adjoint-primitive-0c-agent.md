# R185/R188 附注：残差比例线性延拓、缺陷的形式伴随原像与单高孔通量

日期：2026-11-12（UTC）。作者：l2_moments。状态：完整实际证明；不另编号。

本稿改进有限头误差最小化接口。真实模型差不但在带空白间隔的空间上很小，而且严格杀掉原有限输入。因此整个线性修复的位移可以只由初始残差控制，不再附加一个乘输入范数的小项。所得精确核向量都属于稳定闭像 $N=\overline{B\ker T}$。这仍没有证明 $N=\ker T$；末节给假设缺陷向量必须满足的真实单高孔通量关系。

## 1. 两个实际边界模型与固定有限纠错

在负整数边界 $\mathcal H_-=\ell^2(\mathbb N_0)$ 上，记
$$
Be_0=0,\qquad Be_n=\alpha_{v_2(n)}e_{n-1},\qquad
W_0=1,\quad W_n=\prod_{l=1}^n\alpha_{v_2(l)},
$$
$$
d_j=W_{2^j},\qquad
\mathsf N_j=B^{2^j}/d_j,\qquad
\mathsf Y_j=\mathsf N_j(I+\mathsf N_j)^{-1},
\qquad a_j=(j+1)^{-2}.
$$
取
$$
T=T_N=\sum_j a_j\mathsf N_j
\quad\text{或}\quad
T=T_Y=\sum_j a_j\mathsf Y_j.
\tag{1.1}
$$
以下两个级数均为算子范数绝对收敛。统一使用
$$
M_a=\sum_j a_j<2,\qquad \|T\|\le6.
$$
记
$$
M=\ker T,\qquad N=\overline{BM},\qquad
\mathcal F_m=\operatorname{span}\{e_n:0\le n<2^m\},
$$
以及正交投影 $P_m:\mathcal H_-\to\mathcal F_m$。令
$$
A_m=e^{8m2^m},\qquad L_m=64\,2^m,\qquad m^+=2L_m.
\tag{1.2}
$$
这里 $A_m$ 是标量放大常数，不是原 Haar 算子 $A$。

对每个 $m\ge2$，固定 R185/R188 的有限块右逆向量
$h_0,h_1,\ldots,h_{2^m-1}$。它们位于块 $[L_m,2L_m)$，
满足
$$
h_0=\Omega,\qquad
D_{\mathcal B}h_\nu=h_{\nu-1},\qquad
D_{\mathcal B}=\sum_{j=L_m}^{2L_m-1}a_j\mathsf E_j,
$$
其中 $h_\nu$ 为恰有 $\nu$ 个孔的向量。此后所有输入使用同一组右逆。

令 $T_m=T|_{\mathcal F_m}$，并定义线性映射
$$
R_mv=\sum_{\nu=0}^{2^m-1}(-1)^\nu T_m^\nu v\otimes h_\nu.
\tag{1.3}
$$
未写出的间隔 $[m,L_m)$ 和更高位均为无孔真空。记这个有限张量空间为
$\mathcal U_{m,L_m}\subset\mathcal F_{m^+}$，模型为
$$
\widetilde T_m=T_m\otimes I+I\otimes D_{\mathcal B}.
$$
R185 §§3–5 与 R188 §§2–4 给
$$
\widetilde T_mR_mv=0,\qquad
\|R_mv-v\|\le A_m\|Tv\|,
\tag{1.4}
$$
$$
\|(T-\widetilde T_m)|_{\mathcal U_{m,L_m}}\|
\le26\eta_{L_m-1}.
\tag{1.5}
$$
对 $T_N$，(1.5) 的常数可用 4；本稿统一用 26。
所有非零修正项在新块至少有一个孔，所以 $R_mv-v$ 的整数支持均不小于 $2^{L_m}$。

## 2. 真实模型差严格杀掉原输入

**引理 2.1。** 对每个 $v\in\mathcal F_m$，
$$
(T-\widetilde T_m)v=0.
\tag{2.1}
$$
因此
$$
\boxed{\|TR_mv\|\le26\eta_{L_m-1}\|R_mv-v\|.}
\tag{2.2}
$$

**证明。** 有限头 $\mathcal F_m$ 对 $B$ 不变。于是对 $i<m$，
$\mathsf N_iv=\mathsf N_i^{[m]}v$，而 $i\ge m$ 时
$\mathsf N_iv=0$。故 $T_Nv=T_{N,m}v$ 精确成立。

对 Cayley 模型，不能只写“逆近似”。在有限头上，
$(I+\mathsf N_i)^{-1}v$ 正好等于有限幂零矩阵
$(I+\mathsf N_i^{[m]})^{-1}v$：二者由同一个有限多项式给出，并且始终不离开 $\mathcal F_m$。当 $i\ge m$ 时，
$\mathsf N_iv=0$，故 $(I+\mathsf N_i)^{-1}v=v$、$\mathsf Y_iv=0$。
所以 $T_Yv=T_{Y,m}v$ 同样精确成立。

原输入的新块全真空，$D_{\mathcal B}v=0$，因此两个模型都有
$\widetilde T_mv=T_mv=Tv$。结合 $\widetilde T_mR_mv=0$，
$$
TR_mv=(T-\widetilde T_m)(R_mv-v),
$$
而 $R_mv-v\in\mathcal U_{m,L_m}$。应用 (1.5) 得 (2.2)。证毕。

(2.2) 的右侧没有 $\|v\|$ 项。特别地，若 $Tv=0$，则 $R_mv=v$，没有人为产生新的残差。

## 3. 对全部有限输入的精确线性延拓

从 $m_0=m\ge2$ 开始，递归
$$
m_{n+1}=128\,2^{m_n},\qquad
v_0=v,\qquad v_{n+1}=R_{m_n}v_n.
$$
写
$$
c_n=\|v_{n+1}-v_n\|,\qquad \epsilon_n=\|Tv_n\|.
$$
由 (1.4)、(2.2)，
$$
c_n\le A_{m_n}\epsilon_n,\qquad
\epsilon_{n+1}\le26\eta_{L_{m_n}-1}c_n.
\tag{3.1}
$$
从而
$$
c_{n+1}\le q_{m_n}c_n,\qquad
q_p=26A_{p^+}\eta_{L_p-1}.
\tag{3.2}
$$

实际权满足 $\eta_j\le e^{-770\,16^j}$。置 $L=L_p$，则
$$
\log q_p
\le\log26+16L4^L-\frac{770}{16}16^L
\le-40\,16^L=-40\,4^{p^+}.
\tag{3.3}
$$
最后一步可由
$16L4^L+\log26\le(65/8)16^L$ 直接核对；对本稿的 $L\ge256$ 有巨大余量。
特别地 $q_p<1/2$，故
$$
\sum_{n\ge0}c_n\le2c_0\le2A_m\|Tv\|.
\tag{3.4}
$$
所有估计对任意尺度的有限输入成立；不需要先假定初始残差满足某个小阈值。

因此范数极限
$$
E_mv=\lim_{n\to\infty}v_n
\tag{3.5}
$$
存在，并满足
$$
\boxed{
E_mv\in M,\qquad P_mE_mv=v,\qquad
\|E_mv-v\|\le2A_m\|Tv\|.
}
\tag{3.6}
$$
$T E_mv=0$ 来自 (3.1) 中残差趋零。
保头性质来自每一步新块修正的支持下界。

每个有限迭代是 $v$ 的线性函数，且 (3.2)–(3.4) 在 $\mathcal F_m$ 的单位球上一致控制尾位移。因此 $E_m$ 是真正的有界线性映射，
$$
\|E_m\|\le1+2A_m\|T\|\le1+12A_m.
\tag{3.7}
$$
它固定 $\ker T_m=\mathbb Ce_0$。

## 4. 延拓的像确在稳定闭像，且距离界无附加误差

下面使用已证的快速残差准则：

> 若 $u_n\in\mathcal F_{k_n}$、$u_n\to u$、$k_n\to\infty$ 且
> $A_{k_n+1}\|Tu_n\|\to0$，则 $u\in N$。

对 (3.5) 的序列，固定输入 $v$ 后 $c_n\le c_0$。对 $n\ge1$，
$$
\epsilon_n
\le26c_0\eta_{L_{m_{n-1}}-1}
\le26c_0\exp\!\left(-\frac{770}{16}4^{m_n}\right).
$$
所以
$$
A_{m_n+1}\epsilon_n
\le26c_0
\exp\!\left(8(m_n+1)2^{m_n+1}
-\frac{770}{16}4^{m_n}\right)\longrightarrow0.
\tag{4.1}
$$
若 $c_0=0$，则 $v\in\mathbb Ce_0\subset N$；同一结论也可直接由恒定有限向量在增大窗口中的快速准则得到。
故每个 $E_mv$ 都属于 $N$。

**定理 4.1。** 对两个实际模型、每个 $m\ge2$ 和所有 $v\in\mathcal F_m$，
$$
\boxed{
E_m:\mathcal F_m\longrightarrow N,\qquad
P_mE_m=I,\qquad
\operatorname{dist}(v,N)\le2A_m\|Tv\|.
}
\tag{4.2}
$$
这比原来的 $A_{m+1}\|Tv\|+\kappa_{m+1}\|v\|$ 距离估计更直接。
它仍不提供对 $m$ 一致有界的 $E_m$。

一个立即的加强是：如果 $v_n\in\mathcal F_{m_n}$、$v_n\to f$ 且
$A_{m_n}\|Tv_n\|\to0$，则 $f\in N$。
若 $f\in M$，可取 $v_n=P_{m_n}f$，但没有理由假定任意核向量自动满足这个加权残差条件。

若单位 $f\in M\ominus N$，则
$$
\operatorname{dist}(P_mf,N)\ge
|\langle P_mf,f\rangle|=\|P_mf\|^2.
$$
因此当 $\|P_mf\|\ge1/2$ 时，
$$
\|TP_mf\|\ge\frac1{8A_m},\qquad
\|(I-P_m)f\|\ge\frac1{8\|T\|A_m}.
\tag{4.3}
$$
这里只是必要慢尾下界。

## 5. 缺陷向量的兼容形式伴随原像

以下内积第一变量线性。设 $f\in M\ominus N$，不必单位化。
对任意 $v\in\mathcal F_m$，由 $E_mv\in N$，
$$
|\langle v,f\rangle|
=|\langle v-E_mv,f\rangle|
\le2A_m\|T_mv\|\,\|f\|.
\tag{5.1}
$$
因为 $e_0\in N$，有 $f_0=0$。定义在 $\operatorname{Ran}T_m$ 上的泛函
$$
\ell_m(T_mv)=\langle v,f\rangle.
$$
$\ker T_m=\mathbb Ce_0$ 使它良定，(5.1) 给范数上界。
Riesz 表示给唯一
$$
h^{(m)}\in\operatorname{Ran}T_m
=\operatorname{span}\{e_0,\ldots,e_{2^m-2}\},
$$
满足
$$
\boxed{
T_m^*h^{(m)}=P_mf,\qquad
\|h^{(m)}\|\le2A_m\|f\|.
}
\tag{5.2}
$$

不能仅因各头选择最小范数解就断言全部投影兼容。
$T_m^*$ 的核是最高头坐标 $\mathbb Ce_{2^m-1}$，
较大头解的投影可能与较小头解在这个坐标不同。
正确的兼容性由逐行三角递推给出。

写 $T$ 的实际形式系数为
$$
T\sim\sum_{\ell\ge1}t_\ell B^\ell,\qquad
t_1=a_0/d_0\ne0.
\tag{5.3}
$$
这里不要求整个形式级数按算子范数收敛；在每个有限头上只剩有限项，且等于真实 $T_m$。
形式方程 $T^*h=f$ 的第 $n+1$ 行为
$$
f_{n+1}
=\sum_{\ell=1}^{n+1}\overline{t_\ell}
\frac{W_{n+1}}{W_{n+1-\ell}}\,h_{n+1-\ell}.
\tag{5.4}
$$
首项系数
$\overline{t_1}\alpha_{v_2(n+1)}$ 非零，
所以 (5.4) 从 $h_0$ 开始依次唯一确定所有 $h_n$。
(5.2) 的每个解在 $0\le n\le2^m-2$ 上都必须与此递推一致。
于是得到一个唯一形式序列 $h$，并且借稍大头的界，
$$
\boxed{
\|P_mh\|\le2A_{m+1}\|f\|\qquad(m\ge2).
}
\tag{5.5}
$$
因此单个系数至多以 $\exp(C(n+2)\log(n+2))$ 的尺度增长。
这远小于真实右移逆所可能产生的 $\exp(c\,n^4)$ 尺度。

(5.5) 仍不说明 $h\in\ell^2$，也不允许把形式恒等式
$T^*h=f$ 当作全空间伴随域恒等式。
如果未来能由真实核方程额外推出 $h\in\ell^2$，
那么 $T$ 有界会使 $T^*h=f$ 成为真实等式，
与 $Tf=0$ 给
$\|f\|^2=\langle Tf,h\rangle=0$，从而排除该缺陷。
当前没有完成这一步。

## 6. 实际伴随尾只有单高孔主项，加超小 carry 误差

本节给 (5.2) 的额外真实约束。对 $j\ge m$ 定义等距复制
$$
U_{j,m}:\mathcal F_m\to\mathcal H_-,
\qquad U_{j,m}e_n=e_{2^j+n}\quad(0\le n<2^m).
$$
这些值域两两正交。实际二进位无 carry 恒等式给
$$
\mathsf N_j^*u=U_{j,m}u\qquad(u\in\mathcal F_m,\ j\ge m).
\tag{6.1}
$$
令
$$
\sigma_m=\left(\sum_{j\ge m}a_j^2\right)^{1/2},\qquad
C_m=\sum_{j\ge m}U_{j,m}U_{j,m}^*.
\tag{6.2}
$$
$C_m$ 为正交投影，选出“低于 $m$ 的位任意，而不低于 $m$ 的位恰有一个孔”的系数。
它不是有限秩投影。

对 $i<m$，真实有限头分解给
$$
\|\mathsf N_i-\mathsf N_i^{[m]}\otimes I\|
=\alpha_m/\alpha_i\le\eta_{m-1}.
\tag{6.3}
$$
因此 $T_N$ 的低位伴随越头误差至多 $M_a\eta_{m-1}$。
对 $T_Y$，全空间逆差恒等式与逆范数小于3给低位误差
$9M_a\eta_{m-1}$。高位再用
$$
\|\mathsf Y_j-\mathsf N_j\|\le3\eta_j
$$
支付至多 $3M_a\eta_{m-1}$。
所以两个模型统一有
$$
\boxed{
(I-P_m)T^*u
=\sum_{j\ge m}a_jU_{j,m}u+\mathcal E_mu,\qquad
\|\mathcal E_m\|\le24\eta_{m-1}
\quad(u\in\mathcal F_m).
}
\tag{6.4}
$$
这里只用了真实算子及其通常伴随；没有把纯尾近似当成等号。

对 $h^{(m)}$，由 $Tf=0$ 和 (5.2)，
$$
0=\langle f,T^*h^{(m)}\rangle
=\|P_mf\|^2+
\left\langle (I-P_m)f,\,
\sum_{j\ge m}a_jU_{j,m}h^{(m)}
+\mathcal E_mh^{(m)}\right\rangle.
\tag{6.5}
$$
这是精确的头能量与尾通量关系。
利用正交值域，
$$
\boxed{
\|P_mf\|^2
\le\sigma_m\|h^{(m)}\|\,\|C_mf\|
+24\eta_{m-1}\|h^{(m)}\|\,\|(I-P_m)f\|.
}
\tag{6.6}
$$

若 $\|f\|=1$ 且 $f\in M\ominus N$，
则最终 $\|P_mf\|^2\ge1/4$，且
$48A_m\eta_{m-1}\le1/8$。由 (5.2)、(6.6) 得
$$
\boxed{
\|C_mf\|\ge\frac1{16A_m\sigma_m}
\qquad\text{对所有充分大的 }m.
}
\tag{6.7}
$$
规范慢列满足 $\sigma_m\asymp m^{-3/2}$，
所以这是比仅要求任意高尾质量更有结构的必要条件：
不能把所需尾质量全部放到每个截断之后至少两个高孔的区域。

(6.7) 的右侧仍趋零很快。它不排除一般无限孔向量，
也没有证明假设中的 $M\ominus N$ 为零。

## 7. 本稿提供的接口和剩余问题

已经得到：

- 对全部有限输入的真实线性延拓 $E_m:\mathcal F_m\to N$，误差只乘 $\|Tv\|$；
- 无附加 $\kappa_m\|v\|$ 项的距离估计；
- 缺陷向量的逐行兼容形式 $T^*$ 原像及 $\exp(O(m2^m))$ 有限头范数界；
- 真实伴随尾分解与单高孔质量的必要下界。

仍缺的是从这些约束推出形式原像实际属于 $\ell^2$，
或直接证明 $N=M$。
不能用 $\mathcal F_m$ 在全空间的稠密性替代核内部稠密性；
也不能因为构造的 $E_mv$ 都属于 $N$，就声称它们在 $M$ 中已经稠密。

依赖：R185 §§3–5；R188 §§2–4；R187 的稳定闭像；
[快速有限头残差进入稳定闭像](2026-11-12-boundary-fast-head-residuals-enter-stable-range-and-quotient-norms-0c-agent.md)。
