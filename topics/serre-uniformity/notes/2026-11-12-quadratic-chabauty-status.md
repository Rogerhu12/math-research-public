# 非分裂 Cartan 的 equationless quadratic Chabauty：截至 2026-11-12

会话：`serre-uniformity-astra/2026-11-12`；文献分工笔记。

**可信度：** 文献中的已发表结果、2026 年预印本声称以及本笔记的初等引理分别标注。2026 年预印本在这里用于定位方法进展，未作为本仓库新定理的未经证明前提。本笔记不修改主问题的未解决状态。子群分类见同日 `literature-nonsplit` 笔记。

## 1. 三种不同的进展

| 来源 | 核实的位置 | 实际结论 | 尚不能推出 |
|---|---|---|---|
| Dogra–Le Fourn，Math. Ann. 380 (2021), 393–448 | Theorem 1(2)，Proposition 3 | 对素数层 $N$，若 $X=X_{\rm ns}^+(N)$ 的亏格至少为 $2$ 且 $X(\mathbb Q)\ne\varnothing$，则每个辅助素数 $\ell\ne N$ 的 $X(\mathbb Q_\ell)_2$ 有限 | 这些有限集合已被计算，或其中所有有理点都是 CM |
| Hashimoto–Lido–Lombardo–Mascot–Parent，2026-08-11，arXiv:2608.10919 | Theorem 1.0.1；§§3–8 | 建立以模意义、Mumford torsor 和除子运算为基础的无方程几何 QC；完整演示恢复 $N=13$ 的七个 CM 有理点 | 已对任意大 $N$ 完成有理点枚举 |
| Leonhardt–Rendell，2026-10-22，arXiv:2610.30703 | Theorem A；§4.2；Table 1 | 对 $N=25,29$ 给出 de Rham 基和 $T_3$ 对应的 Hodge filtration 数据 | 已完成这些层的整个 QC，或已经求出 $X_{\rm ns}^+(29)(\mathbb Q)$ |

第一项是已发表定理。后两项目前核实到的是作者预印本。尤其不能把十月论文中的 *starting point* 扩写为完整有理点算法已经实现。

原文：

- Netan Dogra and Samuel Le Fourn, *Quadratic Chabauty for modular curves and modular forms of rank one*, [正式论文](https://link.springer.com/article/10.1007/s00208-020-02112-3)，[arXiv:1906.08751](https://arxiv.org/abs/1906.08751)。
- Sachi Hashimoto, Guido Maria Lido, Davide Lombardo, Nicolas Mascot and Pierre Parent, *Equationless quadratic Chabauty for non-split Cartan modular curves*, [arXiv:2608.10919](https://arxiv.org/abs/2608.10919)。
- Marius Leonhardt and Isabel Rendell, *Aspects of Quadratic Chabauty via modular forms*, [arXiv:2610.30703](https://arxiv.org/abs/2610.30703)。

## 2. 秩条件必须分清：已有全层有限性，不等于完整 Jacobian 的秩全已知

Dogra–Le Fourn 的 Theorem 1(2) 不能被误述为“只有当完整 Jacobian 的秩等于亏格时才有结论”。其 Proposition 3 构造一个同源分解
$$
J\longrightarrow A\times B,
\qquad \operatorname{rank} A(\mathbb Q)=\dim A=\rho(A)\ge2,
$$
并验证所需的 Chow–Heegner 映射消失条件。Theorem 2 提供了相应的 $L'(f,1)\ne0$ 新形式输入。这个商的论证绕过了对整个 $J$ 逐层证明秩等于亏格的要求。

因此，“不知道所有层的 $r=g$”是某个具体算法实现的障碍，不能拿来否定 QC 在这族曲线上已有的无条件有限性。另一方面，有限性也不自动给出排除非 CM 点的算法终止证明。Dogra–Le Fourn §3.1 给出点数上界；该界与 Hecke 轨道能否形成矛盾由本课题另一条几何笔记处理。

八月论文主要实现 $r=g$ 的版本。其 Theorem 4.4.6 还明确要求
$$
J^0(\mathbb Z)_{\bar0}\longrightarrow
J(\mathbb Z/\ell^2\mathbb Z)_{\bar0}
\tag{QC-surj}
$$
满射；见式 (4.4.1)。不能仅由 $r=g$ 就把这个积分满射条件删掉。辅助素数在该文的一般设置中为奇数、是曲线的好约化素数，另需已知有理基点及适当的生成点。Remark 3.0.7 讨论 $r<g+\rho-1$ 的多 torsor 扩展以及使用商的方向。

## 3. 十月论文到底完成了哪一半

Leonhardt–Rendell 的 Theorem A 给出 $X_{\rm ns}^+(25)$ 与 $X_{\rm ns}^+(29)$ 的 $H^1_{\rm dR}$ 基，分别有 $28$ 与 $48$ 个元素（亏格 $14$ 与 $24$），并给出 Hecke 对应 $T_3$ 所需的 Hodge filtration 矩阵。计算输出在[作者代码仓库](https://github.com/izzyrendell/Aspects-of-quadratic-Chabauty-via-modular-forms)；这里未下载或重新运行这些输出。

论文 §4.2 将局部高度拆成 Hodge splitting $\lambda^{\rm Fil}(x)$ 和 Frobenius splitting $\lambda^\phi(x)$。§4.3 实现的是前者；§4.2 对后者引用的已有算法仍要求曲线方程。因此 Theorem A 所给数据尚不足以直接评价完整局部高度。

Table 1 的实例包含 $N=13,17,19,23,25,29$。作者报告 $N=29$ 的模形式输入计算约 $1.03\times10^6$ 秒，后续自有算法约 $884$ 秒；这是作者给出的计算时间，不是本会话的实测值。它说明获得模形式输入仍有实际成本，不能据“无方程”就认为统一遍历任意大层已变成有限工作。

两篇 2026 论文在方法上互补：八月论文避开显式高度的 cohomological 表达，直接在 Mumford torsor 中计算；十月论文推进的是模形式表达的 cohomological QC。八月已经有 $N=13$ 的完整应用，因此“Frobenius splitting 尚未无方程计算”仅是十月这一实现路径的缺项，不是整个 equationless 路线的共同缺项。

## 4. 八月方法给出的具体小次数筛

在八月论文的适用条件和积分坐标选择下，Corollary 4.3.11 说明：在一个固定的 $X(\mathbb F_\ell)$ 剩余圆盘上，以归一化局部参数 $t\in\mathbb Z_\ell$ 表示点，提升映射的坐标模 $\ell$ 都是次数至多 $2$ 的多项式。§3 将 QC 条件变成最后一个坐标函数 $F(t)=0$；不同的独立对应可以给出多个这样的条件。

这个结论比只知道全曲线上的零点集有限更适于认证。不过有两个必须保留的分支：$\bar F$ 可能恒零；其零点也可能是重根。只在 $\bar F\ne0$ 时，才能从次数推出本圆盘至多有两个候选参数模 $\ell$。参数模 $\ell$ 是原圆盘中的进一步细分，不能与曲线点模 $\ell$ 混淆。

下面两个初等引理不依赖 2026 预印本的正确性；它们说明如果获得这些解析函数，什么样的数据足以完成排除、什么样的数据仍然不足。

### Q1（已证明）：共同零点的有限精度认证准则

设紧空间 $X(\mathbb Q_\ell)$ 已被有限多个互不相交的解析圆盘 $D_i$ 覆盖，并有参数双射 $t_i:D_i\to\mathbb Z_\ell$。对每个 $i$，给定有限个限制幂级数
$$
F_{i,1},\ldots,F_{i,m_i}\in\mathbb Z_\ell\langle T\rangle
$$
以及有限个已经证明为有理点的集合 $S_i\subset D_i$。假设：

1. 每个 $P\in X(\mathbb Q)\cap D_i$ 都满足所有 $F_{i,a}(t_i(P))=0$。
2. 对每个共同模 $\ell$ 零点
   $$
   r\in\mathbb F_\ell,\qquad
   \bar F_{i,a}(r)=0\quad\text{对所有 }a,
   $$
   存在 $P_r\in S_i$，使 $t_i(P_r)\equiv r\pmod\ell$。
3. 对上述每个 $r$，至少有一个 $a$ 满足 $\bar F'_{i,a}(r)\ne0$。

则
$$
X(\mathbb Q)=\coprod_i S_i.
$$

**证明。** 右边当然包含于左边。任取左边的 $P\in D_i$，令 $x=t_i(P)$。由条件 1，其剩余类 $r$ 是共同零点。取条件 2 的 $P_r$，记 $c=t_i(P_r)$。因 $P_r$ 是有理点，它也满足条件 1。选条件 3 中的函数 $F$，则 $F(x)=F(c)=0$。

对整数系数限制幂级数，因 $x\equiv c\equiv r\pmod\ell$，差商
$$
\frac{F(x)-F(c)}{x-c}
$$
在 $x\ne c$ 时收敛并属于 $\mathbb Z_\ell$，其模 $\ell$ 等于 $\bar F'(r)$。后者非零，差商是单位。这与分子为零矛盾。因此 $x=c$，由参数双射得到 $P=P_r$。证毕。

这里不要求每个单独函数的所有零点都是有理的，也不要求单个对应就完成排除。它是多个 QC 条件共同筛选的充分条件。若每个 $S_i$ 都是 CM 点，就得到该层没有非 CM 有理点；若能对所有充分大素数层证明这些条件，则得到真正的一致性结果。目前文献中的逐层有限性并未给出最后这个全层认证。

### Q2（已证明）：模素数次数至多二，并不控制所需精度

固定奇素数 $\ell$。对任意整数 $m\ge0$，取
$$
F_m(T)=T^2-\ell^{2m+1}.
$$
它是本原的整数系数二次多项式，模 $\ell$ 恒为 $T^2$；却没有 $\mathbb Q_\ell$ 零点，因为非零平方的 $\ell$ 进赋值是偶数。然而对每个 $k\le2m+1$，$T=0$ 都给出模 $\ell^k$ 的解。

模 $\ell^{2m+2}$ 才必定无解：若 $t^2\equiv\ell^{2m+1}$，则 $v_\ell(t^2)=2m+1$，与平方赋值为偶数矛盾。故即使函数次数固定、首项系数为单位、最终零点集为空，消灭伪解所需精度仍无统一上界。证毕。

这不是声称实际 QC 函数必然具有这种退化；它严格否定了仅凭“二次”“本原”“有限性”三项就推得统一精度界的推理。若要用第一阶筛完成全层证明，需要新的算术输入排除相关重根，或控制其高阶提升。

## 5. 下一步的可检验目标

当前值得推进的目标是：在 Dogra–Le Fourn 保证存在的 Heegner 商上，构造随层 $N$ 可描述的多个 Hecke/QC 条件，并证明它们在非 CM 候选圆盘上的共同零点为空，或给出 Q1 型的精确简单零点认证。需追踪的量是共同零点和重根，而非只有 Jacobian 的秩或单个函数的次数。

即便候选椭圆曲线没有任何有理循环同源，Hecke 对应仍然把一个有理点送到一个有理有效除子，也仍诱导 $J$ 上的有理算子。因此“不能制造更多单个有理邻居”只阻止某种点数放大论证，不阻止上述全局高度条件的构造。

本笔记没有证明统一的零点分离，未把有限层计算或文献状态冒充为主问题的完成。
