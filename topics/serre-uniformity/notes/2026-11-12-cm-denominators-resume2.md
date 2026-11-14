# 固定 CM 的完整分母、三次覆盖和原始指标：接续工作记录

日期：2026-11-12；会话：serre-uniformity-resume2；执行分支：cm-denominators。

**状态：持续研究，O6 尚未解决。** 本分支只维护本笔记及新结果文件；根会话负责拉取、README 差异检查、HANDOFF、索引、日志和推送。研究对象仍是固定 $A:y^2=x^3-x$，没有把它替换成全部 Serre 一致性目标。

## 1. 接续时核查的接口

已读根 README 的授权和全部规则、本题 README、HANDOFF、open，以及算术路线的全部研究笔记；几何/QC 的指定笔记由另一分支负责。重点重读 R19、R32、R34、R37、R42、R46，随后核查根会话新写的 R50 全局对偶步骤。

### R19 的充分方向

没有发现其反向构造中遗漏的额外局部谓词。原始性使每个奇 $q\mid Z$ 为乘性约化，且 $v_q(\Delta)=p\,v_q(Z)$；由于 $p\nmid32Z$，降层属于水平与剩余特征互素的权二情形。需要的结论是该处惯性不分歧，不能换成整个 Tate 扩张已分裂。

特别地，不能用某些较弱版本 Mazur 原理中的 $q\not\equiv1\pmod p$ 假设，错误地否定完整 Ribet 降层的适用。R19 使用的完整水平降低与唯一层 $32$ 新形式给出实际 $E[p]\simeq A[p]$；这不是只凭两个局部导子相同所作的推断。

查阅原始来源入口：K. Ribet, “On modular representations of Gal($\overline{\mathbb Q}/\mathbb Q$) arising from modular forms”, Invent. Math. **100** (1990), 431–476，[作者公开稿](https://math.berkeley.edu/~ribet/Articles/invent_100.pdf)。本轮 PDF 文本提取不足以逐字核对全部原定理；上述审计主要核对仓库中已写出的数学适用条件，没有声称完成独立的降层定理重证。

### R46 的素数 3 与覆盖方向

重点检查了两个容易混淆的环节：

1. 在 $3\nmid a$ 时，$B_a:y^2=x^3+a$ 的三个同源核点在至多非分歧二次扩张后可见；两个有限点模 $3$ 的 $y$ 坐标为单位，均处于尖点三次曲线的光滑连通部分。它们的闭包确为 Néron 恒等分量中的有限 étale 子群，而非只有抽象的未分歧 Galois 模。R46 的 Lang–Hensel 推出论证因此真的将未分歧类送入 Kummer 像。
2. $f_P(T)=T^3-(U/3)T-2V/27$ 是 $\phi^{-1}(P)$ 的三点 Galois 集合，不只是具有相同判别式的一个偶然多项式。R46 的显式互逆公式把此点证明补全。指标覆盖的 Jacobian 是 $B_a$；到 $D_a$ 的映射次数为三，不能把两者方向对调。

核查二元三次覆盖的 Jacobian 公式所用原始文献：L. Alpöge, M. Bhargava, A. Shnidman, “A positive proportion of cubic fields are not monogenic yet have no local obstruction to being so”, Math. Ann. **391** (2025), 5535–5551，§1.1，[作者全文](https://arxiv.org/html/2011.01186v2)。该处给出 $z^3=f(x,y)$ 的 Jacobian 为 $y^2=4x^3+\operatorname{disc}(f)$；R46 的缩放由此确实给 $B_a$。该文的正比例结论没有被外推成指定分母支持上的统一结论。

未发现需要纠正 R19 或 R46 陈述的缺口。

## 2. R51：把最后的原始性谓词补成完整充分条件

完整证明：[R51-primitive-index-sufficiency](../results/R51-primitive-index-sufficiency.md)。

设 $p=6k+e$，$e=1,5$，候选三次域 $L$ 的最大整环基为 $(1,\omega,\eta)$。R42、R46 原先保留的最后接口是：指标覆盖有理点还须满足相应整数原始性。R51 现在证明，以下条件已足够：
$$
I_L(u,v)=\pm\mu_e|Z|^{3k},\qquad
u,v\in\mathbb Z,\qquad \gcd(u,v)=1,
$$
$$
u\operatorname{Tr}(\omega)+v\operatorname{Tr}(\eta)
\equiv0\pmod3.
$$
由此定义迹零整元
$$
\theta=u\omega+v\eta-
\frac{u\operatorname{Tr}(\omega)+v\operatorname{Tr}(\eta)}3.
$$
其特征多项式为 $T^3-XT-2W$，判别式恒等式给
$X^3-27W^2=cZ^p$。全部奇素数处的系数互素性自动恢复；只在族 II 再检查 $X$ 奇，在 III 偶支再检查 $X\equiv2\pmod4$。这与 R19 的实际非 CM 同余严格等价。

关键新局部事实是：若 $q\ge5$，原始非平凡坐标的迹零整元满足 $q\mid X,W$，则三次最大整环在 $q$ 处必为
$\mathbb Q_q\times K_q$，其中 $K_q$ 分歧二次，而且该整元的多项式判别式赋值**恰为三**。写
$$
\theta=(-2s,s+t\pi),\qquad \pi^2=q\varepsilon,
$$
可得 $q\mid s$、$t$ 为单位，以及
$$
\operatorname{disc}(\theta)
=4q\varepsilon t^2(9s^2-q\varepsilon t^2)^2.
$$
其赋值三与实际 $p\,v_q(Z)>37$ 矛盾。若三次代数未分歧，有限 étale 代数中没有非零幂零元，甚至立即违背原始性。

这里最大整环和 $\gcd(u,v)=1$ 都不可删除。只知道覆盖有有理点，仍然得不到精确的整数高指标值。

## 3. R53：通过既有参数筛后 W1 仍能非零

完整证明：[R53-nonzero-mw-after-frobenius-filters](../results/R53-nonzero-mw-after-frobenius-filters.md)。

可复验脚本：[verify_r53_surviving_cubic.py](verify_r53_surviving_cubic.py)。

构造
$$
p=43,\qquad M=\prod_{r\le461,\ r\ {\rm prime}}r,\qquad
n=116M,\qquad q=432n^2-1,\qquad Z=-q.
$$
通过完整 Lucas $N+1$ 证书证明 $q$ 为 387 位素数：取
$(P_0,Q_0,D_0)=(1,-127,509)$，验证 $U_{q+1}=0\bmod q$，
并对 $q+1$ 的全部 $89$ 个素因子 $r$ 验证
$\gcd(U_{(q+1)/r},q)=1$。判据的有限域证明在 R53 内，脚本仅使用 Python 标准库。

$g=T^3-T-8n$ 在模 $467$ 时为无根三次式，故不可约。$2$ 进三个 Hensel 根给最大域判别式 $-q$；$q$ 处有一个单根且判别式指数一。正规闭包 $H/F$ 因而处处不分歧，$F=\mathbb Q(\sqrt{-q})$，且 $2q$ 上方全分裂。

全部奇素数 $\ell\le461$ 处有 $g\equiv T(T-1)(T+1)$，所以完全分裂；这包含 $p=43$ 和全部所需小 Frobenius 窗口。同时
$q\equiv-1\pmod{4p}$，$Z\equiv1\pmod{432}$，$|D_F|>p^4$。

实际整数点
$$
P=(3,108n)\in D_Z:\ V^2=U^3+27q
$$
的同源逆像多项式恰为 $g$，因此非零类域字符真的属于 $W_1$。指标覆盖还有一个原始 $t=1$ 点。但实际 $p=43$ 要求
$$
I_L(u,v)=\pm2q^{21},\qquad (u,v)=1.
$$
把已知点乘以 $q^7$ 会破坏全局原始性；本例没有解决这个高次指标方程。

本例还给出显式最大整环基
$(1,\theta,(\theta^2+\theta)/2)$。指标形式为
$I_L(u,v)=u(u+v)(2u+v)-2nv^3$，迹条件恰为 $3\mid v$。
因此最后问题已经是一条系数完全显式的原始 Thue 方程，不再需要一个隐藏的整基计算步骤。

随后补强为：同一个候选 $L$ 的精确高次指标方程，在每个完成域都有原始解。对 $\ell\ne q$，上述 $q^7$ 缩放仍是局部单位缩放，故保持原始性；在 $q$ 处另用 Hensel 求
$X_q^3=27-q^{43}$、$X_q\equiv3\pmod q$，取 $W_q=1$。相应三次代数为
$\mathbb Q_q\times\mathbb Q_q(\sqrt{-q})=L_q$；其迹零根给原始整坐标，最大判别式恒等式强迫指标为 $\pm2q^{21}$。迹模 $3$ 和族 I 二进条件也都满足。因此这个实例的最后障碍若存在，必为全局整数相容性，不能来自单个完成域。

这排除了“上述必要参数筛一过，$W_e$ 就必然为零”的推断。它没有证明在全部充分大 $p$ 上 $W_e$ 都能存活，也没有声称满足所有局部严格标架条件，更不是实际异常曲线。

## 4. R50 的复核及两个 Selmer 群之间仍无传递

根会话写出的 R50 §2–5 已作数学核查，未发现全局对偶步骤中的缺口。局部杯积与 Weil 配对的两个反对称符号抵消，所以剩余局部形式是对称的分裂双曲形式；两个 Kummer 子空间为全迷向。以 $A$ 的严格 Selmer 为零后，Poitou–Tate 将松弛全局类识别为横截于 $A$ 子空间的 Lagrangian 图；图矩阵因此交替。实际 $E$ 的 Selmer 群等于此矩阵的核。

这个结果控制的是实际同余曲线 $E$ 的模 $p$ Selmer 群。R46 的辅助曲线是 $j=0$ 的 $B_a,D_a$，使用次数三的同源下降。当前没有已知的同源、余核映射、可见性构造或高度兼容性，把
$\operatorname{Sel}_p(E)=0$ 传到 $\operatorname{rank}D_a=0$ 或 $W_e=0$。

例如所有新增素数均非分裂乘法时，R50 确实给 $E$ 秩零及无 $p$-Selmer 类；但这并不等于辅助 $D_a$ 秩零。尝试从 CM 模形式的 $L$ 值同余得到矛盾，还须控制正规化周期和同余模：在 $q\equiv-1\pmod p$ 处出现的 Euler 零因子可能被这些因子抵消。本轮没有证明能阻止这种抵消的统一公式，不能将其记为排除定理。

## 5. 剩余的完整分母问题

R32 控制全局倍乘指标，R34 控制固定支撑下的有效高度；二者均未给变化支撑下的统一深度。R51 把实际条件压成最大整环中的原始精确指标幂值，R53 证明低指标和有理点层确可存活。

因此当前真正目标仍是：对允许变化的 $Z$、候选 $L$ 和 $p=6k+e$，排除 R51 的原始高指标整数点，或找到一个真正随 $p$ 统一的全局输入。不能把固定 $Z$ 的有限性、固定曲线的整点算法、短有限 Frobenius 窗口或辅助覆盖有理点等同于这一步。

本笔记的完整证明产物已经是 R51、R53；没有尚未恢复的未保存计算。根会话继续维护本题 HANDOFF 和共享进度。
