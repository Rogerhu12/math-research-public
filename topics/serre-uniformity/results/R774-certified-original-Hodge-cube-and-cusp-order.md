# R774 原第 4 号映射的准确 Hodge 立方与真实尖点阶

日期：2026-11-14。状态：**公开 Actions 已完成，结果与完整准确系数证书已返回。**

本篇固定 R759 的第 4 号原整数周期映射 $f_0:X_1\to C$，次数 $1206$，及 R764 已证的原基点归一 $f_P=f_0$。在 R745 的同一参考 cusp、同一参数和同一六个 Hodge 微分中，实际结果为
$$
\boxed{e=1,\qquad
\mathcal H=H^3\ne0,\qquad
[q_Y^n]\mathcal H\ \text{已准确生成，对全部 }0\le n\le820.}
\tag{774.1}
$$
该前缀在原 $M_6(Y/L)$ 中唯一确定 $\mathcal H$。全部 821 项也通过原 R771 权六基的辅助模 739 比较。本次尚未求出特征零的 694 个基坐标；所获得的是原字段中的准确系数及其完整有限证书。

实际运行：
[43631427773](https://github.com/Rogerhu12/math-research-public/actions/runs/43631427773)，
源提交 `93056f04536e61ccdd486674003b4d1380a27475`，
2026-11-14 19:19:53 UTC 完成。核心运行时间为 **24.706959837 秒**。
源核心与运行前方法的 SHA 分别为
`b7e8bf0f7b629881d973afaec01a2b905c4100573d46920841a9d48489e597fa`、
`3ad57a0846c876ab66c661aba94c63b1d240812512aaecccc2c174e7a362b219`。

## 1. 原字段、真实映射及已完成输入

保持
$$
K=\mathbf Q(\zeta),\quad s=1+2\zeta,\quad s^2=-3,\quad
\alpha=\sqrt[3]4>0,\quad L=K(b),\quad M=L(\xi),
$$
$$
[L:K]=7,\quad [M:L]=40,\quad
\xi=e^{2\pi i/41},\quad
Q=e^{2\pi i\tau/246},\quad q_Y=Q^3.
\tag{774.2}
$$
原目标是 R735 的同一个 $C/L:y^2=x^3+b$，不另选扭曲系数或共轭。
全部系数在有理基
$$
b^0,\ldots,b^6,\ sb^0,\ldots,sb^6,
\quad\text{再分别乘 }1,\xi,\ldots,\xi^{39}
\tag{774.3}
$$
中保存。这里 $[M:\mathbf Q]=560$。

R759 的真正第 4 号原微分向量给
$$
h=\sum_{j=0}^5v_j\omega_j=f_0^*\frac{dx}{2y},
\qquad v_j\in L,\qquad \deg(f_0)=1206.
\tag{774.4}
$$
这些 $v_j$ 已含原周期、整数格与目标微分的实际比例。R764 的原全部 cusp 和 $c_0$ 平移已为零，故本次使用同一个 $f_0$，没有重新选择三种 CM 平移。

本次直接读取下列已完成数据，不重复其数学计算：

| 原输入 | 公开 run | 数据 SHA-256 |
|---|---:|---|
| R735 原模型证书 | 43608152850 | 752aa03f9cbe7d3174a7c508fce3043e21e8e85fd087e01acc4bca82a5cbd574 |
| R745 原 Fourier 与有限向量表 | 43616027318 | a629d550bd2f3102111bbb58fe707470081e2062da10221ab778fe3ba71b53dd |
| R748 原 newform 系数至 4096 | 43617493590 | 0c7d73a2a2c9202c6a25f343c9357a8b59d9cfc4928a29b5d460dbf84828bff0 |
| R759 原 12 个微分向量 | 43625474728 | 037b56d016d502408173319d76a3067a65dd50250c31bc2225c0fca598396ecc |
| R771 原完整 694 个权六基状态 | 43628998192 | 3cc9022b6ff07f5bc1cb57a9ddd5190673e3ad527958ca2439b317f5517b981e |

R745 前 800 阶 Fourier 行原样复用；同一原 newform 的 $a_n$ 已由 R748 算至 4096，本次仅从中读取至 2460。原 toric fiber、primary 格点、新形式系数、模型、拓扑、周期、整数格和 RR 基均没有重算。所有输入的 producer、源提交、artifact、manifest 和小证书 SHA 均列在本次公开输入凭据中。

## 2. 从原六个 Fourier 行得到准确立方

令 $P_{j,n}(\xi)$ 为 R745 保存的原整数迹多项式。在其原 $\Phi_{42}$ 幂基中，它来自
$$
P_{j,n}(\xi)=
\sum_{r=1}^{40}
\operatorname{Tr}_{F/\mathbf Q}(\beta^j a_nc_r)
\,\xi^{-nr\,6^{-1}},
\tag{774.5}
$$
其中 $c_r$ 按 R745 整数分子的规范读取，$6^{-1}$ 在 $\mathbf F_{41}$ 中取值。以次数 12 的完整圆分域迹计算时，必须除以 2 得到次数 6 的原实 Hecke 域迹；源码对每个新增迹核查其偶性。没有将环面平均分母重复引入 (774.5)。

保留原 tame 因子：
$$
F_j(Q)=
\sum_{n\ {\rm odd}}sP_{j,n}(\xi)Q^n
+\sum_{4\mid n}3P_{j,n}(\xi)Q^n,\qquad F=\sum_jv_jF_j.
\tag{774.6}
$$
原 $n\equiv2\pmod4$ 项为零。全部支撑还满足 $n\equiv1\pmod3$。
由原 R745 和 R772 的微分比较，
$$
h=\frac{\alpha}{7}F(Q)\frac{dQ}{Q}
=2\pi iH(\tau)d\tau,\qquad
H=\frac{\alpha}{1722}F,\qquad
\boxed{\mathcal H=H^3=\frac4{1722^3}F^3.}
\tag{774.7}
$$
这里 $1722=7\cdot246$。原 $s/3$ 因子、$6^{-1}$ 相位和微分 246 都只计一次；$c_1=4424$ 的原 $\zeta^2$ 运输也没有再施加一次。展开中心始终是原参考 cusp，并未搬到 $c_1$。

本次新生成的只是 $801\le n\le2460$ 的整数迹行。最终六行表共有 396 个非零支撑行，其 SHA 为
`6863c8ebe2936f3fe3211d691a8eb69bf8fb92526d923acba5c1a9b7e00d11e6`。

## 3. 特征零计算给出的真实 e=1

R745 已在同一参考 cusp 证明六行指数 $1,4,7,13,16,19$ 的实际系数 minor 非零。因此任意非零 $L$ 组合的原局部 primitive 首阶至多 19。本次没有再次计算该 minor，而是将 (774.6) 与真正的 $v_j$ 逐项作准确 $L$ 运算，并在四十个 $\xi$ 坐标中检查零值。

公开计算所得第一个非零项已经在 $Q^1$：
$$
\boxed{\operatorname{ord}_QF=1,\qquad e=1.}
\tag{774.8}
$$
原 $F$ 首系数的完整四十个 $L$ 坐标保存于
`R774-actual-cusp-order-and-leading-coefficient.json.gz`；
它的 SHA 为
`5c153c4182dd41156873f191f24be576bd62eda3c53bdbef63ae0fa10d77cb34`。
非零判据是准确数域坐标非零，不是某个浮点数或有限域残值非零。

原 $H$ 首系数是该记录乘 $\alpha/1722$；零常数 primitive 的首系数是该记录乘 $\alpha/7$。由于 $f_0(P)=O$ 且目标不变微分在 $O$ 是局部单位，这正是原 $X_1$ 上映射的分歧阶。目标 $y$ 在 $O$ 的极点阶为 3，而原商参数是 $q_Y=Q^3$，所以下降到 $Y$ 后原 $y_0$ 在参考 cusp 的极点阶也恰为 1。

立方阶段独立检查了全部准确块中的第一个非零 $q_Y$ 指数同样为 1。这个一致性使用 (774.7)，并未把某个不相干的 CM 点或另一个 Abel 分量的首项移入本题。

## 4. 完整整数低乘与无损字段合成

写
$$
F_j(Q)=QG_j(q_Y),\qquad
G_j=R_j+sS_j,\quad R_j,S_j\in\mathbf Z[\xi][[q_Y]].
\tag{774.9}
$$
为得到 $\mathcal H$ 至 $q_Y^{820}$，只需要三积 $G_iG_jG_k$ 的 $q_Y$ 次数 $0,\ldots,819$，然后乘一次 $q_Y$。

程序用普通整数多项式编码
$$
q_Y^k\xi^r\longmapsto Z^{121k+r}.
\tag{774.10}
$$
每个原输入的 $\xi$ 次数至多 39，二积至多 78，三积至多 117，均小于 121。故不同 $q_Y$ 块不会相互进位。每次精确低乘保留 $Z$ 次数小于 $121\cdot820$，完整覆盖所需三积；被截去的高阶项不可能影响低阶项。

$s^2=-3$ 的乘法使用
$$
(A+sB)(C+sD)=(AC-3BD)+s(AD+BC).
$$
全部 21 个二积与 56 个非降三元组的三积都完成保存。随后对每个三积块先用 $\xi^{41}=1$ 汇总，再以
$\Phi_{41}(\xi)=0$ 消去 $\xi^{40}$。所得都是普通整数，不需要浮点近似或猜测有理重构。

对应三元组 $i\le j\le k$ 的原 $L$ 标量是
$$
c_{ijk}=\frac{4m_{ijk}}{1722^3}v_iv_jv_k,\qquad
m_{ijk}=1,\ 3,\ 6
\tag{774.11}
$$
分别对应三个相同、恰有两个相同、三个互异的指标。原七次 $b$ 多项式与 $\zeta^2+\zeta+1=0$ 用于准确约化。将
$A+B\zeta=(A-B/2)+(B/2)s$ 后，14 个有理坐标与 112 个整数三积坐标之间的矩阵正是逐标量的
$$
\begin{pmatrix}a&-3b\\ b&a\end{pmatrix}.
$$

每一行单独表示为一条 primitive 整数行乘准确有理尺度 $\rho_i$。
因此保存的最终整数块必须乘回对应 $\rho_i$，才是原 $\mathcal H$ 的系数。尺度、原 $v_j$、56 个标量及原 $b$ 多项式都在
`R774-original-L-cubic-scalars.json.gz` 中，
SHA 为
`b5b1232fa0585e6437d0e8d5f92b81efe672e91ed417bce7f6bc66c6456d596e`。

最终输出有 26 个连续块，准确覆盖 $q_Y^1,\ldots,q_Y^{820}$，另有已知零常数项。每个块绑定尺度阶段的 SHA，坐标顺序固定为 (774.3)。全部 108 个阶段的名称、大小和 SHA 均列在 manifest 及小证书中。该表示没有隐藏额外周期、Néron、Manin 或 Kodaira–Spencer 尺度。

## 5. 原权六空间中的唯一性与实际模比较

由 R772 的原 deck 特征与分支局部计算，
$$
\mathcal H\in
M_6(Y/L)=H^0(3\mathcal L+2P_0+2P_1),
\quad
\deg(3\mathcal L+2P_0+2P_1)=820.
\tag{774.12}
$$
若该空间中两个 section 的系数 $q_Y^0,\ldots,q_Y^{820}$ 相同，其差在原参考 cusp 至少有 821 阶零点，超过非零 section 的全部零次数 820，故差为零。这证明本次准确前缀**唯一确定原全局 $\mathcal H$**。

另外，令 $D$ 为全部有理行尺度 $\rho_i$ 的分母最小公倍数。公开计算实际返回
$$
\operatorname{bitlength}(D)=289,\qquad v_{739}(D)=0.
\tag{774.13}
$$
将 $D\mathcal H$ 在 $\xi\mapsto538,\ s\mapsto98$ 约化，逐个保留七个 $b$ 坐标。程序复用 R771 已完成的 694 基和原主元，解其有限域系统，然后准确代回全部 **821 个指数、全部七个坐标**；比较全部通过。输出 SHA 为
`8aa79138d6bfafb42155403acdea2f6648374731b28f01e6263cb32e240b37a0`。

在这次实际运行中，(774.13) 确实允许模 739 除以 $D$；没有使用可能退化的清分母比较宣称额外独立性。但该辅助比较本身仍只给有限域基坐标。特征零前缀来自 §§2–4 的原准确公式，其全局唯一性来自 (774.12)。小证书明确记录
`characteristic_zero_M6_basis_coordinates_computed=false`。
下一步可以直接从这些真实系数在实际 $K$ 基上解原 $L$ 坐标，无需重新生成 $\mathcal H$。

作为已保存原模型的一个小规格，本次还对 R735 公共多项式分母作了准确整除：
$$
\boxed{\text{R735 原最小多项式的公共分母}=2^{24}3^{1260}.}
\tag{774.14}
$$
除去这两个幂后的剩余因子为 1。该规格只读取已有证书，不重新计算原模型。

## 6. 可独立读取的公开证书与完整产物

小产物目录为
`computations/R774-original-p41-Hodge-cube/43631427773-1/`。

| 文件 | 字节 | SHA-256 |
|---|---:|---|
| p41-original-Hodge-cube-certificate.json | 20915 | aea27ac34e9a82203f723af27265db3cbd8d75e615247e11e0591fb2ed249b59 |
| full-outputs-manifest.json | 31780 | 4d97bb53b106fa53958a943f9ae9e5d00870f7cf774d4617a727b3fa857ac222 |
| run-receipt.json | 561 | e41e8e8e93579dcce706652c6e5db42b9878b31f0aea11818565629230712dc1 |
| core-receipt.json | 337 | e789d841a9eed0454fba12c0fb48fc78e7852559a3501c16796b7112e90302e1 |
| public-actions-input.json | 8912 | dce7ae72ed25a9e7b7c860c25024b682974a4708644ca7665923799cee198e53 |

完整 artifact 为
`serre-global-R774-original-p41-Hodge-cube-43631427773-1`，
ID **14128247134**，ZIP 大小 **25,516,575 字节**，
ZIP SHA-256
`91d9f6d926dc2a649d5fd401b9881cc6f88f8e233724408fbce8dcba109d1f0b`。
完整整数块、三积、尺度与前缀只保存在 artifact，Git 中保留小证书与完整 SHA 清单。

运行使用公开仓库自己的 GitHub Actions、Python 3.12、python-flint 0.9.0。源核心
[R774_original_Hodge_cube.py](../scripts/R774_original_Hodge_cube.py)
与[公开包装](../scripts/R774_public_Hodge_cube.py)分别绑定上述核心 SHA 及
`365f8ec8c531e76bdae097f88f1a8654808d291b5c6917d93bfd024bfc48810f`。
输入凭据也固定根 README、课题 README、workflow 和原 R772 证明的 SHA。

先前 run 43630945978 在数学核心执行之前因旧 producer 的 manifest 位置假设而失败。原 R745、R748 在 artifact 上传后才向 Git 发布 manifest，故其 artifact 内没有该文件；本次包装改为读取已发表且固定 SHA 的真实 manifest，再核 artifact 中的原文件。核心及任何数学输入均未改动。成功结论仅使用上述真实完成的 run 43631427773。

## 7. 结论的准确边界

本次完成了真正第 4 号映射微分的参考 cusp 阶 $e=1$、原 $\mathcal H=H^3$ 的全部准确识别前缀、实际权六基的完整有限域比较，以及原模型分母规格。这些可直接作为下一次原 $L$ 函数恢复的输入。

原 $A,B,y,\beta$ 及实际高度配对尚未由本次计算输出。$\mathcal H$ 保留原 $h$ 的立方信息；恢复 $x$ 时仍必须使用原 $h$，以固定原 CM 微分方向。固定 $p=41$ 的这些原映射输入也不替代全部 $p$ 的 Serre 一致性或实际高度共同排根。上述缺口继续保持 OPEN。

## 依据

- [R735](R735-exact-original-p41-CM-model-and-Neron-input.md)：原 $b$ 与已保存的真实模型。
- [R745](R745-certified-original-p41-Hodge-and-adelic-input.md)：原相位、六 Hodge 基及参考 cusp 的真实 minor。
- [R748](R748-original-signed-real-CM-root-and-rational-Hodge-first-jet.md)：同一原 newform 的已完成 4096 前缀。
- [R759](R759-certified-original-integral-period-lattice-and-map-degrees.md)、[R764](R764-certified-original-cusp-images-and-base-translation.md)：原第 4 号映射、次数和零平移。
- [R767](R767-original-quotient-low-weight-RR-basis-and-cusp-order-bound.md)、[R772](R772-original-RR-descent-and-exact-function-recovery-certificates.md)：原权六线丛、字段、准确立方归一与唯一性界。
- [R774 运行前完整方法](../notes/R774-original-Hodge-cube-method.md)及本篇列出的公开准确证书。
