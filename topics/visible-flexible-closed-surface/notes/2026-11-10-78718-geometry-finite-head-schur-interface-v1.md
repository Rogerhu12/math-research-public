# R520 的可见振幅入口：有限头部低逆证书的准确范围

作者：Astra-visible-flex-78718bd0 / geometric_closure，2026-11-10。

**状态：未参与者独审前的证明与接口备忘。** §2 的算子引理有完整证明；
它仅替代 R518 的一个低 Schur 小量门。本文没有给新 Darboux 零点，
没有证明某个现成有限 BVP 矩阵就是该 Schur 矩阵，也没有移除 R520 的全部
小振幅假设。尤其不是 README 的 G5 或强比例精确存在证明。

## 1. 真实来源与本次核查范围

root 以终端 git 单取下列原 results 文件，没有取相邻数据目录：

| 原文件 | 字节数 | SHA256 |
| --- | ---: | --- |
| `topics/continuous-flexibility-swarm/results/R520-actual-newton-zero-height-closed-flexibility.md` | 70061 | `919f21d91c1e6597e44be0d875d435a9177d925b44e6eec50bf6bedbdbfc292f` |
| `topics/continuous-flexibility-swarm/results/R517-cumulative-direct-log-m3-high.md` | 67563 | `f5f3c7254ae283f20a6f783de400f117c032271f0a461fd31adee6a683030ba6` |
| `topics/continuous-flexibility-swarm/results/R518-cumulative-current-green-network.md` | 44326 | `1aa634f02dea2f4aa6b88a5569f3bd98fa15544e2f0da0a3f3adaaa18c630e13` |

root 核实后二项取回时的 `origin/main` 是
`fd0cd567eab16cc4c5cce2d29b00ea806ecb4cae`。本文以实际冻结内容哈希识别，
不由该来源记录推断新有限矩阵或尾界已经得到验证。暂存路径依次是
`/tmp/78718-source-R520.md`、`/tmp/78718-source-R517.md`、
`/tmp/78718-source-R518.md`。

本次全文读 R520 的数学正文 §§0–13 及来源表。R517 读集中命题、
§§0–1、§§7–8 的实际锚定/高逆/raw-prime 部分；R518 读集中定理、
§§2.1–4、§5.1 的完整几何/源/低块接口。未声称重新独审其全部上游依赖。

R520 的真实内容是：对足够小的固定非零 $q$，在实际嵌套好集上构造
收敛 Newton 序列，取得全 Darboux 残差为零、两端固定开 flat 领的非径向
高度，再经 R95/R78 的展开、封帽和相位作用得到闭曲面族。
所有相位用最终同一度量。其 $q$ 门没有本题可见比例的有效下界。
“先解出一个非径向零点，再固定最终度量并作相位族”确实不要求
在预先冻结的径向剖面上存在一整条振幅分支；但也不允许把有限 jet
或小的有限离散残差代替这个非径向零点。

R517 (7.8) 的 component high 小量含
$J_m^{p-r}=J_m^{-.69}$，其中 $p=1.3$、$r=1.99$。
因此，在**另已取得该实际头部的完整 normal form、真实 target gap、
各物理局部图逆与有限值表**的条件下，有限个头部节点的高块不必通过
“总振幅趋零”来变小：可在开工表中一次提高共同 cut。
这要求同时重建基线低系统和全部 source/row 表，不能在已运行的
Newton 中随意提高 floor。

真正的低块门是 R518 (4.5)–(4.7)。它定义
$$
M=U_L^{-1}(S_*-S_0)U_L^{-1},
\qquad K_*=K_0(I+MK_0)^{-1}.
\tag{1}
$$
$K_0$ 是由原完整物理 Green 真运输而来的选定实现。
原稿用 $\|MK_0\|<1/4$ 支付 (1)。以下给一个无需该总 norm 小量的
准确替代；它保留同一个 $K_0$ 和同一个选定范围。

## 2. 有限头部证书引理

令 $\mathscr H$ 为实或复 Hilbert 空间，$P$ 为有限秩正交投影，
$Q=I-P$。设 $K_0,M\in\mathcal B(\mathscr H)$，置
$$
A=MK_0,\qquad B=I_{P\mathscr H}+PAP|_{P\mathscr H}.
\tag{2}
$$
假设给出以下真实上界：
$$
B^{-1}\text{ 存在},\qquad
\|B^{-1}\|\le b,\qquad
\|PA\|\le a,\qquad
\|QA\|\le t,
\tag{3}
$$
并有严格不等式
$$
\eta=(1+ba)t<1.
\tag{4}
$$
则 $I+A$ 为 $\mathscr H$ 上双向有界可逆算子，且
$$
\|(I+A)^{-1}\|\le\frac{1+ba}{1-\eta}.
\tag{5}
$$
于是
$$
K=K_0(I+MK_0)^{-1},\qquad
\|K\|\le\|K_0\|\frac{1+ba}{1-\eta},\qquad
\operatorname{Ran}K=\operatorname{Ran}K_0.
\tag{6}
$$
不要求 $\operatorname{Ran}K_0$ 闭，不要求 $K_0$ 在任意最大域上为逆，
也不要求 $\|A\|<1$。

**证明。** 先令 $A_P=I+PA$。按
$\mathscr H=P\mathscr H\oplus Q\mathscr H$ 分块，它正是
$$
A_P=\begin{pmatrix}B&PAQ\\0&I_Q\end{pmatrix}.
\tag{7}
$$
设 $\iota:P\mathscr H\hookrightarrow\mathscr H$ 为包含映射。
直接乘法，或按 (7) 解两个分量，得到
$$
A_P^{-1}=I-\iota B^{-1}PA,
\qquad \|A_P^{-1}\|\le1+ba.
\tag{8}
$$
式 (8) 中 $B^{-1}$ 只作用于 $PA$ 的有限维输出，域没有混淆。
现在
$$
I+A=A_P+QA=A_P\bigl(I+A_P^{-1}QA\bigr).
\tag{9}
$$
由 (3)–(4)，第二因子的偏离恒等项的 norm 不超过 $\eta<1$，
故其 Neumann 级数在算子 norm 中绝对收敛，是双向 inverse。
这证明 (5) 及 (6) 的 norm 界。
最后 $(I+A)^{-1}$ 映满 $\mathscr H$，所以
$K_0(I+A)^{-1}(\mathscr H)=K_0(\mathscr H)$，得到范围等式。
证毕。

如果 $S_0$ 在选定场范围 $\mathscr R=\operatorname{Ran}K_0$ 上已经有
真实左右身份，且实际方程的差恰为 $M$，则相同代数也给当前的左右身份。
更精确地，若 $S_0K_0=I$、$K_0S_0x=x$ 对所有 $x\in\mathscr R$
成立，而 $S=S_0+M$ 在该范围合法，则
$$
SK=(S_0+M)K_0(I+MK_0)^{-1}=I.
$$
若 $x=K_0y\in\mathscr R$，则
$$
KSx=K_0(I+MK_0)^{-1}(I+MK_0)y=K_0y=x.
$$
在 R518 的实际应用中，两侧 $U_L$ 必须按原 (4.5)–(4.7) 运输；
上段的 $S_0,S$ 是运输后的实现。不能省掉这两个权，再把任意离散
Jacobian 填入 (2)。

该证书在尾紧情形没有额外的定性损失。事实上，若一列 $P_N$ 满足
$t_N=\|(I-P_N)A\|\to0$，而 $I+A$ 已可逆，记
$c=\|(I+A)^{-1}\|$。当 $ct_N<1/2$ 时，
$$
I+P_NA=(I+A)\bigl(I-(I+A)^{-1}(I-P_N)A\bigr)
$$
可逆，逆 norm 不超过 $2c$。由 (7) 得 $B_N$ 可逆，
$\|B_N^{-1}\|\le2c$，且 $\|P_NA\|\le\|A\|$。
再取 $N$ 使 $(1+2c\|A\|)t_N<1$，便满足 (4)。
这只是完整性的证明，不会从未知的 $c$ 产生实际数值证书。

## 3. 有限矩阵可以怎样被严格计算认证

设选定了 $P\mathscr H$ 的正交基，有数值矩阵 $\widetilde B$ 与一个
明确近似逆 $C$。若对真实 $B$ 有
$$
\|I-C\widetilde B\|\le e_0,\qquad
\|B-\widetilde B\|\le e_1,\qquad
e_0+\|C\|e_1<1,
\tag{10}
$$
则
$$
\|I-CB\|\le e_0+\|C\|e_1<1.
$$
有限维方阵 $CB$ 因此可逆，故 $B$ 也可逆，并且
$$
\|B^{-1}\|\le
\frac{\|C\|}{1-e_0-\|C\|e_1}.
\tag{11}
$$
这里全部范数须对应实际 Hilbert 规范。若所存矩阵用非正交物理基，
必须先用已认证 Gram 矩阵换基，或完整计算等价范数常数。
一张浮点 determinant 非零、未加权的条件数或优化器报告的逆均不够。

(10) 只支付有限 $b$。还必须独立支付 (3) 中的 $a,t$；
仅检查有限 $B$ 可逆不能排除无限尾上的核。

## 4. 无限径向低空间为何可以有尾估计，及尚缺的数据

R518 的“低”按每个径向端口各自的角 floor 定义，仍含无限个径向端口。
它不是一个普通有限矩阵。设其准确空间写为
$$
\mathscr H=\mathbb C^d\oplus\bigoplus_{m\ge1}\mathscr H_m,
\qquad \dim\mathscr H_m<\infty,
$$
每个 $H_m>0$ 且 $H_m\to0$。令 $P_N$ 包含全部 $d$ 个标量槽及
前 $N$ 个端口的完整低频槽。若对实际 $M$ **另已证明**
$$
\|D_{-\delta}M\|\le C_M,
\qquad (D_{-\delta}x)_m=H_m^{-\delta}x_m,
\qquad \delta>0,
\tag{12}
$$
其中有限标量槽的权为 1，则
$$
\|(I-P_N)MK_0\|
\le \Bigl(\sup_{m>N}H_m^\delta\Bigr)C_M\|K_0\|.
\tag{13}
$$
**证明。** 在尾上逐分量提出 $H_m^\delta$，按 Hilbert 平方和求和，
先得 $\|(I-P_N)Mx\|\le(\sup_{m>N}H_m^\delta)C_M\|x\|$，
再代入 $x=K_0y$。证毕。

故在 (12) 下 $MK_0$ 是有限秩算子的 norm 极限。
如果某些标量列只给定属于 $\mathscr H$，也可以将它们的真实列尾范数
逐列加入 (13)，但没有已知列尾率时不能凭其有限秩声称有效的 $t$ 已知。

R518 已显示的相关余量是：四 Schur corners 的第三 resolvent 项
有角/radial 净 gain $.37/.94$，前两项为 $2.68/.76$；两个 $U_L^{-1}$
总共消耗径向 $.5$。最弱直接低项使用
$$
\sigma-\tfrac12-h_{\rm low}\ell
=.08-1.01h_{\rm low}>0.
\tag{14}
$$
这解释为何值得尝试 (12)。但 (14) 本身并不提供本题实际的 $C_M$：
还需原固定 low cut 的上增长界、全部材料吸收、各端口权比、四 corners
和两 scalar 列的真实强表。特别不能只引用 R518 (4.5) 的无权 norm 界
就断言已获得 (12) 的数值常数。

## 5. 这个替换没有支付什么

有限头部路线还必须逐项处理以下依赖；它们是实际证书的输入清单，
不是本文已建立的存在性假设。

1. **完整几何的近正 mean/type 和局部物理图。** R517 §8.2 的
   $E_N^{-1}$ 是在原 Fourier baseline 附近按真差构造的；本引理
   不替代其 raw/prime 变换，也不替代负段 Cauchy 和正 cap 的逆。
2. **有限头部实际主图的规范化。** 原 canonical circle conjugacy、
   两 cones 的同一 lift/常平移、homogeneous DC 与 inhomogeneous
   target gap 都需重新验证。有限 Taylor 符号不代替完整 return。
3. **与当前有限 BVP 的真实运输。** 需要从其完整 ordinary source、
   raw metric column、moving row、mean 和 two-end affine 常数，
   得到 (2) 的同一个 $M,K_0$；有限 moment Jacobian 不自动等于 $B$。
4. **非线性 Newton 的后续。** 即使取得这一真低逆，仍需足够强源范数
   下的真实残差、完整 Hessian 余项、所有角宽损失与当前 good-set 选择。
   小的采样 metric 残差单独不支付这些项。
5. **可见比例。** 真 Newton 修正还须给全曲面 $C^2$ 位移界，才能用
   本题已有稳定性工具保住 held 和 reach 的正余量。原 R520 的
   “足够小 $q$”没有这个定量结论。

本文只把低块的总小量门改写成一个可具体审核的有限矩阵加尾条件。
当这些实际矩阵、范数和局部 provider 未构造时，不据此宣称存在
大振幅精确闭族。本文没有运行 PDE、Newton 或新的数值候选。
