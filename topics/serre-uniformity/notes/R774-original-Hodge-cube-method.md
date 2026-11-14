# R774：原第 4 号微分的完整权六立方前缀

日期：2026-11-14。状态：**公开运行前的方法；没有预称 R774 已返回数值。**
本任务直接生成原 $d=1206$ 映射的微分立方 $\mathcal H=H^3$ 在参考 cusp 的全部 $q_Y^0,\ldots,q_Y^{820}$ 系数，并提取该实际微分的尖点阶 $e$。它读取已经成功的 R771 权六基作有限域核对；不会把有限域坐标冒作特征零坐标，也不预称已得到 $y$、$\beta$ 或高度。

## 1. 已经完成而必须复用的输入

保持原 $K=\mathbf Q(\zeta)$、$s=1+2\zeta$、$s^2=-3$、
$L=K(b)$、$M=L(\xi)$、$\xi=e^{2\pi i/41}$、
$Q=e^{2\pi i\tau/246}$、$q_Y=Q^3$。
$[L:K]=7$、$[M:L]=40$，故
$$
b^i,\ sb^i\quad(0\le i<7),\qquad
1,\xi,\ldots,\xi^{39}
\tag{774.1}
$$
给出本次全部数域系数的准确有理坐标。原 $b$ 是 R735 的真实扭曲系数；不换成另一个同构模型，不选择新的共轭。

| 既有产物 | 公开 run | SHA-256 |
|---|---:|---|
| R735 原模型小证书 | 43608152850 | 752aa03f9cbe7d3174a7c508fce3043e21e8e85fd087e01acc4bca82a5cbd574 |
| R745 原 Hodge 小证书 | 43616027318 | 7fdac934ab8be401afbe793c9dd6d790bba2dc1f39cdbb134fc51748870816be |
| R745 原 Fourier／有限向量表 | 43616027318 | a629d550bd2f3102111bbb58fe707470081e2062da10221ab778fe3ba71b53dd |
| R748 原 newform 系数至 4096 | 43617493590 | 0c7d73a2a2c9202c6a25f343c9357a8b59d9cfc4928a29b5d460dbf84828bff0 |
| R759 原次数小证书 | 43625474728 | 7c2c611b9a5f43bc3a2a0007bf2cb5dd2fa8d10f133b663dbca0d054e1515de0 |
| R759 原 12 个微分向量 | 43625474728 | 037b56d016d502408173319d76a3067a65dd50250c31bc2225c0fca598396ecc |
| R771 原 RR 基小证书 | 43628998192 | 9eb870af949167895daa4e180c16848860f8fea1c9efe1b105ab3cd3a667009f |
| R771 原完整 694 基状态 | 43628998192 | 3cc9022b6ff07f5bc1cb57a9ddd5190673e3ad527958ca2439b317f5517b981e |

R771 实际源是 $\,\mathtt{49abc04d7867c9f56911866494692c597cf642d7}\,$，核心 SHA 为
$\,\mathtt{9cda269687a01c95c9c20695be771706bbddd37b1b8fedc8b9258386c3965d46}\,$。
其实际 $M_2,M_6,M_{12}$ minor 分别为 $550,206,140\bmod739$。本次读它的真实 $M_6$ 系数表与主元列，不再求这三个基。

特别是 R748 已完成**同一个**原 $\theta$ 的 newform 系数至 4096。它的前 801 行和 R745 逐字一致；本次只读到 2460，**不再枚举任何 primary 格点，也不重算任何 $a_n$**。R745 的 40 个原平均坐标 $c_r$ 与原前 800 阶 Fourier 迹也直接复用。

理论范围、归一和唯一性使用已经发表的
[R772](../results/R772-original-RR-descent-and-exact-function-recovery-certificates.md)，
SHA-256 为 $\,\mathtt{30006eca29d55c9b2e227f490e0ec9ffe128073f1c49c6dab25d3e532f4db59d}\,$。

## 2. 实际微分及不变的全部相位

R759 真实第 4 号向量给
$$
h=\sum_{j=0}^5v_j\omega_j,\qquad v_j\in L,\qquad \deg f_0=1206.
$$
这里的 $\omega_j$ 是 R745 原六基；系数向量已含原周期比较所得的比例。不能将它替换为任意同一 Hodge 子空间的组合。

定义原整数迹多项式
$$
P_{j,n}(\xi)=\sum_{r=1}^{40}
\operatorname{Tr}_{F/\mathbf Q}(\beta^j a_n c_r)\,
\xi^{-nr\,6^{-1}},
\tag{774.2}
$$
指数中的 $6^{-1}$ 在 $\mathbf F_{41}$ 中取值。所有 $a_n,c_r,\beta$ 都在 R745 固定的 $\Phi_{42}$ 幂基中。整次数 12 的迹要除以 2，才是原实 Hecke 域的次数 6 迹；源码检查每次所得整数确可被 2 整除。

保留两个原 tame 行因子：
$$
F_j(Q)=
\sum_{n\ {\rm odd}}sP_{j,n}(\xi)Q^n+
\sum_{4\mid n}3P_{j,n}(\xi)Q^n,\qquad
F=\sum_jv_jF_j.
\tag{774.3}
$$
原 $n\equiv2\pmod4$ 项为零。$P_{j,n}$ 在原 $\Phi_{41}$ 基中具有次数至多 39。R745 已保留 (774.3) 到 800；本次仅产生 $801\le n\le2460$ 的新迹行。

准确微分归一是
$$
h=\frac{\alpha}{7}F(Q)\frac{dQ}{Q}
 =2\pi i\,H(\tau)d\tau,\qquad
H=\frac{\alpha}{1722}F,\qquad \alpha^3=4.
\tag{774.4}
$$
因此
$$
\boxed{\mathcal H=H^3=\frac4{1722^3}F^3.}
\tag{774.5}
$$
没有再次乘 $\alpha s$、$246$ 或 $c_1$ 的 $\zeta^2$。
所有展开仍在同一参考 cusp；$c_1=4424$ 只是被保留的原模型标记，不是把展开中心搬到 $c_1$。

## 3. 特征零尖点阶的实际提取

原 R745 的六个参考 cusp 指数 $1,4,7,13,16,19$ 的行列式在模 739 为 407，已证明任何非零 $L$ 线性组合 $h$ 的局部原函数首阶 $e\le19$。
本次不重算该 minor，而是把这几个原 Fourier 多项式与真正的 $v_j$ 作精确 $L$ 运算。

逐个 $\xi$ 坐标检查
$$
\sum_jv_jP_{j,n}(\xi)
$$
是否为零，再乘原 $s$ 或 3。由 (774.1) 的线性独立性，全部四十个 $L$ 坐标为零恰好等价于该实际 $M$ 系数为零。首个非零指数即为真实 $e$，必满足 $1\le e\le19$、$e\equiv1\pmod3$。其完整原 $F$ 首系数保存在 artifact；原 $H$ 首系数是它乘 $\alpha/1722$，原零常数 primitive 的首系数是它乘 $\alpha/(7e)$。

此处的 $e$ 不由所选次数 1206 反算，也不由另一个嵌入的 Abel 首项猜测。后续立方产生的首个非零 $q_Y$ 指数须与该 $e$ 一致。

## 4. 先在小整数系数环立方，避免大数域逐项卷积

原支撑 $n\equiv1\pmod3$ 给
$$
F_j(Q)=Q\,G_j(q_Y),\qquad
G_j=R_j+sS_j,\qquad R_j,S_j\in\mathbf Z[\xi][[q_Y]].
\tag{774.6}
$$
$R_j$ 已含原因子 3，$S_j$ 已含原因子 1；以后不再补这个因子。为得到 $\mathcal H$ 至 $q_Y^{820}$，只须 $G_iG_jG_k$ 的次数 $0,\ldots,819$，然后在 (774.5) 中**恰好移动一次** $q_Y$。

用一个普通整数多项式变量 $Z$ 编码
$$
q_Y^k\xi^r\longmapsto Z^{121k+r}.
\tag{774.7}
$$
每个输入的 $\xi$ 次数不超过 39；二积不超过 78；三积不超过 117，均严格小于 121。因此所有二积和三积的 $\xi$ 指数都不会进位到下一个 $q_Y$ 块。在每次乘法中截去 $Z^{121\cdot820}$ 及以上项，恰好保留全部所需的 $0\le k<820$，不会从被丢弃的高阶项向低阶回流。

对 $s^2=-3$，使用
$$
(A+sB)(C+sD)=(AC-3BD)+s(AD+BC).
\tag{774.8}
$$
交叉项通过 $(A+B)(C+D)-AC-BD$ 计算，全部是整数多项式的精确低乘。程序保存 21 对 $i\le j$ 的二积，然后生成 56 个 $i\le j\le k$ 的三积；每个完成项立即保存，续算不重算它。

对每个完整三积块，再准确约化 $\xi$。先以 $\xi^{41}=1$ 把次数 $0,\ldots,117$ 汇总成 $c_0,\ldots,c_{40}$，再用
$\Phi_{41}(\xi)=1+\cdots+\xi^{40}=0$ 写为
$$
\sum_{r=0}^{39}(c_r-c_{40})\xi^r.
\tag{774.9}
$$
这给出 56 对、每对 $820\times40$ 个普通整数系数。这里没有浮点计算、近似尾项、猜测有理重构或替换根方向。

## 5. 真正 L 系数与每坐标行的精确尺度

对每个有序非降三元组令
$$
m_{ijk}=\begin{cases}
1&i=j=k,\\
3&\text{恰有两个指标相等},\\
6&\text{三个指标互异},
\end{cases}
\qquad
c_{ijk}=\frac{4m_{ijk}}{1722^3}v_iv_jv_k\in L.
\tag{774.10}
$$
它们恰重构整个 $(\sum_jv_jG_j)^3$，并非只取 56 项而漏掉重数。

使用 R735 已有的**原**七次有理最小多项式约化 $b$，使用
$\zeta^2+\zeta+1=0$ 约化 $K$。若
$c=A+B\zeta$，则
$$
c=(A-B/2)+(B/2)s.
\tag{774.11}
$$
记这个表达式为 $a+sb$。与三积 $R+sS$ 相乘时，
$$
(a+sb)(R+sS)=(aR-3bS)+s(bR+aS).
\tag{774.12}
$$
故共有一个 $14\times112$ 的有理矩阵：14 行依次为 $1,b,\ldots,b^6,s,sb,\ldots,sb^6$；112 列是每个三积的实部、$s$ 部。它的四块正是 $a,-3b;b,a$。

原七次多项式的有理系数较大。为避免把每个坐标都乘上不必要的巨大公共分母，程序对每一行单独清分母并除去整数 content：
$$
\text{该有理行}=\rho_i\cdot\text{一条 primitive 整数行}.
\tag{774.13}
$$
$\rho_i$ 的准确有理分子、分母仅保存一次。将 primitive 整数矩阵乘以 (774.9) 的整数系数块，再把对应行乘 $\rho_i$，就是原 $\mathcal H$ 的准确特征零坐标。这个分解只是整数尺度压缩，没有更换数域、基或实际微分。

输出按 32 个 $q_Y$ 指数分块，保存 primitive 整数和尺度阶段的 SHA。每个消费者必须按 (774.13) 乘回尺度；不能把所存整数直接称为 $\mathcal H$ 的系数。$q_Y^0$ 系数为零，其他块完整覆盖 $1,\ldots,820$。
源码核对全部精确块的首个非零指数与 §3 的真实 $e$ 相等。

作为原输入的一个小规格，程序还把 R735 公共最小多项式分母除去 2、3 的幂并记录余因子；不重新计算原模型。没有预称余因子的值。

## 6. 实际 M6 基的辅助有限域核对及其边界

本次读取 R771 真正成功的 694 基、真实主元系数列和非零 minor 206。它们在
$\ell=739,\xi\mapsto538,s\mapsto98$ 使用同一原 cusp 相位。
令 $D$ 为 (774.13) 全部行尺度分母的最小公倍数。
把完整准确 $\mathcal H$ 前缀逐系数乘 $D$，再约化上述 $\xi,s$，得到七个 $b$ 坐标的模 739 系数列。

程序在 R771 原主元列上解 694×694 系统，随后把解代回**全部 821 个指数、全部七个坐标**。它核对的是
$$
D\mathcal H\bmod739,
\tag{774.14}
$$
不是在未经验证 $739\nmid D$ 时擅自除以 $D$。
结果同时记录 $v_{739}(D)$；若该清分母带来退化，凭据明确保留这一事实。这个辅助核对不承担特征零生成的证明。

本次完整特征零 $\mathcal H$ 系数来自 §§2–5 的准确公式。由 R772，
$$
\mathcal H\in M_6(Y/L)
=H^0(3\mathcal L+2P_0+2P_1),\qquad
\deg(3\mathcal L+2P_0+2P_1)=820.
$$
因此所生成的 $q_Y^0,\ldots,q_Y^{820}$ 已**唯一确定原 $\mathcal H$**。
但 (774.14) 单独不能把 694 个模坐标提升为特征零坐标；最终证书明确把
`characteristic_zero_M6_basis_coordinates_computed` 置为 false。
后续 R775 的真实 $K$ 基可以直接使用这些准确前缀，在原 $L$ 上求其真正坐标，而不再重算 $\mathcal H$。

## 7. 精确字段、资源和继续工作

核心：
`scripts/R774_original_Hodge_cube.py`。
包装：
`scripts/R774_public_Hodge_cube.py`。
请求：
`notes/R774-public-original-Hodge-cube-request.json`。
Workflow：
`.github/workflows/serre-p41-original-hodge-cube.yml`。

所有新算术只在公开仓库 Actions、Python 3.12、python-flint 0.9.0 执行。
请求绑定四个实际 producer artifact 的 manifest、run/source，以及 R735 小证书、R772 原证明和所有脚本 SHA。
R771 已真实成功后才填入其实际证书与 $M_6$ 状态；不存在预填的成功哈希。

旧 R745 与 R748 的 producer 在 artifact 上传之后才于发布目录生成小 manifest，因此其 artifact 本身没有该 manifest。包装显式读取 Git 已发表的小 manifest 并核所列固定 SHA，再以这些真实 manifest 校验 artifact 内的数据与 run receipt。较新的 R759、R771 则从 artifact 读取 compute 阶段已生成的 manifest。这一位置区别由四个原 producer 的代码核实，不靠放宽哈希或猜测文件名；首个 R774 run 在数学核心前因旧 manifest 位置假设而失败，修正不改变核心或任何算术输入。

新的 Fourier 迹按 64 个 $Q$ 指数保存游标；六个打包整数函数、21 二积、56 三积、真实 $L$ 尺度、每个最终系数块和辅助模比较各有独立完整阶段。
完成阶段按配置和 SHA 直接恢复。若 80 分钟预算耗尽或异常，全部完整及部分状态保留到 artifact，同一配置续算；不以中断凭据注册成功。

这些可复现整数表和大精确系数仅进入 artifact；Git 只保存小证书、小输入／运行凭据、日志与全文件 SHA 清单。
最终小证书只引用大尺度和系数块，不把整个 560 维系数表塞入 Markdown 或 Git。

真正后继仍是 R772 的原 $K$ 基、$L$ 上的准确函数恢复和完整核验。R764 已证明原平移为零；本次保持这个原基点，不重新选择三个 CM 平移之一。本次不计算 $A,B,y,\beta$，不将 Abel 立方、权六形式或固定层原映射输入替代主目标的实际高度排除。

## 依据

- [R735](../results/R735-exact-original-p41-CM-model-and-Neron-input.md)：原 $b$ 的真实七次多项式。
- [R745](../results/R745-certified-original-p41-Hodge-and-adelic-input.md)：原 $c_r,a_n$、$6^{-1}$ 相位、$s/3$ 因子及微分 246。
- [R748](../results/R748-original-signed-real-CM-root-and-rational-Hodge-first-jet.md)：同一原 newform 的已完成 4096 前缀。
- [R759](../results/R759-certified-original-integral-period-lattice-and-map-degrees.md)：真正第 4 号 $L$ 微分向量和次数 1206。
- R771 [实际公开 run](https://github.com/Rogerhu12/math-research-public/actions/runs/43628998192) 及上表完整证书：实际 694 基、其系数列与非零 minor。
- [R772](../results/R772-original-RR-descent-and-exact-function-recovery-certificates.md)：原字段下降、$H^3$ 的准确归一与权六次数 820。
