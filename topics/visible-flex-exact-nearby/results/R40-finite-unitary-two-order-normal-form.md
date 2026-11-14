# R40：有限组件的两阶酉正规化，不要求低阶系数振幅小

2026-11-12，visible-exact-astra-f6a2。

**结论范围。** 本文完整证明一个实际标量酉传递算子的正规化定理：
在真实主返回已经共轭为同一个 Diophantine 旋转、完整常相位已经识别、
实际余项有三阶平滑界之后，前两阶逆频率系数可由真实酉共轭化成两个
实常数。低阶系数可以大；付出的有限常数也可以大，不能不计入后验门。

本文不从当前曲面的主符号直接假定这些算子输入。多组件、两个传播方向、
真实 source/contact、common Gram 和正负频率耦合必须先由同一个实际
realization 支付。尤其当前 phase 图有外侧负曲率环，中央区的圆周图
不是全域反馈。R39 的局部 Airy 结果和本定理也不自动构成整个网络的逆。

## 1. 空间、实际输入和结论

在圆周长度 $2\pi$ 上令 $\mathcal H_+$ 为严格正 Fourier 模 $j\ge1$。
$D=-i\partial_\theta$，$De_j=je_j$，$T_f=\Pi_+f\Pi_+$。
旋转算子约定为

\[
 S_\alpha u(\theta)=u(\theta+2\pi\alpha),\qquad
 S_\alpha^{-1}T_fS_\alpha=T_{f_-},\quad
 f_-(\theta)=f(\theta-2\pi\alpha).
\]

选非负、递增、次可加 $\omega$，$\omega(0)=0$，令

\[
 W_j=e^{\rho\omega(|j|)},\quad
 \|u\|_{s,\rho}^2=\sum_{j\ge1}j^{2s}W_j^2|u_j|^2,\quad
 A_r(f)=\sum_{l\in\mathbb Z}(1+|l|)^rW_l|f_l|.
 \tag{1.1}
\]

这包括解析权 $\omega(t)=t$，以及 R35 中的直接对数权。
本文不把仅有 $C^\infty$ 的系数称作解析；使用哪个正权就必须实际支付
对应的 $A_r$。固定 $S\ge0$，假设实际 $U$ 是 $L^2$ 上的酉算子，并有

\[
 U=e^{i\phi_0}S_\alpha V,\qquad
 V=I+T_{p_1}D^{-1}+T_{p_2}D^{-2}+R,
 \tag{1.2}
\]

其中 $\phi_0\in\mathbb R$ 是已识别的完整常相位，不是一个可自由丢掉的符号。
假设

\[
 |1-e^{-2\pi il\alpha}|\ge\gamma(1+|l|)^{-\tau}
 \quad(l\ne0),\qquad \gamma>0,\quad\tau\ge0,
 \tag{1.3}
\]

$A_{S+20+\tau}(p_1),A_{S+20+\tau}(p_2)<\infty$，并已给出

\[
 R_*\ge\sup_{|r|\le S+6}
 \|R:H^r_\rho\longrightarrow H^{r+3}_\rho\|.
 \tag{1.4}
\]

负阶输入是实际假设；它保证所需 adjoint 也有平滑性，不能只由一个
正阶估计推断。$\rho=0$ 的相同界也随 (1.1) 的矩阵证明取得；如实际
$R$ 的输入只在固定 $\rho>0$ 给出，则须另给 (1.4) 在 $\rho=0$ 的界。
下文 $R_*$ 取二者最大值。

**定理。** 存在实函数 $a,h,k$ 和实常数 $c_1,c_2$，满足

\[
 p_1=ia,\qquad 2\operatorname{Re}p_2=-a^2-a',
 \quad c_1=\langle a\rangle,\quad c_2=\langle\operatorname{Im}p_2\rangle,
 \tag{1.5}
\]

\[
 h-h_-=c_1-a,\qquad
 k-k_-=c_2-\operatorname{Im}p_2,\qquad
 \langle h\rangle=\langle k\rangle=0.
 \tag{1.6}
\]

定义真正反自伴的有界算子

\[
 B=\frac i2(T_hD^{-1}+D^{-1}T_h)
     +\frac i2(T_kD^{-2}+D^{-2}T_k),\qquad C=e^B.
 \tag{1.7}
\]

则 $C$ 在 $L^2$ 上准确酉，并有

\[
 C^{-1}UC=
 \mathcal D+\widetilde R,\qquad
 \mathcal D_j=\exp i\left(\phi_0+2\pi\alpha j+\frac{c_1}{j}
                                  +\frac{c_2}{j^2}\right).
 \tag{1.8}
\]

令

\[
 Q=1+R_*+A_{S+20}(p_1)+A_{S+20}(p_2)
                    +A_{S+20}(h)+A_{S+20}(k).
 \tag{1.9}
\]

则 $Q$ 可由实际输入计算，例如 (1.3) 给

\[
 A_{S+20}(h)\le\gamma^{-1}A_{S+20+\tau}(a-\langle a\rangle),\quad
 A_{S+20}(k)\le\gamma^{-1}
 A_{S+20+\tau}(\operatorname{Im}p_2-\langle\operatorname{Im}p_2\rangle).
 \tag{1.10}
\]

对每个 $|s|\le S$，有保守但明确的界

\[
 \|C^{\pm1}\|_{H^s_\rho\to H^s_\rho}\le e^Q,\qquad
 \boxed{\ \|\widetilde R\|_{H^s_\rho\to H^{s+3}_\rho}
                  \le K:=200e^{2Q}Q^6.\ }
 \tag{1.11}
\]

没有 $p_1,p_2$ 小量假设。这个指数常数是实际费用；仅仅知道它有限，
不能推出一个已有残差小于相应 Newton 门。

## 2. 直接矩阵估计

由次可加性和 $j/k,k/j\le1+|j-k|$，Young 或 Schur 估计给

\[
 \|T_f\|_{H^r_\rho\to H^r_\rho}\le A_{|r|}(f).
 \tag{2.1}
\]

以下两式的符号尤其影响 (1.5)：

\[
 D^{-1}T_f=T_fD^{-1}+iT_{f'}D^{-2}+E_1(f),
 \tag{2.2}
\]
\[
 (E_1(f))_{jk}=\frac{(j-k)^2}{jk^2}f_{j-k},\qquad
 \|E_1(f)\|_{H^r_\rho\to H^{r+3}_\rho}
       \le A_{|r|+4}(f).
 \tag{2.3}
\]

事实上令 $l=j-k$，左侧矩阵差为
$[j^{-1}-k^{-1}+lk^{-2}]f_l=l^2f_l/(jk^2)$。
乘上 Sobolev 权后 $j^{r+3}/(jk^{r+2})=(j/k)^{r+2}$，
从而 (2.3) 成立。另有

\[
 \|[D^{-1},T_f]\|_{H^r_\rho\to H^{r+2}_\rho}
       \le A_{|r|+2}(f),
 \tag{2.4}
\]

因为其矩阵为 $-lf_l/(jk)$；以及

\[
 \|[D^{-2},T_f]\|_{H^r_\rho\to H^{r+3}_\rho}
       \le2A_{|r|+3}(f),
 \tag{2.5}
\]

因为矩阵为 $-l(j+k)f_l/(j^2k^2)$。正频率投影也不能假装是全乘法：

\[
 (T_fT_g-T_{fg})_{jk}
       =-\sum_{l\le0} f_{j-l}g_{l-k}.
 \tag{2.6}
\]

给任意 $t\ge0$，取 $p=j-l\ge j$、$q=k-l\ge k$，有

\[
 \|T_fT_g-T_{fg}\|_{H^r_\rho\to H^{r+t}_\rho}
       \le A_{|r|+t}(f)A_{|r|+t}(g).
 \tag{2.7}
\]

证明时用 $W_j/W_k\le W_pW_q$，并将
$j^{r+t}k^{-r}$ 以 $(1+p)^{|r|+t}(1+q)^{|r|+t}$ 控制。
固定一行或一列求和都不超过右端两 Wiener 和的积，故 Schur 检验成立。

综合 (2.4)、(2.7)，特别有

\[
 \|T_fD^{-1}T_gD^{-1}-T_{fg}D^{-2}\|_{H^r_\rho\to H^{r+3}_\rho}
       \le2A_{|r|+3}(f)A_{|r|+3}(g).
 \tag{2.8}
\]

这里第一项是 $T_f[D^{-1},T_g]D^{-1}$，第二项是
$(T_fT_g-T_{fg})D^{-2}$。这些是完整矩阵估计，不是只列形式符号。
所留的 $S+20$ 档统一覆盖下面全部至多六次的有限组合与一、二阶导数。

## 3. 酉性强制的两个系数恒等式

$V$ 准确酉。用 $T_f^*=T_{\bar f}$ 和 (2.2)、(2.5)，得到

\[
 V^*=I+T_{\bar p_1}D^{-1}
   +T_{\bar p_2+i\bar p_1'}D^{-2}+\text{三阶平滑项}.
 \tag{3.1}
\]

(1.4) 的负阶范围保证 $R^*$ 以及与已列项的乘积确实是三阶平滑，
所以由 $V^*V=I$ 得

\[
 p_1+\bar p_1=0,\qquad
 p_2+\bar p_2+i\bar p_1'+|p_1|^2=0.
 \tag{3.2}
\]

为说明没有模掉一个未知有限秩项：若
$T_fD^{-1}+T_gD^{-2}$ 是三阶平滑，固定 $l$、令 $j=k+l\to\infty$，
其矩阵元是 $f_l/k+g_l/k^2=O(k^{-3})$。先乘 $k$ 再乘 $k^2$，
依次得 $f_l=g_l=0$。有限秩或 Hankel 项已经在真实余项内。
写 $p_1=ia$ 后 (3.2) 正是 (1.5)。

## 4. 真酉共轭的两阶计算

(1.3) 逐模解出 (1.6)，并给 (1.10)；实右端与共轭对称保证 $h,k$ 实。
(1.7) 中每个括号均自伴，故 $B^*=-B$。它是有界算子，$e^B$ 为真酉，
无需先假定 $B$ 范数小。由 (2.2)、(2.5)，

\[
 B=T_{b_1}D^{-1}+T_{b_2}D^{-2}+E_B,
 \qquad b_1=ih,\quad b_2=ik-\tfrac12h',
 \tag{4.1}
\]

$E_B$ 三阶平滑。令 $B_-=S_\alpha^{-1}BS_\alpha$。完整共轭为

\[
 C^{-1}UC=e^{i\phi_0}S_\alpha e^{-B_-}Ve^B.
 \tag{4.2}
\]

展开到二阶，并只在已经用 (2.8) 支付的三阶余项内交换乘法，
一阶系数为

\[
 q_1=p_1+b_1-b_{1,-}=ic_1.
 \tag{4.3}
\]

二阶系数为

\[
 q_2=p_2+b_2-b_{2,-}
             +\tfrac12(b_1-b_{1,-})^2+p_1(b_1-b_{1,-}).
 \tag{4.4}
\]

用 $b_1-b_{1,-}=ic_1-p_1$ 化为

\[
 q_2=p_2+b_2-b_{2,-}-\tfrac12c_1^2-\tfrac12p_1^2.
 \tag{4.5}
\]

由 (1.6)，$h'-h_-'=-a'$，而
$k-k_-=c_2-\operatorname{Im}p_2$。因此实部中
$\operatorname{Re}p_2=-\tfrac12(a^2+a')$ 与 $a^2/2,a'/2$ 准确抵消，
虚部变成 $c_2$：

\[
                         q_2=ic_2-\tfrac12c_1^2.
 \tag{4.6}
\]

在这个已固定的左符号约定中，$c_2$ 就是 $\operatorname{Im}p_2$ 的平均。
没有一个可省略的“二次小量”误差；二次项已由真酉性逐项抵消。
若换了主半密度、normal shear 或端口 frame，必须先重算实际 $p_1,p_2$，
不能照搬另一 frame 的这两个平均。

## 5. 三阶余项的明确有限预算

以下都在所需 $|r|\le S+3$ 的有限档上使用 (1.9)；每个因子的额外
平滑阶只使中间档增加至 $S+6$。由 (2.1)、(2.4)、(2.5)，

\[
 \|B\|_{H^r_\rho\to H^{r+1}_\rho}\le Q,\qquad
 \|B\|_{H^r_\rho\to H^r_\rho}\le Q,
 \tag{5.1}
\]

\[
 \|E_B\|_{H^r_\rho\to H^{r+3}_\rho}\le Q,
 \qquad
 \|B-T_{b_1}D^{-1}\|_{H^r_\rho\to H^{r+2}_\rho}\le Q.
 \tag{5.2}
\]

例如 (5.2) 第一界的两项至多
$\tfrac12 A_{|r|+4}(h)+A_{|r|+3}(k)$；第二界用 (2.4)。
因而 (2.8) 给

\[
 \|B^2-T_{b_1^2}D^{-2}\|_{H^r_\rho\to H^{r+3}_\rho}\le4Q^2.
 \tag{5.3}
\]

有界算子指数的积分余项为

\[
 e^B-I-B-\tfrac12B^2
      =\tfrac12\int_0^1(1-t)^2e^{tB}B^3\,dt,
 \tag{5.4}
\]

其三阶平滑范数 $\le e^QQ^3/6$。因此若

\[
 P_+=I+T_{b_1}D^{-1}+T_{b_2+b_1^2/2}D^{-2},
 \tag{5.5}
\]

则 $\|e^B-P_+\|_{r\to r+3}\le5e^QQ^3$。同样，

\[
 P_-=I-T_{b_{1,-}}D^{-1}
          +T_{-b_{2,-}+b_{1,-}^2/2}D^{-2}
 \tag{5.6}
\]

满足 $\|e^{-B_-}-P_-\|_{r\to r+3}\le5e^QQ^3$。
记 $V_0=I+T_{p_1}D^{-1}+T_{p_2}D^{-2}$。
对当前各档，$\|V\|\le Q$、$\|V_0\|\le Q$、
$\|P_\pm\|\le4Q^2$、$\|e^{\pm B}\|\le e^Q$。
采用如下准确的三项差式：

\[
 e^{-B_-}Ve^B-P_-V_0P_+
  =(e^{-B_-}-P_-)Ve^B+P_-(V-V_0)e^B
                         +P_-V_0(e^B-P_+),
 \tag{5.7}
\]

得到三阶预算至多

\[
 5e^{2Q}Q^4+4e^QQ^3+20e^QQ^6
                         \le29e^{2Q}Q^6.
 \tag{5.8}
\]

三个二次多项式相乘有 27 项。总逆阶数至少三的项，逐项由 (2.1)
控制；每项系数积不超过 $4Q^5$，全体以 $108Q^5$ 控制足够。
剩余三个一阶乘一阶项各用 (2.8)，总误差至多 $6Q^2$。
所以 $P_-V_0P_+$ 与 (4.3)、(4.6) 所列二阶模型相差至多 $114Q^5$。

最后，实常数的标量 Taylor 余项直接给

\[
 \left|e^{i(c_1/j+c_2/j^2)}-
   \left(1+\frac{ic_1}{j}+\frac{ic_2-c_1^2/2}{j^2}\right)\right|
 \le\frac{|c_1c_2|+c_2^2/2+(|c_1|+|c_2|)^3/6}{j^3}
 \le\frac{2Q^3}{j^3}.
 \tag{5.9}
\]

旋转和常相位在 (1.1) 上等距。合并 (5.8)、$114Q^5$、(5.9) 得
$(29+114+2)e^{2Q}Q^6<200e^{2Q}Q^6$，完成 (1.11) 的全部预算。

## 6. 完整除数、高切和实际有限低块

现在必须对 (1.8) 的**完整相位**验证

\[
 |1+\mathcal D_j|\ge\kappa/j\qquad(j\ge N_0),\quad\kappa>0.
 \tag{6.1}
\]

在适用的已知常相位下，可用 R34 的二次无理危险格门，令其 $\beta=c_1$，
并把 $c_2/j^2$ 纳入实际余项。只有主旋转满足坏逼近并不蕴含 (6.1)。
未知的 $\phi_0$ 也不能免费设零。

取整数

\[
 N\ge\max\{N_0,\lceil\sqrt{2K/\kappa}\rceil\},\quad
 P_H=1_{j\ge N},\quad P_L=1-P_H.
 \tag{6.2}
\]

在高频子空间，$A_0=I+\mathcal D$ 的逆损失一阶，而 $\widetilde R$
增益三阶，故

\[
 \|A_0^{-1}P_H\widetilde R P_H\|_{H^s_\rho\to H^s_\rho}
     \le K/(\kappa N^2)\le1/2.
 \tag{6.3}
\]

完整高块 $A_{HH}=P_H(I+\mathcal D+\widetilde R)P_H$ 因而可逆，

\[
 \|A_{HH}^{-1}:H^{s+1}_\rho\to H^s_\rho\|\le2/\kappa.
 \tag{6.4}
\]

准确的定义域是 $\mathcal G_s=\{u\in P_HH^s_\rho:
A_{HH}u\in P_HH^{s+1}_\rho\}$，带图范数。上式给从源空间
$P_HH^{s+1}_\rho$ 到 $\mathcal G_s$ 的唯一逆；不声称 $A_{HH}$
把整个 $P_HH^s_\rho$ 都映入高一阶空间。核在整个 $P_HH^s_\rho$
上也为零，这是 (6.3) 的收缩直接给出的。

高切没有删除低块或交叉项。完整反馈的剩余条件是实际有限 Schur 矩阵

\[
 \mathcal S_N=A_{LL}-A_{LH}A_{HH}^{-1}A_{HL}
 \tag{6.5}
\]

可逆；所有块都来自 $A=I+\mathcal D+\widetilde R$。
若给出这个实际有限逆，则

\[
 u_L=\mathcal S_N^{-1}(f_L-A_{LH}A_{HH}^{-1}f_H),\qquad
 u_H=A_{HH}^{-1}(f_H-A_{HL}u_L)
 \tag{6.6}
\]

是完整逆，不丢 source 项。指定核规范、均值兼容和真实参数列可进入有限
增广系统，但这些列若有高频部分，也必须用 (6.4) 实际消元，不能当成
本来仅有有限 Fourier 支撑。

## 7. 对本题实际工作留下的门

1. 从真实完整传递取得 (1.2)，包括准确常相位、normal shear、半密度和
   common Gram；并付两方向/多组件的全部交叉项。矩阵值低阶符号不直接
   适用本文标量二阶抵消，若出现矩阵值反馈须另算交换子。
2. 对同一个修正算子、真实返回参数给 R31 的输入，并取得正角权和实际
   有限档三阶余项 (1.4)。C4 径向样条不是这些高 jet 的自动提供者。
3. 付完整常数 $c_1,c_2,R_*$；由 R34 或直接证明 (6.1)，再验证含兼容行的
   实际低块 (6.5)。用一个很大但未知的高切符号不能替代这个工作。
4. 将 (1.11)、(6.4) 的真实费用与当前残差、R37 的导数损失及完整帽源
   放进同一非线性迭代。所有几何/固定 H 预算仍针对最终同一个精确族支付。

本文已付清有限标量酉正规化本身；以上实际曲面输入仍在 open.md 的工作范围内。
