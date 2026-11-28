# R149 WMT：原全 Θ 的有权 model receiver 与新的完整导数残差

**已证明；下面14个新算术目标尚须实际运行。**
2026-11-28。本文给出同一个 UACT/OT 原全算子的新可执行误差界，
并明确其原载体、新8192点输入和不重复旧目标的执行方式。
它针对现有 global Θ error 的512倍 one-loss 放大；绝不把已成
low96 error 当成全频误差。配套纯公式和 owner 只形成新的完整目标。

## 1. 全部保持的原对象

采用 [UACT](R149-supplement-actual-original-finite-Theta-coordinate-inverse.md)、
[UDR](R149-supplement-unit-disk-phase-errors-in-original-Theta-rows.md)、
[TM](R149-supplement-original-model-adjoint-on-complete-finite-Theta-rows.md)
的完整空间、归一测度、频率 $4n$、同一隐式 selected member 和真相位。
记 $G=|\partial_x|^{-1}$、$I=\partial_x^{-1}$，
$T=(C^\dagger)^{-1}$，原96列 $Z=TB$，原完整192模式 trial $Y$。
以下 $B$ 是这条 density 坐标方程的原右端 $B e_j=ND_+e_j$；
target normalizer 仍写 $\mathcal B$，二者不混用。

原 residual 和 row error 为

$$
 R=C^\dagger Y-B,\quad E=Z-Y=-TR,
\qquad
 \Delta r=A^*GZ-\widehat A^*GY,
\quad A^*=Id+I\mathcal T_\alpha .                 \tag{WMT.1}
$$

原 IR 全频证书、SDI 和 UACT 给整个联合界

$$
 \|E\|_{\dot H^{-1/2}}\le H:=\epsilon_H,
\quad \|E\|_2\le S:={51\over50}
       (\epsilon_0+{10\over9}\epsilon_H),
\quad \|\Delta r\|_{H^1}\le E_{V,1}.             \tag{WMT.2}
$$

所有范数均为 $\ell^2_{96}$ 到相应完整函数空间的 operator norm。
$E_{V,1}$ 直接复制 UACT 的第9个完整记录。
原完整 $\widehat\Theta$、$E_M$ 和
$E_\Theta^{old}=850.945862\ldots$ 全部保留。

记 UACT 原四 whole products 中两个 $L^2$ candidates 为

$$
 P_Y\ge\sqrt2\,W D_2,\qquad
 P_E\ge {S D_2\over3},\qquad
 D_2\ge\|\alpha-\widehat\alpha\|_2,\quad
 W=\sum_{n=1}^{192}\left(\sum_j|Y_{nj}|^2\right)^{1/2}/(4n).
                                                        \tag{WMT.3}
$$

这里 $W$、$S$ 是 UACT 完整产品公式使用的确定 saved-bound
coefficients；(WMT.3) 指该公式的完整已保存 upper。
本文只消费 $P_Y,P_E,W$ 的 whole records，不恢复缺失的逐模
误差、不从一个 operator upper 反推出未知输入范数。
尤其未把 $S$ 解释成真实误差的 lower。
由已成原球 $H>.14,\epsilon_0>.435$ 的有理比较，定义的
$S>3/5$。这只比较确定的配权常数。

## 2. 同一个 density inverse 的实际 H1 bootstrap

[SDI](R149-supplement-actual-small-density-inverse-constants-and-Theta-errors.md)
对真 $p=\mathcal H\circ X_-^{-1}$ 已给

$$
 {9749\over10000}<p'<{10251\over10000},\quad
 |p''|<1/6,\quad \|T:L^2_0\to L^2_0\|<8/5 .       \tag{WMT.4}
$$

令 $m=9749/10000$、$M=10251/10000$、$d=251/10000$。
密度算子 $U_p f=p'f\circ p$ 满足

$$
 [\partial_x,U_p]f=p'' f\circ p+(p'-1)p'f'\circ p .
$$

其同号压缩恰给 $[\partial_x,C^\dagger]$。
归一换元给

$$
 \|[\partial_x,C^\dagger]f\|_2
 \le {1\over6\sqrt m}\|f\|_2+d\sqrt M\|f'\|_2 . \tag{WMT.5}
$$

两个 sign blocks 正交，每个压缩的 norm 不超过原完整作用的
norm；不额外乘 $\sqrt2$。

先证明正则性而不预设 $Tf\in H^1$。
在完整 $L^2_0$ 上定义 $L=\partial_x C^\dagger I$。
由于 $I:L^2_0\to H^1_0$，这是有界算子，且

$$
 \|L-C^\dagger\|\le d\sqrt M+{1\over24\sqrt m}.
$$

由 $\sqrt M<81/80$、$m^{-1/2}<51/50$，有
$(8/5)(d\sqrt M+1/(24\sqrt m))<1$。
所以 $L=C^\dagger[Id+T(L-C^\dagger)]$ 有真双侧逆。
对 $h\in H^1_0$，$z=I L^{-1}h'$ 满足
$(C^\dagger z-h)'=0$，而两者的 mean 都是零，故 $C^\dagger z=h$。
原逆唯一性给 $z=Th\in H^1_0$。
现在可以在 (WMT.5) 中用 $z=Th$，得到

$$
 \|z'\|_2\le
 {8/5\over1-(8/5)d\sqrt M}
       \big(\|h'\|_2+{1\over6\sqrt m}\|z\|_2\big)
 \le {17\over10}\big(\|h'\|_2+{17\over100}\|z\|_2\big).
                                                        \tag{WMT.6}
$$

这些有理比较使用的都是真实全空间逆，未用 finite-section
onto 假设。因此一个新完整 $\varepsilon_1\ge\|\partial_xR\|$
立即给

$$
 E_1:={17\over10}(\varepsilon_1+{17\over100}S)
       \ge\|\partial_x E\|.                            \tag{WMT.7}
$$

## 3. 全8192点、2048 head 的新导数 residual

原 IR trial 保持其全 `[192,96,2]` SHA
`02ee6051166f1f23139b39984dbd309592c415405620f99982a3972d8dd49db1`。
原4096点完整 grid 保持 SHA
`74ba633b63b22fff209c2a42cc5bebe66c25ed3acc3e7c8bb7a3c9bc6563ea0f`。
新8192 grid 的偶数点直接读这份完整原 grid；仅另求4096奇数点的
同一个 finite compound $\widehat p=K_{48}\circ A_-$。
原 terminal mean、全部129 terminal coefficients 和48对
postcomposition coefficients 均保留。

给任意 unit real $c$，正频 primitive

$$
 a_c(x)=\sum_{n=1}^{192}{(Yc)_n\over4in}
                        e^{4in\widehat p(x)}
$$

在原完整 image width $w$ 上有统一新界

$$
 M_Y=\sum_{n=1}^{192}{e^{4nw}\over4n}
       \left(\sum_j|Y_{nj}|^2\right)^{1/2} .           \tag{WMT.8}
$$

每条 trial 的整8192点有向 complex DFT 保存读回。
对 $1\le k\le K_R=2048$，其完整 alias upper 是

$$
 M_Y\,{e^{-4\sigma(N-k)}+e^{-4\sigma(N+k)}
                 \over1-e^{-4\sigma N}},\qquad
 N=8192,\quad\sigma=1/256.                           \tag{WMT.9}
$$

这是所有非零 aliases 的几何级数；$M_Y$ 同时支配每一条 column。
乘 $4ik$，在 $k=j$ 减原完整正 RHS $2j(1-i)$，得到
$R^{head}_{j,k}$ 的整 complex ball；补负频 conjugates。
全96条2048 head 先保存读回，再形成所有9216个 signed Gram entries

$$
 \Gamma_{ij}^{R,1}=2\operatorname{Re}
       \sum_{k=1}^{2048}(4k)^2
                  \overline{R^{head}_{i,k}}R^{head}_{j,k}. \tag{WMT.10}
$$

完整 Gram 的 Gershgorin upper 给新 $g_{R,1}$。
原 IR99 的4096-grid/1024-head残差和它的 norm reducer 不调用。
这里是同一个真 residual 的新导数范数与全新的 alias/head 输入。

令 $q=e^{-8\sigma}$。未求的整个 finite-compound output tail 为

$$
 t_1=M_Y\sqrt{512\sum_{k>K_R}k^4q^k}.              \tag{WMT.11}
$$

系数512等于两频号乘 $(4k)^4$。
所有几何四阶矩由其准确 positive rational generating functions
求出；不是一个首 omitted mode。

再支付同一个真 $p$ 与 $\widehat p$ 的差。
由原 IL 完整 $E_p$，$\|\delta^{(r)}\|_\infty\le r!E_p\sigma^{-r}$
对 $r=0,1,2$ 成立。两个端点及其整条 homotopy 有相同
$m,M,1/6$ 的 first/second derivative bounds：finite端由原
$P_1<1.024974,P_2<.132457$，true端由 (WMT.4)。
直接对 $\partial_x U_{p_t}f$ 求参数导数，所有项准确是

$$
 \delta'' f(p_t)+p_t''\delta f'(p_t)
  +2p_t'\delta' f'(p_t)+(p_t')^2\delta f''(p_t).
$$

用真实换元及全 $t\in[0,1]$ 积分，若新完整 trial Gram 给
$Y_d\ge\|\partial_x^dY\|$，$d=0,1,2$，则

$$
 m_1={E_p\over\sqrt m}
   [2Y_0/\sigma^2+(1/6+2M/\sigma)Y_1+M^2Y_2]          \tag{WMT.12}
$$

界整个 true-map 导数误差。因此
$\varepsilon_1=g_{R,1}+t_1+m_1$ 是完整新 residual upper。
三个 $Y_d$ 同样由全192模式、全部96列的9216-entry signed Gram
求得；它们不是原 $GY$ 的已成范数重算。

## 4. 使用旧 whole products 的完整二导 row error

记 $K=2048,M_Y^{mode}=192$，$A_0$ 为原 OT 保存的完整
$\widehat\alpha$ Wiener upper，$T_\sigma,E_3,m_{AS}$ 为整个原
ASR global inputs。原 AS.3、13–14 对所有 $|n|>K$ 的相同
两项分解给新的导数尾

$$
 T_1=1088T_\sigma\sum_{n>K}n^2e^{-4m_{AS}\sigma_{AS}n}
          +{17E_3\over2(K+1)},\quad \sigma_{AS}=1/128 . \tag{WMT.13}
$$

解析项用 $|\alpha_n|\le136n T_\sigma q^n$，再乘 $4n$
及两个频号。非解析项从原 third-derivative source error
到 $\alpha'$ 的完整 multiplier 是
$544n^2/(4n)^3=17/(2n)$。
这是一阶导数的全新尾目标，原零阶 AS tail 未重算。

精确差分 (WMT.1) 给

$$
 \Delta r=GE+I\mathcal T_{\widehat\alpha}GE
            +I\mathcal T_{\alpha-\widehat\alpha}GE
            +I\mathcal T_{\alpha-\widehat\alpha}GY .    \tag{WMT.14}
$$

物理导数与 sign projections 交换。对最后两项再求一导时，
不能漏掉 coefficient derivative 或未知 inverse error。
由完整 $\dot H^1$ Sobolev product
$\|\mathcal T_f Gh\|_2\le\|f\|_2\|h\|_2/3$，
以及 finite head Bernstein，逐项得到

$$
 \boxed{\begin{aligned}
 E_{V,2}:={}&E_1+A_0S+4K A_0H/2\\
 &+(4K+5E_1/3)P_E+ST_1/3\\
 &+4(K+M_Y^{mode})P_Y+\sqrt2 W T_1
 \ \ge\|\partial_x^2\Delta r\| .
 \end{aligned}}                                           \tag{WMT.15}
$$

具体地，$\|(\alpha-\widehat\alpha)'\|_2\le4K D_2+T_1$。
该式在 (WMT.14) 的 $GE$ 上给 $4KP_E+ST_1/3$；另一个
导数落在 $GE$ 时，由 $S>3/5$ 的**确定配权比较**，
$D_2E_1/3\le(5/3)E_1P_E$。
在 $GY$ 上，导数落在 coefficient 给 $4KP_Y+\sqrt2 WT_1$；
导数落在 $GY$ 给 $4M_Y^{mode}P_Y$。
其余两项使用 $\|GE\|_2\le H/2$、$\|E\|_2\le S$ 和
$\|\widehat\alpha'\|_\infty\le4K A_0$。
所有 factors 的位置与 original same-sign $I\mathcal T_\alpha$
一致。没有从旧 subtotal 中减掉任何费用。

## 5. 全有限 model head 和完整 infinite tail

原完整低 reference $\gamma_n=1$ 对 $n\le96$ 保持；
高频 $\gamma_n$ 就是 TM.2 的 signed multiplier。
先独立恢复原 entire2240 model-multiplier carrier 并严格核其
original whole SHA，保全部 $b,\Omega,\mu$ balls。
新 arithmetic 只延续 $2241\le n\le L=2^{20}$ 的自然全序列。
全部 signed denominators/reciprocals 先完整保存读回，再形成

$$
 k_L=\max_{1\le n\le L}{|\gamma_n|\over4n}.          \tag{WMT.16}
$$

这不是重算旧7416个 Cayley label/root distances 或旧 gap gate。
它是这个原 graph-model 的新完整有限 weighted norm。
所有 native parameter qualifications 仍从整 CYA/OT inputs 准入。

在全部 $n>L$，令 $t=\nu/(4n)=\beta/(2n)$，CYA 的精确
$c_n=e^{4in\Omega}(1+it)/(1-it)$ 给

$$
 2|\cos(2n\Omega+\pi/4)-t\sin(2n\Omega+\pi/4)|
       =\sqrt{1+t^2}|c_n-i| .
$$

原已证全 native gap $|c_n-i|\ge1/(1024n)$ 因而给
$|\gamma_n|\le2048n$，即新的完整二阶权尾

$$
 \sup_{n>L}{|\gamma_n|\over(4n)^2}
          \le k_{tail}:={128\over L+1}.                \tag{WMT.17}
$$

对于每个 unit $c$，真实 target 的正交 $v_n^a$ 坐标将
$\overline G^*\Delta r c$ 的 head/tail 平方准确分开。
(WMT.2)、(WMT.15–17) 因而证明

$$
 \boxed{\quad
 \|\Theta-\widehat\Theta\|
 \le E_\Theta^{WMT}:=
       \sqrt{(k_LE_{V,1})^2+(k_{tail}E_{V,2})^2}+E_M .
 \quad}                                                  \tag{WMT.18}
$$

原 UACT global candidate 与 (WMT.18) 都必须保存，只有两个
整个候选正式存在后才取较小者。没有预报新候选必定更小。
反射相位没有被归零，two physical means 始终在独立 slots。

## 6. 对实际 BFP19 的唯一后继消费

在 BFP19 真正完整成功之后，保全部96 exact signed centers、
全部旧 fees、完整 phase 和 independent means。以完整选中的
$E_\Theta$ 替代 BFP.22 中相同 global slot，得到新的整个

$$
 E_{\nu}^{WMT}=(B_{\widehat\Theta}+E_\Theta)\delta_X
                   +E_VB_{model}+E_MB_x+E_{pair}.        \tag{WMT.19}
$$

每个其余量只能从 BFP whole actual/execution 原记录复制；不重跑
forward solve、8192 pullback、old norms、model preimage 或96 pairings。
若 BFP 未完整成功，本条不产生一条虚构的 signed $\Theta\nu$ 列。

本次14目标依序为三个 trial Gram norms、primitive strip vector
bound、导数 residual head Gram/tail/model/whole bounds、inverse
derivative error、alpha derivative tail、full row second-derivative
error、model full-head/tail weights 和最后同一全 $\Theta$ error。
整个大中间数组留在 Actions private workspace，只公开完整 SHA、
scope 和全部新 bound。只有实际 complete 的 whole receipt 能供
后继消费。本条仍不把有限坐标逆变成 full physical Schur，
也不宣称 homogeneous inverse、matching 或最终闭等距族已成。
