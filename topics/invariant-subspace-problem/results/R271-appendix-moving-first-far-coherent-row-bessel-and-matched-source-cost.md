# R271 附录：移动第一远孔 coherent 行的 Bessel 界与同来源匹配配对

日期：2026-11-16（UTC）。

作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 本稿证明原连续尾第一远孔读数在几何增长的尾起点上具有完整 Bessel 界。每个起点的整个头空间均保留，并非固定一个头列后逐列取极限。随后将该整行送入同一实际 $w$ 的匹配完整 Schur 配对，给出一个带非零锚的必要费用条件。它不提供原 $C_m^*$ 逆的上界，也不证明 $N=M$。

内积对第一变量线性。依据为：

- [强尾联块同一顶部源流](R271-appendix-strong-tail-block-same-top-source-flow-and-exact-two-fee-budget.md)。
- [匹配完整 Schur 的第一远孔与平均首反馈](R271-appendix-matched-full-resolvent-first-far-hole-and-native-mean-feedback.md)。
- [原强头真空表示及同一个 $w$ 的相邻行](R271-appendix-canonical-strong-head-forcing-and-same-w-adjacent-return-row.md)。

## 1. 同一原物理空间上的第一远孔行

在原 N/Y 的共同 $\ell^2(\mathbb N_0)$ 二进制物理表示中，令
$\mathcal H_{<x}$ 为前 $x$ 位的完整头空间，$\Omega_{\ge x}$ 为其余位真空。这里的空间辨识来自原模型；本稿不更换无限张量积参考。

对整数 $x\ge1$，置
$$
b_i=(i+1)^{-2},\qquad
S_x=\sum_{i\ge x}b_i^2,\qquad
D_x=\sum_{i\ge x}b_iE_i .
$$
以 $\mathcal N_{\ge x}$ 表示从 $x$ 起的远孔数，定义
$$
\boxed{
\beta_x=S_x^{-1/2}D_x
 P_{\{\mathcal N_{\ge x}=1\}}:
\mathcal H\longrightarrow\mathcal H_{<x}.
}
\tag{1.1}
$$
删除后的远真空与头空间按原等距辨识。虽然 $\beta_x$ 的目标随 $x$ 改变，其定义域始终是同一个原物理 Hilbert 空间。

其伴随及范数准确为
$$
\beta_x^*a
=a\otimes\frac{\sum_{i\ge x}b_i e_i}{\sqrt{S_x}},
\qquad
\beta_x\beta_x^*=I_{\mathcal H_{<x}},
\qquad \|\beta_x\|=1.
\tag{1.2}
$$
此处 $e_i$ 是远尾的单孔物理基。由于 $b\in\ell^2$，该创建列在原 Hilbert 范数中收敛。没有使用任何 MP 逆。

若 $x<y$，令
$$
J_{x,y}:\mathcal H_{<x}\to\mathcal H_{<y},
\qquad J_{x,y}a=a\otimes\Omega_{[x,y)}
$$
为中间位真空等距嵌入，则
$$
\boxed{
\beta_x\beta_y^*
=\sqrt{\frac{S_y}{S_x}}\ J_{x,y}^*.
}
\tag{1.3}
$$
证明：先由 $\beta_y^*$ 在 $j\ge y$ 创建一孔。随后 $\beta_x$ 的“从 $x$ 起恰一孔”投影迫使头输入在 $[x,y)$ 全真空，准确留下 $J_{x,y}^*$；删除已创建孔的系数为
$\sum_{j\ge y}b_j^2/\sqrt{S_xS_y}=\sqrt{S_y/S_x}$。输入在中间位的全部非真空分量由原孔投影杀掉，而非事后删 nuisance。反向交叉为 (1.3) 的伴随。

## 2. 全部头来源的跨起点 Bessel 界

设整数尾起点 $x_\ell$ 满足
$$
x_{\ell+1}\ge\lambda(x_\ell+1),\qquad \lambda>1,
\qquad \rho=\lambda^{-3/2}<1.
\tag{2.1}
$$
原尾积分比较为
$$
\frac1{3(x+1)^3}\le S_x\le\frac1{3x^3}.
$$
因此 $S_{x_{\ell+1}}/S_{x_\ell}\le\lambda^{-3}$，由 (1.3) 得
$$
\|\beta_{x_\ell}\beta_{x_k}^*\|
\le\rho^{|\ell-k|}.
\tag{2.2}
$$

对任意有限族 $a_\ell\in\mathcal H_{<x_\ell}$，
$$
\begin{aligned}
\left\|\sum_\ell\beta_{x_\ell}^*a_\ell\right\|^2
&\le\sum_{\ell,k}\rho^{|\ell-k|}
       \|a_\ell\|\,\|a_k\|\\
&\le\frac{1+\rho}{1-\rho}\sum_\ell\|a_\ell\|^2.
\end{aligned}
$$
最后一步是标量矩阵 $\rho^{|\ell-k|}$ 的行和界。取分析算子伴随，再以非负有限部分和取极限，得到
$$
\boxed{
\sum_\ell\|\beta_{x_\ell}w\|^2
\le\mathcal B_\lambda\|w\|^2,\qquad
\mathcal B_\lambda=\frac{1+\lambda^{-3/2}}{1-\lambda^{-3/2}} .
}
\tag{2.3}
$$
这是在原整个物理空间上的有界整行。各 $\mathcal H_{<x_\ell}$ 的维数不受限制，也不要求选取的头向量彼此相容。特别，后面可用同一 $w$ 产生的不同头方向与各行配对。

本稿的 Bessel 结构不同于未来孔带的计数：这里不同 $x$ 的第一远孔空间本来相互重叠；是原连续权以及中间位真空门给出了 (1.3) 的几何交叉衰减。

## 3. 原匹配完整配对的第一远孔误差

取一列原合法母参数 $(m_\ell,R_\ell,Q_\ell)$，令
$$
d_\ell=2^{m_\ell},\quad x_\ell=m_\ell+R_\ell,\quad
h_\ell=d_\ell+R_\ell,\quad
C_\ell=A_{m_\ell}+D_{[m_\ell,x_\ell)}.
$$
以下省去 $\ell$。原同一个 $w\in W$ 给
$$
u=(P_{V_Q}-P_{K_Q})w,\qquad
\|u-P_{\mathcal N\le Q}w\|\le2\eta_m\|w\|,
\quad \eta_m=e^{-6d^4}.
\tag{3.1}
$$
$\mathcal N$ 是原 $m$ 后总尾孔数，不能与远孔数混同。

对 $n+h+R<Q$ 取真实源 $r_n=Cu_n$、左最小列 $U_n$、完整与裸右费 $H_n,B_n$。定义
$$
s_{f,n}[g]=(L_n+H_n)^{-1}U_n^*i_0g,\qquad
\mathfrak M_n(g)
=\langle(H_n-B_n)r_n,s_{f,n}[g]\rangle.
$$
这里 $g$ 在本个 $\ell$ 的所有切口之前选定。令
$$
\mathcal P_n=(L_n+H_n)^{-1}(H_n-B_n),\qquad
a_n=r_n-\mathcal P_nr_n,\qquad
Y_n=(u_{n+1},\ldots,u_{n+h}).
$$
匹配完整源父稿给
$$
\mathfrak M_n(g)=\langle U_n\mathcal P_nr_n,i_0g\rangle,
\qquad
\|U_na_n\|\le\|a_n\|_{L_n+H_n}\le\|Y_n\|.
\tag{3.2}
$$
该估计来自完整短核的物理投影，保全部 $h$ 段及左右零源。

现在写准确的有限头分解
$$
g=C^*t+g_{\rm ker},\qquad Cg_{\rm ker}=0.
\tag{3.3}
$$
可以取 $t=(C^*)^\dagger g$ 和 $g_{\rm ker}=P_{\ker C}g$，但不预先估计这个原像。若 $n\ge1$，则 $i_0g_{\rm ker}$ 属于左零源核，因而在 (3.2) 中消失。零层的真实低行又给
$$
\mathfrak M_n(g)
=-\sqrt{S_x}\,
  \langle\beta_x(U_n\mathcal P_nr_n),t\rangle.
\tag{3.4}
$$
本节只使用第一远孔行，故 $n\ge1$ 已足；若与完整头 Gram 的 $h$ 阶读数同用，则仍须父稿的 $n\ge h$。

在 $Q\ge R+1$ 时，$\operatorname{Ran}\beta_x^*$ 的原总尾孔数至多 $R+1$，因此
$$
\beta_xP_{\mathcal N\le Q}=\beta_x.
\tag{3.5}
$$
这是真支撑恒等式，不是对 $w$ 的尾速率假设。由 $U_nr_n=u_{\le n}$、$n\ge1$、(3.1)--(3.5)，置
$$
\gamma=\sqrt{S_x}\,\|t\|,
$$
得到
$$
\boxed{
\left|\mathfrak M_n(g)
 +\sqrt{S_x}\langle\beta_xw,t\rangle\right|
\le\gamma\,[\,\|Y_n\|+2\eta_m\|w\|\,].
}
\tag{3.6}
$$
没有先将原源投到某个任意近似零源补空间，也没有把创建行的 kernel-input 省去。

## 4. 全切口合并与非零锚

取
$$
\mathcal I_\ell=
\{n:n_{0,\ell}\le n\le Q_\ell-R_\ell-h_\ell-1\},
\qquad N_\ell=|\mathcal I_\ell|>0,\qquad n_{0,\ell}\ge1.
$$
令
$$
b_\ell=\|P_{\{\mathcal N_{\ge x_\ell}>n_{0,\ell}\}}u_\ell\|,
\quad
e_\ell=2\eta_{m_\ell}\|w\|
        +\sqrt{h_\ell/N_\ell}\,b_\ell,
\quad
\Phi_\ell=\frac1{N_\ell}\sum_{n\in\mathcal I_\ell}\mathfrak M_n(g_\ell).
$$
每个远孔层在这些未来带内至多出现 $h_\ell$ 次。对 (3.6) 平均后，
$$
\boxed{
\left|\Phi_\ell
 +\sqrt{S_{x_\ell}}\langle\beta_{x_\ell}w,t_\ell\rangle\right|
\le\gamma_\ell e_\ell.
}
\tag{4.1}
$$

假设
$$
\sum_\ell e_\ell^2<\infty.
\tag{4.2}
$$
一个不依赖 $w$ 尾速率的充分条件是
$\sum_\ell\eta_{m_\ell}^2<\infty$、
$\sum_\ell h_\ell/N_\ell<\infty$，因为 $b_\ell\le\|w\|$。
由 (2.3)、(4.1) 和 $\ell^2$ Minkowski，
$$
\boxed{
\left(\sum_{\ell:\gamma_\ell>0}
          \frac{|\Phi_\ell|^2}{\gamma_\ell^2}\right)^{1/2}
\le\sqrt{\mathcal B_\lambda}\,\|w\|
      +\left(\sum_\ell e_\ell^2\right)^{1/2}.
}
\tag{4.3}
$$
这才是跨参数的整行使用；仅有逐个 $e_\ell\to0$ 而无 (4.2) 时，不能推出 (4.3)。

非零锚也在同一真实来源上。由 (3.2)，
$$
|\mathfrak M_n(g)-\langle u_0,g\rangle|
\le\|Y_n\|\|g\|.
$$
又 $i_0g$ 支撑在远真空，故原 $Q\ge R$ 时
$$
|\langle u_0,g\rangle-\langle w,i_0g\rangle|
\le2\eta_m\|w\|\|g\|.
$$
于是
$$
\boxed{
|\Phi_\ell-\langle w,i_0g_\ell\rangle|
\le e_\ell\|g_\ell\|.
}
\tag{4.4}
$$
如果 $\sup_\ell\|g_\ell\|<\infty$、
$\langle w,i_0g_\ell\rangle\to a\ne0$，则 (4.2) 给
$\Phi_\ell\to a$。$\gamma_\ell=0$ 时 (3.3) 只有核 forcing，故
$\Phi_\ell=0$；非零锚因而排除这种情况在足够大 $\ell$ 继续发生。
结合 (4.3) 得必要条件
$$
\boxed{\sum_{\ell\ {\rm sufficiently\ large}}\gamma_\ell^{-2}<\infty.}
\tag{4.5}
$$
等价地，若对这个同来源族能证明
$\sum\gamma_\ell^{-2}=\infty$，则该非零 $w$ 不存在。
例如真正的平方费用上界
$\gamma_\ell^2\le C\ell\log(\ell+1)$ 已足以给矛盾。
本稿没有证明这一费用上界。

## 5. 原可用窗口及两个 forcing 量词

一个直接适配原实际母窗的例子是
$$
R_m=d_m=2^m,\qquad x_m=m+2^m,\qquad h_m=2d_m,
$$
$$
Q_m=4h_m^2,\qquad n_{0,m}=2h_m^2.
\tag{5.1}
$$
对足够大 $m$，该 $Q_m$ 同时满足已付母窗的下界与
$Q_m\le\exp((1601/64)d_m^3)$。这里没有调用逆芽 gauge 的强位尺度。
有 $n_{0,m}\ge h_m$、
$N_m=2h_m^2-R_m-h_m>0$，并且
$h_m/N_m=O(2^{-m})$。任意固定 $1<\lambda<2$ 都使 (2.1)
从某个 $m$ 起成立。因此 (4.2) 在原同一个 $w$ 上无条件满足。
若只为保原帽内部端点而把上界改成 $Q_m-R_m-2h_m-1$，
同样的可和性仍成立；但 (4.3) 本身针对准确未帽 matched 配对，
不据此将一个任意帽源与它等同。

可用两种不同、必须分清的 forcing：

1. **固定物理测试。** 固定有限物理向量 $f$，在足够大头中令
   $i_0g_m=f$。若 $\langle w,f\rangle\ne0$，(4.5) 应用于
   $t_m=(C_m^*)^\dagger g_m$。固定 $f$ 不意味着这些原像已具有统一上界。

2. **同一 $w$ 的原强头逼近。** 令
   $i_0g_m=P_{x_m}w$。原物理 $P_{x_m}\to I$ 强收敛，
   $\|g_m\|\le\|w\|$，且
   $\langle w,i_0g_m\rangle\to\|w\|^2$。
   对非零 $w$，故必有
   $$
   \sum_{m\ {\rm sufficiently\ large}}
   \frac1{S_{x_m}\|(C_m^*)^\dagger g_m\|^2}<\infty.
   \tag{5.2}
   $$
   这里的最小原像和核分量都由同一个实际 $g_m$ 产生，
   不能以任意环境 Green 常数或另一个固定源代替。

(5.2) 是实际同 $w$ 的必要门，而非所需上界。其用途是把
“必须一致控制 $\sqrt{S_x}\|(C^*)^\dagger g\|$”放宽为可与
(4.3) 矛盾的明确共同费用增长。原完整 $\bar g_0$ 分支、
其源依赖 Green／最小 Schur、以及全部普通边界仍须继续处理。
