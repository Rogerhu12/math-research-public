# R150 附录：单位 2+1+1 相等非零基点配对且单点相互配对为零支路为空

作者：Astra-ISP-347c-20261126；AI-assisted GPT-6 Astra Pro。日期：2026-11-26 UTC。

**状态：本条范围已证明。** 在同一原 essential-four 外均值、rank $H=4$、单位 $2+1+1$ 与孤立零点分支中，本稿排除 $p=q\ne0,t=0$。这里 $t$ 是两个单位单点之间的 Gram 配对，不是物理曲线参数。新输入是原孤立零点 mean 与最高式合成的一个低次、无除法必要条件；未将这些必要条件当作原临界性的充分条件。

## 1. 原零点方程给出的低次必要条件

保留[相等配对最高基点值附录](R150-appendix-essential-four-unit-two-plus-one-plus-one-equal-base-pairings-zero-highest-value-exclusion.md)的同一原对象和全部定义。规范 $p=q=1$ 后，
$$
\tau(z)=a z_0+z_1+bz_B+cz_C,
\quad l=b+c,\quad a=1-l,\quad bc\ne0,
$$
$$
K_B=\begin{pmatrix}
0&0&1&1\\0&A_1&r&s\\1&r&0&t\\1&s&t&0
\end{pmatrix},\quad
U=(u_0,u_1,u_B,u_C),\quad m=\tau(U).
$$
原最高值和第二梯度满足
$$
P_0=-u_0^3,\quad P_1=-3u_0^2u_1,\quad P_B=-u_B^3,\quad P_C=-u_C^3,
$$
$$
N_0=-mu_0^2,\quad N_1=-2mu_0u_1,\quad N_B=-mu_B^2,\quad N_C=-mu_C^2.
\tag{1.1}
$$
原完整 mean 在孤立零点处还给
$$
\tau(U^2)=2m^2.
\tag{1.2}
$$
可直接从原完整 mean 的孤立零点系数重得 (1.2)：原归一为 $y=\tau X$、$H=\tfrac14\tau X^2$、$V=\tfrac18\tau X^3+\tfrac14R^3$。记零点向量为 $z$，则 $p^Tz=m$、$z^TKHKz=\tau(U^2)/4$；全部其他 mean 项都在四维活跃空间内，零点列的系数是 $4(m^2/4)-8(\tau(U^2)/16)=m^2-\tau(U^2)/2$。原五个 jets 独立，故该系数为零。

这一原方程已明确保留于[单位三加一零基配对稿](R150-appendix-essential-four-unit-three-plus-one-isolated-zero-zero-base-pairing-branch-is-empty.md)式 (1.6)；其来源只用单位活跃代数与一个孤立零点，故对当前同一归一同样成立。原最高式在该点的值是 $P(U)=0$，其中
$$
2P(U)=\tau(U^3)-3m\tau(U^2)+2m^3.
$$
定义
$$
\overline P=aP_0+P_1+bP_B+cP_C,
\qquad \overline N=aN_0+N_1+bN_B+cN_C,
$$
$$
\boxed{\mathscr S=\overline P-2\overline N.}
\tag{1.3}
$$
由原双点乘法，(1.1) 精确给 $\overline P=-\tau(U^3)$、$\overline N=-m\tau(U^2)$，因此
$$
\boxed{\mathscr S=-2P(U)-m\{\tau(U^2)-2m^2\}=0.}
\tag{1.4}
$$
这是全权、全零值范围的多项式身份，没有除以 $m,u_i,P_i,N_i$。它把原零点 mean 和最高式都保留下来。

## 2. $t=0$ 的完整 mean 坐标

已登记的相等配对最高基点值定理排除了 $l=0,1/2,1$，无需重算。于是这里只须
$$
l(l-1)(2l-1)bc\ne0,
\qquad t=0.
\tag{2.1}
$$
置
$$
\beta=bc,\quad \delta=b-c,\quad h=2l-1,
\qquad x=d_B=a+r,\quad y=d_C=a+s,
$$
$$
X=\frac{bx+cy}{l},\qquad V=X-l,\qquad Z=x-y=r-s.
$$
这些 $x,y$ 是原 mean 坐标，不是支撑点。因 $l\ne0$，换元可逆。原 $E_0=0$ 唯一给
$$
f=X/2+l/2-1/4,\qquad A_1=(1-2l)(X-1/2),
$$
$$
r=X+cZ/l-a,\qquad s=X-bZ/l-a.
\tag{2.2}
$$
因此没有自由改写原 Gram 或二阶矩。

用原 $E=e-2D_Kd-2d^2+4fd$ 直接展开，记 $E_w=(bE_B+cE_C)/l$，得到三个准确身份：
$$
E_w=-\frac{2\beta Z^2}{l^2}+Vh,
\tag{2.3}
$$
$$
E_1-lE_w=-2h(V-1/2)(V+l-1/2),
\tag{2.4}
$$
$$
E_B-E_C=\frac{Z}{l}\{2\delta Z-l(2V+2l-1)\}.
\tag{2.5}
$$
因为 $h\ne0$，原 mean 必位于以下两个完整分支之一：
$$
V=1/2\qquad\text{或}\qquad V=1/2-l.
\tag{2.6}
$$
在 (2.1) 内，这两个 $V$ 都非零。(2.3) 因而给 $Z^2\ne0$，所以仅在这时才从 (2.5) 取消 $Z$。

## 3. 第一分支 $V=1/2$

由 (2.3)、(2.5)，
$$
Z^2=\frac{l^2h}{4\beta},\qquad \delta Z=l^2.
\tag{3.1}
$$
把同一原 $P,N$ 和 (2.2) 代入 (1.3)，再使用 (3.1)，准确化简为
$$
\boxed{\mathscr S=\frac12l(2l-1)^2.}
\tag{3.2}
$$
(2.1) 使它非零，与原必要式 (1.4) 矛盾。

这一身份直接以 (3.1) 化简，不必再用 $\delta^2=l^2-4\beta$ 解 $\beta$，也没有除以可能为零的 $l^2+2l-1$。因此不会丢掉所谓判别式退化纤维。

## 4. 第二分支 $V=1/2-l$

此时 (2.3)、(2.5) 给
$$
Z^2=-\frac{l^2(2l-1)^2}{4\beta},\qquad \delta Z=0.
$$
已经有 $Z\ne0$，所以 $\delta=0$，即
$$
b=c=l/2,\quad \beta=l^2/4,\quad Z^2=-(2l-1)^2.
\tag{4.1}
$$
仍从同一原 (1.3) 计算，得到
$$
\boxed{\mathscr S=-\frac12l(l-1)(2l-1)^2.}
\tag{4.2}
$$
它在 (2.1) 内也非零，和 (1.4) 矛盾。

两个分支穷尽全部原 mean，故 (2.1) 无解。接已付的三个特殊 $l$ 后，整个 $p=q\ne0,t=0$ 分支为空。由于排除发生在任何原物理实现都必须满足的同一 Gram 方程上，有限支撑和无穷远支撑都包含在结论中。

## 5. 可复算身份与实际执行

[自足 QQ 源](../notes/2026-11-26-unit-two-plus-one-plus-one-equal-zero-single-pairing-347c.py)直接重建原 Frobenius 乘法、mean 与全部 $P_i,N_i$，验证 (1.4)、(2.3)–(2.5) 和两个精确非零值。为整理对称表达，它使用
$$
\beta=bc,\qquad U=Z^2,\qquad W=(b-c)Z,
$$
但把整理后的每个表达重新代回 $b,c,Z$ 并核回原有理式；没有独立选择一个非物理对称模型。所有关键分母在 (2.1) 中已证明非零。

源码 SHA-256：`90220cc8dee7b4b0642e25d16fb1e1e56002bbcd4dda63bac50f9199668fd19d`。实际执行为 CPython 3.12.14、SymPy 1.14.0，无 `PYTHONPATH` 覆盖；exit $0$，源内 $1.205597$ 秒，峰值 $49728$ KiB。[紧凑执行记录](../notes/2026-11-26-unit-two-plus-one-plus-one-equal-zero-single-pairing-execution-347c.json)保留原命令、源与输出身份，未存可重算数组。

相等非零配对只余 $t\ne0,l\notin\{0,1/2,1\}$；一般非等配对、全局原幂来源与普通 Hilbert ISP 保持开放。

**后续完整闭合（2026-11-26）：** 本条的原边界证明保持有效；余下等配对一般图现由[完整相等配对专条](R150-appendix-essential-four-unit-two-plus-one-plus-one-equal-base-pairings-complete-exclusion.md)关闭，整个 $p=q\ne0$ 不再是待做分支。
