# R53 原始高指标的单素数理想支撑：后续研究记录

日期：2026-11-12；会话：serre-uniformity-resume2；分支：cm-denominators。

**状态：持续研究；固定实例及主目标均未解决。** 接续根会话安排，进一步研究 R53 的显式指标形式
$$
I(u,v)=u(u+v)(2u+v)-2nv^3,\qquad q=432n^2-1.
$$
完整证明已写入 [R56-single-prime-index-ray-class-and-unit-recurrence](../results/R56-single-prime-index-ray-class-and-unit-recurrence.md)。本笔记记录路线的选择、实际进展和计算边界，不重复全文。

## 1. 新的全局约束来自支撑分配，而不是辅助椭圆曲线的秩

对实际方程 $I(u,v)=\pm2q^m$，令
$$
\alpha=u+v/2-(v/2)\theta.
$$
则 $N(\alpha)=\pm q^m$。单独知道这个范数并不足够，因为
$(q)=\mathfrak q_1\mathfrak q_2^2$ 允许许多支撑分配。

原始性使分配大幅收紧。若 $q\mid v$，$\alpha$ 处处为单位，矛盾；所以 $v$ 是 $q$ 进单位。原始多项式在 $q$ 处分歧恰一，因此在二次因子中写
$\theta=s+t\pi$ 时 $t$ 为单位。此时 $\alpha$ 一旦被 $\mathfrak q_2$ 除，估值就恰为一，而且不能同时被 $\mathfrak q_1$ 除。故 $m>1$ 强迫
$$
(\alpha)_q=\mathfrak q_1^m.
$$

在 $2$ 上方，$\alpha$ 的估值只能为
$$
(0,0,0),\qquad (-1,1,0),\qquad (-1,0,1),
$$
依次对应 $v$ 偶、$v$ 奇且 $u$ 偶、$u,v$ 均奇。由此得到三个完整分数理想，未遗漏其他分母。

## 2. 模三迹条件可以并入射线类群

显式元
$$
\eta=3\theta^2-4
$$
满足
$$
N(\eta)=4q,\qquad
(\eta)=\mathfrak q_1\mathfrak p_0^2,\qquad
\eta\equiv-1\pmod3.
$$
另一方面，R51 的迹条件在本例为 $3\mid v$，因而
$\alpha\equiv u\equiv\pm1\bmod3$。所以应在模 $(3)$ 射线类群中，而不是仅在普通类群中，检查完整理想是否为主。

记该射线类群中的范数二素理想类为 $c_0,c_+,c_-$。所需指数 $p=2m+1$ 必满足
$$
(p-1)c_0=0,\qquad
pc_0=c_+,\qquad
pc_0=c_-
$$
三者之一。对 R53 的 $p=43$ 即为
$42c_0=0$ 或 $43c_0=c_\pm$。

根会话给出的导数恒等式同时提供了符号核对：
$$
\eta(3\theta^2-1)^2=4q,\qquad
\left((3\theta^2-1)/2\right)=
\mathfrak q_2\mathfrak p_0^{-1}.
$$
后一个元模三同余于一，故 $[\mathfrak q_2]=c_0$ 在同一个射线类群成立。还应明确
$\eta/q=(2/(3\theta^2-1))^2$ 本来就是平方，不能由此制造新的二次扩张。

## 3. 通过类群筛后，得到真正双向的单位递推

$L$ 的签名为 $(1,1)$，所以数域单位秩为一。这不是假定 R46 的辅助 Mordell 曲线秩为一，也不声称低指标点生成其全部 Mordell–Weil 群。

对一个射线主候选理想选生成元 $\alpha_\sigma$，取正实基本单位
$\varepsilon>1$。全部正范数生成元为 $\alpha_\sigma\varepsilon^j$。其在
$(1,\theta,\beta)$ 基下的 $\beta$ 坐标等于零时，另外两个坐标自动恢复整数 $u,v$，并由完整理想分配自动给原始性。

由于 $3$ 完全分裂，$\varepsilon\bmod3$ 的阶 $r$ 为一或二；迹条件等价于 $j\in r\mathbb Z$。因此剩余问题精确化为某个三阶整数递推的零点，而非宽松的有理点存在性条件。R56 给出完整的 $3\times3$ 乘法矩阵。

若缺失坐标写为
$$
A\varepsilon^j+
B\varepsilon_{\mathbb C}^j+
\overline B\,\overline{\varepsilon_{\mathbb C}}^j,
$$
所有系数都非零，且 $|\varepsilon_{\mathbb C}|=\varepsilon^{-1/2}$。正指数一侧有直接大小界；负指数一侧的复共轭相消需要 Baker–Wüstholz 复对数下界，不能仅引用 Skolem–Mahler–Lech 有限性。R56 分别证明了这两个接口，并指出所有常数仍依赖固定域的基本单位和理想生成元。

引用原始成熟来源：A. Baker, G. Wüstholz, “Logarithmic forms and group varieties”, J. reine angew. Math. **442** (1993), 19–62，[DOI](https://doi.org/10.1515/crll.1993.442.19)；两位作者 *Logarithmic Forms and Diophantine Geometry* (Cambridge, 2008), Chapter 7, pp. 149–166，[出版社章节](https://doi.org/10.1017/CBO9780511542862.008)。本轮核对了作者和出版社的书目信息及定量章节定位；原期刊的全文链接未能取到，不声称已经独立重证对数下界。

没有使用 BHV：这里目前得到的是三阶单位递推，并未建立 Lucas/Lehmer 序列结构。

## 4. 为什么巨大判别式本身没有完成这个筛

根会话要求进一步检查：能否用 $q$ 的巨大规模排除
$42c_0=0$ 或 $43c_0=c_\pm$？目前没有得到这种排除。

若范数二素理想的四十二次幂为主，其生成元可以乘以无限单位；范数小不表示全部嵌入都小。R56 还给出一个完整的反向说明：通过
$T^3+NT-2^{42}$、$N\equiv7\bmod8$，可构造最大判别式无界、$2$ 完全分裂、而某个范数二素理想四十二次幂确实为主的复三次域。利用任意大的素数 $R\equiv2\bmod3$ 和一次判别式赋值，可直接保证最大判别式无界。

这个辅助族不满足全部 R53 特殊条件，也没有证明相应射线关系成立；它仅严格说明“最大判别式大”不能替代实际的类群或单位计算。

## 5. 实际计算状态与下一接口

当前尚未得到以下数值对象：

- $G=\operatorname{Cl}_{(3)}(L)$ 中 $c_0,c_\pm$ 的关系或其证书；
- 一个经过完备性验证的基本单位及调节子；
- 通过筛的候选理想的射线主生成元；
- 相应三阶递推的完整零点区间和零点列表。

当前环境没有 PARI/GP、cypari2 或 Sage；已安装的 SymPy 不提供这里所需的完整数域类群与基本单位功能。没有启动一个未经估算的大规模类群计算，也没有将软件缺失当作任务终点。

对这个判别式为 387 位的固定域，仅按无条件 Minkowski 界枚举类群或盲扫单位并不是已经完成的实算。后续可以先寻找该域的特殊射线类群商或可证明的小关系；若取得真实基本单位和主理想证书，再按 R56 的有效界求递推零点。通过固定实例也不等于控制变化支撑的全部 R51 方程。

本轮完成的是新增的全局射线类群筛与双向递推归约。R53 的全局原始高指标方程和 O6 的统一问题仍保留未解。

