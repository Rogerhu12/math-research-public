# R119 续篇：完整 root-wave 网络差与高外消去后的当前低算子

2026-11-14，visible-exact / tail_connector。

**状态：解析证明，供独立审查。** 本篇接合
[完整物理 Q=7 网络差](R119-supplement-complete-physical-Q7-network-difference-and-weighted-middle.md)
与[保持酉性的高外 Poisson](R119-supplement-unitary-high-exterior-Poisson-and-buffered-angular-projections.md)。
先把完整 strict 条件数重付为 $\delta^{-8}$，包括真正 mean；
再把短负窗口的完整差送到原 root-Airy 波端口，最后在真实
共同酉表示中消去全部高外。

对 $\mathcal X\le2^{-8388608}$ 的同一实际背景，在已覆盖内部
端口上得到
$$
 \|\widehat U_a-\widehat U_0:H^1(\text{邻端口})\to L^2\|,
 \quad\|(\widehat U_a-\widehat U_0)^*:H^1\to L^2\|
 <2^{35000}J^{40}\delta^{-47}\mathcal N_{i|j}\mathcal X .
 \tag{V.1}
$$
在高外已经真实消去后，其完整低 Schur 满足
$$
 \boxed{\quad
 \|v^{-1}(S_{L,a}-S_{L,0})v^{-1}\|<2^{-6000000},
 \qquad v_j=2^{-432000}J^{-4165}\delta_j^{1073/32}.
 \quad}                                                     \tag{V.2}
$$
若存在未覆盖外端口，(V.2) 对内部低输入和内部低输出的压缩
读取；这些外端口的真实 affine/response 列仍另保。
没有对外部另添反射。开口端口直接以相邻完整 positive 元件的
输入/输出编号；未覆盖外部的 return 是另保留的外条件，不属于
这里比较的 $U_a,U_0$。将该开口接入 unitary colligation 的
恒等接线只是这一变量编号，不是一个物理边界反射。

$S_L$ 的低集合仍含无限 deep-low 与未必属于高窗的浅有限前缀。
本篇不将它的内部矩阵称为已反演的最终中频 Schur。
第7节另外把径向谱选择接到同一 root 波单位，明确所需共同参数
好集，而不把 Q=7 的逆范数免费搬到 root 端口。

## 1. 全部 strict 模和真 mean 的新条件数

采用原
[strict 完整密度](R119-supplement-actual-strict-density-complete-relative-Cauchy.md)
(S.23)--(S.28)。对非零模令 $M=1+|m|$。
在任意两个真实 strict 截面之间，原逐频证明给
$$
 2^{180}J\delta^{-1}
 \left[M^{5/3}+2^5J\delta^{-1}M^{4/3}
                       +2^{50}J^2\delta^{-6}M^{-1/3}\right].
 \tag{V.3}
$$
该式来自完整原梯度能量和真实双框架剪切，取上频率阈值之前
已经成立；不能把剪切的 $M^{-1/3}$ 项删掉。

[新 strict 斜率证明](R119-supplement-complete-strict-high-output-in-root-slope-units.md)
(S.9),(S.14) 给同一当前 radial profile：
当 $|m|\ge2^{1024}\lambda$ 时，完整径向两行 norm小于 $4/3$，
其中 $\lambda=2^{32}\sqrt J\,\delta^{-9/4}$。
余下频率有 $M<2^{1057}\sqrt J\,\delta^{-9/4}$。
将此上界分别代入 (V.3)，三项小于
$$
 2^{1942}J^{11/6}\delta^{-19/4},\qquad
 2^{1595}J^{8/3}\delta^{-5},\qquad
 2^{230}J^3\delta^{-7}.                                  \tag{V.4}
$$
第三项只用 $M^{-1/3}\le1$。非mean总费因而小于
$2^{1945}J^3\delta^{-7}$。这没有借新未付的参考 jet 界。

真正 mean 独立使用旧 (S.26)--(S.27) 的电阻积分、
密度比和完整 normal shear：
$$
                    K_{\rm mean}<2^{350}J^3\delta^{-31/4}.
$$
它与非mean合并，得到完整特征标签空间中的
$$
                    K_{0,F}<2^{2000}J^3\delta^{-8}.       \tag{V.5}
$$
这里 $31/4<8$ 是需要保留 mean 的实际收费点。

实际与同一 $\Gamma$ 径向 reference 的完整同阶 generator
差仍由原 (S.22) 及当前 $C^4$ 重实例给出：
$\int\|\Delta A_F\|<2^{256}J^3\delta^{-5}n_i$。
故 interaction 积分小于
$2^{4256}J^9\delta^{-21}n_i$。
[完整负 word](R119-supplement-complete-negative-scattering-and-network-word-in-slope-units.md)
(W.8)--(W.11) 已付的
$2^{5000}J^{20}\delta^{-30}(N_j^c)^\#$ 总和，
包括两接缝及全部浅前缀，给当前全部 interaction 和小于
$2^{241000}\mathcal X<1/64$。
六项邻胞重编号至多增加 $2^{64}$，已包含在显示的1000 bits
余量中。原 full-profile 图仍在同一个实际对象上；没有改变范数
定义来取得这个小量。

因此 actual 标签传播小于 $2K_{0,F}$。
物理 $\mathcal E_r$ 与真正标签 $\mathcal F_r$ 的两个
$2^{24}$ 转换照 Q=7 篇 (D.8) 原样保留，得
$$
 K_{\rm ph}^{\rm new}=2^{2100}J^5\delta^{-8}
 \tag{V.6}
$$
于 $\mathcal E_{-1/2},\mathcal E_{1/2}$，正反任意 strict 子段均可。

## 2. 同一 Q=7 短窗差及真实两缓冲

以下写 $\mathcal N=\mathcal N_{i|j}$、$n=4\mathcal N\mathcal X$。
深层采用原完整六项和。为覆盖已存在的浅内部片，使用同一六项
局部上界，且只求和实际存在的 $N_k^c$、$k\ge129$；
最外未覆盖分量不因此被纳入内部结论。

Q=7 篇 (D.5),(D.10)--(D.13) 的系数比较、实际参数值改变和
物理 total-flux frame 不变。只在直接 Duhamel 的两个位置
改用 (V.6)，便有
$$
 \|U_a-U_0:\mathcal E_{1/2}\to\mathcal E_{-1/2}\|
      <2^{4713}J^{13}\delta^{-21}(n+\gamma_i),\qquad
 \gamma_i<2^{200}J^4\delta^{-6}\mathcal N\mathcal X .
 \tag{V.7}
$$
没有重新乘第三个 Cauchy 因子。
完整短负窗的 scattering 因而满足
$$
 \|\Delta S_Q:H^1\to L^2\|,\quad\|\Delta S_Q^*:H^1\to L^2\|
       <2^{5500}J^{18}\delta^{-27}\mathcal N\mathcal X .
 \tag{V.8}
$$
这两个 $\Gamma^*-\bar\Gamma$ 的值已消费；
未知 Jacobi 方向中的 $D\Gamma^*$ 列仍按原 source 方程保留。

根的 balanced-to-fixed-strict 映射 $L_e$ 完全不改。
Q=7 篇 (D.18)--(D.20) 已证明
$$
 \|L_e^{\pm1}\|<2^{2300}\sqrt b,\quad
 \|\Delta L_e:H^1\to\mathcal E_{-1/2}\|
                              <2^{6700}b^{3/2}n,
$$
$$
 \|\Delta L_e^{-1}:\mathcal E_{1/2}\to L^2\|
                              <2^{11400}b^{5/2}n .
 \tag{V.9}
$$
所有 moving graph、物理 density、normal shear 和 mean 均在
这些已付完整公式中。它不使用已勘误的旧 (H.17) 低模断言。

从 balanced root 到邻近 Q=7 窗口的完整真实缓冲 $B_e$，
按 $J_Q U_{\rm st}L_e$ 及其反序 inverse 收费：
$$
 \|B_e^{\pm1}\|<K_B=2^{4800}J^6\delta^{-73/8},             \tag{V.10}
$$
$$
 \|\Delta B_e:H^1\to L^2\|,
 \quad\|\Delta B_e^{-1}:H^1\to L^2\|
     <E_B=2^{14200}J^{15}\delta^{-177/8}n .                \tag{V.11}
$$
这里 $b<2^{32}\sqrt J\,\delta^{-9/4}$。
(V.10) 的幂是 $8+9/8$；
(V.11) 最坏项是 $(2\cdot8+5)+9/8=177/8$。
逆 root 差乘 strict 的另一项仅有
$\delta^{-8}b^{5/2}$，幂为109/8。
其 bits $11400+2100+128<14200$。
这些不等式同时保正、反 buffer 和两端支交换。

## 3. 完整负根图与原 Airy 波单位

原短窗口 graph $S_Q$ 是 Q=7 incoming 到 outgoing 的完整
unitary。把左右两缓冲的 inverse 作 direct sum，并按原 outward
法向固定交换，即把这个 graph 送到整个负分量的两个 balanced
root。所有这些转换都保持完整 Green pairing。

应用 Q=7 篇的准确 Möbius 差 (D.25)--(D.26)，得到
$$
 \|\Delta S_{\rm bal}:H^1\to L^2\|
       \le4K_BE_B+2K_B^2\|\Delta S_Q:H^1\to L^2\|
       <2^{20000}J^{32}\delta^{-181/4}\mathcal N\mathcal X .
 \tag{V.12}
$$
两类真实幂分别为
$(73+177)/8=125/4$ 与 $73/4+27=181/4$。
这是完整负段，从一个真正根到另一个真正根；没有把两个 Q=7
端口识别成根端口。
实际和径向完整 scattering 酉，径向逐模对角，故 adjoint 有
同一个一阶损失门。

再转到第W、Z束使用的原自由 Airy incoming/outgoing 振幅。
在根 $\xi=0$，由完整两列 $F_m(0)$、其 Wronskian及 (J.27)
的真实 balance，固定变换及 inverse 满足
$$
             \|F_{0,e}^{\pm1}\|<2^{20}b_e^{1/3}.          \tag{V.13}
$$
这是旧 (H.16) 在根点的完整两行门，mean 另由原
$D_{\sigma,0}=c,\ D'_{\sigma,0}=i\sigma c/\pi$ 给出。
它与在 $\xi=1/64$ 的自由端架不同；
后者低非mean可达 $b^{5/6}$，本篇没有再使用错误的 $\sqrt b$ 界。

原所有 Airy 两列的 Green 常数同为 $2c^2/\pi$。
同时乘这个固定公共平方根即可和 standard root Cayley 的
$\mathsf J$ 对齐；该数已包含在 (V.13) 的 $2^{20}$ 中。
它不改变整个 scattering 算子或不同层的单位比。

(V.13) 是 actual 和 radial 共用的固定 Fourier 对角变换。
再次使用完整 Möbius 恒等式，这次 $\Delta T=0$，只收
$2K_F^2\Delta S_{\rm bal}$。
$b^{2/3}<2^{22}J^{1/3}\delta^{-3/2}$，所以
$$
 \|\Delta S_{\rm Airy}:H^1\to L^2\|,
 \quad\|\Delta S_{\rm Airy}^*:H^1\to L^2\|
   <2^{20200}J^{33}\delta^{-47}\mathcal N\mathcal X .
 \tag{V.14}
$$
未放宽的幂是 $181/4+3/2=187/4<47$。

完整 positive balanced-root graph 的差已经是
$2^{170}J^2\delta^{-2}n$；
同一个固定 (V.13) 转换给 Airy positive 差小于
$2^{400}J^3\delta^{-4}n$。
所有 positive cross、mean 和源荷仍在完整两端图中。
按 $U=R_+S_-$ 的准确有序式，一侧只收 actual $L^2$ 酉性，
另一侧只收 radial $H^1$ norm1，得到
$$
 \|\Delta U_{\rm Airy}:H^1\to L^2\|,
 \quad\|\Delta U_{\rm Airy}^*:H^1\to L^2\|
       <2^{25000}J^{36}\delta^{-47}\mathcal N\mathcal X .
 \tag{V.15}
$$

## 4. 实际共同酉表示的完整差

高外篇定义了真正 unitary $H_a$，而 $H_0$ 是同一径向对象的
相应版本。$H_0$ 按层、Fourier 对角，在所有 $H^s$ 上 norm1。
两者均准确保持 mean。

第Z束 (Z.6),(Z.8),(Z.14)--(Z.19) 的完整角预算给
$$
 \epsilon_i^c=2^{8192}J^{16}\delta^{-16}(N_j^c)^\#\mathcal X.
$$
每个真实 principal 图减其参考实平移，在所用 $C^8$ 窗内
小于 $2^{2048}\epsilon_i^c$。原 signed-density 的 FTC 保留
一次角导；随后角锥压缩和 polar 误差用第W束20阶门。
因此每个这样的 unitary 图与径向平移之差
$H^1\to L^2$ 小于 $2^{6144}\epsilon_i^c$。

同一个完整 first-phase 函数减其径向函数的 generator norm
小于 $2^{2048}\lambda_i\epsilon_i^c$；
用准确 Duhamel 比较 exponent，只对左右因素收费1。
这里也包含 individual 径向 phase 随 $\Gamma^*-\bar\Gamma$
的变化：在原 $2^{-64}$ 参数系数盘上，
新的 strict 积分界 $I_1<2^{256}\lambda_i$ 给该部分的
$\Gamma$ 导数小于 $2^{320}\lambda_i$，
乘 (V.7) 的 $\gamma_i$ 仍严格落在上述 $\lambda_i\epsilon_i^c$
宽界内。根 germ 没改变。没有把仅保持的总 $\beta$ 误说成
每个分段 phase 都完全不变。

沿有限且少于32个模型因素展开，右侧完整 $H^1$ 子乘积小于
$2^{64}$，左侧只用 $L^2$ unitary。因此可安全取
$$
 \|H_a-H_0:H^1\to L^2\|,\quad
 \|H_a^*-H_0^*:H^1\to L^2\|
                       <2^{15000}\lambda_i\epsilon_i^c .
 \tag{V.16}
$$
adjoint式也由
$H_a^*-H_0^*=-H_a^*(H_a-H_0)H_0^*$ 准确得到。
mean 恢复和 polar 的有限秩列没有另被删除。

令 $\widehat U_a=H_a^*U_aH_a$、
$\widehat U_0=H_0^*U_0H_0$。应使用如下准确次序：
$$
 \begin{split}
 \widehat U_a-\widehat U_0={}&
 H_a^*(U_a-U_0)H_0+
 H_a^*U_a(H_a-H_0)\\
 &+(H_a^*-H_0^*)U_0H_0 .
 \end{split}                                             \tag{V.17}
$$
第一项右因子是 radial $H_0$，第二项只有右端差索取一阶，
第三项右因子 $U_0H_0$ 仍径向。
因此从不要求 actual $U_a$ 具有 norm1 的 $H^1$ 界。
(V.15)--(V.16) 即给 (V.1)；
其中 $\lambda\epsilon^c$ 的 $\delta$ 幂只有 $73/4<47$。
adjoint一阶门用 actual 酉性和 radial $H^1$ 对角性同样得到。

## 5. 真高外 Schur 差：一次角导按各层 T_i 支付

使用高外篇的真实正交 $P_H$，其共轭回原波端口的投影为
$H_aP_HH_a^*$，没有改成原物理角的裸尖 cutoff。
高外的两个 Poisson 记为 $E_{H,a},F_{H,a}$。
同一径向 Poisson 还满足该篇 (H.25)：
$$
 \|v^{\pm1}F_{H,a}v^{\mp1}\|<2^{-9000},\qquad
 \|\Omega_Hv^{\pm1}E_{H,0}P_{L,\mathrm{int}}v^{\mp1}\|<2^{-9000},
$$
$$
 \Omega_i(m)=\max(1,\langle m\rangle/(1+T_i)).
 \tag{V.18}
$$
原完整 mean、外输入和所有低频属于 $P_L$。
这里 $P_{L,\mathrm{int}}$ 是已覆盖内部层中
$|m|<T_i$ 的真正低输入投影，包含这些层的 mean。
径向 $E_{H,0}$ 对角，所以仅在这一内部低输入上 $\Omega=1$；
同时 $\langle m\rangle<2T_i\Omega_i(m)$。
这正好支付 (V.1) 在每一个真实内部输入层索取的一阶角导。
未覆盖外口按高外篇取 $P_H=0$，因而其 $P_L$ 可含任意高频；
不对这些外输入声称 $\Omega=1$ 或上述收益。
它们继续采用原 $H^1$ / affine-source 端口合同。

准确 Schur 差是
$$
 S_{L,a}-S_{L,0}
   =\begin{pmatrix}I&F_{H,a}\end{pmatrix}
       (\widehat U_a-\widehat U_0)
       \binom I{E_{H,0}} .
 \tag{V.19}
$$
(V.19) 的代数式先在全源定义域成立；下述 $L^2$ 小量估计
只用于其两端均取 $P_{L,\mathrm{int}}$ 的内部压缩。
先在有限层、有限 Fourier 内部低输入上证明；此时 radial 高外只有
有限层，所有真实项位于原有源 inverse 的定义域。
随后用 (V.18) 和下列统一界延拓，不能事先给 $R_H$ 一个
不存在的有界 $L^2$ 全源 inverse。

在中间的差因子左右插入 $v$，并在右侧插入
$T^{-1}\langle D_\theta\rangle$。
左增广 Poisson 在相应 $v^{-1}$ 权中 norm小于2；
右增广 Poisson 连这个一次角导，在 $v$ 权中 norm小于4。
对差的每个邻块，因而只需
$$
 v_i^{-1}\epsilon_i T_k v_k^{-1},
 \qquad
 \epsilon_i=2^{35000}J_i^{40}\delta_i^{-47}\mathcal N_{i|j}\mathcal X .
$$
完整行列和，包括所有相邻层的固定比，安全地小于
$$
 2^{1000000}J^{8400}\delta^{-1969/16}
                           \mathcal N_{i|j}\mathcal X .
 \tag{V.20}
$$
幂准确是
$$
                    47+9+1073/16=1969/16=123+1/16 .
$$
这里没有再额外乘 $M$ 或全高 resolvent；该费用已由
(V.18) 的真实右 Poisson 消费。

## 6. 全有限前缀与无限深尾的同一小量

深层六项和保持原
$$
 \mathcal N_{i|j}<2^{-20010}
                  2^{-(31867/256)(j-8193)}.
$$
在 $8193\le j\le16384$，用 $J<2^{15}$、
$\delta_{8193}^{-1}<2^{8197}$，并保留
$\delta^{-1969/16}\mathcal N$ 的真实下降因子，
(V.20) 的二进制指数小于
$$
 1000000+8400\cdot15+\frac{1969\cdot8197}{16}
                         -20010-8388608<-6000000 .
 \tag{V.21}
$$
真实剩余幂为
$$
 \frac{31867}{256}-\frac{1969}{16}=\frac{363}{256}>1 .
$$
$j\ge16384$ 后 $(1+1/J)^{8400}<2$，所以继续至少按
$2^{-107/256}$ 下降。这里没有在首层错误地把8400次多项式比
估成小于该尚不足的剩余幂。

浅内部层使用第W束 (W.8) 的真正原规范：
$$
 N_j^c<
 \begin{cases}
 2^{220}\delta_j^{7/4},&129\le j\le4096,\\
 2^{185}\delta_{4096}^{-3/2}\delta_j^{827/256},
                                      &4097\le j\le8192 .
 \end{cases}
$$
六邻胞的 reindex 与有限条数可宽放 $2^{400}$。
首段用 $\delta^{-1}<2^{4100}$、$J<2^{15}$，
第二段用 $\delta^{-1}<2^{8197}$ 和
$\delta_{4096}^{-3/2}<2^{6150}$。
对应的指数分别小于
$$
 1000000+126000+400+220
              +(1969/16-7/4)4100-8388608<-6000000,
$$
$$
 1000000+126000+400+185+6150
              +(1969/16-827/256)8197-8388608<-6000000 .
 \tag{V.22}
$$
因此全部已覆盖内部层的行列 Schur 上界统一给 (V.2)。
这是完整前缀加无穷尾的解析不等式；没有只在 deepest 层套用
第三段幂，也没有删除两个规范接缝。

## 7. 同一五盒的径向谱门可接到 root 波端口

这一段说明如何在原参数选择本身付 root 单位，而不使用
$Q=7$ 与 root 两种 resolvent 范数免费相等的假设。
仍先保持原可控层 $j\ge8193$ 和
$I_M=\{i:A_j\le M\le T_j\}$，$M\ge M_*$。
无限 deep-low 和左侧真实前缀按原准确允许线消去，source不删。

五盒篇的每个实际 local crossing form 是物理中心的完整两态型。
从该中心到任一 root-Airy 端口，先用准确 density 转换，
其非mean逐频 norm小于 $2^{65}B^{3/4}$：
$w_d=\sqrt q\,u$、$\zeta_d=\sqrt{k/q}Z_2+
Q_tZ_1/(4Q^{5/4}\sqrt k)$，径向 shear 先准确抵消，
$q\asymp\sqrt B$，$|Q_t|<C B^2$。
随后按真实次序用 (V.6)、(V.9) 的完整 inverse及 (V.13)。
(V.9) 已经包括整个 root Cauchy，不再额外重复乘一次。
它们给中心到左右两 root incoming 的共同充分界
$$
                       K_j=2^{6000}J^8\delta^{-16}.      \tag{V.23}
$$
实际未取粗的 $\delta$ 幂只有
$9/8+8+9/8+3/4=11$，$J$ 幂小于7，bits小于5000。
所以 (V.23) 仍是五盒篇已经用于全部方向的同一个保守 $K_j$。
两个 mean 不参与该非零频率 crossing 门，仍在完整网络另保。

因而五盒篇 (Q.9) 的三个 $D_{jM}$ 在完整 root 负散射中仍成立。
其低、紧、高组的原 constants 余量均超过这里两个端口的固定
范数计数；没有在换端口后保留一个未支付的 local form。
两原相位在每条局部参数线准确固定，root germ 和外正图不变。

五盒篇 (Q.10)--(Q.18) 的目标 $z$ 计数也仍适用：
先在各控制支集内取原 near-identity local transfer，
其外所有 fixed root/buffer/positive 片都吸收到同一个外
selfadjoint relation 中。完整 transmission 仍非零，
所以 target eigenspace 与该关系严格等价，$2|I_M|$ 次数不增加。
因此同样的逐频坏集估计和逐窗 $\mathcal W$，现在给
$$
            \|\mathcal W_M(I-U_M^{\rm root})^{-1}
                               \mathcal W_M\|\le1 .
 \tag{V.24}
$$
可同时保留旧 Q=7 条件：把两个闭好集相交。
每组的总坏测度小于 $5/16384$，与原外 good-$t$ 的
$83/16384$ 合计仍小于 $93/16384<1$。
在这个共同非空紧集中按同一顺序固定一个点。
这是对尚未数值枚举的实际公共参数选择的明确细化；
所有 full-profile、joint、incoming 和物理门本来对整个
允许五盒统一，所用每项常数上面已重新消费。

$H_0$ 在 radial root 波中按层 Fourier 对角 unitary，
且 $\mathcal W_M$ 每个窗口对两 incoming 槽取相同标量，
故它与 $\mathcal W_M$ 交换。(V.24) 也可以在该 radial
共同酉表示中读取。由 $v\le\mathcal W$，相应 $vRv$ 门保留。

(V.24) 的有效 $U_M^{\rm root}$ 仍已经消去真实 low-tail 和
未保留前缀；它不等于尚含这些未知的 $S_{L,0}$。
因此 (V.2),(V.24) 之间还需要这两类真实外 Poisson，不能直接
写成一个最终 Neumann inverse。

## 8. 原源、joint 及当前真实剩余量词

本篇所有端口都先使用 total flux。
root、strict、graph 的 body 源和 weak 端荷按照原精确 Piola、
height 共轭及端图读取。完整 graph 源为
$(D-SB)q+f_v-Sf_u$；其两个 mean 电荷不能清零。
若要 bare flux，仍由真实 producer 提供并减去 $F^t$ 端点迹。
本篇没有从粗径向体源虚授混合图 trace 的 norm。

参数值比较已经含 $\Gamma^*-\bar\Gamma$；
真正变分系统仍是
$$
 (I-\widehat U_a)x=\widehat g_{\rm ord,weak}
                 +\widehat{\mathcal B}_a\dot\Gamma
                 +\widehat g_{\rm ext},\qquad
 \mathcal C_a x+\mathcal A_a\dot\Gamma=g_{\rm phase}.
$$
高外消元按已付真实 (H.23) 同时作用每一列。
它不消除原 source-to-label 转换或把当前
$D\Gamma^*$ 当成径向基点的零导数。

特别，旧可控集合从8193层开始；当 $M$ 接近 $M_*$ 时，较浅的
129--8192层未必满足 $M\ge T_j$。不能把这一实际有限前缀
误名为本篇已经付清的“高外”。无限 deep-low 允许线同样须以
真实强解和完整 affine 数据消费。
接下来必须付这两种外 Poisson、原标签权及 joint 列，才能把
(V.2) 真正接到 (V.24)；最终非线性外匹配仍是原完成标准的一部分。
