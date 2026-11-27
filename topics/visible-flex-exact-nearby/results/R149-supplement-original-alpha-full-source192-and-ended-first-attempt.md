# R149 ASR：原 alpha 首次执行的真实终态与完整 192 模 source 修复

**已证明。** 本条登记实际失败的精确边界，并证明其后继入口保留的完整
原数学对象；不声称新的 alpha 两球或 Theta 已实际完成。
会话 `visible-exact-astra-fb31ed6-20261127`，2026-11-27。

承接 [AS](R149-supplement-original-source-alpha-signed-carrier-and-complete-errors.md)、
[原 SN](R133-supplement-signed-nonmean-density-transport-and-H3-validation.md)
和 [原 source 反射](R133-supplement-complete-coefficient-reflection-and-physical-paired-waist-leading-row.md)。
AS 的公式使用完整有限 raw source；首次程序把其支集误写成了原 SN
终点的支集。本条纠正该实现，并将所有依赖 raw source 的后续量一并
保留完整。原 AS 四源、manifest 和实际失败记录均不改写。

## ASR1. 首次实际已恢复整个旧端点，尚无新 alpha mode

[run45906100247/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45906100247)
的 event commit 为 `c781865c674581730f9017ce1eb9754c4684cb39`；
实际 worker 于 `2026-11-26T23:37:23.785149+00:00` 结束，child returncode
为整数 1，非 timeout。完整文件为：

| 完整自然对象 | bytes | SHA256 |
|---|---:|---|
| [actual](../notes/original_alpha_carrier_ci/run-45906100247-1/actual-original-alpha-carrier.json) | 8886 | `aac7d7db68e43bd22c68faced2f077012b3b9505c19122342323d69d15381d09` |
| [execution](../notes/original_alpha_carrier_ci/run-45906100247-1/execution.json) | 16401 | `2052b326c1e96e3b676837f5a82bf4443f3ee62fc3100c3328324aa571b4e5dc` |
| [原 manifest](../notes/2026-11-27-original-alpha-carrier-inputs.json) | 11219 | `16bf98e27c7f6bf1f7362d2840249368e342dc70ebed8c31344df87663c745fb` |

完整 actual 的 `original_endpoint_restoration.complete=true`：原 3146 个
intervals、12584 个 subcells、2550 个 candidate pieces、两支各 257 个
系数全部完成。245885 B 的原终点整 SHA 为

`3048266ba668164d7d9b5475c5262f1f3568cfe32a6e42c7bb496e4bda6c62b6`。

原 runtime、完整 source/helper 和逐步 serial dyadic rounding 保持；
旧 residual、energy、norm 目标调用为 0。原 207 文件、13612391 B
输入也全部恢复并核原身份。这是必要输入恢复的实际成功，不是新的
alpha、PDE 或 cohomological 结论。

随后原 owner 的 `raw.lo >= -128 and raw.hi <= 128` 断言失败，message
为 `whole finite original raw source support`。完整 actual 仍是
`complete=false, proved=false`，`new_records={}`，`completed_targets=[]`，
完整 mode prefix 为 0，raw/grid/modes/alpha 四个 private receipts
及新 global/tail bounds 都为 null。因此没有已完成 alpha mode 或
误差目标需要跳过，也不能把这次失败登记成 alpha 成功。

## ASR2. 原 selected source 的严格有限支集是 192

原完整 source
`fourfold_codazzi_signed_nonmean_density_H3.py`
的 SHA 为
`6c63241ae5ad865952620f68d63670604875b460e51b083ecb66127cb785b339`。
其 `direction_field(True)` 明确在 labels $-96,\ldots,96$ 放置全部
193 个系数；`root_data(1,True)` 保原 selected-parameter enclosure，
其 root field 是

$$
 u_r=u_0+\delta z_U,\qquad
 \operatorname{supp}u_0\subset[-32,32],\quad
 \operatorname{supp}z_U\subset[-96,96].
 \tag{ASR.1}
$$

这里 $\delta$ 是原选定成员所在的完整已准入区间，不被设为零。
该函数准确形成

$$
 \chi=A_1+B_0-\frac{26}{3}b_*g_0(u_r^2)_\perp,
 \quad \operatorname{supp}\chi_\perp\subset[-192,192].
 \tag{ASR.2}
$$

证明仅用有限 Laurent 乘法的支集相加和原标量系数不改变角频率。
原 helper `LP.__mul__` 进行完整多项式卷积；`.ne()` 只删除常数项，
不截断高频。原 helper 整 SHA 为
`217a91e25ec7bb6cad5c115ddc4749f4d714c5ca47601e8ad8dd540e69ed1718`。
因原已恢复 $\widehat V_+$ 支于 $[-128,128]$，完整 raw source balls

$$
 t^{\mathrm{raw}}=\widehat V_+
       +\chi_\perp/\sqrt{r_*}-\mu/2
 \quad\hbox{支于 }[-192,192].
 \tag{ASR.3}
$$

这不能把 labels 129 至 192 当零删除：其系数来自完整 selected
方向和参数区间，即使某个 dyadic midpoint 恰好为零，系数球半径
仍须保留。这里也没有增加 SN endpoint 的模式数或改变原终点。

## ASR3. 同一完整实 trial 与全部四列误差

对每个 $1\le n\le192$，从完整共轭系数球
$z_n=(t_n^{\mathrm{raw}}+\overline{t_{-n}^{\mathrm{raw}}})/2$
选原算法的 exact-dyadic midpoint $\widehat t_n$，并令
$\widehat t_{-n}=\overline{\widehat t_n}$；完整实常数项也独立取
exact dyadic $\widehat t_0$。真实 raw field 为实函数，故该共轭
平均仍包住每个真实系数。令 $r_n$ 为整个 $z_n-\widehat t_n$ 的
有向绝对值上界，$r_0$ 为完整常数球半径，则

$$
 \rho_q={\bf1}_{q=0}r_0
       +2\sum_{n=1}^{192}(4n)^q r_n,
 \qquad 0\le q\le3.
 \tag{ASR.4}
$$

三角不等式和归一测度上的 $L^2\le L^\infty$ 给完整导数误差。
AS.6--7 因而原样成立，但其 $\rho_q$ **全部按 192 项形成**：

$$
 e_q=E_q^{SN}+\rho_q,\qquad
 e_q^H=\sqrt{j_{upper}}\sum_{k=0}^qD_{qk}e_k,
 \quad s_n=\min_{0\le q\le3}\frac{e_q^H}{(4n)^q}.
 \tag{ASR.5}
$$

这里 $E_q^{SN}$、整个 $D$ 和 SEI 的完整 Jacobian record 都只读取
原成功结果；本次仅形成新 trial 的 enclosure radius 及必要组合。
均值在 $q=0$ 保留，两 physical mean slots 没有被消去。

## ASR4. grid、解析条带、head、全部 aliases 和无限尾同步修复

仍固定 $K=2048,L=8192,\sigma=1/128$，同一 $G=K_{48}\circ H_{24}$、
真实 $\mathcal H$、原 $E_H,G_1,H_1$ 和 $m=2-\max(G_1,H_1)>0$。
完整新 strip norm 必须是

$$
 T_\sigma=|\widehat t_0|
       +2\sum_{n=1}^{192}|\widehat t_n|e^{4n\sigma}.
 \tag{ASR.6}
$$

完整 raw trial 有 385 个 signed slots；Horner grid 使用全部 192 对，
不在旧 128 处停止。有限 raw source 形成时的 Laurent convolution
保整个 385-slot support；后续 composition/exponential 不假定有限
Fourier 支集，也不因 $192<8192/2$ 而免除 alias。由同一完整
$T_\sigma$，AS.9--12 的每一个 $1\le n\le2048$ integral 和误差为

$$
 z_n=\frac1L\sum_{\ell=0}^{L-1}
       \widehat t(\ell\pi/(2L))e^{-4inG(\ell\pi/(2L))},
$$

$$
 A_n=\frac{2T_\sigma e^{4nG_1\sigma}e^{-4\sigma L}}
                    {1-e^{-4\sigma L}},\qquad
 M_n=4nE_HT_\sigma e^{-4nm\sigma}.
 \tag{ASR.7}
$$

周期 analytic trapezoid 的全部非零 multiples of $L$ 由几何级数
$A_n$ 支付；真实 lift 与有限 lift 的完整 contour difference 由
$M_n$ 支付。两者的证明只需完整 strip norm，无需 raw degree 为
128；ASR.6 正是其严格假设。因此这里保留全 alias 和全 model
误差，不是仅把 guard 放宽而使用旧截断 norm。

仍用原 exact quadratic $\Omega$、整个
$b\in2G(0)+\Omega+[-2E_H,2E_H]$、
$q_n=e^{-4in\Omega},t_n=e^{-4inb}$。AS.3 的原相关公式

$$
 \alpha_n=\frac{q_n(v_i)_n+t_n\overline{(v_i)_n}}{q_n-1}
$$

给新 midpoint 的完整误差
$\epsilon_n\ge\text{全 phase/rounding radius}
+2(A_n+M_n+s_n)/|q_n-1|$。所有 head 累加器使用这些已保存、
读回的完整 2048 个自然 mode records。未重设 $b$、均值或原
cohomological divisor；旧无限除数常数只读取已证定理。

同理令 $q=e^{-4m\sigma}$，AS.13--15 的整个无限尾变为

$$
 B_{an}=272T_\sigma
       \frac{q^{K+1}(K+1-Kq)}{(1-q)^2},\qquad
 B_\infty=B_{an}+\frac{17e_3^H}{8}\sqrt{\frac2{3K^3}},
 \quad B_2=B_{an}+\frac{17e_3^H}{8(K+1)^2},
 \tag{ASR.8}
$$

$$
 e_{\alpha,\infty}=2\sum_{n=1}^K\epsilon_n+B_\infty,
 \qquad
 e_{\alpha,2}=\sqrt{2\sum_{n=1}^K\epsilon_n^2+B_2^2}.
 \tag{ASR.9}
$$

其中 ASR.5 与 ASR.6 的新增全部系数都参与。因此 head 和两种
infinite tails 同时覆盖高于 128 的 raw contribution。完整 trial
仍是原 real mean-zero $\widehat\alpha$；改变的是原输入实现的
支集缺陷，不是目标函数、K 或某个已完成科学目标。

## ASR5. 后继实际入口与未运行 OT 的对应修复

新四源为 `fourfold_codazzi_original_alpha_full_source_math.py`、
`fourfold_codazzi_original_alpha_full_source_owner.py`、
`fourfold_codazzi_original_alpha_full_source_public_worker.py` 和
`make_original_alpha_full_source_manifest.py`。新 manifest 是
`notes/2026-11-27-original-alpha-full-source-inputs.json`。
它保全原 29 current inputs 的每个路径、bytes、SHA，另纳入整个
失败 actual/execution/manifest 和此证明；替换的新四源与旧四源
各有独立角色。原 207 native files 继续由完整 SN manifest 继承。
整个旧 worker validator 和结束失败边界都先准入，才生成本次输入。

首次 runner 的公开目录只保存 actual、execution 和小报告；完整
245885 B endpoint 只在已结束 runner 的 private 文件中，没有可直接
复用的公开原件。本次仍须按原 runtime/逐步 rounding 恢复并核同一
**整 endpoint SHA**。这不是重跑旧 residual/norm，也不放宽任何
原 SHA。恢复后才进入尚未执行过的完整 alpha modes。所有科学运算
仅在公开 Actions；本地仅作 source/whole metadata。

未实际运行的 OT 初始入口 commit 为
`08e0b93016a795fd312f83db96ff07f444810bbd`。当时的
`fourfold_codazzi_complete_original_Theta_rows_owner.py` 为 36076 B、
SHA `caea2a2260d5ab4069d3642c6edd89a956f759a94aa4999f17b81bd1d8468651`；
`make_complete_original_Theta_rows_manifest.py` 为 11993 B、
SHA `e1d1c5dca2bfac52e504f123b1ab95a6e33876dbd098d2c4823a9c74afdfe321`。
本次将 OT 的必要 AS carrier 恢复一并改为完整 raw192，保全部
385 slots；其 parent 路径改为整个新 ASR manifest。原始 commit 和
上述完整身份保留，可准确恢复具体差异。它不是改写已经完成的
OT result：该旧入口从未生成 actual manifest 或启动科学执行。

OT 仍须读新 ASR 的整个成功两球、全部 2048 mode 和完整 private
raw/grid/alpha SHA，才允许后继。其 full 96-by-2240 row convolution
由 alpha2048 与 IR192 的既定度数给出，不因本次 raw192 改动而截断
或扩充；所有无限误差仍用同一完整 ASR 两球。没有 alpha 成功时
不生成 OT actual 入口，更不预报 Theta、full Schur 或最终课题门。
