# R200：单下降 step 的准确第三桥响应与不可用二阶 gauge 修复的真实闭几何

日期：2026-11-15。完整纸面证明；没有新 profile 评价、几何积分或研究编译。本文只证明存在一些真实几何失败，不排除其他几何；末节另给同一参数族对一个 period 查询的准确支付。

来源：[R70 仿射完整周期](R70-zero-matrix-bridges-and-affine-complete-fourth-period.md)、[R71 内部桥的真实第三响应](R71-third-holonomy-commutators-and-complete-fourth-P1.md)、[R83 真实传递](R83-true-fourth-transfer-and-zero-lower-history-variations.md)、[R189 无开常段迁移](R189-nowhere-constant-state-matrix-bridges-and-closed-hook-geometry.md)、[R198 最右纯 period 不变量](R198-rightmost-single-profile-period-obstruction-under-all-second-gauges.md)。局部代数也与已发布的 [tau0 三个原式导数身份](../scripts/literature_tau0_response_independent_certificate.mjs) 一致；本稿重新写出所需式子与边界，不重跑该源码。

## 1. 固定规范：未乘时长的正常态算子

在共同 profile 坐标 x 上，取两常态

$$
S_+=(h,k,\omega)=(1,1,1),\qquad
S_-=(1,-1,-1).
$$

两态都有 $d=h\omega-k=0$。令

$$
Q=1+x^2,\qquad L=x^2-1,\qquad
J_q(x)=\int_x^r\{Q(\eta)q''(\eta)^2+2q'(\eta)^2\}\,d\eta.
$$

R62/R73 的正态 second 密度是未乘长度的二次算子 A：

$$
\boxed{
A(q,q)=\frac x2q^2-\frac Q2qq'
+\frac{xQ}{4}q'^2+\frac L8J_q.
}
\tag{1}
$$

负态的密度准确为 $-A$。两态各一个完整 frame 圈的实际正长度都是

$$
\ell=\frac{2\pi}{\sqrt2}=\sqrt2\pi.
\tag{2}
$$

所用的负算子来自真实负 k 常态，未把负长度当作路径。

再令

$$
P(a,b)=\int_x^r a''b'',\qquad
R(a,b)=a'b'+x\int_x^r a''b'',
$$

并用完整三槽交换子 $[P,R]$。它的 diagonal 是

$$
\boxed{\tau_0(q)=[P,R](q;q,q)
=-\frac13\int_x^r q''(\eta)^3\,d\eta.}
\tag{3}
$$

R71 的真实零矩、同 scalar、frame 恒等环可以使任一内部桥的第三算子准确增加 $t[P,R]$，从而其 diagonal 增加 $t\tau_0$。小 t 用同一光滑控制族；任意有限紧 t 区间可由固定次数的小环复制实现，全部基准第四成本保留。

## 2. 纯响应的准确八分之一与完整局部式

定义

$$
\boxed{
\mathcal H(q)=
\frac{D\tau_0(q)[A(q,q)]-2A(q,\tau_0(q))}{8}.
}
\tag{4}
$$

R71 的 (5) 使用的是积分算子 $\mathcal A=\ell A$。所以一对正、负 bulk 之间的桥第三算子增加 $t[P,R]$，其 pure $-4$ 的 N 一次系数准确增加

$$
\boxed{\Delta P_{1,-4}=\ell t\,\mathcal H(q).}
\tag{5}
$$

没有在这里再乘或漏掉 Fourier 的 $1/16$；(4) 本身采用旧纯 $-4$ forcing 规范。

为直接判断固定右 step 的响应，记 $p=q'$、$a=q''$、$m=q-xq'$、$I_3=\int_x^r a^3$，并定义

$$
\begin{aligned}
F_q={}&-qpa^2+\frac x2p^2a^2+\frac{2x}{3}ma^3
+\frac{x(2x^2-1)}{12}a^4-\frac14J_q a^2,\\
G_q={}&-\frac x2a^4+\frac23pa^3.
\end{aligned}
$$

直接对 (1) 求两次导数给

$$
A(q,q)''=qp-xma-\frac x2p^2-\frac{xL}{4}a^2
+\frac14J_q-\frac Q4(2m+La)q'''.
\tag{6}
$$

按同右锚分部积分，有

$$
D\tau_0(q)[A(q,q)]
=-\frac Q6ma^3-\frac{QL}{16}a^4+\int_x^r F_q,
$$

$$
J_e(q,\tau_0(q))
=-\frac Q4a^4+\int_x^r G_q,
\tag{7}
$$

其中 $J_e(q,\tau_0)=\int_x^r(Qq''\tau_0''+2q'\tau_0')$。这些式子可先对 x 求导核对，再用右 collar 的零值确定唯一积分常数。没有把左尾清零。

代入 (4) 后，(7) 的两个局部 $Qa^3m$ 项及两个 $QLa^4$ 项各自相消，得到

$$
\boxed{
8\mathcal H(q)
=\frac{xq-Qq'/2}{3}I_3
+\int_x^r F_q
-\frac{L(x)}4\int_x^r G_q.
}
\tag{8}
$$

这是完整函数身份，保留了 $J_q$、$I_3$ 和全部右尾；不是局部最高符号的替代。

## 3. 固定单右 step 的首项严格非零

取右端 c，并设在其左侧

$$
q(c-t)=a_0t^8+O(t^9),\qquad a_0\ne0,\qquad t=c-x.
\tag{9}
$$

profile 在 c 右方为零。所有右原函数因此也在 c 为零。式 (8) 中首项从 $t^{26}$ 开始；$F_q$ 里仅 $x(2x^2-1)a^4/12$ 从 $t^{24}$ 开始，其余项至少 $t^{25}$；$G_q$ 的首项为 $-xa^4/2$。

因此，完整原式准确给

$$
\boxed{
\mathcal H(q)(c-t)
=
\frac{a_0^4\,8^4\,7^4}{192\cdot25}
c(7c^2-5)t^{25}+O(t^{26}).
}
\tag{10}
$$

这个推导不需要把 R85/R88 的纯幂命题擅自推广成任意右 jet 消项。这里直接使用已完整分部后的 (8)；$O(t^9)$ 只进入 (10) 的更高项。

对 R198 冻结下降 step，$c=155\lambda$，且

$$
q(c-t)=-S(t/\lambda)
=-\frac{6435}{\lambda^8}t^8+O(t^9).
$$

只要 $c>1$，(10) 的首系数严格为正。因此存在下降带内部的 $x_0<c$，使

$$
\boxed{\mathcal H(q)(x_0)\ne0.}
\tag{11}
$$

可以先固定这个内点，再对整个 R183 step 作充分小的 C-infinity 平滑，并重补左方三个矩。式 (8) 对固定紧区间的有限阶 profile 数据连续；所选右点不读左补矩，故 (11) 保持。最终 f、g 是真正光滑、三矩配平且不可换基成不交的 R183 圆，q 是其同一个最右 g 下降资料。

本节只确定一个真实响应函数非零，未计算任一尚未指定路径的基准成本。

## 4. 一对 bulk 的完整成本对 N、t 的真实依赖

取一个固定的 M=0、frame $I\to I$ 的真实桥，从 $S_+$ 接到 $S_-$。在其内部同态端口插入 (3) 的第三环，使该内部桥第三 diagonal 增加 $t\tau_0$。再选固定 M=0、frame $I\to I$ 的返回桥，从 $S_-$ 回到 $S_+$。

在两者之间分别放 N 个正态完整圈及 N 个负态完整圈。N 为正整数。所有连接、内部环和返回桥先固定，不随 N 重新拟合。所得路径记为 $B_{N,t}$，其 scalar 首末为 $S_+$、frame 首末为 I，并有

$$
M_{B_{N,t}}=N\ell A-N\ell A=0.
$$

可在返回部分预置一座 R70 的正则八参数零矩桥，以便后文应用 R189；它的固定成本计入下式的 N 零次项。无需要求 $T_{B_{N,t}}=0$。

R70/R71 保全部桥历史的仿射公式准确给

$$
\boxed{
V_{-4}(B_{N,t};q)
=N\{\Gamma(q)+\ell t\mathcal H(q)\}+P_0(t;q).
}
\tag{12}
$$

$\Gamma$ 包含真实基准内部桥的第三算子以及两常态 drift。$P_0$ 包含全部连接、normal、mixed 和累计历史；它没有被设为零，也未宣称为偶函数。其与 N 无关来自全部桥 M=0 的完整仿射身份，不是把桥当作无成本。

在一个固定紧 t 区间、固定小环复制次数下，真实控制及 $P_0(t;q)$ 连续。

## 5. 用真实倒行消掉未知第三算子，而不丢第四成本

令 $B_{N,t}^R$ 为同 k 的真实倒行。对首末 frame I 的路径，准确 frame 公式为

$$
F^R(s)=D F(L-s)D,\qquad D=\operatorname{diag}(-1,1,-1);
$$

scalar k、h、omega 沿原路径反向取值。它仍为同 scalar 端口、frame 恒等路径。

因为 $M_{B_{N,t}}=0$，R83/R84 的真实传递给

$$
M_{B^R}=0,\qquad T_{B^R}=-T_B,\qquad V_{B^R}=V_B.
$$

因此

$$
\boxed{
D_{N,t}:=B_{N,t}B_{N,t}^R
\quad\text{有}\quad M=T=0,\quad
V_{-4}(D_{N,t};q)=2V_{-4}(B_{N,t};q).
}
\tag{13}
$$

这里没有把倒行当作第四负元。它恰将未知第三成本准确消掉，并将完整第四成本加倍。于是无需为任意变化的 $T_B$ 另作一个未知成本的第三校正。

## 6. 闭 hook 几何及四个有限设计中的非零实例

取 R180 的固定 hook prototype 和两个 R72 的 M=T=0 frame 桥。把 (13) 插入其中一个 prototype，再按 R180 的 Klein 八边词闭合。每种 prototype 在四个 ambient 左旋位置各出现一次；实际位移依新路径相消，而不是先指定单桥位移为零。

所得闭几何记作 $X_{N,t}$。其全部二阶矩阵为零、全部第三算子为同一个固定非零 $\kappa\mathfrak H$，与 N、t 无关。M=0 段之间的第四传递按真实加法，因此

$$
\boxed{
V_{-4}(X_{N,t};q)
=8N\{\Gamma(q)+\ell t\mathcal H(q)\}+C(t;q),
}
\tag{14}
$$

其中 C 包含 (12) 的完整基准和所有 hook/frame 桥成本。

选一个允许的 $t_0\ne0$。对 $N=1,2$ 及 $t=0,t_0$ 四个实际有限设计取混合差，全部基准严格消去：

$$
\boxed{\begin{aligned}
&V_{-4}(X_{2,t_0};q)-V_{-4}(X_{1,t_0};q)\\
&\quad-V_{-4}(X_{2,0};q)+V_{-4}(X_{1,0};q)
=8\ell t_0\mathcal H(q).
\end{aligned}}
\tag{15}
$$

在 (11) 的同一个 $x_0$，右侧非零。因此这四个真实几何中至少有一个满足 $V_{-4}(x_0)\ne0$。R198 的完整单 profile 成本是其 16 倍，所以对应 $\mathcal P_B(g)(x_0)\ne0$。

四份有限控制及全部辅助族先选定，再取一个能同时容纳它们的共同物理 I；重复完整圈不扩大 scalar 值域。可取足够大的 $\lambda$ 使冻结八包支撑落入 I、$c>1$，然后按 §3 固定同一个光滑圆和同一个 $x_0$。该选择没有将不同设计上的 profile 悄悄换成独立输入。

由 R198，对被选中的几何，不论允许的全 I 二阶 gauge $w_\theta$ 如何取值，也不论怎样加合法第三齐次解，其原第四 period 在 $x_0$ 都不能改变。因此其固定圆无法通过完整第四 range。

这是存在性排除。式 (15) 不指出四个未知基准中具体哪一个非零，也不声称它们全都非零。

## 7. 同一非零实例可迁移到无开常段几何

选定上述非零实例及光滑圆后，period 在固定 $x_0$ 的非零是一个真实有限评价，对足够高阶几何邻近连续。真实长度、frame 和全部 s 历史均包含在这个连续性中。

对 $B_{N,t}$ 使用预留的 R70 正则矩阵段，按 R189 任意精细地去掉其开常段，同时准确保 M=0、scalar/frame 端口及全平端 jets。新的第三算子可以变化；它无需单独固定，因为随后仍使用同一新 B 的真实倒行，(13) 自动继续给 M=T=0。

其余 hook 与 frame 构件按 R189 的有限真实词构造同步替换，保持最终非零 $\kappa\mathfrak H$。整个 Klein 词按新的实际位移重新准确闭合。取扰动充分小，原非零 period 值保持。

最终没有任何开常状态段，原光滑 f、g、右端单 step 和查询点保持不变。R183 的低阶论证仍适用，R198 的 gauge 不变量仍适用。所以也存在无开常段的真实闭 hook 几何，其同一固定圆不能由任何允许二阶/三阶 gauge 支付第四 period。

几何扰动会改变基础度量。正确结论是：先选定最终几何，再固定它自己的 $g_X+\varepsilon^2(dY_f)^2$，该固定目标失败。没有声称跨不同几何保持原目标度量。

## 8. 同一参数也能支付一个查询，不能据此否定所有几何

式 (14) 还给一个建设性、但有限的结论。固定 q、$x_0$，令 $H_0=\mathcal H(q)(x_0)\ne0$。由于

$$
V_{-4}(X_{N,t};q)(x_0)
=8N\{\Gamma(q)(x_0)+\ell tH_0\}+C(t;q)(x_0),
$$

取

$$
t_*=-\frac{\Gamma(q)(x_0)}{\ell H_0}.
$$

先固定覆盖 $[t_*-\epsilon,t_*+\epsilon]$ 的小环复制次数。各环 scalar/frame 每次复位，故任意有限 t 不扩大预先选择的小控制族 scalar 包络；共同 I 可先固定。此后 C 在该紧区间有界，且与 N 无关。

选择充分大的有限整数 N，使两个端点的线性项压过 C，则其查询值符号相反。连续性和介值定理给一个实际 $t_N$，准确满足

$$
V_{-4}(X_{N,t_N};q)(x_0)=0.
$$

同理可以取任意一个指定有限实查询值。没有将 C 删除，也没有仅用切向非零冒全局可达。

这一支付只针对一个查询。它不同时使下降段整个函数为零，不保证左侧 period 或 fourth ruling；零值也不能像 §7 的严格非零那样，仅凭开放性迁移到无常段几何。这里不宣称那一步已付。

因此，固定 step 的单点不存在普遍同号障碍。要支付 R198 的完整函数，仍须匹配整个纯成本的函数像；R196 的 universal 正字符本身不提供这一匹配，新的 pure 商结果与后续真实多查询控制也必须按各自已证明范围使用。本文没有构造完整第四解或有限等距族。

