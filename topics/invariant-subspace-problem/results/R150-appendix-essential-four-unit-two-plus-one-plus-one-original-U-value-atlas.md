# R150 附录：unit 2+1+1 的原 U 值坐标层及两条线性退化除子

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-347c-20261126 / unit31_general。日期：2026-11-26。

状态：本文的原 moment 完整值分层、全局 E0/N0 图、N(V) 线性身份及两条退化除子的覆盖已经完成，附短源实际执行成功。非零均值层尚未因此关闭；这些必要方程的抽象解尚未被认作原物理临界点。五坐标分式大展开没有被声称已执行完成。

## 1. 范围与原恒等式

沿用本课题已经登记的 unit 2+1+1 Frobenius 代数：

$$
\mathcal A=\mathbb C[\epsilon]/(\epsilon^2)\oplus\mathbb C\oplus\mathbb C,
\qquad
\tau(v)=av_0+v_1+bv_B+cv_C,\quad a=1-b-c,
$$

其中 $bc\ne0$，单位为 $\mathbf1=(1,0,1,1)$。原活动 Gram 矩阵是

$$
K=\begin{pmatrix}
0&0&p&q\\
0&A_1&r&s\\
p&r&0&t\\
q&s&t&0
\end{pmatrix}.
$$

本层此前已支付 $p=0$、$q=0$、$p=q$、$p=-q$、基点原最高值 $P_0=0$ 与 $m=0$。作同一个原 Gram／$U$ 齐次缩放令 $p=1$，保留

$$
q(q-1)(q+1)bcP_0m\ne0.
$$

这不是分别把 $p$ 与 $U_0$ 设为 $1$。始终有 $P_0=-U_0^3\ne0$，$U_0$ 保持隐含，其立方根及原物理几何均未被任意替换。

记

$$
V=U/U_0=(1,w,h,k),\qquad \lambda=m/U_0\ne0.
$$

原零点 mean、最高恒等式与第二梯度给

$$
\tau(V)=\lambda,\qquad \tau(V^2)=2\lambda^2,\qquad
P(V)=0,\qquad N(V)=0.
$$

由于 $P(v)=\tau((v-\tau(v)\mathbf1)^3)/2$，前三条等价于

$$
\tau(V)=\lambda,\qquad \tau(V^2)=2\lambda^2,\qquad
\tau(V^3)=4\lambda^3. \tag{1}
$$

原四个活动最高及第二梯度值仍须完整保留：

$$
P_1=3wP_0,\quad P_B=h^3P_0,\quad P_C=k^3P_0,
$$

$$
N_0=\lambda P_0,\quad N_1=2\lambda wP_0,\quad
N_B=\lambda h^2P_0,\quad N_C=\lambda k^2P_0. \tag{2}
$$

其中 $P_1,N_1$ 是原双点的一阶 germ 系数，绝非把第二行当成独立简单点后取其基值。

## 2. 完整的值碰撞分层

设

$$
A_\lambda=2\lambda^2-2\lambda+1,\qquad
B_\lambda=4\lambda^3-6\lambda^2+3\lambda-1.
$$

消掉 $w$，(1) 等价于

$$
b(h-1)^2+c(k-1)^2=A_\lambda,\qquad
b(h-1)^3+c(k-1)^3=B_\lambda, \tag{3}
$$

以及 $w=\lambda-a-bh-ck$。又

$$
B_\lambda=(2\lambda-1)A_\lambda-\lambda,\qquad
\gcd(A_\lambda,B_\lambda)=1. \tag{4}
$$

### 2.1 三值互异图

在 $(h-1)(k-1)(h-k)\ne0$ 上，

$$
b=\frac{B_\lambda-(k-1)A_\lambda}{(h-1)^2(h-k)},\qquad
c=\frac{(h-1)A_\lambda-B_\lambda}{(k-1)^2(h-k)}. \tag{5}
$$

这里没有除以 $A_\lambda$ 或 $B_\lambda$；它们各自的零纤维保留在本图内。原条件 $b,c\ne0$ 要求两个对应分子非零。

### 2.2 值碰撞图

若 $h=1$，则 $k\ne1$，(3) 强制 $A_\lambda B_\lambda\ne0$。定义

$$
v=\frac{\lambda(2\lambda-1)^2}{A_\lambda},\qquad
C=\frac{A_\lambda^3}{B_\lambda^2},\qquad
w_c=\frac{\lambda^2(1-2\lambda)}{B_\lambda}. \tag{6}
$$

则本图精确为 $k=v,c=C,w=w_c$，$b$ 自由；仍需 $bc\ne0$。$k=1$ 图为其交换：$h=v,b=C,w=w_c$，$c$ 自由。若 $h=k\ne1$，则精确为 $h=k=v,b+c=C,w=w_c$，保留一个自由权重。$h=k=1$ 会强制 $A_\lambda=B_\lambda=0$，由 (4) 不可能。

因此 (5) 与三个碰撞图完整覆盖原 moment 层；不存在被除去而未支付的值碰撞。

## 3. 原 N(V) 是非平凡的线性约束

沿用原定义

$$
d=D_K\mathbf1,\quad f=\tau(d)/2,
$$

$$
N(v)=\tfrac12\tau((d-f\mathbf1)v^2)
-\tau(v)\tau(dv)+f\tau(v)^2+\tfrac14\tau(vD_Kv).
$$

在 (1) 下，所有显式 $f$ 项合并抵消：

$$
4N(V)=2\tau(dV^2)-4\lambda\tau(dV)+\tau(VD_KV).
$$

设 $C(z)=1+z+z^2-2\lambda(1+z)$。直接按原代数乘法展开，得到

$$
\begin{aligned}
4N(V)={}&(3-4\lambda)A_1+2bC(h)r+2cC(k)s\\
&+2bc\{h^2+hk+k^2-2\lambda(h+k)\}t\\
&+2b\{aC(h)+w(2+h-2\lambda)\}\\
&+2cq\{aC(k)+w(2+k-2\lambda)\}. \tag{7}
\end{aligned}
$$

这是同一原 Gram 参数上的线性等式，不是一个替代范数条件。其线性形式在 moment 层上不会恒零：$\lambda\ne3/4$ 时 $A_1$ 系数非零。若 $\lambda=3/4$，则 $C(z)=(z-1)(z+1/2)$。若 $r,s$ 两个系数亦零，因 $bc\ne0$，$h-1,k-1$ 均属于 $\{0,-3/2\}$，(3) 会给 $B_\lambda=-3A_\lambda/2$；但在 $\lambda=3/4$ 处 $B_\lambda+3A_\lambda/2=1/2$。故原线性形式始终非平凡。

这一论断只给出原线性约束的有效覆盖；在再代入 mean 图后，新的系数退化仍须按下节单独保留。

## 4. 全局原 E0/N0 图与降到五个坐标

设

$$
u=b+cq,\qquad V_2=b+cq^2,\qquad
P_0=P(0,0,1,q),
$$

$$
W_1=V_2/2-u^2+2fu,
$$

$$
W_2=uV_2-2u^3+f(V_2+2u^2)-bcqt+2\lambda P_0.
$$

定义

$$
x=\frac{qW_1-W_2}{b(q-1)},\qquad
y=\frac{W_2-W_1}{cq(q-1)},
$$

$$
r=x-a-ct,\quad s=y-aq-bt,\quad
A_1=2f-2bx-2cy+2bct. \tag{8}
$$

(8) 精确且全局解掉原 $E_0=0,N_0=\lambda P_0$，并满足原 $f=\tau(d)/2$。它仅除以已知非零的 $bcq(q-1)$。

代入 (7) 后，$N(V)$ 对 $f,t$ 仿射：

$$
N(V)=A_f f+A_t t+C_0,\qquad
A_t=\frac{bc}{2(q-1)}LS, \tag{9}
$$

其中

$$
L=q(h-1)-(k-1),\qquad S=h+k+1-2\lambda. \tag{10}
$$

在三值互异图与 $LS\ne0$ 上，

$$
t=-\frac{A_f f+C_0}{A_t}.
$$

由 (5)、(8)、(9)，剩余变量只有 $(f,q,\lambda,h,k)$。仍保留全部九条原条件：

$$
E_1=E_B=E_C=0,
$$

$$
P_1-3wP_0=P_B-h^3P_0=P_C-k^3P_0=0,
$$

$$
N_1-2\lambda wP_0=N_B-\lambda h^2P_0=N_C-\lambda k^2P_0=0. \tag{11}
$$

附短源在原 Gram 坐标中按原 Frobenius 运算生成完整 (11)，并逐式核对本节所用变换；它不把必要结式的解当成充分，也不声称五坐标分式大展开已经完成。分母只来自

$$
\lambda q(q-1)(q+1)(h-1)(k-1)(h-k)bcP_0LS
$$

的非零因子；其中 $u\ne0$ 如沿用已登记层，也保持原必要条件。此处没有声称图像自身空，也没有声称任意抽象解可以在固定物理 Gram 核上实现。

## 5. L=0 的完整线性退化分层

所有值碰撞图都满足 $L\ne0$：在 $h=1$ 图，$L=-(k-1)$；在 $k=1$ 图，$L=q(h-1)$；在 $h=k=v$ 图，$L=(q-1)(v-1)$。

故 $L=0$ 必在三值互异图中。写

$$
h=1+\rho,\qquad k=1+\rho q,\qquad \rho\ne0,
$$

则

$$
V=\mathbf1+\rho k_0+w\epsilon,\qquad k_0=(0,0,1,q).
$$

直接极化原 $N$，并用 $E_0=0$，得到

$$
N(\mathbf1)=0,\quad N(\epsilon)=f-u,
$$

$$
N(\mathbf1,k_0)=\frac{V_2-2u^2}{4},\quad
N(\mathbf1,\epsilon)=u/2-f,\quad N(k_0,\epsilon)=0,
$$

其中 $N(v,z)=N(v+z)-N(v)-N(z)$。因此

$$
N(V)=w(w-1)f+u(w/2-w^2)
+\frac{\rho(V_2-2u^2)}4+\lambda\rho^2P_0. \tag{12}
$$

- $w=0$ 时，$P$ 的平移不变性给 $P(V)=\rho^3P_0\ne0$，故此面已排。
- $w\ne0,1$ 时，(12) 全局解 $f$，保留 $t$ 与全部 (11)。
- $w=1$ 时，令 $R=\rho u=\lambda-2$。原 moment 给 $\rho^2V_2=A_\lambda$。原 $P(V)=0$ 给 $\rho^3P_0=6\lambda-11/2$，而 (12) 乘以 $4\rho$ 给 $4\lambda\rho^3P_0+4\lambda-3=0$。故必须

$$
8\lambda^2-6\lambda-1=0. \tag{13}
$$

这两个代数 $\lambda$ 纤维仍须回原方程排除，不因得到 (13) 就宣布其空。

(13) 上还可无遗漏地再消去 $q$。由 $V_3=(1+q)V_2-qu$ 与第三矩，

$$
q=\frac{B_\lambda-\rho A_\lambda}
{\rho(A_\lambda-\rho(\lambda-2))}. \tag{14}
$$

分母零的可能已支付：$\rho\ne0$，$\lambda-2\ne0$；若 $A_\lambda-\rho(\lambda-2)=0$，原未除式要求 $(\lambda-2)B_\lambda-A_\lambda^2=0$。模 (13)，

$$
A_\lambda=(5-2\lambda)/4,\quad
B_\lambda=(10\lambda-11)/8,\quad
(\lambda-2)B_\lambda-A_\lambda^2=3(7-10\lambda)/16\ne0.
$$

因而 (14) 全局成立。最后

$$
u=(\lambda-2)/\rho,\quad V_2=A_\lambda/\rho^2,
$$

$$
b=\frac{qu-V_2}{q-1},\qquad c=\frac{V_2-u}{q(q-1)}.
$$

本奇异面只余二次数域上的 $(\rho,f,t)$ 三坐标与全部 (11)，仍保留 $q(q-1)(q+1)bcP_0\ne0$。

## 6. S=0 的原式简化及未关闭面

在 $S=0$ 上，令 $z=(h-1)(k-1)$、$T=h+k+hk$。有

$$
C(h)=C(k)=h^2+hk+k^2-2\lambda(h+k)=-T.
$$

利用原 $2f=A_1+2au+2br+2cs+2bct$，(7) 精确化为

$$
4N(V)=zA_1-2Tf-2w\{b(k-1)+cq(h-1)\}. \tag{15}
$$

在 (8) 上，$A_1$ 实际不含 $t$；若 $l=b+c$，则

$$
A_1=
2\left(1-l-\frac{u(q+1-2u)}q\right)f
+\frac{(2u-q-1)(V_2-2u^2)+4\lambda P_0}{q}. \tag{16}
$$

故 $S=0$ 的 $f$ 系数为

$$
A_f=\frac12\left[3-4\lambda
-z\left(l+\frac{u(q+1-2u)}q\right)\right]. \tag{17}
$$

$A_f\ne0$ 时可全局解 $f$，仍保留 $t$ 和 (11)。$A_f=0$ 时必须同时保留 (15) 的常数项；此分支尚未被排除，不能默认为一般图所覆盖。其系数零式可写成低次形式

$$
(3-4\lambda)q
-z\{b(1-2b)+(2l-4bc)q+c(1-2c)q^2\}=0. \tag{18}
$$

值碰撞与 $S=0$ 的交面进一步只有低次 $\lambda$ 纤维：

$$
h=1\ \text{或}\ k=1:\qquad
S=\frac{4\lambda^2-5\lambda+2}{A_\lambda},
$$

$$
h=k:\qquad
S=\frac{(2\lambda-1)(2\lambda^2-1)}{A_\lambda}. \tag{19}
$$

碰撞图已知 $A_\lambda B_\lambda\ne0$，故 (19) 的分母没有新增例外。这些有限 $\lambda$ 纤维仍保留全部原式。

## 7. 已执行短源与失败大展开的严格区别

[成功短源](../notes/2026-11-26-unit211-U-value-small-identities-347c.py)及[实际小回执](../notes/2026-11-26-unit211-U-value-atlas-completed-execution-347c.json)分别固定原输入和实际执行。

冻结源 blob：91fad0d4be319fe57760ac51f7ee2a6b448bbb5a。源码 SHA256：da790bddccce690e0e12cbe3941b6c02c2912319f646c5195834408b4bde965f；5889 bytes。依赖 Python 3.12、SymPy 1.14.0。

该短源直接在原独立 Gram 坐标中核对原 N/P/mean 恒等式；E0/N0 的 Cramer 图只使用低次、已清分母的标量身份。它完整核对 (3)--(9)、S=0 身份以及 L=0 的所有极化 germ 身份，并在原坐标中逐个生成 (11) 的九个原多项式，没有将 f,t 混入七变量分式后每步执行大 gcd。

实际成功身份：

- 公开 Actions run 45803350694，job 139852028816。
- 冻结源提交 31ec7ed7c882830bd16e320a111f93f8ef161c67。
- 源内计时 0.568990 秒，峰值 RSS 70884 KiB；驱动计时 0.871005685 秒，退出码 0。
- 原九式输入 SHA256：943079b018af336d8ddfd4a4d993e4095cc90a83edc972f92ca5f1eda4894e1d。
- stdout SHA256：a208e272b4d18051e4dddf7abc400dd890ea327387a4a07fd1deb260fc2f63df。
- 最终状态 all_original_identity_and_complete_value_atlas_checks_pass。
- 最终输出明确 fiveCoordinateExpansionGenerated=false、claimPhysicalSufficiency=false、claimLambdaLayerEmpty=false、ordinaryISPClaim=false。

原七变量大展开源 notes/2026-11-26-unit211-original-U-value-atlas-347c.py 的身份必须另外保留：blob aaa168ba151ca11e93c4638fce4658882d8f41ce，SHA256 036a62de41e70d397a308c593e2c9f10ce29c5da9f8e684612f2bd6fc7fc6a9d，7680 bytes。其实际 run 45799548882 / job 139838879577 于 wall_time_limit 停止，驱动计时 900.828876020 秒，退出码 -9，峰值 RSS 3443656 KiB，stdout 0 bytes，stdout SHA256 为 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855。该执行没有输出任何已完成的五坐标展开结果，不能从运行中曾进入哪个阶段作推测。

短源的成功证明本附录所写的原身份与分层；它不冒充失败大展开的成功回执。后续稀疏 f 系数生成亦有自己的源及执行身份。任何必要坐标图均不能代替原物理实现条件，几何排除也不能被误当作全局幂身份。
