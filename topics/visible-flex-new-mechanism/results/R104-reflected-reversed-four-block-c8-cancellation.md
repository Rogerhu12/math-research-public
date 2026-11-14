# R104：反射与倒行四块的闭合环带及准确 c⁸ 消项

日期：2026-11-14。**已证明。** 本稿使用 [R70](R70-zero-matrix-bridges-and-affine-complete-fourth-period.md) 的真实零矩桥、[R83](R83-true-fourth-transfer-and-zero-lower-history-variations.md) 的完整传递和 [R100](R100-pure-tail-c8-period-and-three-true-histories.md) 的短 action；没有新的研究计算。

结论是一个有限、光滑、同端口的四块构造。它同时支付 frame 与中心线周期闭合、完整第二矩阵和第三算子为零，并使 R100 的 D25 周期多项式最高未消系数 c⁸ 准确为零。因此该特定 D25 周期多项式的次数降到至多七。这里的带仍有两个横向边界，且只得到正则浸入；没有闭嵌入材料面、完整第四 range、有限等距族或 reach 结论。

## 1. 固定端口及两种不同变换

令

$$
D=\operatorname{diag}(-1,1,-1),\qquad
S=\operatorname{diag}(-1,1,1),\qquad
A=-S=\operatorname{diag}(1,-1,-1).
\tag{1}
$$

固定 h₀>0 和 scalar 常值芽

$$
(h,k,\omega)=(h_0,0,0).
\tag{2}
$$

由 R70 §1，存在正的有限长度 L 及真实 C∞ 路径 B，其首末具有 (2) 的同一常值芽，初始 frame 为 I，末 frame 为 D，并满足完整 M_B=0。记初始位置为零、末位置为 V。

路径方程始终为

$$
F_s=F\Omega(k),\qquad
\Omega(k)=\begin{pmatrix}0&-k&0\\ k&0&1\\0&-1&0\end{pmatrix},
\qquad \alpha_s=h^2T,\qquad \omega_s=\frac{k_s}{2h}.
\tag{3}
$$

定义保持正向 s 的 scalar 反射

$$
\sigma B:(h,k,\omega)\longmapsto(h,-k,-\omega).
\tag{4}
$$

因为 Ω(−k)=SΩ(k)S，且 S 与 D 对易，以 I 为初始 frame 时

$$
F_{\sigma B}=S F_B S,\qquad
\alpha_{\sigma B}=A\alpha_B,\qquad
F_{\sigma B}(L)=D,\qquad
\Delta\alpha_{\sigma B}=AV.
\tag{5}
$$

(2) 恰被 (4) 固定，所以这里无需增添未经计费的连接路径。该反射保持完整 M=0；其系数与迹核对见[反射及右锚说明](../notes/pure-tail-c8-sign-reflection-and-right-anchor-20261114.md) §3。

另一操作是真实同 k 倒行 R。对任一 I→D 的块 C，取其标量控制在 s↦L−s 下的反向值。R45 的准确公式是

$$
F_{C^R}(s)=F_C(L-s)D,\qquad
\alpha_{C^R}(s)=\alpha_C(L-s)-\alpha_C(L),
\tag{6}
$$

所以 C^R 仍从 I 到 D，且位移为 −Δα_C。它保持 u、ξ 的物理分支，不是 (4) 的 scalar 反射。分别应用于 B 和 σB，得到位移 −V 和 −AV。

## 2. 一个共同正物理区间

先固定上面的有限 B。由于 h 连续为正、ω 有界，四块 B、σB、B^R、(σB)^R 共享一个紧 scalar 包络：h 的范围不变，而 ω 的范围包含在 [−W,W] 内，其中 W=max|ω_B|。

可在所有块选好后，一次取一个有界开区间 I=(a,b)，满足 a>W。于是存在 δ>0，使整个四块和 ξ∈I 的闭子区间均满足

$$
\xi+\omega(s)\ge\delta>0,\qquad
u=\frac{h}{\xi+\omega}>0.
\tag{7}
$$

后面全部块使用同一个 I、同一个 ξ 和同一个右 Volterra 锚。没有把原来的 profile 反射到 −I；也没有在各块改变 ω 的规范。

(5) 中与旧几何的直接识别需要 u 反号，但本构造不使用那项识别来比较第四成本。这里把 σB 当作另一个真实正支块，(7) 同时为它支付物理区间。随后使用的只是已经在相同尾参数 c 下证明的 c⁸ 系数恒等式。

## 3. 四块 frame 与中心线准确闭合

按顺序拼接

$$
\boxed{\mathcal C=B\,\sigma B\,B^R\,(\sigma B)^R.}
\tag{8}
$$

每段的相对 frame 增量都是 D，故全局 frame 依次为

$$I\longrightarrow D\longrightarrow I\longrightarrow D\longrightarrow I.$$

将每块的局部中心线位移乘实际入 frame，得到

$$
V,\qquad DAV,\qquad -V,\qquad -DAV.
\tag{9}
$$

完整账目为：

| 块 | 本地初末 frame | 本地位移 | 实际前缀 frame | 全局位移 |
|---|---|---|---|---|
| B | I→D | V | I | V |
| σB | I→D | AV | D | DAV |
| Bᴿ | I→D | −V | I | −V |
| (σB)ᴿ | I→D | −AV | D | −DAV |

前三列由 (5)、(6) 在各自本地初始 frame I 中计算，第四列是之前所有 D 的有序乘积。最后一列才是在同一个全局坐标系中的实际位移。

其和严格为零。这里 α 按 (3) 真实累积，未在块间重设位置；(9) 是全局位置的实际账目。

所有块具有同一 scalar 常值端芽。采用真实入 frame 和真实起点位置拼接，(3) 的 ODE 给所有接缝的 jet 相接。末端又回到原 frame、位置和相同 scalar 芽，所以形成 C∞ 周期数据。

对环向 s∈R/(4LZ) 及横向 ξ∈I，置

$$
X(s,\xi)=\alpha(s)+\frac{h(s)}{\xi+\omega(s)}N(s).
\tag{10}
$$

在物理 (s,u) 坐标中

$$
X_s=(h^2-ku)T-uB,\qquad X_u=N,
$$

故

$$
|X_s|^2=(h^2-ku)^2+u^2>0,\qquad X_s\perp X_u.
\tag{11}
$$

再由 u_ξ=−h/(ξ+ω)²≠0，(10) 为正则浸入环带。若取 I 的闭子区间，该环带有两个横向边界；环向周期闭合不等于主课题要求的无边界闭材料面，也不排自交。

## 4. 完整第二、第三传递均为零

每个块的完整第二矩阵为零。令

$$T_B=\tau,\qquad T_{\sigma B}=\widetilde\tau.$$

不需要假定 σ 保持或取负第三算子。分别对两个零矩块应用 R83 的真实倒行公式，得到

$$
T_{B^R}=-\tau,\qquad
T_{(\sigma B)^R}=-\widetilde\tau.
\tag{12}
$$

零矩块之间的完整第三传递准确相加，环境 frame 的常旋转不改变恢复中的点积。因此 (8) 给

$$
\boxed{M_{\mathcal C}=0,\qquad T_{\mathcal C}=0.}
\tag{13}
$$

这是对完整第三算子及全部 profile 槽成立的身份，不是一个选定 profile 的少量查询。它仍只是 characteristic 周期信息；逐 s 的第三 ruling 或第四 ruling 不因此自动消失。

同一传递也记录了尚未支付的完整第四成本：

$$
\boxed{V_{\mathcal C}=2V_B+2V_{\sigma B}.}
\tag{14}
$$

倒行的第四成本同号，故 (14) 中没有任何被略去的负基准。下面仅证明 (14) 的一个已指定尾系数为零，不把 V_{σB} 当作 −V_B。

## 5. c⁸ 系数的真实加法及两种符号

严格沿用 R100：对单位尾 q=(c−ξ)⁸，令 D25 为完整第四 period 密度中 (c−ξ)²⁵ 的系数；c 是共同尾端点参数。记该周期多项式为

$$\mathscr A_B(c)=\int_B D25(s,c)\,ds,$$

并记

$$
a_8(B)=[c^8]\mathscr A_B(c)
=\frac{307328}{15}\int_B\mathcal R_8\,ds.
\tag{15}
$$

这里使用单位幂尾的既有约定；并未把这个局部尾公式替换成某个已满足全体矩与 collar 条件的合法光滑圆。

R100 的三个真实坐标为

$$
p=B_4,\qquad \eta=\omega-k/h,\qquad
\ell=B_3-J_2/2-\eta p,\qquad
\zeta=B_3-4\eta p,
$$

且

$$
\mathcal R_8=
\frac25p(\zeta+10\ell)\zeta_s
-\frac25\frac{k}{h}p^2
-\frac1{20}p_s\zeta_s-\frac15p_s\ell_s.
\tag{16}
$$

完整 M=0 给 p、ℓ、ζ 在每块两端均为零。因此按同一个真实首锚累计四块时，这些历史在接缝准确复位；没有以形式约定将非零 history 擦去。故 (15) 对四个零矩块直接相加。这也与 (14) 的完整传递一致。

真实同 k 倒行给 p、ℓ、ζ 反向取值并反号，其 s 导数反向取值但不反号；h、k、η 只反向取值。所以 (16) 是倒行偶的：

$$a_8(B^R)=a_8(B).\tag{17}$$

保持正向 s 的 scalar 反射则给

$$
(p,\eta,\ell,\zeta)\longmapsto(-p,-\eta,\ell,\zeta),
$$

并且 k↦−k、h 不变。逐项看 (16)，每项均反号，因此

$$a_8(\sigma B)=-a_8(B).\tag{18}$$

(18) 是在同一尾参数 c 下的系数身份，已经由真实参数系数 ODE 和共同零初值推出。这里没有对完整右锚函数作 ξ↦−ξ 的替换；所以不需要、也没有假设左右锚缺陷为零。

将 (17)、(18) 与真实加法合并，得到

$$
\boxed{
a_8(\mathcal C)=a_8(B)-a_8(B)+a_8(B)-a_8(B)=0.
}
\tag{19}
$$

原 B 的 a₈ 可以是任意实数，也可以已经为零；构造无须先决定它的符号或证明非零。

## 6. 准确次数降阶及尚欠条件

R95 已证明任意完整 M=0、常端芽路径的 D25 周期多项式次数至多八：原 c¹⁰、c⁹ 项是已支付的真实零端势。对 (8) 再用 (19)，得到

$$\boxed{\deg\mathscr A_{\mathcal C}\le7.}\tag{20}$$

这结束了“c⁸ 必须为同号且无法通过真实闭合设计消去”的潜在障碍；即使它在某个原 B 上非零，四块仍准确支付它。没有证明所有奇或偶参数系数的统一变换法则。尤其 c⁷ 以及更低项、其他幂尾系数和完整两个相位模式仍然保留。

式 (14) 是必须保留的完整成本。反射把完整几何的正支识别到负支，并交换左右 Volterra 锚；这些缺陷不会因 (19) 自动消失。本稿的共同正 I 和真实系数加法只足以证明所述一个尾系数消项。

下一步可以从完整 D25 原式核对更低系数的准确奇偶变换，或处理剩余 c⁷ 与 ruling；不能仅据 (18) 猜测完整第四成本反号。高阶收敛、有限等距族、全域嵌入、厚度、幅度和完整闭面仍未支付。
