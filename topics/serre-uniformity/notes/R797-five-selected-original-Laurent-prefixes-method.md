# R797：五个已选原 Hom 的最小完整 Laurent 前缀

日期：2026-11-15。状态：**已固定准确方法；五个新前缀的实际完成以公开 Actions 为准。**

本次直接消费 R794 成功 run43691270124 的五个原映射与六条原微分坐标。
目标是原目标 $C/L:y^2=x^3+b$ 上的五个 $y_f$ 的准确局部输入。
不替换原 $b$、原 cusp、原 $c_0$ 基点或原 Néron 微分；
不施加实下降的 $1-\zeta^2$，不重算原 $f_4$ 的 Laurent 前缀。

## 1. 原微分、共同六行与规范逐项一致

R794 的五条记录按原顺序为

| candidate index | 原映射 | 次数 $d$ | 普通幂 $m$ | 完整条件数 $N$ | 新 $R$ 最高阶 | 新 $H^3$ 最高阶 |
|---:|---|---:|---:|---:|---:|---:|
| 0 | $f_0$ | 1485 | 7 | 170 | 169 | 170 |
| 3 | $f_3$ | 1521 | 7 | 172 | 171 | 172 |
| 1 | $f_1$ | 1602 | 7 | 176 | 175 | 176 |
| 21 | $f_0+f_{10}$ | 1674 | 8 | 193 | 192 | 193 |
| 15 | $f_0+f_4$ | 1728 | 8 | 196 | 195 | 196 |

本表 $f_i$ 一律使用 R759 的零起始整数 Hom 索引；
旧 R774/R781 文字中称为 $f_0$ 的固定次数1206参考映射是这里的 $f_4$。
程序使用 candidate index 和完整原 Hom 整数列绑定，避免这两个记号混淆。

R794 保存

$$
h_f=f^*\omega_C=\sum_{j=0}^5 v_{f,j}\omega_j,
\qquad v_{f,j}\in L=\mathbb Q(b,\zeta),\quad s=1+2\zeta.
\tag{797.1}
$$

其坐标字段明确是 R759 原 $b^0,\ldots,b^6$、$1,\zeta$，
微分基明确是 R745 原 $\omega_0,\ldots,\omega_5$。
R774 的公共整数行就是同一基对应的

$$
F_j(Q)=\sum_{n\ {m odd}}sP_{j,n}(\xi)Q^n
       +\sum_{4\mid n}3P_{j,n}(\xi)Q^n
       =QG_j(q_Y),
\quad q_Y=Q^3,\quad Q=e^{2\pi i\tau/246}.
\tag{797.2}
$$

原比较是

$$
\omega_j=\frac{\alpha}{7}F_j(Q)\frac{dQ}{Q},
\quad \alpha^3=4,\quad
h_f=2\pi i H_f(\tau)d\tau,
\quad H_f=\frac{\alpha}{1722}\sum_jv_{f,j}F_j,
\tag{797.3}
$$

因为 $dQ/Q=(2\pi i/246)d\tau$，$1722=7\cdot246$。
因此所有五个映射都使用同一个准确式

$$
\boxed{H_f^3=
 q_Y\sum_{0\le i\le j\le k\le5}
 \frac{4\,m_{ijk}}{1722^3}\,
 v_{f,i}v_{f,j}v_{f,k}\,G_iG_jG_k,}
\tag{797.4}
$$

其中 $m_{ijk}$ 为1、3、6的真实多项式重数。
R774 的56个 `R774-cubic-monomial-*.json.gz` 保存的恰是
$G_iG_jG_k$ 的实部、$s$ 部，既没有第4号映射的 $v$，
也没有 $4/1722^3$ 或前面的 $q_Y$。
因此本次只复用这56个共同三积；对每个新映射重新形成 (797.4) 的标量，
把 $q_Y$ 恰好移动一次。

R774 的 `R774-original-L-cubic-scalars.json.gz` 只作为原 $b$ 最小多项式的
已认证载体读取。它的旧第4号标量矩阵和旧行尺度完全不消费。
旧六行的 tame 因子已经在 $G_j$ 中；R794 的微分坐标已经在原基中。
不额外乘 $s$、3、246、$\alpha$ 或 $c_1$ 的 $\zeta^2$。

## 2. 准确收缩及公共底层算术的复用

各个 $v_{f,i}v_{f,j}v_{f,k}$ 只在同一原
$\mathbb Q[b,\zeta]$ 中约化。若新标量为 $A+B\zeta$，改写成
$(A-B/2)+(B/2)s$，然后与每个已成三积的 $R+sS$ 相乘：

$$
(a+sb)(R+sS)=(aR-3bS)+s(bR+aS).
\tag{797.5}
$$

这给每个新映射一个 $14\times112$ 有理矩阵。
逐行清有理分母、提出整数 content，保存 primitive 整数行和其有理尺度。
用整数矩阵乘法收缩已成三积的所需前缀，不重新计算三积或 Fourier 行。
对条件数 $N$ 的映射，只消费三积的 $q_Y^0,\ldots,q_Y^{N-1}$，
输出 $H_f^3$ 的 $q_Y^1,\ldots,q_Y^N$。

R781 的冻结 `Field` 和 `Element` 类仅作同一系数域的准确算术实现：
$B=\lambda b$、$s^2=-3$、$t=\xi+\xi^{-1}$，
基为 $B^is^jt^r$，$0\le i<7$、$0\le j<2$、$0\le r<20$。
核心源码 SHA 单独绑定；不会调用其旧 `Job` 或运行原 $f_4$ 递推。
字段的原 $b=B/\lambda$ 始终保持。

按 R781 作明确换参

$$
v=\xi^{-10}q_Y,\qquad
H_f^3=\sum_{n=1}^N\kappa_{f,n}v^n,
\quad \kappa_f=\kappa_{f,1}.
\tag{797.6}
$$

每个新系数准确乘 $\xi^{10n}$，对14个 $b^i,sb^i$ 行逐项核
$\xi\mapsto\xi^{-1}$ 不变性，再用原 Chebyshev 多项式换成20坐标。
不以平均制造不变性。
R793 的原 Hom/cusp 定理已经证明五个非零映射都在全部 cusp 不分歧；
本次仍准确核 $\kappa_f\ne0$，并以此实际确认原 $e=1$。

## 3. 每个新映射独立的无逆递推

R764 的原基点规范给所有这些整数 Hom 的 $f(c_0)=O$。
原微分方程保持

$$
(\mathscr D y_f)^3=27(y_f^2-b)^2H_f^3,
\qquad \mathscr D=\frac1{82}v\frac d{dv}.
\tag{797.7}
$$

由一阶极点和 (797.7) 的首项，

$$
y_f=-\frac{1}{246^3\kappa_f v}\,Z_f(v),\qquad Z_f(0)=1.
\tag{797.8}
$$

设 $v=\kappa_fw$、$R_f(w)=Z_f(\kappa_fw)$，并置

$$
\widetilde A_{f,0}=1,\quad
\widetilde A_{f,n}=\kappa_{f,n+1}\kappa_f^{n-1}\ (n\ge1),
\qquad c_{f,*}=246^6b\kappa_f^4.
\tag{797.9}
$$

R781 的同一逐项推导适用于每个这些原映射，给

$$
(R_f-wR_f')^3=\widetilde A_f(R_f^2-c_{f,*}w^2)^2,
\qquad R_{f,0}=1.
\tag{797.10}
$$

暂取 $R_{f,n}=0$ 时左减右残差为 $E_{f,n}$；未知项的系数为
$3(1-n)-4=-(3n+1)$，所以

$$
R_{f,n}=\frac{E_{f,n}}{3n+1}.
\tag{797.11}
$$

每阶只使用已成卷积状态，不重新展开旧阶。
加入新系数后准确核该阶恒等式，按归纳认证全部前缀。
保存 $R,W,R^2,W^2,U,U^2,\widetilde A,\kappa_f^n$ 的当前阶，
其中 $W=R-wR'$、$U=R^2-c_{f,*}w^2$，供同配置续算。
只除以明确的非零有理整数，不反演代数元素 $\kappa_f$。

## 4. 恰好满足完整原函数界

R793/R794 已给

$$
m=\left\lceil\frac{d+254}{272}\right\rceil,
\qquad N=\left\lfloor\frac{272m+d}{20}\right\rfloor+1.
\tag{797.12}
$$

完整候选认证是 $-1\le n\le N-2$ 的全部 $N$ 条关系

$$
246^3\kappa_f^{n+2}A_n+
 \sum_{j=0}^{n+1}\kappa_f^jR_{f,n-j+1}B_j=0.
\tag{797.13}
$$

故需要且这里只生成 $R_0,\ldots,R_{N-1}$，
从 (797.9) 只需要 $H_f^3$ 至 $N$ 阶。
普通截面基必须另给 $q_Y^0,\ldots,q_Y^{N-1}$；
其全部20个 $M^+/L$ 坐标不能省略。
本次既不生成这些新普通高次基，也不把理论核维数当作已执行结果。

只有五个映射各自的全部所需阶实际完成、源配置和逐阶 SHA 链通过、
全部原相位和残差等式均通过，才输出完整成功证书。
断点按映射和阶保存，续算不重做已成映射或已成阶。
旧 R774 原第4号 $H^3$、旧 R781 第4号 Laurent、原 newform、period、Hom、
SVP、LLL 都不重算。

成功的对象是五条真实局部 Laurent 输入；不是已恢复的 $A/B$、
极除子、$\eta$、Poincaré 刚性化常数或实际高度。
全部新算术在本公开仓库 Actions 执行；系数与活跃输入只在一日临时包转交，
不进入 Git 或 Release。

依据：[R774](../results/R774-certified-original-Hodge-cube-and-cusp-order.md) §§2、4–5；
[R781 原证明](../results/R781-original-tangent-descent-and-inverse-free-Laurent-relations.md) §§1–6；
[R793](../results/R793-original-RR-pole-divisors-and-CM-local-algebra.md)；
[R794 实际五方向](../results/R794-certified-original-low-degree-eta-basis.md)。
