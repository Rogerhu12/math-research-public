# R245：分裂加性导子素数的惯性归一化与平方级素数下界

日期：2026-11-13。状态：**已证明。**

本篇继续变化共同导子 $bc$ 的实际支撑问题。对类数一商域，在
分裂于 $K$ 的三阶/四阶加性素数处，使用同一个局部表示的惯性
改变 Frobenius 截面，消去角色差的一部分。所得迹来自真实的
全分歧良约化扩张，剩余域仍为 $\mathbb F_q$。
比较两种不同的普通 CM 约化域给平方级下界；剩下的相位给准确
线性下界。结论不要求 $j(E)$ 整，也不依赖任何中心值非消失。

## 1. 固定参考与准确角色

保持 R66/R214 的实际小惯性分支，并设 $h_K=1$。
固定 R21 中的一条 $A_K/\mathbb Q$，其 CM 域为 $K$，在 $p$ 好约化。
设 $N_K$ 为其导子，并按 R21 对齐两个 CM 方向之一，使

$$\lambda=\psi\nu,\qquad
\nu^{12}=\nu^{p+1}=1,\qquad\nu^\iota=\nu^{-1}.          \tag{245.1}$$

$\iota$ 为复共轭，$\psi$ 是同一个参考曲线 $A_K[p]$ 的 CM 字符。
记

$$\sigma=\nu^6,\qquad\chi=\nu^4,\qquad D=|D_K|.$$

这正是 R233 的实际二次差和 R229/R232 的实际三次差。
固定例外集

$$S_0=\{q:q\mid6DN_K\}.$$

下面只讨论素数

$$q\notin S_0\cup\{p\},\qquad q\text{ 在 }K\text{ 分裂}.
                                                               \tag{245.2}$$

此处 $S_0$ 由先固定的参考曲线决定，不随实际曲线 $E$ 的新加性
素数变化。可以给九个类数一域选取坏素数均在 $2,3,D$ 上的参考；
证明本身只需要明确条件 $q\nmid N_K$。

若 $q\mid c$，$E$ 的惯性阶为 $3$ 或 $6$，$\sigma$ 在 $q$ 未分歧。
若 $q\mid b$，惯性阶为 $4$，$\chi$ 在 $q$ 未分歧。
选 $K$ 中 $q$ 上方的一个素理想 $\mathfrak q$；
$\sigma(\mathfrak q)$ 不依赖方向，而
$\chi(\overline{\mathfrak q})=\chi(\mathfrak q)^{-1}$，所以
“$\chi(\mathfrak q)=1$”也不依赖方向。

## 2. 结论表

**定理 245.1（三阶加性支撑）。** 设 (245.2) 且 $q\mid c$。

| 商域与实际二次值 | 必须满足的下界 |
|---|---|
| $K=\mathbb Q(i)$，任意 $\sigma(\mathfrak q)$ | $q>p^2/16$ |
| $K\ne\mathbb Q(\sqrt{-3})$，$\sigma(\mathfrak q)=+1$ | $q>p^2/16$ |
| $K\ne\mathbb Q(i)$，$\sigma(\mathfrak q)=-1$ | $q>p/4$ |

其中第三行包含 $K=\mathbb Q(\sqrt{-3})$。
对 $K=\mathbb Q(\sqrt{-3})$、$\sigma(\mathfrak q)=+1$，本方法不
给新下界：两边的 CM 约化域相同，整数迹可以相等。

**定理 245.2（四阶加性支撑）。** 设 (245.2) 且 $q\mid b$。

| 商域与实际三次值 | 必须满足的下界 |
|---|---|
| $K=\mathbb Q(\sqrt{-3})$，任意 $\chi(\mathfrak q)$ | $q>p^2/16$ |
| $K\ne\mathbb Q(i)$，$\chi(\mathfrak q)=1$ | $q>p^2/16$ |
| $K\ne\mathbb Q(\sqrt{-3})$，$\chi(\mathfrak q)\ne1$ | $q>p/9$ |

第三行包含 $K=\mathbb Q(i)$。对 $K=\mathbb Q(i)$、
$\chi(\mathfrak q)=1$，CM 约化域相同，故不声称有新下界。

## 3. 任意所选 Frobenius 都可来自同一个真实局部曲线的良约化

因为 $q$ 在 $K$ 分裂，整个实际局部残余像属于交换 Cartan $C$。
曲线在 $q\mid bc$ 潜在好约化。令
$\Gamma=\rho_{E,p}(I_q)$ 为特征零有限惯性像。
R63 §§3.2–3.4 已证明：模 $p$ 在 $\Gamma$ 上忠实；局部整个
特征零像与 $\Gamma$ 交换；对于**任意**算术 Frobenius 提升
$\phi$，可构造次数 $|\Gamma|$ 的循环全分歧扩张 $L_\phi/\mathbb Q_q$，
使 $E$ 在其上好约化且 $\phi\in G_{L_\phi}$。

为保留这个量词，构造为：由 $1\mapsto\phi$ 得连续
$\widehat{\mathbb Z}$ 截面，将 $I_q\to\Gamma$ 沿此截面延拓为
在截面上平凡的同态。其核的固定域就是 $L_\phi$。
所以可先乘惯性改变 $\phi$，再对该 $\phi$ 作这个真实扩张。
这不是在约化后任意更改一个虚构的迹。

因此存在整数

$$a=q+1-\#\widetilde E_\phi(\mathbb F_q),
\qquad |a|<2\sqrt q,                                   \tag{245.3}$$

其模 $p$ 特征值正是所选 $\phi$ 的残余特征值。
严格不等式因为 $q$ 为素数，$2\sqrt q$ 不是整数。

同时 $A_K$ 在 $q$ 好约化且 $q$ 分裂于 $K$，有同方向的
$\alpha\in\mathcal O_K$ 满足

$$\alpha\overline\alpha=q,
\quad v=\alpha+\overline\alpha\in\mathbb Z,
\quad|v|<2\sqrt q,\quad
\psi(\phi)\equiv\alpha\pmod{\mathfrak P}.               \tag{245.4}$$

末式使用固定的 $p$ 进剩余嵌入。改变 $\phi$ 的惯性部分不改变
参考特征值，因为 $A_K$ 在 $q$ 未分歧。
在一个共同的 $p$ 进剩余嵌入下，若 $\zeta$ 是
$\nu(\phi)$ 的十二次单位根提升，行列式给

$$\boxed{a\equiv t:=\zeta\alpha+\zeta^{-1}\overline\alpha
\pmod{\mathfrak P}.}                                   \tag{245.5}$$

每次都追踪同一个实际 $E$、同一个 $\nu$ 和对应的实际良约化迹。

## 4. 惯性同时确定特殊纤维的 CM 域

当 $q\mid c$ 时，$\Gamma$ 有三阶元。
良约化特殊纤维有三阶自同构，故其 $j$ 为零。
由于 Frobenius 与这个自同构交换，$q\equiv1\pmod3$；等价地，
特征 $q$ 的 $j=0$ 曲线为普通曲线。
因此其 Frobenius 根 $\pi_3$ 满足

$$\pi_3\in\mathbb Q(\sqrt{-3}),\quad
\pi_3\overline\pi_3=q,\quad\pi_3+\overline\pi_3=a.$$

当 $q\mid b$ 时同理：四阶自同构迫 $j=1728$，交换关系迫
$q\equiv1\pmod4$，故为普通约化，其 Frobenius 根
$\pi_4\in\mathbb Q(i)$，范数 $q$、迹 $a$。

这些根都不在 $\mathbb Q$ 中，因为一个有理代数整数的范数若为
素数 $q$，会要求 $q$ 为整数平方。因此它们生成上述准确二次域。
$\alpha$ 也生成准确的 $K$，理由相同。

由此得到一个简单但关键的整数比较：若 $t\in\mathbb Z$ 是
某个 $K$ 中范数 $q$ 元的迹，而 $K$ 与上述特殊纤维的普通 CM 域
不同，则 $a\ne t$。否则两根有相同不可约多项式
$X^2-aX+q$，两个域会相同。
结合 (245.3)–(245.5)，

$$\boxed{a\ne t\in\mathbb Z
\quad\Longrightarrow\quad p\le|a-t|<4\sqrt q.}          \tag{245.6}$$

这正是平方级下界的来源。

## 5. 三阶加性素数：先消去三次相位

在 $q\mid c$ 处，$\psi$ 未分歧，且 $\nu(I_q)$ 的阶为 $3$ 或 $6$，
所以包含全部三次单位根。利用 $\mu_{12}=\mu_4\mu_3$，可选择
$\phi$ 使

$$\zeta=\nu(\phi)\in\mu_4.$$

由于 $\sigma$ 在此未分歧，

$$\zeta^2=\zeta^6=\sigma(\mathfrak q).                  \tag{245.7}$$

若 $\sigma(\mathfrak q)=+1$，则 $\zeta=\pm1$，
$t=\pm v$ 为 $K$ 中范数 $q$ 元的整数迹。
若 $K\ne\mathbb Q(\sqrt{-3})$，(245.6) 给 $q>p^2/16$。

若 $K=\mathbb Q(i)$，不论 $\zeta\in\mu_4$ 为何，
$\zeta\alpha\in\mathcal O_K$ 仍有范数 $q$，其迹为整数。
$K$ 与特殊纤维的 $\mathbb Q(\sqrt{-3})$ 不同，故四种相位全部
由 (245.6) 给 $q>p^2/16$。

最后设 $K\ne\mathbb Q(i)$ 且 $\sigma(\mathfrak q)=-1$。
则 $\zeta=\pm i$。写

$$\alpha=\frac{v+w\sqrt{-D}}2,
\qquad v,w\in\mathbb Z,\quad w\ne0.$$

有 $t=\mp w\sqrt D$，它不是有理数，因为 $D$ 为非平方。
所以

$$0\ne a^2-Dw^2\in p\mathbb Z.$$

又 $v\ne0$：否则 $\alpha^2=-q$ 使 $K=\mathbb Q(\sqrt{-q})$，
与 $q$ 在 $K$ 分裂矛盾。因此 $t^2=4q-v^2<4q$，而 $a^2<4q$，故

$$\boxed{0<|a^2-Dw^2|<4q,\qquad p<4q.}                 \tag{245.8}$$

这证明定理 245.1 的全部分支。

## 6. 四阶加性素数：先消去二次幂部分

在 $q\mid b$ 处，$\nu(I_q)=\mu_4$，而 $\chi=\nu^4$ 未分歧。
乘一个惯性元素后可令

$$\zeta\in\mu_3,\qquad
\zeta=\zeta^4=\chi(\mathfrak q).                        \tag{245.9}$$

若 $\chi(\mathfrak q)=1$，则 $t=v$。当 $K\ne\mathbb Q(i)$ 时，
与特殊纤维的普通 CM 域 $\mathbb Q(i)$ 不同，(245.6) 给
$q>p^2/16$。

若 $K=\mathbb Q(\sqrt{-3})$，全部 $\zeta\in\mu_3$ 都是
$\mathcal O_K$ 单位，所以 $\zeta\alpha$ 的迹为整数且范数为 $q$。
其域与 $\mathbb Q(i)$ 不同，故任意 $\chi$ 值仍给 $q>p^2/16$。

余下 $K\ne\mathbb Q(\sqrt{-3})$、$\chi(\mathfrak q)\ne1$。
此时 $\zeta$ 为原始三次根。两个实共轭迹为
$\zeta\alpha+\zeta^{-1}\overline\alpha$ 及
$\zeta^{-1}\alpha+\zeta\overline\alpha$，其和为 $-v$，积为
$v^2-3q$。它们在 $\mathbb Q(\sqrt{3D})$ 中且非有理，因
$3D$ 不是平方且 $w\ne0$。由 (245.5)，

$$0\ne a^2+va+v^2-3q\in p\mathbb Z.$$

对 $|a|,|v|<2\sqrt q$，有
$0\le a^2+va+v^2<12q$，所以

$$\boxed{0<|a^2+va+v^2-3q|<9q,\qquad p<9q.}             \tag{245.10}$$

这证明定理 245.2。

## 7. 对共同导子支撑的准确推论

对七个非额外单位的类数一域

$$K=\mathbb Q(\sqrt{-D}),\qquad
D\in\{7,8,11,19,43,67,163\},$$

定理 245.1–245.2 给出不依赖相位的统一必要条件：

$$\boxed{q\mid bc,\ q\notin S_0\cup\{p\},\ q\text{ 分裂于 }K
\quad\Longrightarrow\quad q>p/9.}                      \tag{245.11}$$

所以共同导子中不超过 $p/9$ 的新素数全部惰性于 $K$。
更强地，任何分裂 $q\mid c$ 若 $\sigma(\mathfrak q)=1$，或任何
分裂 $q\mid b$ 若 $\chi(\mathfrak q)=1$，都必须大于 $p^2/16$。
若全局 $\sigma=1$，三阶支撑的全部分裂新素数都满足这个平方界。

对两个额外单位域，保留准确区别：

- $K=\mathbb Q(i)$：三阶加性支撑中每个分裂新素数都大于 $p^2/16$；
- $K=\mathbb Q(\sqrt{-3})$：四阶加性支撑中每个分裂新素数都大于
  $p^2/16$。

因此若相应分裂支撑含 $s$ 个不同新素数，其乘积严格大于
$(p^2/16)^s$；一般 (245.11) 对 $s$ 个分裂新素数给
$(p/9)^s$。R214 的奇部平方自由说明这些都是实际导子的对应因子，
不是无关的辅助素数乘积。

这些结论将尚可能的小新加性支撑压到 $K$ 的惰性素数，或两个
额外单位域中 CM 类型已经对齐的分支。它们不控制这些剩余支撑的
总大小；没有由下界推出 $bc$ 有界或 Serre 一致性。

## 8. 依赖、来源与 Manifest

- R21, Theorem B：同一个 $h_K=1$ 实际特征差 $\nu$ 的十二次幂、
  norm-one 与反圆分性质。
- R63 §§3.2–3.4：有限惯性上的模 $p$ 忠实性、交换关系、任意
  连续 Frobenius 截面及真实循环全分歧良约化扩张；本文使用它的
  完整量词，而非固定一次后再私自更改迹。
- R66/R214：$q\mid c$ 的三阶部分、$q\mid b$ 的四阶惯性及
  互斥支撑；R232/R233：同一实际 $\chi,\sigma$ 的命名。
- 椭圆曲线在剩余特征大于三的三阶/四阶自同构迫 $j=0/1728$，
  以及普通 CM Frobenius 的准确域，均为上述既有局部输入；§4–6
  给出了本篇所需的全部迹比较和非零性证明。

**Manifest：纯证明。** 新交付只有本 Markdown；无数据、脚本、
有限枚举或未经证明的新外部定理。
