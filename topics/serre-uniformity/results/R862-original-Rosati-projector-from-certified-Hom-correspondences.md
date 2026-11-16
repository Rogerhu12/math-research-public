# R862：由原七个 Hom 对应构造同一 Rosati 投影与准确整数分母

日期：2026-11-16。状态：**本篇证明一个可直接消费已成 R791 数据的有限构造；尚未执行新的范数多项式算术。** 新对象是原 $J_X$ 上同一个 $A$ 因子的 Rosati 投影、其一个明确整数倍，以及实际有限对应的组合。它不替换原 $Y$ 上的活跃 Hecke 投影，不计算非 $p$ 高度或原完整高度。

## 1. 已有输入与两种不能混用的投影

保持原 $p=41$、$X=X_1$、$Y=W_{41}$、$\phi:X\to Y$、原基点 $c_0,c_1$、原商
$$
q:J_X\longrightarrow A,
\qquad \kappa=qq^\dagger.
\tag{862.1}
$$
adjoint 使用原极化，不将 $\kappa$ 设为一。

[R791](R791-certified-original-Hom-descent-and-eta-inputs.md) 已经给原 $f=f_4$、$f_R=[1-\zeta^2]f$，以及真实 $\mathbf Q$ 同态
$$
q_R:J_X\longrightarrow
B=\operatorname{Res}_{L^+/\mathbf Q}C,\qquad
q_R=vq.
\tag{862.2}
$$
其像是 R728 的原六维本原因子；$B$ 的剩余第七维未混入。$B$ 使用该来源的分量 theta 极化。记
$$
M_v=v^\dagger v,\qquad
a_A=\kappa M_v\in F,\qquad
F=\mathbf Q[S]/(\Psi_{21}(S)),
\tag{862.3}
$$
其中
$$
\Psi_{21}(S)=S^6-S^5-6S^4+6S^3+8S^2-8S+1.
\tag{862.4}
$$
本文用 $a_A$ 指 R791 的 (791R.8) 式中的元素 $e$，避免与 YP 的 $e_\eta$ 混名。

原实际坐标是
$$
a_A=3870+711s_1-801s_2-360s_3+612s_4+864s_5,
\qquad s_j=t^j+t^{-j},\quad S=s_1.
\tag{862.5}
$$
这些是已完成的数据。本文不重新求 Hom 格、Gram、原 Galois 矩阵或这些六坐标。

本篇目标为
$$
\varepsilon_A=q^\dagger\kappa^{-1}q
\in\operatorname{End}_{\mathbf Q}^0(J_X).
\tag{862.6}
$$
YP 所需的 $e_\eta\in\operatorname{End}_{\mathbf Q}^0(J_Y)$ 是另一对象：它由原五个 $\eta_{h_j}$ 的实际活跃等型块定义。二者没有可省略的识别。

## 2. 一个已经有真实映射来源的整对应

定义
$$
\mathcal D_A=q_R^\dagger q_R
             =q^\dagger M_vq
\in\operatorname{End}_{\mathbf Q}(J_X).
\tag{862.7}
$$
$q_R$ 是原整数 Hom 映射形成的 Weil restriction 同态，$J_X$ 与 $B$ 的此处极化均为指定的主极化，故其 adjoint 及 (862.7) 是实际整同态。此断言不要求原 $A$ 的极化为主，也不将 $v^{-1}$ 当作整同态。

在包含七个实域嵌入的共同原域上，令 $h_\tau=\tau(f_R):X\to C_{\tau(b)}$。则
$$
\boxed{\quad
\mathcal D_A=\sum_{\tau:L^+\hookrightarrow\overline{\mathbf Q}}
                   h_\tau^*h_{\tau,*}.
\quad}
\tag{862.8}
$$
这里 $h_{\tau,*}:J_X\to C_{\tau(b)}$ 是由 $c_0\mapsto O$ 归一的原映射，$h_\tau^*$ 是其原主极化 adjoint。若使用同靶表示，可换成 $\mathcal T^j f_R$，$0\le j\le6$；原 $\rho_j$ 的靶同构保持 $[O]$ 和主极化，故不改变 pull–push。必须保留 $\mathcal T^7=[\zeta^2]$，不能把原 Galois 作用改为无相位的周期。

每个 pull–push 可由纤维积对应
$$
X\times_{C_{\tau(b)}}X
\tag{862.9}
$$
的循环实现，保各分支重数。固定其算子方向为“第二因子推前到 $C$，再向第一因子拉回”，以此定义 (862.8)；不靠未校准的 Poincaré 除子符号猜算子正负。纤维积的两个投影有限，有限对应的和及复合仍是有限对应的整线性组合。

R791 的十二阶矩阵 kappa_times_vdagger_v_Hom_matrix 正是从这七个原 pull–push 恢复的作用；其计算逐项保留原次数 Hermitian 配对。由于 (862.7) 定义于 $\mathbf Q$，七个分量的和已经具有真实下降，不能单取一个分量称作有理对应。

R849 的完整 U.1 全局源及 R850 的原实下降提供 (862.9) 的可消费映射表达式。这里引用的是原全局映射；四个 CM 点响应不足以定义 (862.9)。

## 3. 范数多项式给原投影

取原六次域中的特征多项式
$$
P_A(X)=\operatorname{Norm}_{F/\mathbf Q}(X-a_A)
 =X^6+c_5X^5+\cdots+c_1X+c_0.
\tag{862.10}
$$
它可以由 $F$ 的固定基 $1,S,\ldots,S^5$ 上的六阶乘法矩阵计算；不要求先证明 $a_A$ 生成整个 $F$。

**命题 862.1。** $c_i\in\mathbf Z$，$c_0>0$，且
$$
\boxed{\quad
\varepsilon_A=1-\frac{P_A(\mathcal D_A)}{c_0}.
\quad}
\tag{862.11}
$$
因此，令
$$
d_A=c_0,\qquad
F_A=-\bigl(\mathcal D_A^6+c_5\mathcal D_A^5+
                    \cdots+c_1\mathcal D_A\bigr),
\tag{862.12}
$$
便有
$$
F_A=d_A\varepsilon_A,\qquad
F_A^2=d_AF_A,\qquad F_A^\dagger=F_A.
\tag{862.13}
$$
$d_A$ 是一个具体正整数整化分母，不声称最小。

**证明。** (862.5) 是实圆分整数的整线性组合，所以 $a_A$ 是代数整数，(862.10) 为首一整系数多项式。$\kappa$ 与 $M_v$ 是同一全实域中的 Rosati 正元素；它们交换，且 $v$ 在原 $A$ 上是同源，所以 $a_A$ 在全部实嵌入下严格为正。因此
$$
c_0=(-1)^6\operatorname{Norm}_{F/\mathbf Q}(a_A)>0.
$$

在有理同态范畴中，(862.6) 给
$$
J_X\sim \operatorname{im}(q^\dagger)\times\ker(q)^0,
\tag{862.14}
$$
并在第一因子恒等、第二因子为零。由 $\kappa M_v=M_v\kappa$，
$$
\mathcal D_Aq^\dagger=q^\dagger M_v\kappa=q^\dagger a_A,
\qquad \mathcal D_A|_{\ker(q)^0}=0.
\tag{862.15}
$$
所以 $P_A(\mathcal D_A)$ 在第一因子为零，在第二因子为 $c_0$。这证明 (862.11)，包括整个 $J_X$ 上的等式，不只是十二个原 Hom 上的乘回。

从 (862.11) 展开并取消常数项就得 (862.12)。它是整对应 (862.8) 的整系数多项式，故是实际整同态。原 $\varepsilon_A^2=\varepsilon_A=\varepsilon_A^\dagger$ 给 (862.13)。特征零阿贝尔簇的 Hom 无整数挠，所以这些等式同时是实际整同态等式。$\square$

此证明保留了真实 $\kappa$ 与 $M_v$。它没有将 $q_R$ 当作极化同构，也没有从 $\deg f_R$ 除一个未经证明的共同标量来形成投影。

## 4. 同原标记与已有矩阵的准确衔接

R791 保存的原 $\mathcal T$ 矩阵满足
$$
T^7=J^2,\qquad T^{21}=I,\qquad
J^2+J+I=0,\qquad \Phi_{21}(T)=0.
\tag{862.16}
$$
可按旧真矩阵中 $S=T+T^{-1}$ 的作用核对 (862.5)。令 $E$ 为旧 kappa_times_vdagger_v_Hom_matrix，新消费者只需附加
$$
P_A(E)=0,\qquad
-\bigl(E^6+c_5E^5+\cdots+c_1E\bigr)=d_AI_{12}.
\tag{862.17}
$$
这给本次小多项式与旧十二个原 Hom 的准确接缝；全 $J_X$ 的识别依据命题862.1，不把 (862.17) 冒充对其余 Hodge 方向的数值检验。

在原六次域中可另外保存
$$
Q_A(X)=\frac{1-P_A(X)/c_0}{X},
\qquad a_AQ_A(a_A)=1.
\tag{862.18}
$$
$Q_A$ 是次数至多5的有理多项式；分母已由 $d_A$ 给出。它只编码 $a_A^{-1}$，不能写成未经证明的 $\kappa^{-1}$ 或 $M_v^{-1}$。

使用全部六次域的特征多项式是为了不增加“$a_A$ 必须本原”的条件。即便 $P_A$ 有重复因子，(862.11)–(862.18) 仍然成立；$c_0\ne0$ 已足够。

## 5. 原五个对称对应也有有限映射表达式

R791 原 $h_j=\kappa^{-1}a_A(s_j-r_j)$，并令
$$
\frac{p_j}{q_j}=2+r_j.
\tag{862.19}
$$
在原共同定义域中取 $q_{R,j}=(1+\mathcal T^j)q_R$，其分量是原 $g_{R,j}=(1+\mathcal T^j)f_R$，定义
$$
\mathcal D_{R,j}=q_{R,j}^\dagger q_{R,j}.
\tag{862.20}
$$
这里不声称 $g_{R,j}$ 自身在 $L^+$ 上定义。下式的对称组合由原真实 Galois 作用下降到 $\mathbf Q$。同原 target theta、原 Rosati 与 $\mathcal T$ 等距性给
$$
\boxed{\quad
q^\dagger h_jq
 =\mathcal D_{R,j}-\frac{p_j}{q_j}\mathcal D_A.
\quad}
\tag{862.21}
$$
确切地，$\mathcal D_{R,j}=q^\dagger M_v(2+s_j)q$，再用 $M_v=\kappa^{-1}a_A$ 即得式子。因此 $q_j\mathcal D_{R,j}-p_j\mathcal D_A$ 是实际整有限对应。这些正是原五个方向，不能把 $g_j=f+\mathcal T^jf$ 与其实下降 $g_{R,j}$ 混名。

此段只将 R791/R849 已有原映射与方向写成对应消费者所需的真实算子表达，不重新登记五个方向或 $\eta$ 的新计算。若要把算子对应改成原 Poincaré 线丛对应，仍使用原极化/autoduality，保两轴归一及 modified diagonal；不同的曲线乘积除子代表还须沿真实主函数比较。相同 Jacobian 算子不使任意未标记截面相等。

## 6. 与原 Y 活跃 Hecke 投影的准确比较

原新 Prym 关系给
$$
q\phi^*=0,\qquad \phi_*q^\dagger=0.
\tag{862.22}
$$
故本篇实际投影满足
$$
\boxed{\quad
\varepsilon_A\phi^*=0,\qquad
\phi_*\varepsilon_A=0,\qquad
\phi_*F_A\phi^*=0.
\quad}
\tag{862.23}
$$
特别地，不能把 $\phi_*F_A\phi^*/3$ 当作 YP 所需的 $f=de_\eta$：它准确是零。原 $\eta_{h_j}$ 的 modified-diagonal 构造先沿对角拉回对应线丛，再作原基点修正；它与把 (862.21) 夹在 $\phi_*$ 和 $\phi^*$ 之间不是同一操作。后者同样为零，不推出 $\eta_{h_j}=0$。

本篇得到的是原 $A$ 的规范投影及真实有限对应。要继续 YP 的 Hecke 校准，仍需：

- 原 $J_Y$ 的实际活跃 Hecke 算子及同一个 $e_\eta$；
- 真实清分母 $d$ 与杀掉 $(f-d)\xi_j$ 的实际挠阶 $N$；
- 在原曲线/纤维上的对应、norm、刚性化与必要主函数比较。

$d_A$ 不替换上述 $d$ 或 $N$。本篇没有改写原参考 splitting。

## 7. 最小新算术及可续消费契约

首个消费者只需要已成 R791 的两个小阶段与其完整原来源：

| 原阶段 | bytes | SHA256 |
|---|---:|---|
| R791-original-Hom-Galois-matrices.json.gz | 15617 | f3793ddc7680b718a4448d45587661182986a3558db346ad0a2c9031c8952183 |
| R791-original-real-descent-and-eta-basis-inputs.json.gz | 5573 | 24a894163f136a4e8c71b117e373f8fafb66a6e0c94b4efe3f141f78bb39b968 |
| 原最终证书 | 2298 | 94429377ebd63ff8bdcb9fd1d9468fc2e28e981db2b10b8c494d15c05e073d46 |

这些原字节已在 R850/R852 的活跃载体中继续保留。先读其原 manifest、run/core/public-input 与原 configuration，不能重新标记为本次输出。首 scope 不需要展开原 Hom 周期、全局2420解或395 MB全局函数载体。

新数学严格按下列顺序进行，全部在本公开仓库 Actions：

1. 读取原 $\Psi_{21}$ 与 $a_A$ 的六个 Chebyshev 坐标。用 $s_0=2,\ s_1=S,\ s_{j+1}=Ss_j-s_{j-1}$ 转到原幂基；$a_A$ 的常数坐标3870只乘1，不乘 $s_0$。
2. 在 $\mathbf Q[S]/(\Psi_{21})$ 建六阶乘法矩阵，准确计算 (862.10)。保存全部七个整数系数、$d_A$、(862.18) 的原幂基坐标及乘回。
3. 只新增 (862.17) 的原十二阶矩阵乘回。旧 $E,T,J$、Gram 与原六坐标直接消费，未重解它们。
4. 保存两个来源层明确分开的对象：新多项式/整数分母；(862.8)、(862.12)、(862.21) 的对应 DAG。后者指向原 Hom 字和真实全局映射来源，未声称已物化纤维积方程。

每个新完成阶段独立存原子输出，续算只消费已成阶段。算法的有限性只涉及固定6阶特征多项式和12阶矩阵乘回，不依赖一个尚未成功的数值高度判别。

若后继需要实际对应方程或 c0/c1 的主函数比较，它必须继续携带 R849/R850 原完整全局 source carrier；首个小算术证书本身不替代那些叶。

## 8. 对非 p 项与高度的严格边界

(862.12) 给一个明确整同态，原有理投影 $\varepsilon_A$ 的分母支持包含于 $d_A$ 的素因子。这只描述投影的整化，不是所有原点、纤维、主函数或高度非 $p$ 支持的完整集合。实际点可能在其他好素数约化到相关 theta 支撑；不能仅凭 $d_A$ 或模型坏素数删除这些项。

R724.24–25 的原局部群/刚性化算法、YP.32 的同一个全球校准行，以及 RF/ZA 的 $\nu,\kappa,M_j,\mathcal R_j$ 全保留。完整修正线丛在原 c1 的非 $p$ 值为零，不迫其椭圆和 Picard 因子逐项为零。

本篇没有声称 $e_\eta,N$ 已算出，没有新的 Hecke period 数值、精确非 $p$ 求和或高度。新增的是一个完全使用原实际 Hom 来源、可立即作固定小算术的规范 Rosati 投影接口；它同时严格说明该接口不能替代仍待完成的 Y 校准。

依据：R728 原 Weil restriction 与本原因子；R759 原完整整数 Hom 格；R791 原 Galois、极化元素及五方向；R849/R850 原全局映射和完整刚性化；R596/R724、YP、UE 的原 Hecke 与全局高度规范。
