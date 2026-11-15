# R168：修正低层 action 的真实反射奇偶与四条字符头部关系

日期：2026-11-15。**已证明。** 本稿只有纸面论证，并只读已发表 head 的状态键。没有新的研究原式编译、profile 评价、路径积分或候选优化。

依据 [R70](R70-zero-matrix-bridges-and-affine-complete-fourth-period.md)、[R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md)、[R109](R109-local-density-of-the-complete-fourth-quotient.md)、[R130](R130-true-fourth-span-from-horizontal-normal-coefficients.md)、[R140](R140-full-action-multiplier-equivalence-for-real-cost-positivity.md)、[R145](R145-true-curvature-reflection-and-even-positive-characters.md)、[R163](R163-complete-normal-coefficient-cocycle-and-single-weight-character-head.md) 和 [R164](R164-covariant-eight-matrix-multiplier-for-positive-affine-characters.md)。

**结论。** 对任一真实权 −2 仿射字符，按 R164 扣掉同一个唯一协变矩阵乘子后，完整开路径 action 在真实 $(k,\omega)\mapsto(-k,-\omega)$ 下不变。二次层因此准确满足

$$
b_0(-k)=b_0(k),\qquad b_1(-k)=-b_1(k),\qquad b_2(-k)=b_2(k).
$$

证明不先要求字符正。因而这些等式不仅是正性测试，也是完整权 −2 字符头部的真实线性关系。对已发 head 的原系数索引，得到

$$
\boxed{\lambda(V_{26})=\lambda(V_{41})
=\lambda(V_{61})=\lambda(V_{67})=0.}
$$

八参考态的规范化本身不反射对称；本稿保留其完整 cocycle。尤其一般 $\lambda F_0$ 并非偶函数，不能用未经矩阵修正的静态系数代替修正 action。

## 1. 真实反射及八矩变换

令 $\sharp$ 为 R145 的真实路径变换

$$
h^\sharp=h,\quad k^\sharp=-k,\quad \omega^\sharp=-\omega,
\quad F^\sharp=E F E,\quad \alpha^\sharp=-E\alpha,
\quad E=\operatorname{diag}(-1,1,1).
\tag{1}
$$

允许中心线另作常量平移。它保持时间方向、$h>0$ 和真实水平约束

$$
\omega_s=\frac{k_s}{2h}.
$$

初、末 scalar germs、末 frame 均作真实变换。原输入槽、右锚和全部 history 沿用 R145；不是把 profile 支撑镜像后重新换锚，也不是物理取 $h<0$。

R145 已证明完整成本作用为

$$
V_{B^\sharp}=\mathsf S V_B,\qquad
\mathsf S=\mathsf P_{-1,0}^{\rm alg}.
\tag{2}
$$

后一个负数只用于有限 Laurent 表示的代数延拓。在真权 −2 上它等于恒等。因此若

$$
\lambda(R)=0,\qquad
\lambda\mathsf P_{H,d}=H^{-2}\lambda
\quad(H>0,\ d\in\mathbb R),
\tag{3}
$$

则

$$
\boxed{\lambda\mathsf S=\lambda.}
\tag{4}
$$

八矩方向顺序固定为 $(p_0,p_1,p_2,r_0,r_1,s_0,s_1,t_1)$。直接从 R73 的完整矩阵密度得到

$$
\boxed{m^\sharp=J_8m,\qquad
J_8=\operatorname{diag}(-1,1,-1,-1,1,1,-1,1).}
\tag{5}
$$

这同时包含 $m_0$ 和 $m_2$，不是只对常态矩阵求符号。例如 $d_{\rm geom}=h\omega-k$ 及
$d_{{\rm geom},s}=h_s\omega-k_s/2$ 都变号，而 $1+d_{\rm geom}^2$ 与
$h_s(1+d_{\rm geom}^2)/h-2d_{\rm geom}d_{{\rm geom},s}$ 不变；代入八矩原式给出 (5) 的每个符号。因此

$$
M_{B^\sharp}=J_8M_B.
\tag{6}
$$

## 2. 固定八参考规范化，不假设其反射对称

沿用 R163 的

$$
S_i^*=(1,k,d+k),\qquad
d\in(0,1,-1,2),\quad k\in(0,1),
$$

矩阵坐标 $a_i(M)$ 和

$$
\Gamma(M)=\sum_i a_i(M)L_0(S_i^*),\qquad
F_0=L_0-\Gamma(m_0).
\tag{7}
$$

二次层同样减去 $\Gamma(m_2)$，随后作完整正规化，得到 $\widehat Q_2$；最高正规层记为 $\widehat L_4$。R130 保证这些规范化族的所有真实 profile 系数属于 U。定义

$$
\Lambda(B)=\int_B\lambda(F_0+\widehat Q_2+\widehat L_4)\,ds.
\tag{8}
$$

全部边界势在平端路径的两个常值 germs 上分别为零，故 (8) 与规范化原局部密度的积分相同。它对真实平端拼接准确相加，但不把一般非零 M 路径的完整 V 误当可加量。

参考状态集合包含 k=1 而不包含 k=−1，故不得假设 $\Gamma$ 与反射交换。为准确测量其差，置

$$
J_\sharp(B)=\Lambda(B^\sharp)-\Lambda(B).
\tag{9}
$$

下面证明存在**同一个** $\beta_\sharp\in E_8^*$，使全部真实开平端路径满足

$$
\boxed{J_\sharp(B)=\beta_\sharp(M_B).}
\tag{10}
$$

### 2.1 从零矩阵闭端口到全部端点

首先，若 B 同 scalar germ、frame $I\to I$、$M_B=0$，R109 给
$\Lambda(B)=\lambda(V_B)$，无需预设第三成本 T=0。这样的 $V_B$ 确在 U 中：按 R130 的真倒行，
$BB^R$ 是实际 $M=T=0$ 字且 $V_{BB^R}=2V_B$。反射后的路径也有这些性质。由 (2)、(4)，$J_\sharp(B)=0$。

其次，取两条 scalar 闭路径，具有同一末 frame A 和矩阵 M。R70 给同一个真实补偿段，将它们各自补到 frame I、矩阵 0。局部可加性和上段零式说明二者的 $J_\sharp$ 值相同。于是该局部积分下降到 $SO(3)\times E_8$ 的端点纤维上。它是连续加法同态：拼接给加法，环境旋转不改变局部密度，R70 的局部光滑截面给连续性。$SO(3)$ 紧，故其到实数的连续加法同态为零，只剩一个矩阵线性函数。

此时才对任意**开** scalar 路径 B 使用真倒行。其局部完整导数权为 0、2、4，所以 $J_\sharp(B^R)=J_\sharp(B)$、$M_{B^R}=M_B$。虽然 $BB^R$ 的 frame 通常不是 I，上一步已覆盖全部末 frame，故可对该 scalar 闭词使用矩阵公式，再除以 2，得到开路径公式。

最后，不同起始 germs 之间用 R70 的真实零矩阵桥比较。桥与其倒行构成零矩阵 scalar 闭词，所以其局部差为零；在两侧接同一任意矩阵路径，便证明不同 germs 得到的是同一个线性函数。由此得到 (10)。

这一论证没有对完整 V 作未经支付的接缝相加，没有要求实际第四成本可取负，也没有把非恒等 frame 的倒行先当成闭 frame。

### 2.2 反射 cocycle 的准确参考态公式

在参考状态 $S_i^*$ 取任意正时长的常态路径。它的 frame 可以旋转；式 (10) 已允许所有末 frame，所以仍可直接使用。由原式 $F_0(S_i^*)=0$，得到

$$
\beta_\sharp(m_0(S_i^*))=\lambda F_0((S_i^*)^\sharp).
$$

八个矩阵构成基，因此

$$
\boxed{\beta_\sharp(M)
=\sum_i a_i(M)\lambda F_0((S_i^*)^\sharp).}
\tag{11}
$$

这就是固定八参考规范化的反射缺陷，不能默置为零。它只对 U 中的真实 $F_0$ 取值，不要求把 $\lambda$ 直接作用于可能位于 U 外的单个 $L_0(S_i^*)$。

若一定使用 raw 密度，可任取 $\lambda$ 在 R130 有限环境上的延拓 $\widetilde\lambda$。令 $I_{\rm raw}(B)=\int\widetilde\lambda(L)\,ds$，则

$$
\Lambda(B)=I_{\rm raw}(B)-\widetilde\lambda\Gamma(M_B).
$$

故若 $\beta_{\rm raw,\sharp}$ 表示对应 raw 反射差，其准确关系是

$$
\boxed{\beta_\sharp
=\beta_{\rm raw,\sharp}
-\widetilde\lambda\Gamma\circ J_8+\widetilde\lambda\Gamma.}
\tag{12}
$$

改变延拓或 raw 代表时，这几项一起改变，而 (10)–(11) 的规范化差不变。证明从来没有假定 $\beta_{\rm raw,\sharp}=0$ 或 $\Gamma J_8=\mathsf S\Gamma$。

## 3. 唯一协变乘子迫完整修正 action 反射不变

对任一满足 (3) 的真实字符，R164 已证明存在唯一协变乘子 $\mu=\mu_{\rm cov}(\lambda)$。定义

$$
\mathcal A_\mu(B)=\Lambda(B)-\mu(M_B).
\tag{13}
$$

它满足全部真实正仿射变换的准确协变

$$
\mathcal A_\mu(gB)=H^{-2}\mathcal A_\mu(B),
\qquad g=(H,d),\ H>0.
\tag{14}
$$

这里存在性和协变不以正性为前提；如果字符正，R164 进一步说明同一 $\mu$ 也是 R140 唯一可行乘子。

由 (6)、(10)，令

$$
\mu'=\mu\circ J_8-\beta_\sharp,
\tag{15}
$$

便有

$$
\mathcal A_\mu(B^\sharp)=\mathcal A_{\mu'}(B).
\tag{16}
$$

现在使用真实几何关系

$$
(gB)^\sharp=\bar g(B^\sharp),
\qquad g=(H,d),\quad \bar g=(H,-d).
\tag{17}
$$

它直接来自 $g(h,k,\omega)=(Hh,k,(\omega+d)/H)$；两边始终保持 h 正。$\bar g$ 与 g 的字符因子同为 $H^{-2}$。于是

$$
\begin{aligned}
\mathcal A_{\mu'}(gB)
&=\mathcal A_\mu((gB)^\sharp)\\
&=\mathcal A_\mu(\bar g(B^\sharp))
=H^{-2}\mathcal A_\mu(B^\sharp)
=H^{-2}\mathcal A_{\mu'}(B).
\end{aligned}
\tag{18}
$$

故 $\mu'$ 也是同一个规范化局部积分的正仿射协变乘子。R70 的任意矩阵可达性把 (18) 转为 R164 同一组乘子协变方程，唯一性给 $\mu'=\mu$。因此

$$
\boxed{\beta_\sharp=\mu\circ J_8-\mu,\qquad
\mathcal A_\mu(B^\sharp)=\mathcal A_\mu(B)}
\tag{19}
$$

对所有真实开平端 B 成立。

为看清这里的唯一性不隐藏正性假设：若两个协变乘子之差为 $\nu$，缩放权迫 $\nu$ 只能在权 −2 的 $r_1,s_0$ 两坐标非零。平移不变性再给

$$
(-\nu_{r_1}+\nu_{s_0})/2=0,\qquad
\nu_{r_1}+2\nu_{s_0}=0,
$$

于是 $\nu=0$。所以 (19) 的确适用于全部真实权 −2 仿射字符，而非只适用于已证明正的字符。

## 4. 同一反射缺陷的显式低层形式

用 R164 §10 的记号，令

$$
a_0=a_{\rm static}(0),\qquad a_1=a_{\rm static}(1).
$$

这里 $a_1$ 是在 k=1 的静态函数值，不是一次多项式系数。唯一规范化乘子为

$$
\mu=(0,2a_0,2a_1,0,0,0,0,8a_0).
\tag{20}
$$

结合 (5)、(19)，得到

$$
\boxed{\beta_\sharp(M)=-4a_1M_{p_2}.}
\tag{21}
$$

原矩阵满足

$$
(m_0)_{p_2}=-kh/2,\qquad (m_2)_{p_2}=0.
$$

故

$$
\boxed{\beta_\sharp(m_0)=2a_1kh,\qquad
\beta_\sharp(m_2)=0.}
\tag{22}
$$

这说明静态规范化的确可能有非零反射缺陷。另一方面，同一乘子的二次层

$$
\mu(m_2)=-a_0(h_s/h)^2
\tag{23}
$$

本身在真实反射下不变。不能把静态 (22) 的非零项删除；也不需要在三个二次系数中分别选新的乘子。

## 5. 从全开路径恒等到二次正规系数的奇偶

令

$$
A_0^\lambda=\lambda F_0-\mu(m_0),\quad
A_2^\lambda=\lambda\widehat Q_2-\mu(m_2),\quad
A_4^\lambda=\lambda\widehat L_4.
\tag{24}
$$

它们的完整积分就是 (13)。将任意固定真实平端形状作正时长缩放 $s=\delta t$，反射与该缩放交换；式 (19) 给

$$
\delta\Delta_0+\delta^{-1}\Delta_2+\delta^{-3}\Delta_4=0
\quad\hbox{对每个 }\delta>0.
$$

因此三个系数分别为零。特别对全部真实开平端路径，

$$
\int\!\left[
A_2^\lambda(S^\sharp;u,-w)-A_2^\lambda(S;u,w)
\right]ds=0.
\tag{25}
$$

这一步只是恒等式分层，不把完整正性拆成各层分别非负。

二次层已经过 R129/R163 的完整正规化，不再含线性加速度。为从 (25) 得点态式，在任意状态 $S_*$ 选非零 $\psi\in C_c^\infty$，令

$$
h_s=\varepsilon\alpha\psi,\qquad
k_s=\varepsilon\beta\psi,
$$

并按真实 $\omega_s=k_s/(2h)$ 积分。对于足够小的正、负 $\varepsilon$，h 保持正，路径两端都是平坦 germs。左右状态允许不同，因为 (25) 已覆盖开端口。除以 $\varepsilon^2$ 并令 $\varepsilon\to0$，得到二次反射差在 $S_*$、速度 $(\alpha,\beta)$ 处乘 $\int\psi^2$ 等于零。任取实 $\alpha,\beta$，各二次系数分别为零，所以

$$
\boxed{A_2^\lambda(S^\sharp;u,-w)=A_2^\lambda(S;u,w).}
\tag{26}
$$

同理，静态层取常态路径得到 $A_0^\lambda(S^\sharp)=A_0^\lambda(S)$。最高层的对应奇偶已由 R145/R163 支付，本稿不重复把它计成新门。

按 R164 的完整协变，

$$
A_0^\lambda=h^{-2}a_{\rm static}(k),\qquad
A_2^\lambda=\sum_{i=0}^2h^{-2-i}b_i(k)u^iw^{2-i}.
\tag{27}
$$

将 (27) 代入 (26) 并比较速度单项，准确得到

$$
\boxed{
a_{\rm static}(-k)=a_{\rm static}(k),\qquad
b_i(-k)=(-1)^i b_i(k)\quad(i=0,1,2).
}
\tag{28}
$$

利用 (22)–(23)，未经矩阵修正的规范化族则满足

$$
\lambda F_0(h,-k,-\omega)-\lambda F_0(h,k,\omega)
=2a_1kh,
\tag{29}
$$

$$
\lambda\widehat Q_2(S^\sharp;u,-w)
=\lambda\widehat Q_2(S;u,w).
\tag{30}
$$

式 (29) 明确标出了“直接假定原低层全部简单奇偶”会漏掉的项。正确的偶静态对象是 $A_0^\lambda$。

## 6. 已发 head 中的四条具体原索引关系

只读取公开 run [43665345551](https://github.com/Rogerhu12/math-research-public/actions/runs/43665345551)、源提交 0aae9a6a85583a9f87415e586d8db2c9c7fea6a7 的完整导出：

    notes/actions-43665345551-1-character_head_minus2/
    character-head-minus2-original-expressions.json.gz

其压缩 SHA256 为 2c1242e13d253ba352c7ff1b025a91cf564ab2a7cfd93c6bcedc19baa5fac45c，原始 SHA256 为 7a93a53aa7fafa1cff76608aceaeac294911ca4f828746913c1b125ae2fd33af。完整十四族 gate 已成功。记 $\nu_i=\lambda(V_i)$，这里只用原 normal_family_records 的 family/state_key。

由真 h 幂对应的原键，三个修正二次系数准确为

$$
b_0(k)=\nu_{23}+\nu_{26}k+\nu_{28}k^2,
\tag{31}
$$

$$
b_1(k)=\nu_{38}k+\nu_{41}k^2+\nu_{43}k^3,
\tag{32}
$$

$$
b_2(k)=\nu_{58}+\nu_{61}k+\nu_{63}k^2+\nu_{67}k^3+\nu_{69}k^4.
\tag{33}
$$

这里第三式取 h 的 −4 次系数；$\mu(m_2)$ 在 h 的 −2 次 $u^2$ 项中的修正并不改变它。不是在 h=1 后把两个不同 h 次数未经区分地合并。

因此 (28) 在这份完整原呈示上给出

$$
\boxed{\nu_{26}=\nu_{41}=\nu_{61}=\nu_{67}=0.}
\tag{34}
$$

| 原 index | 族及错误奇偶单项 |
|---:|---|
| 26 | $Q2_0$ 的 $h^{-2}k$ |
| 41 | $Q2_1$ 的 $h^{-3}k^2$ |
| 61 | $Q2_2$ 的 $h^{-4}k$ |
| 67 | $Q2_2$ 的 $h^{-4}k^3$ |

这四条并不表示四个原算子各自为零，也不表示它们都已在 R 中。它们是所有真实权 −2 仿射字符必须满足的等式；在更大的外部坐标空间中，应作为准确线性行加入，而不能把曾经不满足它们的点称作真实字符。

## 7. 它们确是头部关系，但不授新的 signed control

R163 的完整字符头部为

$$
H_{-2}=U_{-2}/(R_{-2}+\mathsf N U_{-1}).
\tag{35}
$$

任取其真实实对偶泛函，先投影到真权 −2 再取商，即得到 U 上一个杀 R 的实泛函。它杀掉 $\mathsf N U_{-1}$，从而杀掉全 U 上平移生成元的像：其他真权在投影后均为零。有限仿射表示中的平移由该生成元指数给出，因此所得泛函满足 (3)。反过来，满足 (3) 的真权 −2 字符也下降到 (35)。

故 (34) 对 $H_{-2}^*$ 的每个元素成立。有限维真实函数空间的对偶分离给出

$$
\boxed{V_{26},V_{41},V_{61},V_{67}
\in R_{-2}+\mathsf N U_{-1}.}
\tag{36}
$$

这是一个不依赖不完备 normal-form 的真实头部成员结论。本文没有输出它们在已存 40 响应和 66 平移组合上的显式系数，也没有计算四条关系彼此或与旧等式的独立秩；这些数量必须由后继实际增量准确报告。

(36) 不能改写成 $V_i\in R_{-2}$，也不自动给实际闭成本半群中可调的正负方向。它排除的是违反这些头部等式的外点，尚不证明剩余完整正字符不存在，更没有支付全部 period/ruling 或主课题完成标准。

本稿所用反射始终是 (1) 的真实 h 正路径。形式负缩放仅用于 (4) 的有限输出作用判定，从未作为一条不合法的负 h 几何变换使用。
