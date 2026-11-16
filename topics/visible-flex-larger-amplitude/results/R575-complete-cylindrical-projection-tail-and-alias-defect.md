# R575　完整圆柱分量 Fourier 尾与全部 DFT 别名的投影缺陷界

**可信度：已证明（限下述完整闭域、固定 Frenet 符号和准确有限 DFT 条件命题）。**  
作者：geometry agent（AI）  
日期：2026-11-16

## 575.1　这条结论支付哪一项

R569 的准确分解保留了两个不同的缺陷：

$$
\partial_s F_Q-V_\sigma(F_Q)
=\mathcal S\bigl(Q'-\Phi_{M,N}(Q)\bigr)
+\bigl(\mathcal S\Phi_{M,N}(Q)-V_\sigma(F_Q)\bigr).
\tag{575.1}
$$

这里 $Q$ 是当前准确有限系数曲线，$\mathcal S$ 是完整有限 Fourier 合成，
$\Phi_{M,N}$ 是准确三角函数与准确有限 DFT 所定义的参考系数 RHS。
原 solver 的浮点 RHS 不是凭名称就等于 $\Phi_{M,N}$。

本结论给第二项的一个完整可计算充分上界。它保留所有被原有限模型截去的频率和全部整数别名，不以有限尾抽查替无限和，不以一个角叶或一个采样最小值充当整圈正域。第一项的原 cubic 残差、样点到闭单元的形成差、准确标量差、边界锚定及最终全域 relative-metric 误差仍各自保留。

新增库直接读原 R553 同次返回的全系数盒与正 $P$ 盒，并调用原 R521 的一、二阶公式；不复制 Frenet majorant 内核，不重新求场、不启动第二个角网格、不改变原 metric/DFS/BVP 判定。当前没有新 request、数值 run、实际常数、接受 checkpoint 或误差下降结论。

## 575.2　实际源码的网格与投影约定

源码依据是同一现存调用链的下列精确文本：

| 来源 | 实际函数/责任 | SHA256 |
|---|---|---|
| computations/alternative-outward-probe.py | Probe.__init__、unpack、jet、project、frame；物理角网格与完整布局 | cf163a5c42cff95137a78eefda058b6a18f5f226b4261b686a42e645f4002fcb |
| computations/geometry_20261114_r225_outward_probe.py | FullCoreProbe 继承原 Probe；保全部 core 与 N 的范围 | 64a3fd482f6ee01f4d149971dff1212b2c2ca3bdb00f1b733c7b119b458bab5f |
| computations/geometry_20261114_r225_high_core_bvp.py | BatchedFlow 的同一圆柱三分量与完整投影 | e12916dcf30dd2088ad59d2059647c8a03bed446aeee693b88f423730fa5a530 |
| computations/geometry_20261114_r225_free_core_bvp.py | BatchedFFTFlow.synth_real、project_real、__call__ | a1e5486a3b5bfa4e8a52923335e7d7cb507f372c399cf6aaa72bde58fa1f8b08 |
| computations/geometry_20261114_fft_frenet.py | real_jet、real_project、enable_fft；原 even-grid/Nyquist 限制 | 973898fcea1e8706d0ff9f87bbe72cde3576bc0055149af0a2e2058b144ac401 |
| computations/geometry_20261116_actual_prefix_coefficient_tube_majorants.py | R553 的实际全部六幂、完整角盒、同次 scalar/P、原退休计数 | 81d33e7135eeba50b7d0b372d82cbcd656f0da34cf3f2691792f865e2dada96b |
| computations/geometry_20261116_finite_frenet_tube_residual_majorants.py | R521 的 frenet_directional_majorants | 4217bf9a30ade1934c473146131067de2ff778ea62bc0b7811b55356a7cd71ad |

原 Probe 的字面式为

$$
\phi_\ell=\frac{2\pi\ell}{N},\qquad
\ell=0,\ldots,N-1,\qquad
n_j=2j,\quad j=0,\ldots,M.
\tag{575.2}
$$

它不含重复的 $\ell=N$ 端点。准确参考与这些字面式对应；由浮点 $\pi$、数组或 FFT 实际形成的字词误差另列。库采用原 even-grid 约束

$$
M\ge1,\qquad N\ {\rm even},\qquad N\ge4M+4.
\tag{575.3}
$$

因此最大的保留频率 $2M$ 严格低于 Nyquist $N/2$。没有把 Nyquist 槽当普通双边正频率，也没有丢掉一个网格端点之后错误声称多采了一个点。

物理系数完整排列为

$$
(r_0,\ldots,r_M,\ t_1,\ldots,t_M,\ z_0,\ldots,z_M),
\tag{575.4}
$$

总维数 $3M+2$。两个均值 $r_0,z_0$ 全保；$t_0$ 从来不是该模型的状态槽，后文将证明被投影速度的该均值准确为零，而不是把非零值删掉。

## 575.3　被投影的是旋转圆柱基中的分量

写

$$
\begin{aligned}
R(\phi)&=r_0+\sum_{j=1}^M r_j\cos(n_j\phi),\\
T(\phi)&=\sum_{j=1}^M t_j\sin(n_j\phi),\\
Z(\phi)&=z_0+\sum_{j=1}^M z_j\cos(n_j\phi).
\end{aligned}
\tag{575.5}
$$

若 $E(\phi)$ 是把圆柱正交基转到世界坐标的矩阵，则场是
$F(\phi)=E(\phi)(R,T,Z)^T$。原 synth_real 形成的是世界角导数在这个旋转基中的分量：

$$
d=(R_\phi-T,\ T_\phi+R,\ Z_\phi),\qquad
e=(R_{\phi\phi}-2T_\phi-R,\ T_{\phi\phi}+2R_\phi-T,\ Z_{\phi\phi}).
\tag{575.6}
$$

Frenet 运算在这些分量上进行；叉积、内积和范数由正交基保持。
原 project_real 的输入就是运算返回的三分量 $v(\phi)$。
它不是把世界速度 $E(\phi)v(\phi)$ 的三个 Cartesian 分量分别作原 even-frequency 投影。

尤其

$$
\frac{d}{d\phi}\bigl(E(\phi)v(\phi)\bigr)
=E'(\phi)v(\phi)+E(\phi)v_\phi(\phi).
\tag{575.7}
$$

世界二阶导数还含 $E''v$ 和 $2E'v_\phi$。下文 $B_2$ 必须界定
$\|v_{\phi\phi}\|_2$；不能把世界二阶导数界未经变换代入。
同样 $e\ne d_\phi$：$e$ 还含基旋转项。
新增函数是逐项微分(575.6)的分量三角多项式，正是为避免这个错误。

## 575.4　同一参考 Frenet 映射及其合法域

在固定径向位置，准确标量 $A,\nu,\mu$ 不随物理角改变。
其量纲与 R553/R569 相同：

- $A>0$ 是准确半径；
- $\mu>0$ 是该数值径向图下的准确径向尺度；
- $\nu=dA/ds_{\rm numeric}$；
- 原 BatchedFFTFlow 的 nominal 参考为 $\mu=1$，使用其实际 profile 字；从它到当前准确 scalar tuple 的形成/比较责任仍未删。

置

$$
q=d\cdot d,\quad W=|d\times e|^2,\quad
B=q e-(d\cdot e)d,\quad
P=A^2\mu^2W-\nu^2q^3.
\tag{575.8}
$$

当 $A>0,\mu>0,P>0$ 时 $q,W>0$，每个固定 $\sigma\in\{-1,1\}$ 定义准确光滑映射

$$
v_\sigma=\mathcal F_\sigma(d,e,A,\nu,\mu)
=\frac{\sigma\sqrt P\,(d\times e)-\nu q B}{A W}.
\tag{575.9}
$$

其范数为 $\mu$。这与原 normal/binormal 写法相同：曲率
$\kappa=\sqrt W/q^{3/2}$，法向系数 $-\nu/(A\kappa)$，
binormal 系数为 $\sigma\sqrt{\mu^2-\nu^2/(A^2\kappa^2)}$。

本结论不重新选择原 worker 的 root 或 $\sigma$。正的 majorant 对两个固定符号都有效，但不允许沿 $\phi$ 任意换号；后者可能破坏连续性和 Fourier 尾证明。
R553 的原同次独立盒扩大可给整个角单元上的 $P_-$。
仅中心 $P>0$、采样最小值、局部 domain.completed 标签均不替代所需闭域包围。

材料密度 $\rho=\Phi'$ 仍属于准确目标的角分量 $A^2\rho^2$。
它不是在(575.8)中再乘一次的因子。
R569 已修正几何 Gram 归一化的 $\rho_-$；本结论不改变原 P 域。

## 575.5　π 周期及原投影所需奇偶性

式(575.5)给 $R,Z$ 为偶函数，$T$ 为奇函数；全部频率为偶整数，因此三者均为 $\pi$ 周期。由(575.6)，$d$ 的分量奇偶为
$(\mathrm{odd},\mathrm{even},\mathrm{odd})$，
$e$ 为 $(\mathrm{even},\mathrm{odd},\mathrm{even})$。

令 $D=\operatorname{diag}(-1,1,-1)$，$\det D=1$。有

$$
d(-\phi)=D d(\phi),\quad e(-\phi)=-D e(\phi).
\tag{575.10}
$$

所以 $q,W,P$ 为偶函数，
$B(-\phi)=-DB(\phi)$，
$(d\times e)(-\phi)=-D(d\times e)(\phi)$。
固定符号的(575.9)给

$$
v(-\phi)=-D v(\phi),\qquad v(\phi+\pi)=v(\phi).
\tag{575.11}
$$

故实际被投影速度的分量奇偶是
$(\mathrm{even},\mathrm{odd},\mathrm{even})$，其 tangential 均值为零。
该证明依赖完整固定符号合法域，并非根据一个有限 FFT 数组推断函数奇偶。

## 575.6　准确 DFT 与原 normalization 的逐项对应

令

$$
\widehat v_k=\frac1{2\pi}\int_0^{2\pi}v(\phi)e^{-ik\phi}\,d\phi,\qquad
\widetilde v_k=\frac1N\sum_{\ell=0}^{N-1}
v(\phi_\ell)e^{-ik\phi_\ell}.
\tag{575.12}
$$

原 np.fft.rfft 是未除 $N$ 的 forward 和。
原 project_real 对正频率 R/Z 使用 $2/N$ 乘实部，对 T 使用
$-2/N$ 乘虚部，对 R/Z 的 $k=0$ 再乘 $.5$。
所以在准确算术下，输出为

$$
\begin{aligned}
r'_0&=\widetilde v_{0,R},&
r'_j&=2\operatorname{Re}\widetilde v_{2j,R},\\
t'_j&=-2\operatorname{Im}\widetilde v_{2j,T},\\
z'_0&=\widetilde v_{0,Z},&
z'_j&=2\operatorname{Re}\widetilde v_{2j,Z}.
\end{aligned}
\tag{575.13}
$$

对应 synth_real 的正频率谱为 $N/2$ 倍 cos 系数、
$-iN/2$ 倍 sin 系数，两个零频再倍2；
irfft 的 $1/N$ inverse normalization 因而恰好还原原三角多项式。

准确网格上 $\ell$ 与 $N-\ell$ 配对，结合(575.11)，
$\widetilde v_{k,R},\widetilde v_{k,Z}$ 为实数，
$\widetilde v_{k,T}$ 为纯虚数且 $\widetilde v_{0,T}=0$。
因此合成后的原准确投影为完整三向量

$$
\Pi_{M,N}v(\phi)
=\sum_{k\in K_M}\widetilde v_k e^{ik\phi},\qquad
K_M=\{-2M,-2M+2,\ldots,2M\}.
\tag{575.14}
$$

$|K_M|=2M+1$ 是三向量复系数的个数，不再无故乘3。
向量界已经对三个分量的 Euclidean norm 负责。
Nyquist 不在 $K_M$；原重复半周期网格保留了全部 $N$ 行，而非删半行后沿用错误 normalization。

## 575.7　一个完整二阶界足够控制全部连续尾

假设在完整物理圆周上

$$
\sup_\phi\|v_{\phi\phi}(\phi)\|_2\le B_2.
\tag{575.15}
$$

合法域保证 $v$ 为至少 $C^2$ 的周期函数，函数及一阶导数端点接齐。
对非零 $k$ 两次分部积分，边界项准确相消：

$$
\widehat v_k=-\frac1{k^2}\widehat{v_{\phi\phi}}_k,\qquad
\|\widehat v_k\|_{\mathbb C^3}\le\frac{B_2}{k^2}.
\tag{575.16}
$$

此处先对向量积分用三角不等式，得到的是完整 $\mathbb C^3$ norm；
没有把逐分量上界直接当向量上界。
因此 Fourier 级数绝对且一致收敛。π 周期使所有奇数频率准确为零。
完整连续截断尾满足

$$
\begin{aligned}
T_M&=\sum_{k\notin K_M}\|\widehat v_k\|_{\mathbb C^3}\\
&\le 2\sum_{j=M+1}^\infty\frac{B_2}{(2j)^2}
=\frac{B_2}{2}\sum_{j=M+1}^\infty j^{-2}
\le\frac{B_2}{2M}.
\end{aligned}
\tag{575.17}
$$

最后一步只用正项积分界；不是运行有限和后把余项填零。
它对 $M\ge1$ 成立，不要求记录到某个任意尾频率。

## 575.8　全部整数 alias 与端点责任

绝对收敛允许把 Fourier 级数与有限 $N$ 和交换。准确等比和给

$$
\widetilde v_k=\sum_{\ell\in\mathbb Z}\widehat v_{k+\ell N}.
\tag{575.18}
$$

这包括正、负所有别名和零频均值的别名。由于 $N$ 偶，保留的偶 $k$
所遇到的 $k+\ell N$ 仍是偶频率。由(575.3)，当 $\ell\ne0$ 时

$$
|k+\ell N|\ge|\ell|N-2M>2M.
\tag{575.19}
$$

没有一个 alias 来源与原保留频率重合，也不会撞到零分母。
对每个保留三向量系数，

$$
\begin{aligned}
\|\widetilde v_k-\widehat v_k\|
&\le2B_2\sum_{\ell=1}^\infty(\ell N-2M)^{-2}\\
&\le\frac{2B_2}{(N-2M)^2}\sum_{\ell=1}^\infty\ell^{-2}
\le\frac{4B_2}{(N-2M)^2}.
\end{aligned}
\tag{575.20}
$$

这里 $\ell N-2M\ge\ell(N-2M)$，并用
$\sum_{\ell\ge1}\ell^{-2}\le2$。
所有保留槽的 alias 总量故不超过

$$
A_{M,N}^{(1)}
=\frac{4(2M+1)B_2}{(N-2M)^2}.
\tag{575.21}
$$

另一个完整界来自 residue 不重叠。若
$k+\ell N=k'+\ell'N$ 且 $k,k'\in K_M$，则
$|k-k'|\le4M<N$，所以 $k=k'$、$\ell=\ell'$。
因此所有保留槽的非零 alias 来源是遗漏频率集合的一个子集，每项最多计一次：

$$
A_{M,N}\le T_M\le\frac{B_2}{2M}.
\tag{575.22}
$$

这不是把 alias 删除；它是对同一无限非负和使用第二个完整上界。
代码保留(575.21)和(575.22)的值及所用较小值。

## 575.9　全角投影缺陷的最终式

由连续尾与全部 alias 的三角不等式，

$$
\boxed{
\sup_{\phi\in[0,2\pi]}
\|\Pi_{M,N}v(\phi)-v(\phi)\|_2
\le
\frac{B_2}{2M}
+\min\!\left\{
\frac{4(2M+1)B_2}{(N-2M)^2},
\frac{B_2}{2M}
\right\}.}
\tag{575.23}
$$

世界向量乘 $E(\phi)$ 后范数不变，因此同一上界支付(575.1)第二项的参考部分。
即使 $B_2=0$ 也没有丢失均值：此时允许的常向量只有 R/Z 均值，
原投影准确保留它们。

当 $B_2$ 固定时，增大 N 能降低显示的 alias 上界；固定 M 时连续尾项未被消除。
当 M 也增加时，实际新场及其 $B_2$ 可能变化，不能凭形式中的 $1/M$ 宣称已观察到误差持续下降。
该界可能很宽；未付正域或实际不收紧均不是更换原目标或 solver 门的理由。

## 575.10　如何从实际全系数给出分量角导数

令当前完整系数盒给
$\bar r_j,\bar t_j,\bar z_j$ 的准确非负绝对上界，$n=2j$。
由(575.6)完整展开

$$
\begin{aligned}
d_R&=-\sum(nr_j+t_j)\sin(n\phi),\\
d_T&=r_0+\sum(nt_j+r_j)\cos(n\phi),\\
d_Z&=-\sum nz_j\sin(n\phi),\\
e_R&=-r_0-\sum((n^2+1)r_j+2nt_j)\cos(n\phi),\\
e_T&=-\sum((n^2+1)t_j+2nr_j)\sin(n\phi),\\
e_Z&=-\sum n^2z_j\cos(n\phi).
\end{aligned}
\tag{575.24}
$$

定义非负三向量

$$
u_j=(n\bar r_j+\bar t_j,\ n\bar t_j+\bar r_j,\ n\bar z_j),\quad
w_j=((n^2+1)\bar r_j+2n\bar t_j,\
(n^2+1)\bar t_j+2n\bar r_j,\ n^2\bar z_j).
\tag{575.25}
$$

则逐分量准确有

$$
|d_\phi|\le\sum n u_j,\quad
|d_{\phi\phi}|\le\sum n^2u_j,\quad
|e_\phi|\le\sum n w_j,\quad
|e_{\phi\phi}|\le\sum n^2w_j.
\tag{575.26}
$$

库先完整求这四个三向量，再以原 R521 的有理外包 sqrt 求各 Euclidean norm。
没有使用 $\max$ 分量代向量范数，也没有略去高模态。
$r_0$ 在 d/e 零阶仍由原完整盒保留；它和 $z_0$ 在(575.26)中的导数准确为零。
这不意味着从状态、边界或端点数组中删除两 mean。

输入是原675全部六幂在同一个闭径向单元的 Bernstein 盒，或另一个已有真实比较 tube；
本次接法只消费 R553 的实际 Q 盒，不冒充已捕获 original cubic。
径向盒独立扩大不破坏(575.26)对每个实际径向位置的有效性。

## 575.11　非仿射角曲线的完整链式法则

R521 给 $\mathcal F_\sigma$ 沿仿射输入方向的一、二阶上界。
角输入曲线

$$
x(\phi)=(d(\phi),e(\phi),A,\nu,\mu)
\tag{575.27}
$$

一般不是仿射，故只取 R521.second_upper 不够。准确链式式为

$$
v_{\phi\phi}
=D^2\mathcal F_\sigma(x)[x_\phi,x_\phi]
+D\mathcal F_\sigma(x)[x_{\phi\phi}].
\tag{575.28}
$$

对同一个原 R553 正域，第一次原函数调用用
$(\bar d_\phi,\bar e_\phi,0,0,0)$；
第二次用
$(\bar d_{\phi\phi},\bar e_{\phi\phi},0,0,0)$。
若第一调用的 second_upper 为 $H$，第二调用的 first_upper 为 $J$，则

$$
\|v_{\phi\phi}\|_2\le H+J=:B_{2,\mathrm{cell}}.
\tag{575.29}
$$

第一调用的 first_upper 也保留为 $B_{1,\mathrm{cell}}$。
这里只需映射在该角曲线上各点合法及原值/方向包围正确；
局部导数公式由 $A>0,P>0$ 的开域光滑性成立。
没有把角曲线误当一条仿射段，也没有假定 d/e 的角加速度为零。

标量角导数为零是该同一径向标量参考的定义，不是由区间盒宽度推出。
若未来改成角依赖标量，必须补全对应一、二阶输入；本库不注册该模型。

## 575.12　局部正域到全角上界的原覆盖责任

单个角叶只有 $B_{2,\mathrm{cell}}$，没有资格应用整圈的(575.16)。
实际 observer 的全局返回须同时满足：

1. 原 metric DFS 的全部工作完成；所有 root、闭端点、prefix 片及两反射片由原覆盖负责。
2. 原 R553 的 complete_prefix_constant_cover 为真，全部必要终叶的实际 P 域已付。
3. R575 的 observed/committed/split/terminal 计数与同一个 R553 活对象逐项相同。
4. 每个终叶都保完整可用 R575 记录，未付终叶为零，且至少有一个 prefix 终叶。
5. 原 error、stop、close error 仍按 R553 的完整定义处理。

这些是新增诊断可否自称全域界的条件，不是原场/metric 的新接受门。
原 traversal 仍独自决定 split 和退休；R575 不能把某个不适合的叶改成成功。
在这些条件下，取全部终叶的 $B_{2,\mathrm{cell}}$ 最大值，
对每个原 prefix 径向位置及其完整物理圆周有效，才能代入(575.23)。

中断或未付时仍返回观察到的局部极值、第一/最后未付地址、原完整账本身份，
以及原 coverage 中当前 frontier/未访根的责任引用；
局部极值明确不叫全局界。完整每叶输入、错误和结果在原临时 ledger，
不声称这份必要摘要已经回传全部 ledger 行。

## 575.13　全 phase、材料角和反射的边界

先在原基场的完整物理角上证明(575.23)。
对已有准确相位族的径向独立角映射及共同刚转，
已构造缺陷的平移/重参数拉回保持完整圆周上的上确界，正交世界变换保持向量范数。
帽、tail、collar、cut patch 没有因这个 prefix 结论获得一个新的 Fourier 模型。

必须保留一个区别：固定原 grid 和 parity 子空间的 $\Pi_{M,N}$
不必与任意角平移交换。对
$(v_R\ {\rm even},v_T\ {\rm odd},v_Z\ {\rm even})$
作一般平移后，它不再关于原零点具有相同奇偶性；
不得把原 project_real 原封应用于平移函数再假称相同模型。

本结论允许的是：

- 对已经构造的基场缺陷 $\Pi_{M,N}v-v$ 作实际完整相位/材料拉回；或
- 明确使用相位共轭的投影算子，使 grid/basis 同时相应改变。

它没有新增每个 t 的 FFT 运行。
共同材料映射仍须原 R443/R447/R457 等准确同场合同，方向、严格正密度和与帽的粘接责任不变；此处不拿材料 q 导数代物理 $\phi$ 导数。
若映射依赖径向坐标，径向导数会有额外项，本结论不替它们填零。

反射由真实正交变换处理；其行列式可能为负，对应 Frenet binormal 符号必须一致变换。
两个固定 $\sigma$ 使用同一非负 majorant，故真实反射分支可使用该界，
但不能逐叶任意换号制造不连续参考。

## 575.14　实际形成误差和原容差依旧未付

(575.23)针对准确的三角函数、sqrt 和有限 DFT 参考。
实际 BatchedFFTFlow 的浮点 spectrum 填写、FFT、normalization、profile、normal/binormal、sqrt、projection 和 residual norm 都有自身形成差。
原表 literal trigonometric words 与准确三角函数的差也没有由本定理自动付清。

若实际 rounded 输出记为 $\widehat\Phi_{M,N}$，
则还需要真实来源的

$$
\|\mathcal S(\widehat\Phi_{M,N}-\Phi_{M,N})\|
\tag{575.30}
$$

及相应 scalar/state 比较界。
原 R521 的有限投影行算子界可传播已知形成差，但它不凭空生产该差。
原 RMS、节点 .05 项、native 末容差都不被替换成全域 metric floor。

R569 的真实同次 cubic 捕获及 $Q-C_{\rm lit}$ 连接仍由 R570 的未来 caller 注册支付；
本次库不要求它作为新诊断的启动前门，也不把 Q-only 角界冒成已付 cubic residual。

## 575.15　实际源接口与完成状态

新源：

computations/geometry_20261116_same_evaluation_full_angle_projection_defect.py

实际入口是
bind_loaded_projection_defect(prefix_tubes)，其中 prefix_tubes 必须是原 R553
BoundPrefixTubes 的真实已加载对象。模块从实际 type.__module__ 核原完整源码，
不按 sys.modules 中第一个同路径类猜身份；R521 也按实际定义函数模块核 source。
M/N 来自当前对象，N 与当前 SavedPrefix 的真实 N 相等。
五个原 reference 文件只作为准确 DFT 定义的真实来源绑定，不把其文件存在当作 FFT 舍入证书。

inspect 消费同次 R553 原返回；commit_original_retirement 只附原退休记录；
summary 读取同一个原 observer 的完整覆盖计数。
资源 callback 仍为原回调，RuntimeError 类资源异常不被数学异常 catch 吞掉。
没有新 clock、subprocess、worker、cleanup 权限或实际 request。

当前完成的是完整条件证明与可执行库源码。
没有本地 import、AST、compile、fixture、数值试跑或科学计算。
R576/request241/R577 仅为未来完整来源入口预留；当前235/238及所有既有运行件保持原字节。
