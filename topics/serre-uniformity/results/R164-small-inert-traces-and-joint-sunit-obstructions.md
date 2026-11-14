# R164：小惰性素数的严格首差条件与联合 $S$-单位矩阵

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明。** 本文把实际整数 Frobenius 迹的 Hasse 小量性质，
加到 R161 的首次伴随差类上。它给出更多真正的全局互反行，
并把这些行识别为明确有限数域中的 $S$-单位类。
同时证明一个准确界限：对任何固定的有限小素数集合，
Gaussian 主理想行与这些新行的联合矩阵都有无限多个候选零列。
所以不能仅以这些必要线性关系的数量宣称变化支撑处必满秩。

固定 R19 的一个实际原始解，指数为 $p>37$，
$$
A:y^2=x^3-x,\qquad K=\mathbb Q(i),\qquad
p\equiv3\pmod4,
$$
并保留 R157、R161 的
$$
n=\min_{q\mid Z}v_p(pv_qZ),\qquad
R=\prod_{\substack{q\mid Z\\v_p(pv_qZ)=n}}q,\qquad
c_E=x_EJ+c_W.
\tag{164.1}
$$
$W$ 是 $\operatorname{ad}^0A[p]$ 的二维非 CM 分量，
$J=[i]$，$x_E|_{G_K}=\kappa$。

## 1. 两个必须区分的小惰性素数集合

对实际 $E$ 可用的集合是
$$
\mathcal S_-(E,p)=
\{t:\ t\text{ 为素数},\ t\equiv3\pmod4,\quad
t<p^2/16,\ t\nmid pZ\}.
\tag{164.2}
$$
也可选其中任意有限子集。

一个不依赖 $E$ 的安全集合是
$$
\mathcal S_-^0(p)=
\{t:\ t\text{ 为素数},\ t\equiv3\pmod4,\quad
t<\min(p^2/16,4p-1),\ t\ne p\}.
\tag{164.3}
$$
R132 给每个在 $K$ 惰性的分母素数 $q\mid Z$ 满足
$q\ge4pg-1\ge4p-1$，所以 (164.3) 一定包含在 (164.2)。

不能只用 $t<p^2/16$ 就宣称任意惰性 $t$ 都不除 $Z$：
大 $p$ 时区间 $[4p-1,p^2/16)$ 非空，实际坏素数可能落在这里。
若要使用较大的 (164.2)，必须明确排除 $t\mid Z$。
$p$ 本身也必须排除：它有不同的局部惯性，已经由 R157、
R161 的完整晶体同构单独处理。

$t=3$ 没有遗漏：R19 给 $3\nmid Z$，两曲线在 $3$ 好约化；
对所有当前 $p$，$3$ 都属于 (164.3)。
$2$ 处不属于这组好素数，仍使用完整 $Q_8$ 局部型。

## 2. 小惰性好素数上的整个 $W$ 局部类为零

**引理 164.1。**
对每个 $t\in\mathcal S_-(E,p)$，有
$$
\boxed{\operatorname{loc}_t(c_W)=0
\quad\text{于 }H^1(\mathbb Q_t,W).}
\tag{164.4}
$$

**证明。**
$E,A$ 都在 $t$ 好约化。实际同余 $E[p]\simeq A[p]$
给整数迹模 $p$ 相等，Hasse 界给
$$
|a_t(E)-a_t(A)|\le4\sqrt t<p.
$$
所以两个整数准确相等。因 $t$ 在 $K$ 惰性，
$a_t(A)=0$，遂有 $a_t(E)=0$。

令 $F_t=\bar\rho_A(\operatorname{Frob}_t)$。
它满足
$$
\operatorname{tr}F_t=0,\qquad
F_t^2=-tI,\qquad F_tJ=-JF_t.
\tag{164.5}
$$
因此 $F_t$ 本身属于 $W$，而 $\operatorname{Ad}(F_t)$ 在 $W$
上有特征值 $1,-1$，其 $+1$ 线准确为 $\mathbb F_pF_t$。
它绝不会是标量：$p$ 为奇数，标量且迹零会使它为零，
与行列式 $t\not\equiv0\bmod p$ 矛盾。

两个实际迹在特征零相等，故把
$\rho_E=(1+p^nc_E)\rho_A$ 的迹等式除以 $p^n$ 再模 $p$，
得到
$$
\operatorname{tr}(c_E(\operatorname{Frob}_t)F_t)=0.
\tag{164.6}
$$
$J$ 分量在此迹中为零；所以同样有
$\operatorname{tr}(c_W(\operatorname{Frob}_t)F_t)=0$。
局部类已经不分歧，因而由
$$
H^1_{\mathrm f}(\mathbb Q_t,W)=W/(\operatorname{Ad}(F_t)-1)W
\simeq\mathbb F_pF_t
$$
表示。迹泛函在这个一维商上非退化，因为
$$\operatorname{tr}(F_t^2)=-2t\ne0\bmod p.$$
它也杀掉 $(\operatorname{Ad}(F_t)-1)W$，
所以 (164.6) 与 cocycle 代表无关，准确迫使该不分歧类为零。证毕。

这不要求 $t\equiv\pm1\bmod p$，也不要求 $t$ 在 $T=K(A[p])$
完全分裂。若使用更精细的界，由 $a_t(A)=0$ 其实可把这里的 Hasse
安全条件放宽为 $2\sqrt t<p$。本文保留统一的 $p^2/16$，
以便与 R157 的 split/Gaussian 条件使用同一范围；
没有把较宽界自动变成不除分母的保证。

## 3. 放松对偶局部条件后，维数准确为 $1+\#\mathcal S_-$

固定任意 $\mathcal S_-\subset\mathcal S_-(E,p)$。
在 R161 的 primal 严格结构 $\mathcal F_0$ 上，
再把每个 $t\in\mathcal S_-$ 的不分歧条件缩成 $0$，
记所得结构为 $\mathcal F_{0,\mathcal S_-}$。
其全局群仍为零，因为它是
$H^1_{\mathcal F_0}(\mathbb Q,W)=0$ 的子群。

对偶结构在 $p$ 仍是整个 $H^1$，
在 $t\in\mathcal S_-$ 也变成整个 $H^1(\mathbb Q_t,W(1))$，
其余处仍不分歧，$2$ 处自动为零。
记其全局群为
$$
\mathcal D_{p,\mathcal S_-}=
\{d\in H^1(\mathbb Q,W(1)):
d\text{ 在 }2,p,\mathcal S_-\text{ 外不分歧}\}.
\tag{164.7}
$$

每个 $t$ 的 primal 不分歧空间准确为一维，
故 Poitou–Tate 维数公式相对 R161 每处增加一维：
$$
\boxed{\dim_{\mathbb F_p}\mathcal D_{p,\mathcal S_-}
=1+\#\mathcal S_-.}
\tag{164.8}
$$
更准确的比较序列是
$$
0\longrightarrow\mathcal D_p
\longrightarrow\mathcal D_{p,\mathcal S_-}
\longrightarrow
\bigoplus_{t\in\mathcal S_-}H^1_{\mathrm s}(\mathbb Q_t,W(1))
\longrightarrow0.
\tag{164.9}
$$
右边每一项都一维；末端为零正是最小 primal Selmer 为零的结果，
不是假设局部数据总能随意拼成全局类。

为避免把“全松弛”与一维空间混淆，完整局部维数为
$$
h^0(\mathbb Q_t,W)=1,\qquad
h^0(\mathbb Q_t,W(1))=
\begin{cases}1,&t\equiv1\text{ 或 }-1\bmod p,\\
0,&\text{否则}.
\end{cases}
$$
因此 $H^1(\mathbb Q_t,W(1))$ 在前一情形二维，后一情形一维；
但相对于其不分歧子空间，新增奇异商在两种情形都准确一维。
特别地 $t=3$ 时，当前 $p>37$ 使其不分歧子空间为零，
整个对偶 $H^1$ 即为新增的一维奇异方向。

## 4. 新的对偶行是真实 $S$-单位类

可以在比完整除法域更小的数域内实现这些类。令
$$
F=K(A[p])^{\mathbb F_p^\times}.
$$
R163 给
$$
[F:K]=p+1,\qquad
\operatorname{Gal}(F/\mathbb Q)
=C_{p+1}\rtimes\langle\tau\rangle,\qquad
\tau a\tau^{-1}=a^{-1}.
\tag{164.10}
$$
$W$ 通过这个群作用。Kummer、次数与 $p$ 互素的
inflation–restriction 给
$$
H^1(\mathbb Q,W(1))
\simeq
\left((F^\times/F^{\times p})\otimes_{\mathbb F_p}W\right)^{
       \operatorname{Gal}(F/\mathbb Q)}.
\tag{164.11}
$$
不需要假设 $\mu_p\subset F$；Kummer 同构
$H^1(F,\mu_p)=F^\times/F^{\times p}$ 本身不要求这一条件。

记 $\mathcal O_{F,\mathcal S_-}^\times$ 为允许在
$\mathcal S_-$ 上方素理想有非零赋值的 $S$-单位群。
则
$$
\boxed{\mathcal D_{p,\mathcal S_-}\simeq
\left(\mathcal O_{F,\mathcal S_-}^\times/
     (\mathcal O_{F,\mathcal S_-}^\times)^p\otimes W\right)^{
       \operatorname{Gal}(F/\mathbb Q)}.}
\tag{164.12}
$$

以下说明没有在 (164.12) 隐藏未知类群项。
R163 §2–4 已证明 $F$ 的 $p$ 类群在
$\chi=a^{p-1}$、$\chi^p$ 型上为零，
也就是 $\mathbb F_p[\operatorname{Gal}(F/\mathbb Q)]$ 的 $W$ 型为零。
在标准的 $S$-单位、赋值和理想类精确序列中投影到这一型，
并使用 $p\nmid2(p+1)$ 的精确取不变量，
得到每个允许素理想的 $W$ 等变赋值向量都可由实际 $S$-单位
实现模 $p$。$2,p$ 上方的赋值模在张量 $W$ 后没有不变量：
相应分解群包含 R161 所用的无不变量惯性。
因此允许在 $2,p$ 处作 $S$-单位并不会增加这一型；
其余类群项已经为零。Kummer 序列遂给 (164.12)。

特别地，对每个惰性 $t$，
$\operatorname{Frob}_t$ 在 (164.10) 的商中是反射，
其分解群阶为二。故
$$
\left(\bigoplus_{\lambda\mid t}\mathbb F_p[\lambda]\otimes W\right)^{
       \operatorname{Gal}(F/\mathbb Q)}
\simeq W^{\operatorname{Frob}_t}
=\mathbb F_pF_t
\tag{164.13}
$$
准确一维。这把 (164.9) 的新增方向实现成一个具体的等变
素理想赋值向量。

取 R163 的 Robert 生成元 $d_0=d_p^{\mathrm{Rob}}$。
对每个 $t\in\mathcal S_-$，选择一个
$d_t\in\mathcal D_{p,\mathcal S_-}$，
其在 $t$ 的 (164.13) 坐标为一个固定非零基，
在其他 $s\in\mathcal S_-$ 的奇异坐标为零。
由 (164.9)、(164.12) 这样的 $d_t$ 存在，且可用实际
$S$-单位形式给出；$\{d_0\}\cup\{d_t\}$ 是一组基。
改变 $d_t$ 只能添加 $d_0$ 的倍数，不改变后文矩阵的核。

这里也有有限的精确构造程序，而不是把“存在某类”当作输入：
由 $A[p]$ 和标量不变量构造 $F$，
计算其整数环、各 $t$ 上方素理想及理想类关系，
在 (164.13) 的等变方向解赋值主化问题。
具体可先在 $\mathbb Z_p[G]$ 的 $W$ 块取幂等投影，再用
$\mathbb Z[G]$ 元素模 $p^k$ 逼近它，其中 $p^k$ 杀掉已计算的
整个类群 $p$ 部分。投影块的 $p$ 类群为零，其他块的误差也被
$p^k$ 杀掉，所以得到具有指定模 $p$ 赋值的实际整除子，
其理想类阶与 $p$ 互素。取这个素于 $p$ 的阶倍数成为主理想，
再模 $p$ 反转该倍数。
所得主生成元及全局单位给出所需 $S$-单位类。
这是一般数域的有限代数算法；本文没有声称已经对变化 $p$
实际计算了这些整数环、主生成元或完整评价矩阵。
R161 的 $d_0$ 列已经有独立的有限域直接公式。

## 5. 与 Gaussian 主理想关系使用同一组实际列权重

先假定 $R$ 的全部素因子在 $K$ 惰性。
对每个 $q\mid R$，按照 R161 选择同一个 tame 基，
令
$$
F_q=\bar\rho_A(\operatorname{Frob}_q),\quad
K_q=JF_q,\quad x_q=\kappa(\sigma_q)\ne0,
$$
并记 $\epsilon_q=+1$ 或 $-1$ 分别表示 $E$ 的分裂或非分裂乘法。
实际 nilpotent 首差给
$$
(c_W)^{\mathrm s}_q=\epsilon_qx_qK_q.
\tag{164.14}
$$

定义矩阵 $B$，列由 $q\mid R$ 编号，行由 $0$ 和
$t\in\mathcal S_-$ 编号：
$$
B_{h,q}=\langle K_q,\operatorname{loc}_q(d_h)\rangle_q,
\qquad h\in\{0\}\cup\mathcal S_-.
\tag{164.15}
$$
同一局部 Tate 配对、同一 tame 基、同一 $K_q$ 用于全部行；
所以列上的未知权重确实相同，不能逐行另选独立的比例。
(164.4) 使新增辅助处的全局杯积项全部为零；
$p,2$ 项亦为零，其余两类都不分歧。因而实际曲线必须满足
$$
\boxed{B\,\operatorname{diag}(\epsilon_q)(x_q)_{q\mid R}=0.}
\tag{164.16}
$$
(164.9) 中不同的基选择只对 $B$ 作可逆行变换，
或给一行添加第零行，不改变这个约束。

现在加入 split 小素数。令
$$
\mathcal S_+(p)=
\{t:\ t\text{ 为素数},\ t\equiv1\bmod4,\ t<p^2/16\}.
$$
R132 的 split 分母素数下界大于 $4p^2$，
所以这些 $t$ 全部不除 $Z$，无需另外作未知支撑删除。
取 $t=\pi_t\bar\pi_t$ 的一个 primary 高斯素元。
R157 的实际整数迹论证给
$$\kappa(\operatorname{Artin}(\pi_t))=0.$$
等价地，$x_E$ 在该好素数处的不分歧局部类为零。

Kummer 元素
$$u_t=\pi_t/\bar\pi_t$$
与 $\eta$ 张量后正下降为一个
$e_t\in H^1(\mathbb Q,\eta(1))$：
复共轭将 $u_t$ 变成逆元，$\eta(\tau)=-1$，
两个负号正好相消。
这些类对应实际的 Gaussian 主理想关系。
用同一列惯性坐标定义
$$
A_{t,q}=\langle J,\operatorname{loc}_q(e_t)\rangle_q.
\tag{164.17}
$$
这里把 $\eta J$ 与其对偶通过迹配对识别；
因而 $-2=\operatorname{tr}(J^2)$ 的非零比例已经包含在配对中。
全局互反给 $A(x_q)=0$。
所以全部实际条件合成一个矩阵：
$$
\boxed{
\begin{pmatrix}
A\\[2pt]B\,\operatorname{diag}(\epsilon_q)
\end{pmatrix}
(x_q)_{q\mid R}=0,\qquad
(x_q)_{q\mid R}\in(\mathbb F_p^\times)^{\omega(R)}.
}
\tag{164.18}
$$
它同时保留了 R157 的反循环方向和 R161 的 $W$ 方向，
而不是把两种矩阵各自的核向量误当成可以独立选择。

R157 的所有小高斯主理想关系由其素因子关系得到，
因此允许在 (164.17) 增加任意这些主理想行；
这些都是实际全局类的局部评价。
R158 的小高斯乘积计数仍然适用，但不自动赋予新增矩阵满秩。

若 $R$ 含在 $K$ 分裂的素数，则该处 $W$ 奇异空间为二维，
应保留向量列并直接使用
$$
\sum_{q\mid R}\langle(c_W)^{\mathrm s}_q,
                         \operatorname{loc}_q(d_h)\rangle_q=0.
\tag{164.19}
$$
不能强行改写成 (164.14) 的单标量式；
其实际 nilpotent 二次型限制仍为 R161 (161.19)、(161.25)。

## 6. 真复共轭给无限零列：有限联合矩阵不能自动满秩

下面给一个完全全局的边界，不只说“某有限窗口中仍有候选”。

**命题 164.2。**
固定 $p$ 和任意有限组已确定的 $e_t,d_h$。
存在无限多个素数 $q\equiv-1\bmod4p$，
避开这些类的全部分歧处，使
$$
\operatorname{loc}_q(e_t)=0,\qquad
\operatorname{loc}_q(d_h)=0
\quad\text{对全部 }t,h.
\tag{164.20}
$$
所以 (164.18) 在这样的单列 $R=q$ 上是零矩阵。
这不是实际曲线存在性的结论。

**证明。**
每个有限系数连续一次上同调类及其残余表示
都通过某个有限 Galois 扩张：
可取相应半直积表示的核。
令 $L/\mathbb Q$ 为所有这些控制域与 $T=\mathbb Q(A[p])$
的有限 Galois 合成。取一个真正的复共轭 $c\in G_{\mathbb Q}$，
记其在 $\operatorname{Gal}(L/\mathbb Q)$ 的像仍为 $c$。

对任一系数为 $\mathbb F_p$ 的 cocycle $z$，
$c^2=1$ 给
$$(1+c)z(c)=0.$$
因 $p$ 为奇数，$c$ 的 $+1,-1$ 分解精确，所以
$$\ker(1+c)=\operatorname{im}(c-1).$$
因此 $z(c)$ 在不分歧商 $M/(c-1)M$ 中为零。
这同时适用于 $\eta(1)$、$W(1)$ 的全部已选类；
该论证不依赖 cocycle 代表或控制域基选择。

Chebotarev 定理给无限多个不分歧素数，
其 Frobenius 共轭类在 $\operatorname{Gal}(L/\mathbb Q)$ 中为 $[c]$。
这些素数满足 (164.20)。
因为 $L$ 包含 $K=\mathbb Q(i)$ 与 $\mu_p$，
真正复共轭同时在两者上取逆，
故 $q\equiv-1\bmod4p$。
去掉有限多个小素数或辅助素数仍有无限多个。证毕。

甚至可额外把任意固定的 $\mu_{4M}$ 加入 $L$，
得到 $q\equiv-1\bmod4M$；
这与 R132 的惰性支持同余相容。
也可令所有这些 $q$ 超过 R157、R158 给定的任意固定下界。
所以这里的零列并不与既有超多项式支撑下界冲突。

命题只说明这批必要的一阶线性条件没有统一满秩性质。
它没有构造某个实际 $E$，没有验证完整 Tate Frobenius 有限部分，
没有把一阶 cocycle 提升为全部 $p$ 进表示，
也没有解决原三族的整数原始性。
这些附加条件仍可能排除 (164.20) 中的素数。
后续若要完成 O6，必须把其中的实际额外条件带回，
不能以有限联合矩阵的行数大于列数代替秩证明。

## 7. 引用和已落实的范围

- [R157](R157-first-adjoint-character-and-cubic-denominator-support.md)：
  精确整数迹、完整 $p$ 局部对齐、反循环首差和小高斯主理想核。
- [R158](R158-small-gaussian-products-and-superpolynomial-support.md)：
  同一核的乘积计数和支撑下界；本文未把这些下界当成上界。
- [R161](R161-strict-adjoint-selmer-line-and-tate-support-orthogonality.md)：
  严格 $p$ 的零 primal Selmer、唯一 dual 线、
  惰性 Tate 符号与实际 nilpotent 条件。
- [R163](R163-all-prime-primitive-adjoint-robert-generator.md)：
  $F$ 的正确类群分量消失、全 $p$ 原始 Robert 生成元。
- B. Mazur and K. Rubin, *Kolyvagin Systems*, Memoirs AMS
  **168** (2004), no. 799，Theorem 2.3.4、
  Proposition 2.3.5（印刷页 17），
  [全文](https://webusers.imj-prg.fr/~christophe.cornut/ES/Ref/KolySys.pdf)：
  (164.8)、(164.9) 使用的是完整 Selmer 条件比较。
- Kummer、Dirichlet、类域论和 Chebotarev 的标准定理；
  本文分别给出了相关角色、类群分量、有限控制域与复共轭零类的
  明确计算，没有使用概率独立假设。

新增结论是 (164.4)、(164.8)、(164.12) 和实际共同列权重 (164.18)。
S-unit 评价矩阵的变化 $p$ 数值尚未执行，
其必满秩断言则由命题 164.2 明确排除。

