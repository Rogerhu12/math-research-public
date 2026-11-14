# R180 — 全函数端值 primitive 的准确径向相消与材料角漂移

本结果给 R125 一个无需拟合、无需截断端点角函数的具体 primitive。它针对 R173 已明确定义的完整实际场及准确物理目标；在计算余项时先消去 $n_s,m_s$，保留正确的材料角漂移和全部 Gauss 作用。该恒等式本身不要求 Gauss 或 Codazzi 已解，不把当前坏场宣称为合格候选。

## 1. 明确坐标和完整对象

在一个准确物理子区间 $s\in[a,b]$ 上，设旋转目标为
$g=ds^2+A(s)^2du^2$，其中 $A>0$。为避免本节端点 $a$ 与半径混淆，半径写作 $A$。完整实际第二基本形式记为 $(n,m,l)$。计算角为 $\xi$，材料角是准确固定 atlas

$$
u=U(s,\xi),\qquad U_\xi>0,\qquad
\omega=\frac{U_s}{U_\xi}.
\tag{1}
$$

原生字段为材料字段与 $U$ 的完整复合。因此

$$
\partial_s|_u=\partial_s|_\xi-\omega\,\partial_\xi,
\qquad
\partial_u=\frac1{U_\xi}\partial_\xi.
\tag{2}
$$

允许 R149/R141 的分片径向 atlas：$U$ 及角一、二 jet 具有共同迹，而 $U_s$ 可跳。下面恒等式在各片内部成立；若完整字段具有声明的共同值/角迹，分片拼合不产生跳跃测度项。

定义实际三缺陷和 R119 forcing：

$$
\begin{aligned}
G&=nl-m^2-K,\qquad K=-A_{ss}/A,\\
R_n&=n_s|_u-m_u/A-(A_s/A)(l-n),\\
R_m&=m_s|_u-l_u/A+2(A_s/A)m,\\
H&=(-A R_n,\ A R_m,\ -A G),\qquad
\alpha=(m,-l,0).
\end{aligned}
\tag{3}
$$

这些是完整实际字段；raw、seed/reference/tail lifting、R153 和 R155 的所有项都包括在内，不能只对 raw 代入后遗失 nonlinear lifting。

## 2. 由端点全角函数准确确定 $q$

令

$$
v(s,\xi)=(-A(s)n(s,\xi),\ A(s)m(s,\xi),\ 0),
\qquad
T=(m_u+A_s l,\ -l_u+A_s m,\ -A G).
\tag{4}
$$

直接对 $v$ 求物理径向导数并代入 (3)，得到准确恒等式

$$
H=\partial_s|_u v+T.
\tag{5}
$$

例如第一分量为
$(-A n)_s|_u+m_u+A_s l
=-A n_s|_u+m_u+A_s(l-n)$；第二分量同理。

令 $\ell=b-a$、$t=(s-a)/\ell$，取**同一固定 native $\xi$** 下的两端完整函数

$$
v_a(\xi)=v(a,\xi),\qquad v_b(\xi)=v(b,\xi),\qquad
L_v(s,\xi)=(1-t)v_a(\xi)+t v_b(\xi),
\tag{6}
$$

并定义

$$
q=v-L_v,\qquad M=\frac{v_b-v_a}{\ell}.
\tag{7}
$$

端点不是有限角样本，也不是把相同 $\xi$ 错认成相同材料角：$v_a$ 和 $v_b$ 分别包含 $U(a,\xi),U(b,\xi)$ 的准确复合。它们是由绑定实际场确定的完整周期函数。故逐角准确成立

$$
q(a,\xi)=q(b,\xi)=0,\qquad
q_\xi(a,\xi)=q_\xi(b,\xi)=0.
\tag{8}
$$

因为 $\ell$ 与角无关，

$$
(L_v)_\xi=(1-t)(v_a)_\xi+t(v_b)_\xi.
\tag{9}
$$

准确末格的 $\ell$ 是 R171/R172 定义的 $S-b_{\rm saved}$；Arb 端点只用于包围，不能以其中点重新定义 $\ell$。

## 3. 漂移符号和完整 R125 剩余

固定材料角求导时，(2)、(6) 给出

$$
\partial_s|_u L_v=M-\omega(L_v)_\xi.
$$

因此由 (5)–(7)，

$$
\partial_s|_u q
=H-T-M+\omega(L_v)_\xi,
$$

即

$$
H-\partial_s|_u q
=M+T-\omega(L_v)_\xi.
\tag{10}
$$

令 $\widehat q$ 表示叉乘矩阵，沿用 R125 的改变量
$\widetilde D=D-F\widehat q$。R119 的实际 frame/error 方程为

$$
F_s=F\widehat\alpha,\qquad
D_s=D\widehat\alpha+F\widehat H.
$$

按固定材料角对 $\widetilde D$ 求导，使用
$[\widehat q,\widehat\alpha]=\widehat{q\times\alpha}$，得

$$
\widetilde D_s
=\widetilde D\,\widehat\alpha+F\widehat E,
\qquad
\boxed{E=M+T-\omega(L_v)_\xi+q\times\alpha.}
\tag{11}
$$

这证明余项中漂移项的符号是负号，作用于端点插值 $L_v$ 的角导。它不是 $+\omega(L_v)_\xi$，也不能在非恒等 atlas 中删去。

等价地，若仍按原 R125 写法计算
$E=H-q_s|_\xi+\omega q_\xi+q\times\alpha$，则
$q_s|_\xi=v_s|_\xi-M$、$q_\xi=v_\xi-(L_v)_\xi$，包含 $v_\xi$ 的两项准确相消，得到 (11)。所以程序不必先给 $n_s,m_s$ 一个宽区间再相减；(11) 只需要完整值、角一导、$A,A_s,A_{ss}$、真实 $U_s,U_\xi$ 和完整端点角函数。

## 4. Gauss 第三分量的进一步准确相消

本结果没有假定 $G=0$。因为 $v_3=(L_v)_3=q_3=\alpha_3=0$，叉乘只影响第三分量。由 (4)，

$$
(v\times\alpha)_3
=(-A n)(-l)-(A m)m=A(nl-m^2).
$$

因此在整个实际字段上，无论 Gauss 是否满足，

$$
\begin{aligned}
E_3
&=-A G+(q\times\alpha)_3\\
&=-A(nl-m^2-K)+A(nl-m^2)-(L_v\times\alpha)_3\\
&=A K-(L_v\times\alpha)_3\\
&=\boxed{-A_{ss}+(L_v)_1l+(L_v)_2m}.
\end{aligned}
\tag{12}
$$

式 (12) 保留了完整 Gauss 作用。它只是先做同一有限表达式的准确消元，不是把 solver 的 Gauss 行投影为零。若某盒确处于 R153 或 R155 的准确平台，原表达式可以另用已证明的 $G=0$；两种合法包围可取交集的向外包围，哪个更窄取决于实际盒及其相关性。

式 (12) 也解释为何在 $G=0$ 平台上原 $q\times\alpha$ 有时更好：$q$ 可能很小，而把它展开为较大的端点项会增加区间依赖。本条不预先声称代数展开必然收紧每个盒。

## 5. 端点、分片和退化 cut 的作用域

在每个端点，(8) 对整个角函数是恒等式。实际接口具有共同的值和角迹，故左/右片选择只改变各自内部的径向导数，不改变准确 $q=0$ 的端点值。沿固定材料角路径，$\xi(s,u)$ 连续；于是 $q$ 连续且分片绝对连续，(10) 可逐片积分，无额外跳跃项。

当前完整准确消费者使用 R173 的 saved P1 单元，完整 atlas 和窗口作为准确函数消费；没有重新拟合或改变保存场。碰到未能证明的 R153 分母或 R155 平方根盒仍返回未决，不能借本恒等式跳过字段存在性条件。

对 R172 准确末格，右端 $v_b$ 用准确 R132/R170 tail 的值和角一导定义。它不需要 cut 的径向 II jet。R174 给该处的真实值/角一阶迹；R178 可另付一侧第一阶 forcing 的积分。因此本构造没有增加 cut 正 $n$、全局 $C^3$ 或 $II_{uu}$ 一致有界要求。

当前代码仍沿完整 interval field 的明确作用域返回：一般 touching-cut 盒若没有相应内部导数包围，保持未决。端点代数式可使用准确角迹，但不把这种端点求值冒充整末格连续证明，也不据此赋 $E_s$、$n_s$ 或 $l_s$。

## 6. 与原后验累计的接合

因 $q$ 在两端为零，$D$ 与 $\widetilde D$ 在每段起点和终点相同。右乘 skew flow 保持算子范数，故若段首实际 $\|D\|\le d_a$，

$$
\|D(b)\|\le d_a+\int_a^b\|E(s)\|\,ds.
\tag{13}
$$

位置相容误差仍满足
$C_s=D\mathbf e_1=\widetilde D\mathbf e_1+F\widehat q\,\mathbf e_1$，
其中 $\mathbf e_1=(1,0,0)^T$ 是坐标向量。因此

$$
\sup_{s\in[a,b]}|C(s)|
\le c_a+\ell d_a+
 \int_a^b(b-r)\|E(r)\|\,dr+
 \int_a^b|q(r)\times\mathbf e_1|\,dr.
\tag{14}
$$

当前 $q_3=0$，所以最后一项的被积函数为 $|q_2|$；消费者使用一般向量范数 $\|(q_2,q_3)\|$。这项不能因 $q$ 两端为零而删掉。

(13)–(14) 可逐段累积，与 R125 已有一般 primitive 框架完全一致。它们只是一种准确的误差分配，不保证任意 primitive 的预算优于原 $\int\|H\|$。实际前段初值、全盒覆盖和几何/seam 仍须分别支付。

## 7. 明确程序接口

[fd2d_gc_connection_endpoint_primitive.py](../scripts/fd2d_gc_connection_endpoint_primitive.py) 定义 ExactConnectionEndpointPrimitive(field, cell)。构造器绑定完整 accurate-domain schema、字段内容 binding 和准确 cell definition。它缓存的是某一准确角盒的完整两端函数包围，键包含准确角端点及单位；没有近邻缓存或截断角谱。

box(field, tlo, thi, alo, ahi) 使用归一化真实物理标签，返回 $q,q_\xi,M,L_v,(L_v)_\xi,T,E$ 的全盒包含。$E$ 的实现不消费 $n_s,m_s$。当标签准确等于 0 或 1 时，$q,q_\xi$ 由 (8) 准确置零；这不是小值阈值或浮点吸附。

源码 SHA256 为 2a5f3e966751f787ce53bb7ee420cfc3480be78e925fe16ab203965a15f3931b。

[fd2d_gc_connection_primitive_gauss_reduction.py](../scripts/fd2d_gc_connection_primitive_gauss_reduction.py) 的 reduce_gauss_component 消费已求出的同一 packet，按 (12) 给另一合法第三分量包围，再用两区间交集端点向外包围。它不重新求场、不改变 $q$ 或目标；绑定原 source SHA 和自身 enclosure source。交集装入 Arb ball 时半径仍可能再次外舍入，代码和报告均不把它声称为严格单调缩小的浮点宽度。

## 8. 实际非零单 cell 和真实大余项

实际输入为 dyadic30 archive 3bceef937899fad65e512e56d3bd747a6d225b20301b64ed9d04582a4f6db981，以及其准确新 $\delta$ packet a6215af63b98cc8409faf9dbb46c039f86c1ef9e9bc6fedacdd62514ba3dcb5a。所有原 source/数组保持。

第一检查进程 session 97962，首块 8698bb、末块 65bbb7，真实 exit 0；耗时 0.47681855800328776 秒、峰 RSS 95196 KiB。其 [实际 report](../notes/2026-11-12-fd2d-metric-dyadic30-connection-primitive-R180-01-report.json) 绑定 cell 69。

在 $t=1/2,\ \xi$ 为保存的 binary64 .78 时，严格区间证明

$$
q_1\approx0.0066787498313066,\qquad
q_2\approx0.000514347087374704,\qquad q_3=0.
$$

所以本次不是零函数的形式测试。两端 $q,q_\xi$ 都准确为零。原完整径向公式
$H-q_s|_\xi+\omega q_\xi+q\times\alpha$
与 (11) 的三个差分区间均包含 0；实际漂移约 0.2102507081，不能忽略。

该点 $\|H\|$ 上界约 0.3618980941，所选 endpoint primitive 的 $\|E\|$ 上界约 0.3833924140。一个真正正宽连续矩形给
$\|E\|\le0.3848334033$、$\|q\|\le0.00677974351$。因此本次没有声称该 primitive 使这个坏场的预算更小，更没有冒称全域 metric 已过。

第二个小检查仅消费同一矩形的第三分量表达，session 11063，首块 390364、末块 d80293，真实 exit 0；耗时 0.49855672500416404 秒、峰 RSS 93776 KiB。其 [实际 report](../notes/2026-11-12-fd2d-metric-dyadic30-connection-primitive-reduced-R180-01-report.json) 保留两种合法包围：

- 原平台 $G=0$ 与 $q\times\alpha$ 方式约为 $[0.00140883169669,\ 0.00147054076657]$；
- (12) 展开式约为 $[0.00134852136317,\ 0.00153085280896]$。

此例原式更窄；交集端点再装为 Arb ball 产生约 $5.7\cdot10^{-14}$ 的外舍入膨胀，报告如实保留，没有把舍入宽度变化解释为数学错误或改进。它只验证可交换使用的准确表达和完整来源身份。

## 9. 重做与后续消费

在本课题目录，以新输出 stem 运行：

~~~sh
PYTHONPATH=/workspace/scratch/fd2d-recovered-deps/python-flint-0.9.0 \
python scripts/fd2d-metric-connection-endpoint-primitive-check.py \
  --native-definition notes/2026-11-12-fd2d-dyadic-tail-accurate-last-cell-30-01-native-definition.json \
  --profile-packet notes/2026-11-12-fd2d-metric-dyadic30-accurate-profile-rebind-02-packet.json.gz \
  --out-prefix notes/2026-11-12-fd2d-metric-connection-primitive-R180-replay
~~~

独立第三分量包围检查用同样三项参数调用 scripts/fd2d-metric-connection-primitive-reduced-check.py，并选择另一输出 stem。

本结果的新内容是可直接消费的全函数端值选择、正确负漂移项和第三分量准确消元。它服务后续真实后验计算；没有进行坏场 whole-body 认证、额外 BVP 或大矩阵核验，也没有把单 cell 的连续盒扩称成全域证书。

