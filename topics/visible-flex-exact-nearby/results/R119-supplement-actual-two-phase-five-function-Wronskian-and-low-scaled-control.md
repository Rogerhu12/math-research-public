# R119 续篇：实际两 phase 的五函数 Wronskian 与低缩放正定控制

2026-11-14，visible-exact / tail_connector。

**状态：已证明。** 本篇在同一个当前受控尾、同一个未使用
quartic 区间上，只消去真正的两条 phase 核。三个完整 Sym2 核与
这两条 phase 核的五函数 Wronskian 准确非零；其中控制横截的
两个残差之 Wronskian 完全不依赖 $\lambda=M^2$。此处保留
$Q=7+Bf$ 的常数 $7$，没有用 $B=\infty$ 的形式计算替代实际对象。

在低缩放段 $16\le M^2\le B$，本篇进一步构造真正的 $C^9$
紧支方向，其 $C^4$ 范数不超过 $1$，准确消去原两 phase，并对
完整二维复散射给
$$
 -iS_M^*DS_M[\psi]>
 2^{-22016}M^{50}B^{-39}\Delta^{-103}K_j^{-2}I_2.       \tag{F.1}
$$
与先前二十阶消去不同，局部方向只使用四阶算子。局部两行
Cauchy 门在原未使用区间的一片内直接证明，不再乘整窗的
$K_j^2$；从局部中心到真实散射端口的 $K_j^{-2}$ 仍明确保留。

这里的方向可以依赖当前 $M$。本篇没有把它作为完整非径向
多频簇的共同正定方向，也没有据此授予同权全 Green 或
$\mathcal F=0$。实际 mean、另一 Fourier 锥、ordinary/weak 源、
两 physical 端图和此前保留的截断交叉项均未删除。

## 1. 同一对象与真实的两条 phase

沿用[尺度正确中频控制](R119-supplement-scale-correct-polynomial-middle-scattering-generator.md)
的记号：
$$
 j\ge8193,\quad J=j+5,\quad
 a=\frac{\delta_j^{3/2}}{8\sqrt6},\quad B=\Delta/a,\quad
 80<\Delta<3J,\quad B>2^{190},\quad
 K_j=2^{6000}J^8\delta_j^{-16}.                         \tag{F.2}
$$
取原未使用区间的中心闭子区间 $I$，中心 $c$、长度 $\ell$，
$$
 I\subset[7/16,15/32],\qquad
 \ell=\frac1{512(n+1)(n+2)}>2^{-31}J^{-2}.
$$
其邻域中所有此前 compact 方向及两个补偿 bump 都为零，故
$$
 Q(x)=7+Bf(x),\quad f(x)=30x^2(1-x)^2,\quad
 dt=a\,dx,\quad \mu_t/\mu=-1-Q.                       \tag{F.3}
$$
原 band 编号 $n$ 是从该层的首个 middle band 开始计数；
不假设 $n$ 与 $j$ 成比例，也不假设整个 $I$ 已满足
$\Delta\ell\ll1$。下文将另取真实更短的局部片。

置
$$
 e=B^{-1},\quad F=Q/B=f+7e,\quad H=F+e,\quad
 \kappa=\lambda/B,\quad \lambda=M^2.
$$
整个实区间上
$$
 1<F<2,\quad \tfrac34<F'<2,\quad |F''|<30,\quad
 |F'''|\le45,\quad F^{(4)}=720,\quad F^{(5)}=0.        \tag{F.4}
$$
原两条 phase 核分别乘上非零常数、再乘 $F^{9/2}$ 后，
恰张成以下两个真正多项式：
$$
 p_1=F^3F',\qquad
 p_2=\Delta^2(12F^4-8eF^3+12e^2F^2)F'
             +40FF'F''-35(F')^3-8F^2F'''.            \tag{F.5}
$$
因此 $\int F^{-9/2}p_i\psi\,dt=0$ 对 $i=1,2$ 就是原来
两条 phase 的准确一阶约束。没有扩大到所有次数不超过十九的
多项式，也没有改变原补偿图。

对 $A=A^T\in{\rm Sym}(2,\mathbb R)$，$\|A\|_F=1$，以原中心
wave frame
$$
 Y=(\sqrt k\,\sqrt\mu h,\;(\sqrt\mu h)_t/\sqrt k),
 \qquad k=\sqrt{7\lambda-16}                         \tag{F.6}
$$
归一两条基本解。完整核仍为
$\mathcal K_A=Z-2\lambda Y_b+\lambda X$，不要求 $A$ 正定。
记 $g=F^{9/2}\mathcal K_A$。前篇 (S.8) 的真实三阶算子
$\widetilde{\mathscr D}=\sum_{r=0}^3A_r\partial_x^r$
满足 $\widetilde{\mathscr D}g=0$，其中 $A_3=F'F^3$。

## 2. 频率准确消去及完整 $e>0$ Wronskian

令
$$
 r_i=\widetilde{\mathscr D}p_i,\qquad
 W_{\rm res}=r_1r_2'-r_2r_1'.                         \tag{F.7}
$$
把 $F,F',F'',F''',F^{(4)}$ 暂作独立 jet，并令第五 jet 为零，
直接代入 (S.8) 给以下准确恒等式：
$$
 \partial_\kappa r_1=0,\qquad
 \partial_\kappa r_2=-32\Delta^2r_1,\qquad
 \partial_\kappa W_{\rm res}=0.                       \tag{F.8}
$$
例如第一残差为
$$
 r_1=-\frac{F^3}{8}\left[
 12\Delta^2F^4(F')^3-12\Delta^2e^2F^2(F')^3
 -8F^3F'F^{(4)}+8F^3F''F'''
 +48F^2(F')^2F'''-150F(F')^3F''+105(F')^5\right].
$$
$W_{\rm res}$ 只含 $\Delta^0,\Delta^2,\Delta^4,\Delta^6$，
最后一项系数准确为
$$
 [\Delta^6]W_{\rm res}
             =45F^8(F')^7(F-e)^3(F+e)^3.              \tag{F.9}
$$
这说明 (F.8) 是完整实际恒等式，而非高频渐近省略。

为对全部余项付清下界，记 $z=x(1-x)$。在 $e=0$ 时完整因式
分解为
$$
 W_{\rm res}(x,0,\Delta)
 =661197634560000000000000000\,z^{17}(1-2x)^7
                  [P_0+\Delta^2P_2+\Delta^4P_4+\Delta^6P_6],
                                                               \tag{F.10}
$$
其中
$$
 \begin{aligned}
 P_0&=7(135-690z+1136z^2-576z^3),\\
 P_2&=450z^6(475-1766z+1344z^2),\\
 P_4&=202500z^{12}(19-28z),\\
 P_6&=91125000z^{18}.
 \end{aligned}
$$
$1/5<z<1/4$。$P_0/7$ 与 $P_2/(450z^6)$ 在这段递减，
在 $z=1/4$ 分别大于 $24$、$117$，其余两项也正。
由 (F.9) 及 $F>1,F'>3/4$，
$W_{\rm res}(x,0,\Delta)>4\Delta^6$。

完整多项式
$$
 \frac{W_{\rm res}(x,e,\Delta)-W_{\rm res}(x,0,\Delta)}{e}
$$
在变量 $(x,e,\Delta)$ 中的系数绝对和小于 $2^{180}$。
这是随本篇脚本提供的准确有理多项式运算，未抽样。
由于 $|x|\le1$, $0<e<2^{-190}$, $\Delta>1$ 且最高
$\Delta$ 次数为 $6$，实际误差小于 $\Delta^6$。因此
$$
                         W_{\rm res}>\Delta^6.       \tag{F.11}
$$
这一结论对全部 $\lambda$ 成立。

## 3. 真两 phase 的二阶消去算子

令 $W_p=p_1p_2'-p_2p_1'$。它在 $e=0$ 的准确因式分解是
$$
 W_p(x,0,\Delta)
 =4199040000000\,z^9(1-2x)^3
                           [450\Delta^2z^6+5-8z].   \tag{F.12}
$$
其 $\Delta^2$ 系数为 $12F^6(F')^3>4$。
$(W_p(x,e,\Delta)-W_p(x,0,\Delta))/e$ 的完整系数绝对和
小于 $2^{80}$；同一 $e$ 预算给
$$
             W_p>\Delta^2,\qquad W_p<2^{72}\Delta^2.  \tag{F.13}
$$
故以下真正的二阶算子在整个实 $I$ 上无奇点：
$$
 \mathcal A=\partial_x^2+b_1\partial_x+b_0,\qquad
 b_1=-W_p'/W_p,\quad
 b_0=\frac{p_1'p_2''-p_1''p_2'}{W_p},\qquad
                       \mathcal A p_1=\mathcal A p_2=0.
                                                               \tag{F.14}
$$

这里给后续构造所需的完整系数费。将 $p_2$ 除以 $\Delta^2$，
以 $r=\Delta^{-2}$ 为独立变量。$\overline W_p=W_p/\Delta^2$
的系数绝对和小于 $2^{72}$，$\partial_x\overline W_p$ 的
小于 $2^{80}$，$b_0$ 的相应分子小于 $2^{96}$。
这些都对 $|x|,|e|,|r|\le1$ 直接成立。

在每个实点半径 $2^{-82}$ 的复盘，$\overline W_p$ 离其
实点值的变化小于 $1/4$，故其模大于 $3/4$。
只对这些明确多项式的商用 Cauchy，得到
$$
        \max_{0\le l\le5}(|b_0^{(l)}|+|b_1^{(l)}|)
                                                     <2^{520}. \tag{F.15}
$$
例如每一个商的第 $l$ 阶界可取
$l!2^{82l+97}$；两项之和仍在 (F.15) 内。没有对真实解假定
未经支付的复域。

## 4. 五函数行列式的准确降阶

令 $g_1,g_2,g_3$ 为真实三阶方程的一组基，列按
$(g_1,g_2,g_3,p_1,p_2)$ 排列，行取 $0,\ldots,4$ 阶导数。
在最后两行先作 $\widetilde{\mathscr D}/A_3$ 及其导数的
三角行变换，得到
$$
 \operatorname{Wr}_5(g_1,g_2,g_3,p_1,p_2)
  =\operatorname{Wr}_3(g_1,g_2,g_3)\,
                                    \frac{W_{\rm res}}{A_3^2}.
                                                               \tag{F.16}
$$
再以 $\mathcal A$ 及其前两导数消去 phase 两列，得到
$$
 \operatorname{Wr}_5
   =W_p\,\det[(\mathcal A g_i)^{(l)}]_{0\le l\le2,1\le i\le3}.
$$
所以从 $(g,g',g'')$ 到
$(\mathcal A g,(\mathcal A g)',(\mathcal A g)'')$ 的真实
$3\times3$ 矩阵 $\mathcal T$ 满足
$$
           \det\mathcal T=\frac{W_{\rm res}}{A_3^2W_p}
                                      >2^{-80}\Delta^4.         \tag{F.17}
$$
这里用 $A_3=F'F^3<16$。其非零性对所有 $\lambda$ 成立。

现在限定 $16\le\lambda\le B$。真实三阶方程的 monic 系数及
一阶导数由 (S.8)、(F.4) 直接小于 $2^{100}\Delta^2$；
分母 $A_3>1/2$ 已计入。结合 (F.15)，消去 $g'''$、$g''''$
后 $\mathcal T$ 每个矩阵元小于 $2^{640}\Delta^4$。
完整余子式公式因而给
$$
 \max(|g|,|g'|,|g''|)
 \le2^{1365}\Delta^4
       \max_{0\le r\le2}|(\mathcal A g)^{(r)}|.         \tag{F.18}
$$
这里使用的是整个 $3\times3$ 逆，不是只对秩一核检查符号。

## 5. 低缩放段的实际中心可观测性

记 $s=1+Q$、$b=2\lambda(\lambda-1)$。完整 Sym2 恒等式给
$$
 X=\frac{\mathcal K_{xx}/a^2+
                     (4\lambda Q-s^2-Q_t)\mathcal K}{bQ_t},
 \qquad
 X_t=\frac{(s-2\lambda)\mathcal K-\mathcal K_x/a}{b}.
                                                               \tag{F.19}
$$
在本段 $b\ge\lambda^2$, $Q_t\ge B/(2a)$,
$|4\lambda Q-s^2-Q_t|<20B^2$。设
$W=\max(|\mathcal K|,|\mathcal K_x|,|\mathcal K_{xx}|)$，则
$$
             |X|<41\Delta\lambda^{-2}W,\qquad
             |X_t|<6B\lambda^{-2}W.                  \tag{F.20}
$$
在准确中心 wave frame (F.6)，原给定矩阵 $A$ 的三项是
$$
 A_{11}=kX,\quad A_{12}=X_t/2,\quad
 A_{22}=\frac{\mathcal K+(\lambda-s/2)X_t+
                                  (\lambda Q-s^2/4)X}{k}.
                                                               \tag{F.21}
$$
$2M<k<3M$。三项分别小于
$123\Delta M^{-3}W$、$3BM^{-4}W$、
$100\Delta B^2M^{-5}W$。因为 $\lambda\le B$，
其完整 Frobenius 范数小于 $2^9\Delta B^2M^{-5}W$。
故真正的中心归一给
$$
                  W>2^{-9}\frac{M^5}{\Delta B^2}.    \tag{F.22}
$$
另一个准确核验是从 $(X,Y_b,Z)$ 到
$(\mathcal K,\mathcal K_x,\mathcal K_{xx})$ 的行列式
$8a^3\lambda^2(\lambda-1)^2Q_t$。

由 $F>1,|F'/F|<2,|F''/F|<32$ 对
$\mathcal K=F^{-9/2}g$ 微分两次，完整系数和小于 $2^9$。
(F.18)、(F.22) 因而保证在同一个中心 $c$ 有一个
$r\in\{0,1,2\}$ 满足
$$
 |(\mathcal A g)^{(r)}(c)|>
       \epsilon:=2^{-1400}\frac{M^5}{B^2\Delta^5}.    \tag{F.23}
$$

## 6. 真实局部两行上界；不再重复整窗 $K_j^2$

置 $u=\sqrt\mu h$、$N=aM\sqrt B=\Delta\sqrt\kappa$、
$\gamma=1+\Delta+N$。准确方程及实际两行是
$$
 u_{xx}+[N^2F+\tfrac{\Delta}{2}f'
                         -\tfrac{\Delta^2}{4}H^2]u=0,\qquad
 \mathcal Y=(\sqrt\gamma u,\;u_x/\sqrt\gamma).          \tag{F.24}
$$
在本段 $\Delta<\gamma<3\Delta$；其一阶矩阵的范数小于
$5\gamma$。只在
$$
 |x-c|\le r_0:=\min(\ell/8,\;2^{-12}/\gamma)
                                                               \tag{F.25}
$$
使用该系统。完整双向 Cauchy 范数小于 $2$。从 (F.6) 到
$\mathcal Y(c)$ 的两行变换准确为
$\operatorname{diag}(\sqrt{\gamma/k},a\sqrt{k/\gamma})$；
两向没有被混为一谈，其向前范数平方小于 $\Delta$。
故每条中心单位解在此片内的 $\mathcal Y$ 长度小于
$2\sqrt\Delta$，不需要整窗 $K_j$。

各阶一阶矩阵系数的有限多项式界满足
$$
       \|C^{(l)}\|\le l!(64\gamma)^{l+1}\quad(0\le l\le6).
$$
完整 Leibniz 递推给
$|\mathcal Y^{(l)}|\le2\sqrt\Delta\,l!(64\gamma)^l
 <2^{56}\gamma^l\sqrt\Delta$，$0\le l\le7$。
核的准确表达式是
$$
 \mathcal K_A=
 \frac{\gamma}{a^2}\mathcal Y_2^2+
 \frac{1+Q-2\lambda}{a}\mathcal Y_1\mathcal Y_2+
 \frac{(1+Q)^2/4-\lambda Q}{\gamma}\mathcal Y_1^2,      \tag{F.26}
$$
对一般 $A$ 取其两个实谱方向的和。系数到五阶均小于
$2^{40}\gamma^2/a^2$。实点半径 $1/8$ 复盘上，明确的
$F^{9/2}$ 无零且模小于 $2^{20}$，其前五 raw jet
小于 $2^{42}$。完整乘积和由此给
$$
 \max_{0\le l\le5}|g^{(l)}|<2^{224}B^2\Delta^6,\qquad
 \max_{0\le l\le3}|(\mathcal A g)^{(l)}|
                                    <G:=2^{800}B^2\Delta^6 .
                                                               \tag{F.27}
$$
只有显式系数用了复 Cauchy；未知两行完全使用实短片的积分方程。

## 7. 四阶紧支方向与全部 Sym2 的正定性

取
$$
 \rho=\frac{\epsilon}{16G}
      =2^{-2204}\frac{M^5}{B^4\Delta^{11}}.             \tag{F.28}
$$
$M^2\le B$ 给 $\rho<2^{-2204}B^{-3/2}\Delta^{-11}$。
由 $B>\delta_j^{-3/2}$、$\ell>2^{-31}J^{-2}$ 和
$J^2\delta_j^{9/4}<1$，有 $\rho<\ell/8$；
又 $\rho\gamma<2^{-12}$。所以整个支集位于 (F.25) 的真实
两行预算内。这一步不依赖 band 编号的额外下界。

对 (F.23) 选中的 $r$，令
$$
 f_0(x)=\rho^{r+6}
                 (1-((x-c)/\rho)^2)_+^{14},
 \qquad
 \psi_A=\sigma\,2^{-700}F^{9/2}\mathcal A^*(f_0^{(r)}),
                                                               \tag{F.29}
$$
其中
$\sigma=\operatorname{sign}((-1)^r(\mathcal A g)^{(r)}(c))$。
$\mathcal A^*v=v''-(b_1v)'+b_0v$ 是相对于 $dx$ 的准确形式
伴随。$dt=a\,dx$ 的常数将在 pairing 中保留。

$f_0$ 的最低接缝阶为 $13$，所以 $\psi_A\in C^9_c(I)$。
用 (F.15)、$F^{9/2}$ 的前四导数及
$$
 \max_{0\le l\le8}
     |\partial_y^l(1-y^2)^{14}|<2^{64}\quad(|y|\le1)
$$
作完整 Leibniz 和，得到
$$
                \sum_{l=0}^4\|\psi_A^{(l)}\|_\infty<1.
                                                               \tag{F.30}
$$
因为最大算子阶是 $r+2\le4$，在这个估计中出现的 $\rho$
幂均非负。精确分部积分给
$$
 \int F^{-9/2}p_i\psi_A\,dt
   =\sigma a2^{-700}\int(\mathcal A p_i)f_0^{(r)}\,dx=0.
                                                               \tag{F.31}
$$
两个补偿参数的一阶变动因此准确为零；并未删除它们在有限参数
盒中的真实二阶项。

由 (F.27)、(F.28)，支集内
$(\mathcal A g)^{(r)}$ 不变号，模大于 $\epsilon/2$。
且 $\int_{-1}^1(1-y^2)^{14}dy>1/8$。于是完整实际 pairing
满足
$$
 \begin{aligned}
 \int \mathcal K_A\psi_A\,dt
 &>a\,2^{-704}\epsilon\rho^{r+7}
 \ge a\,2^{-704}\epsilon\rho^9\\
 &>d_*:=2^{-22000}M^{50}B^{-39}\Delta^{-103}.          \tag{F.32}
 \end{aligned}
$$
$B^{-39}$、$\Delta^{-103}$ 包括最后的真实 $dt=a\,dx$；
不是用 $dx$ pairing 冒充物理归一。

令 $L_\psi$ 为该完整二次型的实对称 $2\times2$ 矩阵。
(F.32) 对每个 $\|A\|_F=1$ 均成立，因此允许的单位 $C^4$
方向在 $\operatorname{Sym}(2,\mathbb R)$ 中的像之对称闭凸包含半径
$d_*$ 的球。取目标 $(d_*/4)I$，用三维 Carathéodory 定理，
至多四个上述方向的凸组合给一个真实 $\psi$，仍满足
(F.30)、(F.31)，并且
$$
                          L_\psi=(d_*/4)I.           \tag{F.33}
$$
这是真正全部 Sym2 的共同方向，未把 rank-one 的下界当作
不定二次型的下界。

最后消费原完整两行到真实两端 scattering 的同一规范：
incoming 向量 $z$ 与中心态 $Y_c$ 满足
$\|z\|^2\le2K_j^2\|Y_c\|^2$，完整变分恒等式为
$z^*(-iS_M^*DS_M[\psi])z=Y_c^*L_\psi Y_c$。
所以 generator 大于 $d_*/(8K_j^2)I$，即 (F.1)。

## 8. 已付范围与后续真实接口

本篇的五函数行列式非零性对全部 $M$ 成立；局部可观测性、
紧支方向和显示的多项式下界则只用于 $16\le M^2\le B$。
高缩放区仍用已支付的完整两行 WKB 或原全部中频结论，不把
(F.27) 在 $\kappa>1$ 免费沿用。

这是当前 profile 上的真实一阶方向。若要在一个有限盒中保持
正定性，仍需原完整两 phase 补偿图及散射 Hessian；若要在
非径向混模背景中保持它，须支付实际变分响应、两个 principal
端图及全部交叉块，而不能用一个绝对小数直接除径向 gap。
原全网络所消去的 prefix/低尾/positive 块与源列也不能免费
视为常数。

普通源与 weak 源继续使用
[完整 canonical 变分合同](R119-supplement-actual-canonical-profile-generator-and-complete-weak-sources.md)
的 $\dot s-\psi Bs$、total flux 与两个 mean 行；本篇没有把
齐次二次型的正定性变成这些仿射列的 Green 范数。
physical 两端图、circle return 和
[完整高锥](R119-supplement-actual-local-wave-square-root-and-complete-high-cone.md)
中的硬投影交叉项仍保留其原权限。

实际精确计算：

- [运算源码](../scripts/fourfold_actual_two_phase_five_function_20261114.py)；
- [原生有理运算记录](../notes/2026-11-14-R119-actual-two-phase-five-function-budget.json)。

该记录包含自由 jet 恒等式、真实 quartic 全系数余项、
两个 Wronskian、全部中心三态与局部两行费用。它没有运行或
声称完成整个非线性方程。
