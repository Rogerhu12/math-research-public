# R222：完整 pure 与八个固定圆通量的真实有限同时支付

日期：2026-11-15。**完整纸面证明；无新的研究计算。**

[R219](R219-eight-packet-fluxes-independent-on-pure-zero-responses.md) 给八个真实固定圆 gauge 不变量及其满秩 pure-zero 响应。本稿将其推进为实际可达结论：存在有限真实闭 hook，保 $M=0$、整个 $T=\kappa\mathfrak H$ 和空间闭合，同时使**完整 universal pure 函数与这八个通量全部准确为零**。

证明使用已经完成的 [R212 全 pure $C^1$ 截面](R212-C1-sections-for-complete-real-pure-cost-control.md)，不重新证明或计算 pure 分类。每个响应 prototype 的成本、复制字的偶基准，以及最终 pure 校正带来的 mixed 成本全部保留。最后只对八个有限坐标使用有限大整数和 Brouwer；在既有 $C^1$ 范围内还可得固定有限词的连续目标截面。

本稿没有假定所有权均有 $\pi U=\pi\mathcal R$。准确商仍为 $P/\pi\mathcal R$；也没有把八个必要门为零当作完整 mixed period 或逐 ruling 商已付。

## 1. 统一有限空间和增强观测的真实商

采用 R105 的真实成本空间 U 与真实响应空间 $\mathcal R$。记

$$
P=\pi U,\qquad L=\pi\mathcal R,\qquad
Q=P/L,\qquad q:P\longrightarrow Q.
\tag{1}
$$

R210 已证明实际 pure 半群为 P，R212 给任意紧 pure 目标集上的真实 $C^1$ 截面。这不蕴含 $P=L$；R210 明确保留尚未逐权比较的奇权空间。

暂取一个固定线性观测

$$F:U\longrightarrow\mathbb R^m,$$

并假设有有限个真实响应方向

$$
K_j\in\mathcal R\cap\ker\pi,\qquad 1\le j\le m,
\qquad
\mathsf K=(F(K_1)\ \cdots\ F(K_m))
\text{ 可逆}.
\tag{2}
$$

本稿的实际应用取 $m=8$，$K_j=\delta^{j-1}K$，F 为 R219 的八个修正通量。为使 F 在全 U 上有定义，沿用同一公式，只将其中的
$V_d$ 解释为固定相位输出 $V(f^2,g)$。在 pure 核上，这正好是 R213 的 $s^2$ 系数。因此这个延拓是明确的原函数查询，不是任意选择一个抽象补空间。

定义

$$E=(\pi,F):U\longrightarrow P\oplus\mathbb R^m.$$

由 (2) 可以在不改变 pure 的情况下任意改 F。于是准确有

$$
\boxed{
E(U)=P\oplus\mathbb R^m,\qquad
E(\mathcal R)=L\oplus\mathbb R^m.
}
\tag{3}
$$

例如给定 $(p,z)$，先选 $u\in U$ 使 $\pi u=p$，再用 (2) 加一个 pure-zero 响应将 F 从 $F(u)$ 改成 z。若 $p\in L$，第一步可在 $\mathcal R$ 内完成，给第二个等号。故自然商同构是

$$
\boxed{
\frac{E(U)}{E(\mathcal R)}
\ \simeq\ Q,\qquad [(p,z)]\longmapsto qp.
}
\tag{4}
$$

### 1.1 原缩放作用怎样准确下降

原正几何缩放 $\mathsf D_H$ 保 U、$\mathcal R$，并与 pure 投影交换。固定圆 F 本身通常不与它交换；本文不需要这样的假设。

对任意 $u\in U$，其增强商在缩放后准确为

$$q\pi(\mathsf D_Hu)=D_H(q\pi u).$$

若两个 u 的 E 像在 (4) 中同类，差的 pure 属 L；缩放后仍属 L，故这条公式与代表无关。因此 (4) 上真正下降的 H 作用就是 R206/R212 原来的 $D_H$，不是在固定圆上虚构一个新的仿射作用。

R201 已付整个权零像等号 $Q_0=0$，所以原缩放生成元在 Q 上可逆。R210 的满 pure 闭锥与 R206 的严格正配平、floor 整数、真实端口桥和商截面都仍适用。这说明 (3) 没有把未知 Q 丢掉。

这里说的是线性空间及商上的作用。实际缩放通常改变 scalar 端口；固定端口路径仍须按 R206 §4 用真实 M0 桥夹住，保留 $2V_A$ 的连接成本，不把裸缩放宣称为原实际半群的自映射。

下面直接调用 R212 已经完成 Q 与 L 两部分后的**全 pure 截面**，从而不重做这些步骤。

## 2. 一般真实联调定理

**定理。** 在 (2) 及 R212 已付的全 pure 截面下，对每个

$$p\in P,\qquad z\in\mathbb R^m,$$

存在有限真实同 scalar germ、frame $I\to I$ 的路径 B，满足

$$
\boxed{
M_B=T_B=0,\qquad
\pi V_B=p,\qquad F(V_B)=z.
}
\tag{5}
$$

任意固定紧目标集还可在一个固定有限词中获得 $C^1$ 目标截面。所用整数重复次数可在该紧集上固定，实际总长与空间位移不要求为零。

共同物理 I 与 F 的选择遵守第 6 节的顺序：先固定全部小族与有限原生成器的 scalar 包络，再放入合法圆。不是保证任意预给的窄 I 能容纳这些辅助几何。

## 3. 响应方向可为有限组合，基准却不能省

式 (2) 的 $K_j$ 不必是一个原始 $\mathcal B_E(\tau)$。写成有限原响应组合

$$
K_j=\sum_{\nu=1}^{N_j}c_{j\nu}
\mathcal B_{E_{j\nu}}(\tau_{j\nu}).
\tag{6}
$$

R219 的方向具有这种已证明的表达式，来自 R217 的 E8 导子表与 R71 交换子闭性。删去零系数后，每组非空。

对每项选 R71/R101 的真实第三 prototype $L_{j\nu}$，使

$$M_{L_{j\nu}}=0,\qquad T_{L_{j\nu}}=\tau_{j\nu},\qquad
V_{L_{j\nu}}=v_{j\nu}.$$

每个 $v_{j\nu}\in U$：真实 $L_{j\nu}L_{j\nu}^{\rm rev}$ 的 M、T 均为零、成本为 $2v_{j\nu}$；取半仅用于空间归属。令

$$v_j=\sum_{\nu=1}^{N_j}v_{j\nu}.$$

使用 R212 对有限 pure 目标 $-\pi v_j$ 的实际校正，选
$C_j$ 满足

$$M_{C_j}=T_{C_j}=0,\qquad \pi V_{C_j}=-\pi v_j.$$

将 $C_j$ 追加在第 j 组的一个固定 prototype 后面。它不改变该 prototype 的第三算子，因此 (6) 的响应方向完全不变。记改后的成本和为 $\widehat v_j$，则

$$
\boxed{\pi\widehat v_j=0.}
\tag{7}
$$

$\widehat v_j$ 的 mixed 成本可能很大；下文完整保留。

对第 $(j,\nu)$ 项，R101 用二阶参数 $c_{j\nu}t_j$，第三 prototype 使用上面已固定的版本。取同一个正整数 n，有限拼接该组的真实复制词。每块 M=T0，R83 的完整传递给

$$
\boxed{
V_{Z_j(t_j,n)}
=E_j(t_j)+n(2\widehat v_j+t_jK_j),
\qquad M_{Z_j}=T_{Z_j}=0.
}
\tag{8}
$$

$E_j$ 是真实的完整偶基准，与 n 无关，在固定 t 盒上为 $C^1$。式 (6) 的负系数只改变小矩阵族的真实正负参数，不表示负路径或负成本。大的有限参数由固定小族的有限重复实现，保原 scalar 包络。

拼接 m 组，得

$$
V_{Z(t,n)}
=E_0(t)+n\left(2\sum_j\widehat v_j+\sum_jt_jK_j\right).
\tag{9}
$$

所有传入历史、同一右锚及每段的实际位移均按原词传递，没有在组间重置。

## 4. 先准确支付整 pure，再保留校正的全部 F 成本

由 (2)、(7)，(9) 的 pure 是

$$\pi V_{Z(t,n)}=\pi E_0(t),\tag{10}$$

与最后复制数 n 无关。

令

$$
v_\Sigma=\sum_jF(\widehat v_j),\qquad
t^0=-2\mathsf K^{-1}v_\Sigma,\qquad
\mathcal C=t^0+[-1,1]^m.
\tag{11}
$$

先固定覆盖这个盒所需的 R101 小族重复数，使 $E_0(t)$ 在
$\mathcal C$ 的邻域已经是一个固定 $C^1$ 函数。此时还未选择 n。

对给定 pure 目标 p，集合

$$Y_p=\{p-\pi E_0(t):t\in\mathcal C\}\subset P$$

紧。R212 给其开邻域上的同一个实际全 pure $C^1$ 截面
$\mathscr D(y)$，其整数、构件与词排列固定，且

$$M_{\mathscr D(y)}=T_{\mathscr D(y)}=0,\qquad
\pi V_{\mathscr D(y)}=y.$$

定义真实字

$$
\widetilde Z(t,n;p)
=Z(t,n)\mathscr D\bigl(p-\pi E_0(t)\bigr).
\tag{12}
$$

全部块 M=T0，第四成本严格相加，故对所有 t，

$$\boxed{\pi V_{\widetilde Z(t,n;p)}=p.}\tag{13}$$

其 F 坐标准确为

$$
\boxed{
F(V_{\widetilde Z(t,n;p)})
=\mathcal E(t,p)+n(2v_\Sigma+\mathsf Kt),
}
\tag{14}
$$

其中

$$
\mathcal E(t,p)
=F(E_0(t))
+F\!\left(V_{\mathscr D(p-\pi E_0(t))}\right).
\tag{15}
$$

最后一项就是 pure 校正真实带来的全部 mixed 查询成本；没有假设它属于响应像、为零、随目标线性或只有小量。

R212 的路径族为 $C^1$，R56 的完整恢复在共同物理间隙上为 $C^1$。U 有限维，所以固定线性 F 的这些值也是 $C^1$。因此 (15) 在 $\mathcal C$ 上有界，并在选择 n 之前已经固定。

## 5. 有限 n 同时付八坐标；紧目标可得真实截面

先用连续性完成存在性。对给定 z，选有限整数 n，使

$$
\sup_{t\in\mathcal C}
\left\|\mathsf K^{-1}\bigl(z-\mathcal E(t,p)\bigr)\right\|_\infty<n.
$$

映射

$$
t\longmapsto
t^0+n^{-1}\mathsf K^{-1}\bigl(z-\mathcal E(t,p)\bigr)
\tag{16}
$$

连续地把 $\mathcal C$ 映入自身。Brouwer 给不动点 $t_*$；由 (11)、(14)，其 F 坐标恰为 z。与 (13) 一起，得到 (5)。

若目标 $(p,z)$ 限于一个紧集，先用其 pure 投影及固定 $\mathcal C$ 选一个共同的紧 Y 和 R212 截面，固定全部词。再令 n 同时大于上面的值界以及

$$
\sup_{(t,p)}
\left\|\mathsf K^{-1}D_t\mathcal E(t,p)\right\|_\infty.
$$

则 (16) 在同一盒上为统一严格收缩，且可留严格内点余量。唯一不动点由 IFT 对 $(p,z)$ 为 $C^1$。于是所得真实固定有限词 $B(p,z)$ 满足

$$
E(V_{B(p,z)})=(p,z),\qquad
D_{(p,z)}E(V_{B(p,z)})=\operatorname{id}.
\tag{17}
$$

这是对新增 m 个观测的真实联调截面；R212 的 full-pure 截面作为已付模块使用，没有重新证明旧结果。式 (17) 也未支付任何离开准确 M=T0 层的额外约束。

## 6. 共同 I、圆与控制生成器的选择没有循环

对 R219 八通量应用，选择顺序如下。

1. 先固定 R206/R212 所需的有限满锥见证、近 1 缩放与端口桥小族、pure 响应原生成器、小二阶族及实际第三 prototypes。这一有限库由 universal pure 空间决定，不使用将来的固定圆。
2. 加入 (6) 中 $\delta^0K,\ldots,\delta^7K$ 所需的有限原响应、小二阶族与第三 prototypes；若要下面的闭 hook 推论，也先加入背景 hook 和全部 frame/scalar 桥。由有限性得到一个共同紧 scalar 包络，h 有正下界。
3. 支付有限个 (7) 的 pure 基准。这些校正仍用第 1 步库的固定小族；R212 §5.2 已证明以后改变紧目标只增加有限重复，不扩大原包络。
4. 在这个包络之外选共同合法物理 I，然后选 R217/R219 的同一个 R183 圆。现在 F 才固定。R219 的 Vandermonde 证明对这个最终坐标中的任意互异平移成立，因此 (2) 真正可用；没有先假设一个未知实际矩阵可逆。
5. 用完整 $\widehat v_j$ 的 F 值确定 (11) 的盒，并固定覆盖该盒的有限小族重复数。负系数和大有限中心不扩大第 2 步包络。
6. 对实际所需紧 pure 目标 Y 固定 (12) 的全 pure 截面。其自身 mixed 成本保留为 (15)。
7. 最后才选 n 并解 (16)。

所有小参数族和它们使用的 frame、scalar germs 在每次出现末端准确复位。无论后续整数多大，都只有限重复已固定的 scalar 轨迹；同一 I、右锚和 h 正性继续成立。

本定理没有保证一个任意预先指定窄 I、固定总长或预定空间位移。这些实际量可能随整数增大；位置由真实 $\alpha_s=h^2T$ 积累，不被重设。

## 7. 实际闭 hook 同时取得整 pure 零和八通量零

取 R180 的一个有限真实闭 hook 背景 $X_0$，其

$$M_{X_0}=0,\qquad T_{X_0}=\kappa\mathfrak H,\qquad\kappa\ne0.$$

可使用 R210 已 pure-zero 的背景，但证明不需要预先要求其 pure 为零。
$V_{X_0}\in U$ 由真实 $X_0X_0^{\rm rev}$ 的成本
$2V_{X_0}$ 给出；取半只说明线性空间归属。

按第 6 节将该背景先纳入共同包络，选同一个 R183 圆。对 (5) 指定

$$
p=-\frac14\pi V_{X_0},\qquad
z=-\frac14F(V_{X_0}).
\tag{18}
$$

得到实际 $M=T=0$、frameI 同端口块 D。将同一个 D 插入 Klein 的一类 prototype，连同其四个正确 ambient 副本。R210 已支付这个真实组合的 frame、第三算子和位置闭合；R83 给

$$V_X=V_{X_0}+4V_D.$$

所以

$$
\boxed{
X\text{ 是有限真实闭 hook},\quad
M_X=0,\quad T_X=\kappa\mathfrak H,\quad
\pi V_X=0,\quad
\mathcal F_0(V_X)=\cdots=\mathcal F_7(V_X)=0.
}
\tag{19}
$$

没有把 D 的空间位移要求为零；Klein 闭合使用改后 prototype 的真实位移。八通量是同一个固定圆上的准确原函数积分与平台点值，不是有限采样近似。

R196 仍给

$$
\lambda_+(V_X)=\int k^2\,ds
=L+\int(h_s/h)^2\,ds>0.
\tag{20}
$$

因此现在有一个实际成本的正值见证：完整 pure 与八个固定圆通量同时为零，并不会使该 universal 正字符为零。它不是一个由有符号成本线性组合虚构的路径。

同一一般定理还可用于 R219(24) 的三个读出
$(\mathcal L_d,\mathcal L_e,\mathcal F_j)$，使整 pure 与这三个量同时准确为零。本文没有证明八通量再加两个左尾的十元组在 pure-zero 响应上满秩，所以不将两个应用合并。

## 8. 已付和未付的真实边界

本稿实际支付了整 universal pure 与八个明确的 fixed-circle period 必要门。它们的值不再只是“可以有符号变化”，而能在所有基准保留时共同取指定值。

仍未证明完整 $V_d,V_e$ 属于 R181 的 $L_f$ 像，也未找到同一个二阶 gauge 同时解 R184 的逐 ruling 商。R221 的完整 ruling 线性展开与本稿的有限观测控制是不同的数据；本文没有把后者代替前者。

插入新控制块通常改变基础度量。结论是选定最终闭 hook 后，它有上述同一个合法圆与准确成本身份；不是在几何设计参数变化期间保持原参考 g 的等距变形。无开常段、无四阶 flat 点或全域 Morse 的保持也不能仅由 (19) 推出，若要兼容须在实际精确约束族中另外处理。

完整 mixed、逐 ruling、更高阶、有限连续等距族、全时嵌入与 reach 以及主课题的宏观幅度要求均未被本稿冒称完成。
